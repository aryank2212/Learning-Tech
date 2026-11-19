#!/usr/bin/env python3
"""Polite, depth-limited offline copy of one website (standard library only).

Usage: mirror_site.py START_URL OUT_DIR MAX_DEPTH MAX_MB

- Stays on the start host and obeys robots.txt.
- Pauses between requests, caps total pages and size.
- Saves files under OUT_DIR/<host>/<path>. Links are not rewritten,
  so some links only work while online.
"""
import os, random, re, sys, time, urllib.error, urllib.robotparser, urllib.parse, urllib.request, hashlib
from collections import deque
from html.parser import HTMLParser

UA = "learning-library-fetch/1.0 (personal offline reading copy)"
SKIP_EXT = (".mp4", ".mp3", ".zip", ".tar", ".gz", ".mov", ".avi", ".webm", ".exe", ".dmg", ".iso")
MAX_PAGES = 300

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.anchors, self.assets = [], []
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "a" and d.get("href"):
            self.anchors.append(d["href"])
        elif tag in ("img", "script", "source") and d.get("src"):
            self.assets.append(d["src"])
        elif tag == "link" and d.get("href"):
            self.assets.append(d["href"])

def local_path(out_root, url, is_html):
    parts = urllib.parse.urlsplit(url)
    path = parts.path or "/"
    segs = [s for s in path.split("/") if s not in ("", ".", "..")]
    if path.endswith("/") or not segs:
        segs.append("index.html")
    elif is_html and "." not in segs[-1]:
        segs.append("index.html")
    name = os.path.join(out_root, parts.netloc, *segs)
    if parts.query:
        root, ext = os.path.splitext(name)
        name = f"{root}__{hashlib.md5(parts.query.encode()).hexdigest()[:8]}{ext}"
    return name

def load_robots(start):
    """Fetch robots.txt with our own user agent (Python's default one is blocked by some sites).
    Returns a parser, None when there is no robots.txt (4xx: allowed), or False when it can't be read (5xx/network)."""
    url = urllib.parse.urljoin(start, "/robots.txt")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=30) as r:
            lines = r.read().decode("utf-8", errors="replace").splitlines()
    except urllib.error.HTTPError as e:
        return None if 400 <= e.code < 500 else False
    except Exception:
        return False
    rp = urllib.robotparser.RobotFileParser()
    rp.parse(lines)
    return rp

def main():
    start, out_dir, max_depth, max_mb = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4])
    host = urllib.parse.urlsplit(start).netloc
    rp = load_robots(start)
    if rp is False:
        print(f"  robots.txt for {host} could not be read safely; skipping this site", file=sys.stderr)
        return 1
    seen, queue = set(), deque([(start, 0)])
    total, pages, fails = 0, 0, 0
    while queue and pages < MAX_PAGES and total < max_mb * 1024 * 1024:
        url, depth = queue.popleft()
        url = urllib.parse.urldefrag(url)[0]
        if url in seen:
            continue
        seen.add(url)
        p = urllib.parse.urlsplit(url)
        if p.netloc != host or p.path.lower().endswith(SKIP_EXT):
            continue
        if rp is not None and not rp.can_fetch(UA, url):
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                ctype = r.headers.get("Content-Type", "")
                final = r.geturl()
                data = r.read(40 * 1024 * 1024)
        except Exception as e:
            fails += 1
            print(f"  skip {url}: {e}", file=sys.stderr)
            continue
        is_html = "html" in ctype
        target = local_path(out_dir, final, is_html)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "wb") as f:
            f.write(data)
        total += len(data); pages += 1
        if is_html:
            parser = Links()
            try:
                parser.feed(data.decode("utf-8", errors="replace"))
            except Exception:
                pass
            if depth < max_depth:
                for href in parser.anchors:
                    queue.append((urllib.parse.urljoin(final, href), depth + 1))
            for src in parser.assets:  # assets belong to the same page depth
                queue.append((urllib.parse.urljoin(final, src), depth))
        time.sleep(0.6 + random.random() * 0.6)
    print(f"  saved {pages} files, {total/1048576:.1f} MB, {fails} failed -> {out_dir}")
    return 0 if pages else 1

if __name__ == "__main__":
    sys.exit(main())
