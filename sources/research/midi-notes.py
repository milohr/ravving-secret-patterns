#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Camilo Higuita <milo.h@aol.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Print a MIDI file's notes, track by track, by name: the quick way to read a public-domain
melody (a chant, a traditional tune) off a MIDI file into a pack's scale degrees.

    curl -sLo dies.mid https://www.mfiles.co.uk/downloads/gregorian-dies-irae.mid
    sources/research/midi-notes.py dies.mid [--max 64]

Each track with notes: its count, then the note-ons in order ("F4 E4 F4 D4 …"; notes struck
together appear one after another). Read the file with python3 -I (it is downloaded data).
"""

import argparse
import struct
import sys

NAMES = ["C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]


def vlq(data, i):
    value = 0
    while True:
        byte = data[i]
        i += 1
        value = (value << 7) | (byte & 0x7F)
        if not byte & 0x80:
            return value, i


def tracks(data):
    i = 14 + struct.unpack(">I", data[4:8])[0] - 6 if data[:4] == b"MThd" else 0
    while i + 8 <= len(data):
        length = struct.unpack(">I", data[i + 4:i + 8])[0]
        if data[i:i + 4] == b"MTrk":
            yield data[i + 8:i + 8 + length]
        i += 8 + length


def notes(track):
    j, status, out = 0, 0, []
    while j < len(track):
        _, j = vlq(track, j)
        byte = track[j]
        if byte == 0xFF:
            length, k = vlq(track, j + 2)
            j = k + length
            continue
        if byte in (0xF0, 0xF7):
            length, k = vlq(track, j + 1)
            j = k + length
            continue
        if byte & 0x80:
            status = byte
            j += 1
        kind = status & 0xF0
        if kind in (0xC0, 0xD0):
            j += 1
            continue
        note, velocity = track[j], track[j + 1]
        j += 2
        if kind == 0x90 and velocity > 0:
            out.append(note)
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("file")
    parser.add_argument("--max", type=int, default=64)
    args = parser.parse_args()
    data = open(args.file, "rb").read()
    for n, track in enumerate(tracks(data)):
        played = notes(track)
        if played:
            print(f"track {n}: {len(played)} notes")
            print("   ", " ".join(NAMES[x % 12] + str(x // 12 - 1) for x in played[:args.max]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
