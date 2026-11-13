"""Build outputs/slides/deck.html (artifact body, images inlined) and index.html (standalone)."""
import re, base64, pathlib
d = pathlib.Path("outputs/slides")
t = (d / "template.html").read_text(encoding="utf-8")
def inline(m):
    p = d / "img" / m.group(1)
    return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
body = re.sub(r"\{\{img:([^}]+)\}\}", inline, t)
(d / "deck.html").write_text(body, encoding="utf-8")
(d / "index.html").write_text('<!doctype html>\n<html lang="zh-Hant">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    + body.replace("<div class=\"deck\">", "</head>\n<body>\n<div class=\"deck\">", 1) + "\n</body>\n</html>\n", encoding="utf-8")
print("deck.html", len(body)//1024, "KB")
