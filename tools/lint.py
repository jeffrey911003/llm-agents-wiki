"""Lint the LLM Agents wiki (AGENTS.md §5 Lint).
Usage: python tools/lint.py   (run from the project root)"""
import re, os, glob, sys

WIKI = "wiki"
SPECIAL = {"index", "log"}
REQUIRED_FM = {"type", "title", "sources", "updated"}
CITE = re.compile(r"§|Table|Fig\.|Algorithm|Abstract|p\.\d")

files = sorted(glob.glob(f"{WIKI}/**/*.md", recursive=True))
pages = {os.path.splitext(os.path.basename(f))[0]: f for f in files}
inbound = {p: 0 for p in pages}
problems = {"broken": [], "orphan": [], "frontmatter": [], "uncited": [], "not_in_index": []}

index_txt = open(f"{WIKI}/index.md", encoding="utf-8").read()
for name, f in pages.items():
    txt = open(f, encoding="utf-8").read()
    for link in set(re.findall(r"\[\[([^\]|#]+)", txt)):
        if link not in pages:
            problems["broken"].append(f"{f} -> [[{link}]]")
        elif link != name:
            inbound[link] += 1
    if name in SPECIAL:
        continue
    if f"[[{name}]]" not in index_txt:
        problems["not_in_index"].append(f)
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    keys = set(re.findall(r"^(\w+):", m.group(1), re.M)) if m else set()
    if not REQUIRED_FM <= keys:
        problems["frontmatter"].append(f"{f} missing {sorted(REQUIRED_FM - keys)}")
    # a bullet / table row / paragraph line with a factual-looking number but no citation
    section_cited = False
    for i, line in enumerate(txt.split("\n"), 1):
        if line.startswith("#"):
            section_cited = bool(CITE.search(line))
            continue
        bare = re.sub(r"\[\[[^\]]*\]\]", "", line)
        if line.startswith("| [[") or "lint-ok" in line:
            continue  # catalog rows point to cited pages; explicit opt-out marker
        if re.search(r"\d", bare) and not CITE.search(line) and not section_cited \
           and not line.startswith(("---", "updated", "year", "arxiv", "authors", "venue", "|---", "sources", "tags", "title", "type")):
            if name.startswith(tuple("0123456789")) or "/papers/" in f:
                continue  # paper pages: whole page is one source; sections cite §
            problems["uncited"].append(f"{f}:{i}: {line.strip()[:90]}")

CANDIDATES = ["hallucination", "Tree of Thoughts", "Self-Refine", "Inner Monologue", "multi-agent", "episodic memory", "WebGPT"]  # fine-tuning is covered by capability-acquisition
all_txt = {n: open(f, encoding="utf-8").read().lower() for n, f in pages.items() if n not in SPECIAL}
problems["missing_concept_page"] = []
for term in CANDIDATES:
    hits = [n for n, t in all_txt.items() if term.lower() in t]
    slug = term.lower().replace(" ", "-")
    if len(hits) >= 4 and slug not in pages:
        problems["missing_concept_page"].append(f"'{term}' mentioned on {len(hits)} pages, no page")
problems["orphan"] = [p for p, c in inbound.items() if c == 0 and p not in SPECIAL]
total = 0
for k, v in problems.items():
    print(f"\n## {k} ({len(v)})")
    for x in v:
        print("  -", x)
    total += len(v)
print(f"\n{len(pages)} pages, {total} issues")
sys.exit(1 if total else 0)
