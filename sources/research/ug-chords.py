#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Camilo Higuita <milo.h@aol.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Fetch songs' chord sheets or tabs from Ultimate Guitar, for a genre pack's research.

Each query is "artist::title" (the search goes by title: the artist picks among the results;
without it the most voted result of any artist is taken, which is often another song), with a
"TAB:" prefix to prefer a tab (riffs) over a chord sheet. Each sheet is saved as text in OUT_DIR
(the source URL, its votes, key and capo on the first line); --summary then prints each saved
sheet's chord sequence, the quick way to read a style's progressions.

    sources/research/ug-chords.py OUT_DIR "the cure::a forest" "TAB:darkthrone::transilvanian hunger"
    sources/research/ug-chords.py OUT_DIR --summary

Reads the pages' embedded JSON (data-content), as a browser gets them; a second between
requests. The sheets are the site's users' transcriptions: check what a pack quotes against the
recording, and quote progressions, not lyrics or whole arrangements.
"""

import argparse
import glob
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

UA = "Mozilla/5.0 (X11; Linux x86_64) Firefox/130.0"
CHORD = re.compile(r"^[A-G][#b]?(m|maj|min|dim|aug|sus|add|[0-9]|/|[#b]|\(|\))*(/[A-G][#b]?)?$")


def get(url):
    return subprocess.run(["curl", "-sL", "-A", UA, url], capture_output=True, text=True).stdout


def page_data(text):
    match = re.search(r'data-content="([^"]+)"', text)
    return json.loads(html.unescape(match.group(1))) if match else None


def find(node, key):
    if isinstance(node, dict):
        if key in node:
            return node[key]
        node = list(node.values())
    if isinstance(node, list):
        for value in node:
            found = find(value, key)
            if found is not None:
                return found
    return None


def fetch(out, query):
    kind = "Chords"
    if query.startswith("TAB:"):
        kind, query = "Tabs", query[4:]
    artist, title = query.split("::", 1) if "::" in query else ("", query)
    data = page_data(get("https://www.ultimate-guitar.com/search.php?search_type=title&value=" + urllib.parse.quote(title)))
    results = [r for r in (find(data, "results") or []) if isinstance(r, dict) and r.get("type") in ("Chords", "Tabs")
               and artist.lower() in (r.get("artist_name") or "").lower()]
    results.sort(key=lambda r: (r.get("type") != kind, -(r.get("votes") or 0)))
    if not results:
        print("none:", query)
        return
    best = results[0]
    tab = page_data(get(best["tab_url"]))
    wiki = find(tab, "wiki_tab")
    meta = find(tab, "meta") or {}
    content = re.sub(r"\[/?(ch|tab)\]", "", wiki["content"]) if wiki else ""
    name = re.sub(r"\W+", "_", f"{artist} {title}".strip())[:48]
    with open(os.path.join(out, name + ".txt"), "w") as f:
        f.write(f"# {best.get('artist_name')} - {best.get('song_name')} ({best.get('type')}, votes {best.get('votes')}, "
                f"{best['tab_url']}) key {meta.get('tonality')} capo {meta.get('capo')}\n{content}")
    print(f"{best.get('artist_name')} - {best.get('song_name')} ({best.get('type')}, {best.get('votes')} votes)")


def summary(out):
    for path in sorted(glob.glob(os.path.join(out, "*.txt"))):
        lines = open(path).read().split("\n")
        chords = []
        for line in lines[1:]:
            tokens = line.split()
            if tokens and all(CHORD.match(t.strip("()")) or t in ("|", "x2", "x4", "-", "/") for t in tokens):
                chords += [t for t in tokens if CHORD.match(t.strip("()"))]
        print(lines[0][:150])
        print("   ", " ".join(chords[:48]) or "(a tab: read its staff lines)")


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("out")
    parser.add_argument("queries", nargs="*")
    parser.add_argument("--summary", action="store_true", help="print each saved sheet's chord sequence")
    args = parser.parse_args()
    os.makedirs(args.out, exist_ok=True)
    for query in args.queries:
        fetch(args.out, query)
        time.sleep(1)
    if args.summary:
        summary(args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
