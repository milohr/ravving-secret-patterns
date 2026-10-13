#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Camilo Higuita <milo.h@aol.com>
# SPDX-License-Identifier: GPL-3.0-or-later
#
# The release zip, ready to unzip onto a USB stick's root: the repository's ravving/ folder
# (every pack's presets and templates, as a stick holds them) and the README beside it, with
# no wrapper folder around them.
#
#     ravving/presets/<drums|bass|lead|chords>/patterns/<Genre> · <Name>.json
#     ravving/presets/templates/<name>.json
#     README.md
#
# Run validate.py first: it fails on a file two packs write, or one the device can't read.
#   python3 sources/build-zip.py [OUT.zip]      # default: ravving-packs.zip

import os
import sys
import zipfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "ravving-packs.zip"
    files = []
    for folder, dirs, names in os.walk(os.path.join(REPO, "ravving")):
        dirs.sort()
        files += [os.path.join(folder, name) for name in sorted(names)]
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, os.path.relpath(path, REPO).replace(os.sep, "/"))
        archive.write(os.path.join(REPO, "README.md"), "README.md")
    patterns = sum(1 for path in files if f"{os.sep}patterns{os.sep}" in path)
    print(f"{out}: {patterns} pattern presets and {len(files) - patterns} templates under ravving/presets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
