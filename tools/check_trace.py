"""Trace check for generated outputs (AGENTS.md §5 output loop, steps 3 and 5).
For every slide, each number and each Latin-script term must appear on at least
one of the wiki pages the slide cites. Usage:
  python tools/check_trace.py outline outputs/slides/outline.md
  python tools/check_trace.py html    outputs/slides/index.html"""
import re, sys, glob, os, html as H

pages = {os.path.splitext(os.path.basename(f))[0]: open(f, encoding="utf-8").read()
         for f in glob.glob("wiki/**/*.md", recursive=True)}
IGNORE_TERMS = {"LLM", "LLMs", "Agent", "Agents", "Wiki", "API", "AI", "Profile", "Memory",
                "Planning", "Action", "Thought", "Observation", "prompt", "context", "window",
                "Fig", "Survey", "sources", "image", "png", "LLM Wiki", "vs", "CoT"}

def norm_num(n):  # 0.60 == 60%, 29.89 etc. -> keep literal and percent variants
    out = {n}
    if re.fullmatch(r"0\.\d+", n): out.add(str(round(float(n) * 100)))
    if re.fullmatch(r"\d{1,2}", n): out.add(f"0.{int(n):02d}")  # 52% on a slide == 0.52 in a table
    return out

def check(slide_id, text, srcs):
    corpus = "\n".join(pages.get(s, "") for s in srcs)
    missing_pages = [s for s in srcs if s not in pages]
    bad = []
    for n in set(re.findall(r"(?<![\w.])\d+(?:\.\d+)?(?![\w])", text)):
        if not any(re.search(rf"(?<![\d.]){re.escape(v)}(?![\d])", corpus) for v in norm_num(n)):
            bad.append(f"number {n}")
    for t in set(re.findall(r"[A-Za-z][A-Za-z\-]{2,}(?: [A-Z][a-z]+)?", text)):
        if t in IGNORE_TERMS or t.split()[0] in IGNORE_TERMS:
            continue
        if t.lower() not in corpus.lower():
            bad.append(f"term '{t}'")
    status = "PASS" if not bad and not missing_pages else "FAIL"
    print(f"{slide_id:4} {status}  sources={srcs}" + (f"  missing_pages={missing_pages}" if missing_pages else ""))
    for b in sorted(bad): print("       -", b)
    return status == "PASS"

mode, path = sys.argv[1], sys.argv[2]
raw = open(path, encoding="utf-8").read()
ok = True
if mode == "outline":
    for block in re.split(r"\n(?=## S\d+)", raw)[1:]:
        sid = re.match(r"## (S\d+)", block).group(1)
        srcs = [s.strip() for s in re.search(r"sources: (.*)", block).group(1).split(",")]
        body = "\n".join(l for l in block.split("\n") if not l.startswith(("sources:", "image:")))
        body = re.sub(r"## S\d+ ", "", body)
        ok &= check(sid, body, srcs)
else:  # html: <section data-sources="a,b"> ... </section>
    for i, (srcs, inner) in enumerate(re.findall(r'<section[^>]*data-sources="([^"]+)"[^>]*>(.*?)</section>', raw, re.S), 1):
        inner = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", inner, flags=re.S)
        inner = re.sub(r'<footer class="src">.*?</footer>', "", inner, flags=re.S)
        inner = re.sub(r'<img[^>]*>', "", inner)
        text = H.unescape(re.sub(r"<[^>]+>", " ", inner))
        ok &= check(f"S{i}", text, [s.strip() for s in srcs.split(",")])
print("\nRESULT:", "ALL PASS" if ok else "FAILURES — go back (see AGENTS.md output loop)")
sys.exit(0 if ok else 1)
