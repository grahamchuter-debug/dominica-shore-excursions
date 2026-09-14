#!/usr/bin/env python3
"""Build the Dominica content site as static HTML. No commerce."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"
ORIGIN = "https://dominicashoreexcursions.com"
UPDATED = "2026-09-14"

NAV = [
    ("/best-dominica-shore-excursions", "Excursions"),
    ("/dominica-cruise-port-guide", "Cruise Port Guide"),
    ("/dominica-waterfalls-hot-springs", "Waterfalls"),
    ("/titou-gorge", "Titou Gorge"),
    ("/champagne-reef-snorkeling", "Snorkelling"),
    ("/whale-watching-dominica", "Whale Watching"),
    ("/one-day-in-dominica-from-cruise-port", "One Day"),
]

FOOT = [
    ("Excursions", [
        ("/best-dominica-shore-excursions", "Compare excursion ideas"),
        ("/trafalgar-falls", "Trafalgar Falls"),
        ("/titou-gorge", "Titou Gorge"),
        ("/emerald-pool-dominica", "Emerald Pool"),
        ("/dominica-waterfalls-hot-springs", "Waterfalls and rainforest"),
        ("/champagne-reef-snorkeling", "Champagne Reef"),
    ]),
    ("Planning", [
        ("/dominica-cruise-port-guide", "Roseau cruise port guide"),
        ("/one-day-in-dominica-from-cruise-port", "One day from the port"),
        ("/best-beaches-dominica-cruise-passengers", "Beaches"),
        ("/whale-watching-dominica", "Whale watching"),
        ("/private-dominica-tours", "Private-tour ideas"),
        ("/kalinago-cultural-tour-dominica", "Kalinago heritage"),
    ]),
]


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def nav(current: str) -> str:
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n        ".join(links)


def crumbs_html(items: list[tuple[str, str]]) -> str:
    bits = ['<a href="/">Home</a>']
    for href, label in items[:-1]:
        bits.append(f'<a href="{href}">{esc(label)}</a>')
    bits.append(esc(items[-1][1]))
    return '<p class="crumbs">' + " / ".join(bits) + "</p>"


def faq_html(faqs: list[tuple[str, str]]) -> str:
    if not faqs:
        return ""
    blocks = []
    for q, a in faqs:
        blocks.append(f'<div class="faq"><h3>{esc(q)}</h3><p>{a}</p></div>')
    return "<h2>Questions cruise passengers ask</h2>\n" + "\n".join(blocks)


def related_html(links: list[tuple[str, str, str]]) -> str:
    cards = []
    for href, title, blurb in links:
        cards.append(
            f'<a href="{href}"><strong>{esc(title)}</strong><span>{esc(blurb)}</span></a>'
        )
    return '<div class="related">' + "".join(cards) + "</div>"


def schema(path: str, title: str, description: str, crumbs: list[tuple[str, str]], faqs: list[tuple[str, str]]) -> str:
    url = ORIGIN + path
    graph: list[dict] = [
        {
            "@type": "WebSite",
            "@id": ORIGIN + "/#website",
            "url": ORIGIN + "/",
            "name": "Dominica Shore Excursions",
            "description": "Independent planning guides for cruise passengers visiting Dominica.",
        },
        {
            "@type": "Article",
            "headline": title,
            "description": description,
            "dateModified": UPDATED,
            "mainEntityOfPage": url,
            "author": {"@type": "Organization", "name": "Dominica Shore Excursions"},
            "publisher": {"@type": "Organization", "name": "Dominica Shore Excursions", "url": ORIGIN + "/"},
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": i + 1, "name": label, "item": ORIGIN + href}
                for i, (href, label) in enumerate([("/", "Home"), *crumbs])
            ],
        },
    ]
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in faqs
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def page(
    path: str,
    filename: str,
    title: str,
    description: str,
    h1: str,
    body: str,
    crumbs: list[tuple[str, str]] | None = None,
    faqs: list[tuple[str, str]] | None = None,
    related: list[tuple[str, str, str]] | None = None,
    hero_html: str = "",
) -> dict:
    crumbs = crumbs or []
    faqs = faqs or []
    related = related or []
    crumb_block = crumbs_html(crumbs) if crumbs else ""
    faq_block = faq_html(faqs)
    rel_block = related_html(related) if related else ""
    foot_cols = []
    for heading, links in FOOT:
        items = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in links)
        foot_cols.append(f"<div><h2>{heading}</h2><ul>{items}</ul></div>")
    if hero_html:
        opening = hero_html
        prose_open = '<div class="prose section">'
        prose_close = "</div>"
    else:
        opening = f'<div class="prose section"><h1>{h1}</h1>'
        prose_open = ""
        prose_close = "</div>"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{ORIGIN}{path}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{ORIGIN}{path}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,620&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/site.css">
  <script type="application/ld+json">{schema(path, h1, description, crumbs, faqs)}</script>
</head>
<body>
  <a class="skip" href="#content">Skip to content</a>
  <header class="site-header">
    <div class="header-bar wrap">
      <a class="brand" href="/">
        <svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#0d3a30"/><path d="M6 22c4-9 7-14 10-14s6 5 10 14" fill="none" stroke="#e7f0ea" stroke-width="1.7"/><path d="M16 8v14" stroke="#c47a5a" stroke-width="1.4"/></svg>
        <span><strong>Dominica Shore Excursions</strong><span>Planning guides</span></span>
      </a>
      <input class="nav-toggle" type="checkbox" id="nav-toggle">
      <label class="nav-btn" for="nav-toggle">Menu</label>
      <nav class="site-nav" aria-label="Primary">
        {nav(path)}
      </nav>
    </div>
  </header>
  <main id="content">
    <article class="wrap">
      {crumb_block}
      {opening}
      {prose_open}
      {body}
      {faq_block}
      {f'<h2>Continue planning</h2>{rel_block}' if rel_block else ''}
      <p class="updated">Planning guide updated {UPDATED}. This site does not sell tours.</p>
      {prose_close}
    </article>
  </main>
  <footer class="site-footer">
    <div class="wrap foot-grid">
      <div>
        <h2>Dominica Shore Excursions</h2>
        <p>Independent guides for cruise passengers planning a day around Roseau. Not a tour operator, and not affiliated with any cruise line.</p>
      </div>
      {''.join(foot_cols)}
    </div>
    <div class="wrap fine">
      <p>Editorial planning only. Journey times, access, sea conditions and any operator arrangements vary. Confirm details yourself before you go ashore. No prices or availability are published here.</p>
    </div>
  </footer>
</body>
</html>
"""
    return {"path": path, "filename": filename, "title": title, "html": html, "faqs": faqs}


def not_found() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Page not found | Dominica Shore Excursions</title>
  <meta name="robots" content="noindex, follow">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/css/site.css">
</head>
<body>
  <main id="content" class="wrap prose section">
    <p class="eyebrow">404</p>
    <h1>That page is not on this guide</h1>
    <p>The address does not match a Dominica planning page. Nothing has been moved to the homepage in its place.</p>
    <div class="actions">
      <a class="btn" href="/">Homepage</a>
      <a class="btn-quiet" href="/best-dominica-shore-excursions">Excursion ideas</a>
      <a class="btn-quiet" href="/dominica-cruise-port-guide">Cruise port guide</a>
    </div>
  </main>
</body>
</html>
"""


def write_site() -> None:
    import sys
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from content_pages import all_pages

    ROOT.mkdir(parents=True, exist_ok=True)
    pages = all_pages()
    paths = {p["path"] for p in pages}
    for item in pages:
        (ROOT / item["filename"]).write_text(item["html"], encoding="utf-8")
        if 'rel="canonical" href="' + ORIGIN + item["path"] + '"' not in item["html"]:
            raise SystemExit(f"canonical mismatch {item['path']}")
        if ".html" in item["html"].split("canonical")[1][:80]:
            raise SystemExit(f"html canonical {item['path']}")

    (ROOT / "404.html").write_text(not_found(), encoding="utf-8")

    locs = []
    for item in pages:
        priority = "1.0" if item["path"] == "/" else "0.8"
        locs.append(
            f"""  <url>
    <loc>{ORIGIN}{item['path']}</loc>
    <lastmod>{UPDATED}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>"""
        )
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(locs)
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /content/\nDisallow: /partials/\n\n"
        f"Sitemap: {ORIGIN}/sitemap.xml\n",
        encoding="utf-8",
    )

    rules = [
        "/whale-watching /whale-watching-dominica 301",
        "/whale-watching.html /whale-watching-dominica 301",
        "/whale-watching/ /whale-watching-dominica 301",
        "/index.html / 301",
    ]
    old_content = {
        "/content/home": "/",
        "/content/home.html": "/",
        "/content/page-starter": "/",
        "/content/page-starter.html": "/",
    }
    for item in pages:
        if item["path"] == "/":
            continue
        slug = item["path"].strip("/")
        rules.append(f"/{slug}.html {item['path']} 301")
        rules.append(f"/{slug}/ {item['path']} 301")
        old_content[f"/content/{slug}"] = item["path"]
        old_content[f"/content/{slug}.html"] = item["path"]
    for src, dest in old_content.items():
        rules.append(f"{src} {dest} 301")
    for item in pages:
        if item["path"] == "/":
            rules.append("/ /index.html 200")
        else:
            rules.append(f"{item['path']} /{item['filename']} 200")
    rules.append("/partials/* / 301")
    rules.append("/content/* / 301")
    (ROOT / "_redirects").write_text("\n".join(rules) + "\n", encoding="utf-8")
    (ROOT / "_headers").write_text(
        "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n\n"
        "/404.html\n  X-Robots-Tag: noindex\n",
        encoding="utf-8",
    )

    banned = ["Book a Tour", "Book now", "Check availability", "best seller", "selling fast", "AggregateRating", '"@type": "Product"', '"@type": "Offer"']
    blob = "\n".join(p["html"] for p in pages)
    for word in banned:
        if word.lower() in blob.lower():
            raise SystemExit(f"banned phrase: {word}")
    for needle in ["whale-watching-dominica.jpg", "titou-gorge.jpg", "bonaire", "tortola", "magens", "jost"]:
        if needle in blob.lower():
            raise SystemExit(f"unsafe asset reference: {needle}")
    if len(paths) != 13:
        raise SystemExit(f"expected 13 pages, got {len(paths)}")
    print(f"wrote {len(pages)} pages to {ROOT}")


if __name__ == "__main__":
    write_site()
