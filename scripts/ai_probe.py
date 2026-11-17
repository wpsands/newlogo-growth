#!/usr/bin/env python3
"""Ask AI assistants buyer questions and record whether a company appears.

Part of the newlogo-growth plugin (story sync surface 6). Standard library only.

Each question is asked RUNS times per provider, with the provider's web search
turned on so answers reflect what a buyer sees today. For every answer the script
records whether the brand is named, its position among the named vendors, the
sentence that describes it, and the sources cited. A brand counts as present for
a question only when it appears in a majority of runs (consensus).

Keys are read from environment variables and never printed. A provider without a
key is skipped and listed in the output. Model names can be overridden.

  ANTHROPIC_API_KEY   NLG_ANTHROPIC_MODEL  (default claude-opus-5-5)
  OPENAI_API_KEY      NLG_OPENAI_MODEL     (default gpt-5)
  PERPLEXITY_API_KEY  NLG_PERPLEXITY_MODEL (default sonar)
  GEMINI_API_KEY      NLG_GEMINI_MODEL     (default gemini-2.5-flash)

Or one OPENROUTER_API_KEY for all four families, each with its provider's native
search. Defaults: openai/gpt-5.6-terra, anthropic/claude-sonnet-5.5,
google/gemini-3.8-flash, perplexity/sonar; override with
NLG_OPENROUTER_{OPENAI,ANTHROPIC,GEMINI,PERPLEXITY}_MODEL. A direct key for a
family takes precedence over its OpenRouter route.

Example:
  python3 ai_probe.py --brand Outreach --aliases outreach.ai,outreach.io \
    --competitors Gong,Salesloft,Apollo --questions-file questions.txt \
    --runs 3 --out probe.json
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

TIMEOUT = 180


def post(url, headers, body):
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return json.load(r), None
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")[:400]
        return None, f"HTTP {e.code}: {detail}"
    except Exception as e:  # network errors, timeouts
        return None, f"{type(e).__name__}: {str(e)[:200]}"


# Providers. Each returns (text, [cited urls], error)

def ask_anthropic(q, key, model):
    headers = {
        "x-api-key": key,
        "anthropic-version": "2023-06-01",
        "anthropic-beta": "server-side-fallback-2026-07-01",
        "content-type": "application/json",
    }
    tools = [{"type": "web_search_20260209", "name": "web_search", "max_uses": 5}]
    messages = [{"role": "user", "content": q}]
    for _ in range(5):  # resume pause_turn up to five times
        data, err = post("https://api.anthropic.com/v1/messages", headers, {
            "model": model, "max_tokens": 16000, "tools": tools,
            "messages": messages, "fallbacks": "default",
        })
        if err:
            return "", [], err
        if data.get("stop_reason") == "refusal":
            return "", [], "refusal"
        if data.get("stop_reason") != "pause_turn":
            break
        messages = [{"role": "user", "content": q}, {"role": "assistant", "content": data["content"]}]
    text, urls = [], []
    for block in data.get("content", []):
        if block.get("type") == "text":
            text.append(block.get("text", ""))
            for c in block.get("citations") or []:
                if c.get("url"):
                    urls.append(c["url"])
    return "".join(text), urls, None


def ask_openai(q, key, model):
    headers = {"authorization": f"Bearer {key}", "content-type": "application/json"}
    data, err = post("https://api.openai.com/v1/responses", headers, {
        "model": model, "input": q, "tools": [{"type": "web_search"}],
    })
    if err:
        return "", [], err
    text, urls = [], []
    for item in data.get("output", []):
        for part in item.get("content", []) or []:
            if part.get("type") == "output_text":
                text.append(part.get("text", ""))
                for a in part.get("annotations") or []:
                    if a.get("url"):
                        urls.append(a["url"])
    return "".join(text), urls, None


def ask_perplexity(q, key, model):
    headers = {"authorization": f"Bearer {key}", "content-type": "application/json"}
    data, err = post("https://api.perplexity.ai/chat/completions", headers, {
        "model": model, "messages": [{"role": "user", "content": q}],
    })
    if err:
        return "", [], err
    text = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    urls = list(data.get("citations") or [])
    urls += [r.get("url") for r in data.get("search_results") or [] if r.get("url")]
    return text, urls, None


def ask_gemini(q, key, model):
    headers = {"x-goog-api-key": key, "content-type": "application/json"}
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{urllib.parse.quote(model)}:generateContent"
    data, err = post(url, headers, {
        "contents": [{"parts": [{"text": q}]}], "tools": [{"google_search": {}}],
    })
    if err:
        return "", [], err
    cand = (data.get("candidates") or [{}])[0]
    text = "".join(p.get("text", "") for p in cand.get("content", {}).get("parts", []))
    chunks = cand.get("groundingMetadata", {}).get("groundingChunks", []) or []
    urls = []
    for c in chunks:
        w = c.get("web", {})
        u, title = w.get("uri"), (w.get("title") or "").strip()
        if u and "vertexaisearch" in u and re.match(r"^[\w.-]+\.[a-z]{2,}$", title):
            u = "https://" + title
        if u:
            urls.append(u)
    return text, urls, None


def make_openrouter(family):
    def ask(q, key, model):
        headers = {"authorization": f"Bearer {key}", "content-type": "application/json",
                   "x-title": "newlogo-growth ai_probe"}
        body = {"model": model, "messages": [{"role": "user", "content": q}]}
        if family != "perplexity":  # Sonar always searches; it rejects the web plugin
            body["plugins"] = [{"id": "web", "engine": "native"}]
        data, err = post("https://openrouter.ai/api/v1/chat/completions", headers, body)
        if err:
            return "", [], err
        if data.get("error"):
            return "", [], str(data["error"])[:300]
        msg = (data.get("choices") or [{}])[0].get("message", {})
        urls = []
        for a in msg.get("annotations") or []:
            c = a.get("url_citation", {})
            u, title = c.get("url"), (c.get("title") or "").strip()
            # Gemini cites Google redirect links; the title carries the real site
            if u and "vertexaisearch" in u and re.match(r"^[\w.-]+\.[a-z]{2,}$", title):
                u = "https://" + title
            if u:
                urls.append(u)
        urls += list(data.get("citations") or [])
        return msg.get("content") or "", urls, None
    return ask


# OpenRouter routes one key to every family, with each provider's native search.
# A direct key for a family takes precedence over its OpenRouter route.
OPENROUTER_MODELS = {
    "openai": "openai/gpt-5.6-terra",
    "anthropic": "anthropic/claude-sonnet-5.5",
    "gemini": "google/gemini-3.8-flash",
    "perplexity": "perplexity/sonar",
}

PROVIDERS = {
    "anthropic": ("ANTHROPIC_API_KEY", "NLG_ANTHROPIC_MODEL", "claude-opus-5-5", ask_anthropic),
    "openai": ("OPENAI_API_KEY", "NLG_OPENAI_MODEL", "gpt-5", ask_openai),
    "perplexity": ("PERPLEXITY_API_KEY", "NLG_PERPLEXITY_MODEL", "sonar", ask_perplexity),
    "gemini": ("GEMINI_API_KEY", "NLG_GEMINI_MODEL", "gemini-2.5-flash", ask_gemini),
}


def first_index(text, names):
    hits = []
    for n in names:
        m = re.search(r"(?<![\w.])" + re.escape(n) + r"(?![\w])", text, re.I)
        if m:
            hits.append(m.start())
    return min(hits) if hits else None


def analyze(text, urls, brand_names, competitors):
    pos = first_index(text, brand_names)
    named = {}
    for c in competitors:
        i = first_index(text, [c])
        if i is not None:
            named[c] = i
    if pos is not None:
        named["__brand__"] = pos
    order = sorted(named, key=named.get)
    rank = order.index("__brand__") + 1 if "__brand__" in order else None
    sentence = ""
    if pos is not None:
        start = max(text.rfind(".", 0, pos), text.rfind("\n", 0, pos)) + 1
        end_candidates = [i for i in (text.find(".", pos), text.find("\n", pos)) if i != -1]
        end = min(end_candidates) + 1 if end_candidates else len(text)
        sentence = text[start:end].strip()[:300]
    domains = sorted({urllib.parse.urlparse(u).netloc.removeprefix("www.") for u in urls if u})
    brand_domains = [d for d in domains if any(n.lower() in d for n in brand_names if "." in n)]
    return {
        "mentioned": pos is not None,
        "rank_among_named_vendors": rank,
        "vendors_named": [c if c != "__brand__" else "BRAND" for c in order],
        "brand_sentence": sentence,
        "cited_domains": domains,
        "brand_domain_cited": bool(brand_domains),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--brand", required=True)
    ap.add_argument("--aliases", default="", help="comma-separated other names or domains")
    ap.add_argument("--competitors", default="", help="comma-separated competitor names")
    ap.add_argument("--questions-file", required=True, help="one buyer question per line")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--providers", default="anthropic,openai,perplexity,gemini")
    ap.add_argument("--out", required=True, help="path for the JSON results")
    a = ap.parse_args()

    brand_names = [a.brand] + [x.strip() for x in a.aliases.split(",") if x.strip()]
    competitors = [x.strip() for x in a.competitors.split(",") if x.strip()]
    questions = [l.strip() for l in open(a.questions_file) if l.strip() and not l.startswith("#")]

    result = {"brand": a.brand, "aliases": brand_names[1:], "competitors": competitors,
              "questions": questions, "runs": a.runs,
              "started": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "providers": {}, "skipped": {}}

    plan = []  # (label, fn, key, model, route)
    or_key = os.environ.get("OPENROUTER_API_KEY")
    for name in [p.strip() for p in a.providers.split(",") if p.strip()]:
        if name not in PROVIDERS:
            result["skipped"][name] = "unknown provider"
            continue
        key_var, model_var, default_model, fn = PROVIDERS[name]
        key = os.environ.get(key_var) or (os.environ.get("GOOGLE_API_KEY") if name == "gemini" else None)
        if key:
            plan.append((name, fn, key, os.environ.get(model_var, default_model), "direct"))
        elif or_key:
            model = os.environ.get(f"NLG_OPENROUTER_{name.upper()}_MODEL", OPENROUTER_MODELS[name])
            plan.append((name, make_openrouter(name), or_key, model, "openrouter, native search"))
        else:
            result["skipped"][name] = f"{key_var} and OPENROUTER_API_KEY not set"

    for name, fn, key, model, route in plan:
        prov = {"model": model, "route": route, "questions": []}
        for q in questions:
            runs = []
            for r in range(a.runs):
                text, urls, err = fn(q, key, model)
                entry = {"run": r + 1, "error": err} if err else {"run": r + 1, **analyze(text, urls, brand_names, competitors), "answer_excerpt": text[:1500]}
                runs.append(entry)
                print(f"{name} | run {r + 1} | {q[:60]} | " + (f"ERROR {err[:120]}" if err else f"mentioned={entry['mentioned']} rank={entry['rank_among_named_vendors']}"), file=sys.stderr)
                time.sleep(1)
            ok = [x for x in runs if not x.get("error")]
            hits = sum(1 for x in ok if x["mentioned"])
            prov["questions"].append({
                "question": q, "runs": runs, "valid_runs": len(ok), "mentioned_runs": hits,
                "consensus_present": bool(ok) and hits > len(ok) / 2,
            })
        result["providers"][name] = prov

    result["finished"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(a.out, "w") as f:
        json.dump(result, f, indent=1)

    # Markdown summary on stdout
    print(f"# AI answer probe: {a.brand}\n")
    print(f"{a.runs} runs per question per provider; present = named in a majority of valid runs.\n")
    if result["skipped"]:
        print("Skipped: " + "; ".join(f"{k} ({v})" for k, v in result["skipped"].items()) + "\n")
    for name, prov in result["providers"].items():
        print(f"## {name} ({prov['model']}, {prov['route']})\n")
        print("| Question | Present | Runs named | Valid runs |")
        print("|---|---|---|---|")
        for qq in prov["questions"]:
            print(f"| {qq['question']} | {'yes' if qq['consensus_present'] else 'no'} | {qq['mentioned_runs']} | {qq['valid_runs']} |")
        print()
    print(f"Full results: {a.out}")


if __name__ == "__main__":
    main()
