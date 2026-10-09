#!/usr/bin/env python3
"""Static site generator for TechNewsCompany.com.

Add a news story:      drop a .md file in content/articles/
Add a client release:  drop a .md file in content/releases/
Then run:  python build.py   (writes the site into docs/, which GitHub Pages serves)

File format: "key: value" header lines, a line with ---, then the body.
Body supports: ## / ### headings, paragraphs, "- " bullet lists, "> " quotes,
**bold**, and [link text](https://url).
Header keys: title, dek, priority (higher = shown first that day), date (YYYY-MM-DD), category, company, source ("Name|URL"),
dateline (releases), contact_name, contact_email, website (releases).
"""
import html, json, re, shutil
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "docs"
SITE = "https://technewscompany.com"
NAME = "Tech News Company"
ORDER_EMAIL = "thefulltimehobby@gmail.com"   # where /submit orders are emailed
CF_BEACON_TOKEN = ""
INDEXNOW_KEY = "70f6a9be0a7c7aff97f68c6d5ccc87d6"                 # served at /<key>.txt; run indexnow.py after each deploy                          # Cloudflare Web Analytics token; empty = no beacon

CATS = {
    "AI": "#6d28d9",
    "Chips": "#0e7490",
    "Devices": "#be123c",
    "Cloud & Infrastructure": "#1d4ed8",
    "Security": "#b45309",
    "Deals & Funding": "#047857",
    "Markets": "#334155",
    "Press Release": "#475569",
}

def slugify(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def esc(s):
    return html.escape(s or "", quote=True)

def inline(s, sponsored=False):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    rel = "sponsored noopener" if sponsored else "noopener"
    s = re.sub(r"\[(.+?)\]\((https?://[^)\s]+)\)",
               lambda m: f'<a href="{m.group(2)}" rel="{rel}" target="_blank">{m.group(1)}</a>', s)
    return s

def md_to_html(text, sponsored=False):
    out, para, lst = [], [], []
    def flush():
        if para:
            out.append("<p>" + inline(" ".join(para), sponsored) + "</p>"); para.clear()
        if lst:
            out.append("<ul>" + "".join(f"<li>{inline(i, sponsored)}</li>" for i in lst) + "</ul>"); lst.clear()
    for line in text.splitlines():
        l = line.strip()
        if not l:
            flush(); continue
        if l.startswith("### "):
            flush(); out.append(f"<h3>{inline(l[4:], sponsored)}</h3>")
        elif l.startswith("## "):
            flush(); out.append(f"<h2>{inline(l[3:], sponsored)}</h2>")
        elif l.startswith("> "):
            flush(); out.append(f"<blockquote>{inline(l[2:], sponsored)}</blockquote>")
        elif l.startswith("- "):
            if para: flush()
            lst.append(l[2:])
        else:
            if lst: flush()
            para.append(l)
    flush()
    return "\n".join(out)

def load(folder, kind):
    items = []
    for f in sorted((ROOT / "content" / folder).glob("*.md")):
        raw = f.read_text(encoding="utf-8")
        head, body = raw.split("\n---\n", 1)
        meta = {}
        for line in head.splitlines():
            if ":" in line:
                k, v = line.split(":", 1); meta[k.strip()] = v.strip()
        meta["slug"] = f.stem
        meta["kind"] = kind
        meta["body_md"] = body
        meta["dt"] = datetime.strptime(meta["date"], "%Y-%m-%d")
        meta["url"] = f"/{'news' if kind == 'news' else 'press-releases'}/{f.stem}/"
        words = len(re.findall(r"\w+", body))
        meta["read"] = max(2, round(words / 200))
        items.append(meta)
    items.sort(key=lambda a: (a["dt"], int(a.get("priority", 0)), a["title"]), reverse=True)
    return items

def nice_date(dt):
    return f"{dt:%B} {dt.day}, {dt.year}"

def art(a, size=""):
    if a.get("image"):
        lazy = "" if size in ("big", "wide") else ' loading="lazy"'
        return (f'<div class="art img {size}"><img src="{esc(a["image"])}" alt="{esc(a["title"])}"'
                f'{lazy} decoding="async"></div>')
    color = CATS.get(a["category"], "#334155")
    label = esc(a.get("company", ""))
    return (f'<div class="art {size}" style="--c:{color}" aria-hidden="true">'
            f'<span class="art-co">{label}</span><span class="art-cat">{esc(a["category"])}</span></div>')

def credit_html(a):
    if not a.get("image_credit"):
        return ""
    text, url = (a["image_credit"].split("|", 1) + [""])[:2]
    link = f'<a href="{esc(url)}" target="_blank" rel="noopener">{esc(text)}</a>' if url else esc(text)
    return f'<p class="credit">Photo: {link}</p>'

def beacon():
    if not CF_BEACON_TOKEN:
        return ""
    return ("<script defer src='https://static.cloudflareinsights.com/beacon.min.js' "
            f"data-cf-beacon='{{\"token\": \"{CF_BEACON_TOKEN}\"}}'></script>")

def nav_html(active=""):
    links = [("Latest", "/"), ("AI", "/category/ai/"), ("Chips", "/category/chips/"),
             ("Devices", "/category/devices/"), ("Cloud", "/category/cloud-infrastructure/"),
             ("Security", "/category/security/"), ("Deals", "/category/deals-funding/"),
             ("Markets", "/category/markets/"), ("Press Releases", "/press-releases/")]
    return "".join(f'<a href="{u}"{" class=on" if active == u else ""}>{t}</a>' for t, u in links)

def page(title, body, desc="", path="/", active="", extra_head="", og_type="website", og_image=""):
    full = title if title == NAME else f"{title} | {NAME}"
    today = datetime.now().strftime("%A, %B %d, %Y").replace(" 0", " ")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{SITE}{path}">
{f'<meta property="og:image" content="{SITE}{og_image}"><meta name="twitter:card" content="summary_large_image">' if og_image else '<meta name="twitter:card" content="summary">'}
<link rel="alternate" type="application/rss+xml" title="{NAME}" href="/rss.xml">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Source+Serif+4:opsz,wght@8..60,500;8..60,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{extra_head}
</head>
<body>
<div class="topbar"><div class="wrap"><span>{today}</span><a href="/submit/" class="topcta">Publish a press release &rarr;</a></div></div>
<header class="mast"><div class="wrap">
  <a href="/" class="logo"><span class="logo-mark">TNC</span><span class="logo-word">Tech News <b>Company</b></span></a>
  <a href="/submit/" class="btn btn-sm hide-sm">Submit a Release</a>
</div></header>
<nav class="nav"><div class="wrap">{nav_html(active)}</div></nav>
<main>
{body}
</main>
<footer class="foot"><div class="wrap foot-grid">
  <div><a href="/" class="logo logo-foot"><span class="logo-mark">TNC</span><span class="logo-word">Tech News <b>Company</b></span></a>
  <p>Independent coverage of AI, chips, devices, cloud and security, plus press release publishing for technology companies.</p></div>
  <div><h4>Sections</h4><a href="/category/ai/">AI</a><a href="/category/chips/">Chips</a><a href="/category/devices/">Devices</a><a href="/category/cloud-infrastructure/">Cloud &amp; Infrastructure</a><a href="/category/security/">Security</a><a href="/category/deals-funding/">Deals &amp; Funding</a></div>
  <div><h4>Press Releases</h4><a href="/submit/">Submit a Release</a><a href="/submit/#pricing">Pricing</a><a href="/press-releases/">Latest Releases</a><a href="/editorial-policy/">Editorial Policy</a></div>
  <div><h4>Company</h4><a href="/companies/">Companies Covered</a><a href="/about/">About</a><a href="/contact/">Contact</a><a href="/rss.xml">RSS Feed</a></div>
</div><div class="wrap copy">&copy; {datetime.now().year} {NAME}. News coverage is independently written and links to original sources. Press releases are submitted by the issuing company.</div></footer>
{beacon()}
</body>
</html>
"""

def card(a, cls=""):
    return f"""<article class="card {cls}">
  <a href="{a['url']}" class="card-art">{art(a)}</a>
  <div class="card-body">
    <a class="kicker" href="/category/{slugify(a['category'])}/" style="color:{CATS.get(a['category'])}">{esc(a['category'])}</a>
    <h3><a href="{a['url']}">{esc(a['title'])}</a></h3>
    <p>{esc(a['dek'])}</p>
    <div class="meta">{nice_date(a['dt'])} &middot; {a['read']} min read</div>
  </div>
</article>"""

def row(a):
    return f"""<li><a href="{a['url']}"><span class="kicker" style="color:{CATS.get(a['category'])}">{esc(a['category'])}</span>{esc(a['title'])}</a><span class="meta">{nice_date(a['dt'])}</span></li>"""

def release_row(r):
    return f"""<li><a href="{r['url']}"><span class="kicker pr">Press Release</span>{esc(r['title'])}</a><span class="meta">{nice_date(r['dt'])}</span></li>"""

CTA = """<section class="cta"><div class="wrap cta-in">
  <div><h2>Get your announcement in front of the tech world.</h2>
  <p>Publish a press release on Tech News Company from $149. Permanent page, same-day publishing, flat pricing.</p></div>
  <a class="btn btn-light" href="/submit/">See packages</a>
</div></section>"""

def write(path, content):
    p = OUT / path.strip("/") / "index.html" if not path.endswith((".xml", ".txt", ".html", ".svg", ".css", ".js")) else OUT / path.strip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def build_home(news, rels):
    lead, side, rest = news[0], news[1:5], news[5:]
    ticker = " ".join(f'<a href="{a["url"]}">{esc(a["company"])}: {esc(a["title"])}</a>' for a in news[:8])
    sections = ""
    for cat in [c for c in CATS if c != "Press Release"]:
        items = [a for a in news if a["category"] == cat][:3]
        if not items:
            continue
        sections += f"""<section class="sec"><div class="sec-h"><h2 style="--c:{CATS[cat]}">{esc(cat)}</h2><a href="/category/{slugify(cat)}/">More {esc(cat)} &rarr;</a></div>
<div class="grid3">{''.join(card(a) for a in items)}</div></section>"""
    body = f"""
<div class="ticker"><div class="wrap"><span class="tk-label">Latest</span><div class="tk-track"><div class="tk-move">{ticker} {ticker}</div></div></div></div>
<div class="wrap">
<section class="hero">
  <article class="lead">
    <a href="{lead['url']}" class="card-art">{art(lead, 'big')}</a>
    <a class="kicker" href="/category/{slugify(lead['category'])}/" style="color:{CATS.get(lead['category'])}">{esc(lead['category'])}</a>
    <h1><a href="{lead['url']}">{esc(lead['title'])}</a></h1>
    <p class="dek">{esc(lead['dek'])}</p>
    <div class="meta">{nice_date(lead['dt'])} &middot; {lead['read']} min read</div>
  </article>
  <div class="side">
    <h2 class="side-h">Top Stories</h2>
    {''.join(card(a, 'mini') for a in side)}
  </div>
</section>
<div class="cols">
  <div class="main-col">
    <div class="sec-h"><h2 style="--c:#111">Latest News</h2></div>
    <div class="grid2">{''.join(card(a) for a in rest[:8])}</div>
  </div>
  <aside class="rail">
    <div class="box box-dark">
      <h3>Publish your press release</h3>
      <p>Launches, funding rounds, partnerships and product news. Live on a permanent page, usually within one business day.</p>
      <a class="btn" href="/submit/">From $149 &rarr;</a>
    </div>
    <div class="box">
      <h3 class="box-h">Press Releases</h3>
      <ul class="list">{''.join(release_row(r) for r in rels[:6])}</ul>
      <a class="more" href="/press-releases/">All press releases &rarr;</a>
    </div>
    <div class="box">
      <h3 class="box-h">Most Read</h3>
      <ol class="list ranked">{''.join(row(a) for a in news[:5])}</ol>
    </div>
  </aside>
</div>
{sections}
</div>
{CTA}"""
    ld = {"@context": "https://schema.org", "@type": "NewsMediaOrganization", "name": NAME, "url": SITE,
          "logo": f"{SITE}/favicon.svg", "publishingPrinciples": f"{SITE}/editorial-policy/"}
    write("/", page(NAME, body, "Tech News Company: independent coverage of AI, chips, devices, cloud and security, plus press release publishing for technology companies.",
                    "/", "/", f'<script type="application/ld+json">{json.dumps(ld)}</script>'))

def build_item(a, news, rels):
    is_pr = a["kind"] == "release"
    body_html = md_to_html(a["body_md"], sponsored=is_pr)
    related = [x for x in news if x["slug"] != a["slug"] and (x["category"] == a["category"] or x.get("company") == a.get("company"))][:3]
    if len(related) < 3:
        related += [x for x in news if x["slug"] != a["slug"] and x not in related][:3 - len(related)]
    if is_pr:
        dl = esc(a.get("dateline", ""))
        first = f'<p class="dateline"><strong>{dl}, {nice_date(a["dt"])}</strong> &mdash;</p>' if dl else ""
        notice = '<div class="pr-note">Press release. This content was provided by the issuing company and is published as submitted. Tech News Company did not write or verify it. <a href="/editorial-policy/">Learn more</a>.</div>'
        src = ""
        contact = ""
        if a.get("contact_name") or a.get("contact_email") or a.get("website"):
            contact = '<div class="pr-contact"><h3>Media contact</h3>'
            if a.get("contact_name"): contact += f'<p>{esc(a["contact_name"])}</p>'
            if a.get("contact_email"): contact += f'<p><a href="mailto:{esc(a["contact_email"])}">{esc(a["contact_email"])}</a></p>'
            if a.get("website"): contact += f'<p><a href="{esc(a["website"])}" rel="sponsored noopener" target="_blank">{esc(a["website"])}</a></p>'
            contact += "</div>"
        byline = f"Press release from {esc(a.get('company', ''))}"
        kicker = '<span class="kicker pr">Press Release</span>'
        section = "/press-releases/"
    else:
        first, notice, contact = "", "", ""
        sname, surl = (a.get("source", "|").split("|", 1) + [""])[:2]
        src = f'<div class="source">Source: <a href="{esc(surl)}" target="_blank" rel="noopener">{esc(sname)}</a></div>' if surl else ""
        if a.get("company"):
            src += f'<a class="co-more" href="/company/{slugify(a["company"])}/">More {esc(a["company"])} news &rarr;</a>'
        byline = "By TNC Newsdesk"
        kicker = f'<a class="kicker" href="/category/{slugify(a["category"])}/" style="color:{CATS.get(a["category"])}">{esc(a["category"])}</a>'
        section = f"/category/{slugify(a['category'])}/"
    share = f"{SITE}{a['url']}"
    body = f"""<div class="wrap">
<div class="cols">
<article class="story">
  {notice}
  {kicker}
  <h1>{esc(a['title'])}</h1>
  <p class="dek">{esc(a['dek'])}</p>
  <div class="byline"><span>{byline}</span><span>{nice_date(a['dt'])} &middot; {a['read']} min read</span></div>
  {art(a, 'wide')}{credit_html(a)}
  <div class="prose">{first}{body_html}</div>
  {contact}
  {src}
  <div class="share">Share:
    <a target="_blank" rel="noopener" href="https://www.linkedin.com/sharing/share-offsite/?url={share}">LinkedIn</a>
    <a target="_blank" rel="noopener" href="https://twitter.com/intent/tweet?url={share}&text={esc(a['title'])}">X</a>
    <a target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u={share}">Facebook</a>
  </div>
</article>
<aside class="rail">
  <div class="box box-dark"><h3>Have news to share?</h3><p>Publish your press release on Tech News Company.</p><a class="btn" href="/submit/">Submit a release &rarr;</a></div>
  <div class="box"><h3 class="box-h">Latest News</h3><ul class="list">{''.join(row(x) for x in news[:6] if x['slug'] != a['slug'])}</ul></div>
  <div class="box"><h3 class="box-h">Press Releases</h3><ul class="list">{''.join(release_row(r) for r in rels[:4])}</ul></div>
</aside>
</div>
<section class="sec"><div class="sec-h"><h2 style="--c:#111">Related Coverage</h2></div><div class="grid3">{''.join(card(x) for x in related)}</div></section>
</div>"""
    ld = {"@context": "https://schema.org", "@type": "NewsArticle", "headline": a["title"][:110],
          "description": a["dek"], "datePublished": a["dt"].strftime("%Y-%m-%dT09:00:00-07:00"),
          "dateModified": a["dt"].strftime("%Y-%m-%dT09:00:00-07:00"),
          "mainEntityOfPage": f"{SITE}{a['url']}", "articleSection": a["category"],
          "author": {"@type": "Organization", "name": a.get("company") if is_pr else "TNC Newsdesk"},
          "publisher": {"@type": "Organization", "name": NAME, "logo": {"@type": "ImageObject", "url": f"{SITE}/favicon.svg"}}}
    if a.get("image"):
        ld["image"] = [SITE + a["image"]]
    if not is_pr and a.get("company"):
        ld["about"] = {"@type": "Organization", "name": a["company"]}
    crumbs = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": "Press Releases" if is_pr else a["category"], "item": SITE + section},
        {"@type": "ListItem", "position": 3, "name": a["title"]}]}
    head = (f'<meta property="article:published_time" content="{a["dt"].strftime("%Y-%m-%d")}">'
            f'<script type="application/ld+json">{json.dumps(ld)}</script>'
            f'<script type="application/ld+json">{json.dumps(crumbs)}</script>')
    write(a["url"], page(a["title"], body, a["dek"], a["url"], section, head, "article", a.get("image", "")))

def build_list(path, title, intro, items, active, is_pr=False):
    if items:
        grid = '<div class="grid3">' + "".join(card(a) for a in items) + "</div>"
    else:
        grid = '<p class="empty">No stories yet.</p>'
    extra = ""
    if is_pr:
        extra = '<div class="box box-dark inline-cta"><h3>Publish your release here</h3><p>Permanent page, structured data, homepage and newsletter options. From $149.</p><a class="btn" href="/submit/">Submit a release &rarr;</a></div>'
    body = f"""<div class="wrap"><header class="list-h"><h1>{esc(title)}</h1><p>{esc(intro)}</p></header>{extra}{grid}</div>{CTA if not is_pr else ''}"""
    write(path, page(title, body, intro, path, active))

def build_companies(news):
    groups = {}
    for a in news:
        if a.get("company"):
            groups.setdefault(a["company"], []).append(a)
    for co, items in groups.items():
        cats = sorted({a["category"] for a in items})
        intro = f"All {NAME} coverage of {co}: the latest {', '.join(c.lower() for c in cats)} news, with links to every original source."
        build_list(f"/company/{slugify(co)}/", f"{co} News", intro, items, "")
    rows = "".join(f'<li><a href="/company/{slugify(co)}/">{esc(co)}</a><span class="meta">{len(items)} {"story" if len(items) == 1 else "stories"}</span></li>'
                   for co, items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())))
    body = f'<div class="wrap narrow"><header class="list-h"><h1>Companies &amp; Organizations</h1><p>Every company and organization we have covered, with all of our stories about each.</p></header><ul class="list co-index">{rows}</ul></div>'
    write("/companies/", page("Companies & Organizations", body, f"Browse {NAME} coverage by company and organization.", "/companies/"))
    return groups

def build_submit():
    tiers = [
        ("Starter", 149, "For simple announcements", [
            "Published on a permanent TechNewsCompany.com page",
            "Listed in the Press Releases feed and RSS",
            "NewsArticle structured data for search engines",
            "Up to 2 links and 1 image",
            "Published within 1 business day"], False),
        ("Featured", 299, "Most popular for launches and funding", [
            "Everything in Starter",
            "Featured in the homepage Press Releases rail for 7 days",
            "Up to 4 links, 3 images and a video embed",
            "Shared on Tech News Company social channels",
            "Same-day publishing when received by noon PT"], True),
        ("Premium", 599, "We write it for you", [
            "Everything in Featured",
            "Press release written by our team from your notes (1 revision)",
            "Homepage feature for 30 days",
            "Included in the weekly newsletter",
            "Performance report after 30 days"], False),
    ]
    cards = ""
    for name, price, sub, feats, pop in tiers:
        cards += f"""<div class="tier{' pop' if pop else ''}">{'<span class="badge">Most popular</span>' if pop else ''}
  <h3>{name}</h3><p class="tier-sub">{sub}</p><div class="price">${price}<span> USD / release</span></div>
  <ul>{''.join(f'<li>{f}</li>' for f in feats)}</ul>
  <a class="btn {'btn-red' if pop else 'btn-outline'}" href="#order" data-tier="{name}">Choose {name}</a></div>"""
    faqs = [
        ("How fast will my release go live?", "Starter releases go live within one business day. Featured and Premium releases received by noon Pacific time are published the same day."),
        ("Is my release labeled?", "Yes. Every release is clearly marked as a press release and kept separate from our independent news coverage. This protects your brand and keeps our pages trusted by readers and search engines."),
        ("Are links followed?", "Links in press releases carry the rel=\"sponsored\" attribute, which is what Google requires for paid placements. Your release still gets a permanent indexed page, referral traffic and brand search visibility."),
        ("What won't you publish?", "We decline releases that are misleading, make unverifiable financial or medical claims, promote gambling, adult content, or unregistered securities, or attack competitors. If we decline, you are not charged."),
        ("Can I edit after publishing?", "Yes. Small corrections are free within 30 days. Email us with the page link and the change."),
        ("Do you guarantee coverage by other outlets?", "No. We publish and promote your release on Tech News Company. We do not promise pickup by other publications, and anyone who does is overpromising."),
    ]
    faq_html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}
    body = f"""<section class="sub-hero"><div class="wrap">
  <span class="eyebrow">Press release publishing</span>
  <h1>Publish your tech news where tech readers look.</h1>
  <p>Flat pricing, fast turnaround, permanent pages. Built for startups, SaaS companies, hardware makers and the agencies that represent them.</p>
  <div class="hero-btns"><a class="btn btn-red" href="#pricing">View pricing</a><a class="btn btn-ghost" href="#order">Submit now</a></div>
  <div class="trust"><span>&#10003; Live within 1 business day</span><span>&#10003; Permanent indexed page</span><span>&#10003; No subscription</span></div>
</div></section>
<div class="wrap">
<section id="pricing" class="tiers">{cards}</section>
<p class="addons"><strong>Add-ons:</strong> Rush publishing within 4 business hours +$75 &middot; Additional homepage week +$99 &middot; Bulk packs of 5 releases save 20% (email us)</p>
<section class="how"><h2>How it works</h2><div class="steps">
  <div><b>1</b><h3>Submit</h3><p>Send your release text, links and images with the form below.</p></div>
  <div><b>2</b><h3>Review</h3><p>An editor checks formatting and our publishing guidelines and sends a payment link.</p></div>
  <div><b>3</b><h3>Publish</h3><p>Your release goes live on its own page and in our feeds. You get the link to share.</p></div>
</div></section>
<section id="order" class="order"><div class="order-grid">
  <div><h2>Submit your release</h2><p>Fill this out and hit send. It opens a pre-filled email to our editors. We reply with a proof and a payment link, usually within a few hours. You pay only once we approve the release.</p>
  <p class="small">Prefer email? Send your release to <a href="mailto:{ORDER_EMAIL}?subject=Press%20release%20submission">{ORDER_EMAIL}</a>.</p></div>
  <form id="orderForm" class="form" data-email="{ORDER_EMAIL}">
    <label>Package<select name="tier"><option>Starter ($149)</option><option selected>Featured ($299)</option><option>Premium ($599)</option></select></label>
    <div class="two"><label>Your name<input name="name" required></label><label>Work email<input name="email" type="email" required></label></div>
    <div class="two"><label>Company<input name="company" required></label><label>Website<input name="website" type="url" placeholder="https://"></label></div>
    <label>Headline<input name="headline" required maxlength="160"></label>
    <label>Release text, or notes for Premium<textarea name="body" rows="8" required placeholder="Paste your full press release here. Include a dateline, quotes, and your company boilerplate."></textarea></label>
    <label class="chk"><input type="checkbox" name="rush"> Add rush publishing (+$75)</label>
    <label class="chk"><input type="checkbox" name="agree" required> I confirm this release is accurate and I am authorized to publish it on behalf of the company named.</label>
    <button class="btn btn-red" type="submit">Send submission</button>
    <p class="form-msg" hidden></p>
  </form>
</div></section>
<section class="faq"><h2>Questions</h2>{faq_html}</section>
</div>
<script src="/app.js"></script>"""
    write("/submit/", page("Submit a Press Release", body,
        "Publish your technology press release on Tech News Company. Permanent page, same-day publishing, flat pricing from $149.",
        "/submit/", "", f'<script type="application/ld+json">{json.dumps(faq_ld)}</script>'))

def build_static_pages():
    about = """<div class="wrap narrow prose-page"><h1>About Tech News Company</h1>
<p>Tech News Company covers the businesses shaping technology: AI labs, chipmakers, device makers, cloud providers and the startups chasing them. Our newsdesk writes short, factual stories about what companies announced, what it means, and where to read the original.</p>
<p>Every news story links to its primary source or the publication that first reported it. When a story is based on reports rather than an official announcement, we say so in the headline or the first paragraph.</p>
<h2>Press releases</h2>
<p>We also publish press releases for technology companies. Releases are clearly labeled, kept separate from our news coverage, and never influence what our newsdesk covers. <a href="/submit/">See packages and pricing</a>.</p>
<h2>Corrections</h2>
<p>If we got something wrong, tell us through our <a href="/contact/">contact page</a> and we will fix it and note the correction.</p></div>"""
    policy = """<div class="wrap narrow prose-page"><h1>Editorial Policy</h1>
<h2>News coverage</h2>
<p>News stories on Tech News Company are written by our newsdesk based on official company announcements, regulatory filings and reporting by established publications. Each story names and links its source. We do not accept payment for news coverage, and advertisers and press release clients receive no say over it.</p>
<p>When information comes from reports or unnamed sources rather than the company itself, we label it as reported. We do not publish rumors as fact.</p>
<h2>Press releases</h2>
<p>Press releases are paid placements submitted by the issuing company. They are:</p>
<ul><li>Labeled "Press Release" at the top of the page and in every list</li><li>Published in a separate Press Releases section with a disclosure notice</li><li>Marked with rel="sponsored" on all outbound links</li><li>The responsibility of the issuing company, which confirms the content is accurate and that it is authorized to publish it</li></ul>
<p>We decline releases that impersonate another company, make false or unverifiable claims, contain financial promotions for unregistered securities, or target individuals. We remove a release if we learn it is inaccurate.</p>
<h2>Corrections and takedowns</h2>
<p>Errors are corrected promptly with a note. Companies with concerns about coverage can reach us through the <a href="/contact/">contact page</a>.</p></div>"""
    contact = f"""<div class="wrap narrow prose-page"><h1>Contact</h1>
<p><strong>Press release submissions:</strong> use the <a href="/submit/#order">submission form</a>.</p>
<p><strong>News tips, corrections and everything else:</strong> <a href="mailto:{ORDER_EMAIL}?subject=Tech%20News%20Company">{ORDER_EMAIL}</a></p>
<p>We read every message and usually reply within one business day.</p></div>"""
    write("/about/", page("About", about, "About Tech News Company, an independent technology news site and press release publisher.", "/about/"))
    write("/editorial-policy/", page("Editorial Policy", policy, "How Tech News Company separates independent news coverage from paid press releases.", "/editorial-policy/"))
    write("/contact/", page("Contact", contact, "Contact Tech News Company for press release submissions, news tips and corrections.", "/contact/"))
    nf = """<div class="wrap narrow prose-page"><h1>Page not found</h1><p>That page has moved or never existed. Head back to the <a href="/">latest news</a>.</p></div>"""
    write("/404.html", page("Page not found", nf, "", "/404.html"))

def build_feeds(news, rels, groups=None):
    urls = ["/", "/submit/", "/press-releases/", "/about/", "/editorial-policy/", "/contact/"]
    urls += [f"/category/{slugify(c)}/" for c in CATS if c != "Press Release"]
    urls += ["/companies/"] + [f"/company/{slugify(co)}/" for co in (groups or {})]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        sm.append(f"<url><loc>{SITE}{u}</loc></url>")
    for a in news + rels:
        sm.append(f"<url><loc>{SITE}{a['url']}</loc><lastmod>{a['dt'].strftime('%Y-%m-%d')}</lastmod></url>")
    sm.append("</urlset>")
    write("/sitemap.xml", "\n".join(sm))
    allitems = sorted(news + rels, key=lambda a: a["dt"], reverse=True)[:40]
    rss = ['<?xml version="1.0" encoding="UTF-8"?>', '<rss version="2.0"><channel>',
           f"<title>{NAME}</title><link>{SITE}/</link><description>Technology news and press releases</description><language>en-us</language>"]
    for a in allitems:
        rss.append(f"<item><title>{esc(('[Press Release] ' if a['kind']=='release' else '') + a['title'])}</title><link>{SITE}{a['url']}</link>"
                   f"<guid>{SITE}{a['url']}</guid><pubDate>{a['dt'].strftime('%a, %d %b %Y 09:00:00 -0700')}</pubDate>"
                   f"<category>{esc(a['category'])}</category><description>{esc(a['dek'])}</description></item>")
    rss.append("</channel></rss>")
    write("/rss.xml", "\n".join(rss))
    # Google News sitemap: articles from the last 2 days (relative to the newest story)
    newest = max(a["dt"] for a in news)
    ns = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">']
    for a in news:
        if (newest - a["dt"]).days <= 2:
            ns.append(f"<url><loc>{SITE}{a['url']}</loc><news:news><news:publication><news:name>{NAME}</news:name><news:language>en</news:language></news:publication>"
                      f"<news:publication_date>{a['dt'].strftime('%Y-%m-%d')}</news:publication_date><news:title>{esc(a['title'])}</news:title></news:news></url>")
    ns.append("</urlset>")
    write("/news-sitemap.xml", "\n".join(ns))
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\nSitemap: {SITE}/news-sitemap.xml\n")

def main():
    OUT.mkdir(exist_ok=True)
    for x in OUT.iterdir():
        if x.name == ".git":
            continue
        shutil.rmtree(x) if x.is_dir() else x.unlink()
    for f in (ROOT / "static").iterdir():
        shutil.copytree(f, OUT / f.name) if f.is_dir() else shutil.copy(f, OUT / f.name)
    (OUT / "CNAME").write_text("technewscompany.com\n")
    (OUT / ".nojekyll").write_text("")
    news, rels = load("articles", "news"), load("releases", "release")
    build_home(news, rels)
    for a in news + rels:
        build_item(a, news, rels)
    for c in CATS:
        if c == "Press Release":
            continue
        build_list(f"/category/{slugify(c)}/", c, f"The latest {c.lower()} news from Tech News Company.",
                   [a for a in news if a["category"] == c], f"/category/{slugify(c)}/")
    build_list("/press-releases/", "Press Releases", "Announcements submitted by technology companies. Press releases are provided by the issuing company and published as submitted.",
               rels, "/press-releases/", is_pr=True)
    groups = build_companies(news)
    build_submit()
    build_static_pages()
    build_feeds(news, rels, groups)
    write(f"/{INDEXNOW_KEY}.txt", INDEXNOW_KEY)
    print(f"Built {len(news)} news stories, {len(rels)} press releases into {OUT}")

if __name__ == "__main__":
    main()
