"""Ping IndexNow (Bing, Yandex, Seznam, Naver) with every URL in the sitemap. Run after each deploy."""
import json, re, urllib.request
from pathlib import Path
import build
urls = re.findall(r"<loc>(.*?)</loc>", (Path(__file__).parent / "docs" / "sitemap.xml").read_text(encoding="utf-8"))
host = build.SITE.split("//")[1]
body = json.dumps({"host": host, "key": build.INDEXNOW_KEY, "keyLocation": f"{build.SITE}/{build.INDEXNOW_KEY}.txt", "urlList": urls}).encode()
req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body, headers={"Content-Type": "application/json; charset=utf-8"})
with urllib.request.urlopen(req) as r:
    print(r.status, len(urls), "URLs submitted")
