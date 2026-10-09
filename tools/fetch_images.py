"""Fetch openly licensed Wikimedia Commons images for news articles.
usage: python fetch.py <site_root> <queries.json>   (queries: {slug: [query, ...]})
Writes static/img/news/<slug>.jpg and adds image/image_credit headers to the article."""
import json, re, sys, io, time, html
from pathlib import Path
import requests
from PIL import Image

UA = {"User-Agent": "NewsCompanyImageBot/1.0 (thefulltimehobby.com)"}
API = "https://commons.wikimedia.org/w/api.php"
OK = re.compile(r"^(CC0|CC BY(-SA)? [0-9.]+|CC BY(-SA)?|Public domain|PD.*|Attribution)$", re.I)

def strip(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()

def get_json(**kw):
    for i in range(6):
        resp = requests.get(**kw)
        try: return resp.json()
        except ValueError: time.sleep(5 * (i + 1))
    raise SystemExit("Commons API kept failing")

def search(q):
    exact = q.startswith("File:")
    sel = {"titles": q} if exact else {"generator": "search", "gsrnamespace": 6,
        "gsrsearch": f"{q} filetype:bitmap", "gsrlimit": 15}
    r = get_json(url=API, headers=UA, params={**sel,
        "action": "query", "format": "json", "prop": "imageinfo",
        "iiprop": "url|size|extmetadata|mime", "iiurlwidth": 1400}, timeout=30)
    pages = sorted(r.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 99))
    for p in pages:
        ii = p["imageinfo"][0]; md = ii.get("extmetadata", {})
        lic = strip(md.get("LicenseShortName", {}).get("value"))
        if ii["mime"] not in ("image/jpeg", "image/png", "image/webp"): continue
        if not exact and (ii["width"] < 1000 or ii["width"] < ii["height"]): continue
        if not OK.match(lic): continue
        artist = strip(md.get("Artist", {}).get("value")) or "Unknown"
        artist = re.sub(r"\s+", " ", artist)[:80]
        return {"title": p["title"], "thumb": ii["thumburl"], "page": ii["descriptionurl"], "lic": lic, "artist": artist}

root = Path(sys.argv[1]); queries = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
out = root / "static" / "img" / "news"; out.mkdir(parents=True, exist_ok=True)
for slug, qs in queries.items():
    f = root / "content" / "articles" / f"{slug}.md"
    if "image: /img/news/" in f.read_text(encoding="utf-8"):
        continue
    hit = None
    for q in qs:
        hit = search(q)
        if hit: break
        time.sleep(1.5)
    if not hit:
        print(f"MISS  {slug}"); continue
    img = None
    for i in range(6):
        try:
            img = Image.open(io.BytesIO(requests.get(hit["thumb"], headers=UA, timeout=60).content)).convert("RGB"); break
        except Exception:
            time.sleep(8 * (i + 1))
    if img is None:
        print(f"DLFAIL {slug}"); continue
    if img.width > 1400: img = img.resize((1400, round(img.height * 1400 / img.width)), Image.LANCZOS)
    img.save(out / f"{slug}.jpg", "JPEG", quality=80, optimize=True, progressive=True)
    raw = f.read_text(encoding="utf-8")
    head, body = raw.split("\n---\n", 1)
    head = "\n".join(l for l in head.splitlines() if not l.startswith(("image:", "image_credit:")))
    credit = f"{hit['artist']} / {hit['lic']} via Wikimedia Commons|{hit['page']}"
    f.write_text(f"{head}\nimage: /img/news/{slug}.jpg\nimage_credit: {credit}\n---\n{body}", encoding="utf-8")
    print(f"OK    {slug:55} {hit['title'][:70]}  [{hit['lic']}]")
    time.sleep(1.5)
