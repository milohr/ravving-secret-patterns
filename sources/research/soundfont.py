#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Camilo Higuita <milo.h@aol.com>
# SPDX-License-Identifier: GPL-3.0-or-later
"""Look inside SF2 / SF3 soundfonts before putting them in kits.json, and hear them without
ravving: what a FluidSynth sound source needs to know. Runs on the laptop or the device
(python3 only; `render` needs fluidsynth).

  soundfont.py presets FILE…      every preset: bank:program and name (the `bank` / `program`
                                  a kits.json source takes; most SFZ-converted fonts hold one
                                  preset at 0:0, ACBass.sf3 only one at 0:3)
  soundfont.py ranges FILE…       the key range and velocity range the instrument zones cover
                                  (a font whose zones say velRange 0–0 is mute at any velocity:
                                  SynStrings, LaString, MelloString and Organ on the image)
  soundfont.py keys FILE… [--bank B --program P]
                                  a preset's zones, key by key: the key range each covers and
                                  its instrument's name, to see how a kit lays its drums out
                                  (unnamed instruments, as the AVL kits', fall back to the
                                  General MIDI keys in DrumKit) or where a font's notes sit
  soundfont.py render FILE… [--notes 48,52,55,59] [--seconds 3] [--velocity 96] [--bank B --program P]
                                  render one chord offline (fluidsynth -F) and print the level
                                  every quarter second: whether and how fast the font speaks
                                  (select the preset a kits.json source names with --bank/--program)
  soundfont.py categorise FILE… [--json]
                                  propose kits.json sources: a category from the font's name
                                  and folder ("Strings · Fat", "Organ · Pipe", "Alien · Winds"
                                  for the Ambients & Drones fonts, Keys, Bass, Guitar, Winds,
                                  Voices, Synth, Drums, Other), the first preset's bank and
                                  program (its first; --all-presets lists every one of a font
                                  that holds several), and MUTE for a font whose zones say
                                  velRange 0–0; --json prints the entries ready to paste into a
                                  machine's "sources" (mute fonts left out). The categories are
                                  words in the name or folder (CATEGORIES below): review the
                                  proposal, it is a start, not a verdict

On the device: `scp sources/research/soundfont.py root@<device>:/tmp/` then
`ssh root@<device> python3 /tmp/soundfont.py presets "/zynthian/zynthian-data/soundfonts/SFZ Synths/"*.sf3`.
"""
import argparse
import math
import re
import struct
import subprocess
import sys
import tempfile
import wave

GENERATORS = {5: "modLfoToPitch", 6: "vibLfoToPitch", 7: "modEnvToPitch", 8: "initialFilterFc", 9: "initialFilterQ", 10: "modLfoToFilterFc",
              11: "modEnvToFilterFc", 13: "modLfoToVolume", 15: "chorus", 16: "reverb", 17: "pan", 21: "delayModLFO", 22: "freqModLFO",
              23: "delayVibLFO", 24: "freqVibLFO", 25: "delayModEnv", 26: "attackModEnv", 27: "holdModEnv", 28: "decayModEnv",
              29: "sustainModEnv", 30: "releaseModEnv", 33: "delayVolEnv", 34: "attackVolEnv", 35: "holdVolEnv", 36: "decayVolEnv",
              37: "sustainVolEnv", 38: "releaseVolEnv", 41: "instrument", 43: "keyRange", 44: "velRange", 48: "initialAttenuation",
              51: "coarseTune", 52: "fineTune", 53: "sampleID", 54: "sampleModes", 56: "scaleTuning", 57: "exclusiveClass", 58: "overridingRootKey"}


def chunk(data, tag):
    """The payload of the first RIFF sub-chunk called `tag` (the pdta chunks are unique)."""
    i = data.find(tag)
    if i < 0:
        return b""
    size = struct.unpack("<I", data[i + 4:i + 8])[0]
    return data[i + 8:i + 8 + size]


def presets(path):
    """[(bank, program, name)] from the phdr chunk (its last record is the terminator)."""
    phdr = chunk(open(path, "rb").read(), b"phdr")
    out = []
    for off in range(0, len(phdr) - 38, 38):
        name = phdr[off:off + 20].split(b"\0")[0].decode("latin1")
        program, bank = struct.unpack("<HH", phdr[off + 20:off + 24])
        out.append((bank, program, name))
    return out


def preset_keys(path, bank=0, program=0):
    """A preset's zones in key order: [(key range or None, instrument name)]."""
    data = open(path, "rb").read()
    phdr, pbag, pgen, inst = (chunk(data, t) for t in (b"phdr", b"pbag", b"pgen", b"inst"))
    u16 = lambda b, o: struct.unpack("<H", b[o:o + 2])[0]  # noqa: E731
    for record in range(0, len(phdr) - 38, 38):
        if (u16(phdr, record + 22), u16(phdr, record + 20)) != (bank, program):
            continue
        out = []
        for zone in range(u16(phdr, record + 24), u16(phdr, record + 38 + 24)):
            key_range, instrument = None, None
            for gen in range(u16(pbag, zone * 4), u16(pbag, zone * 4 + 4)):
                op = u16(pgen, gen * 4)
                if op == 43:
                    key_range = (pgen[gen * 4 + 2], pgen[gen * 4 + 3])
                elif op == 41:
                    instrument = u16(pgen, gen * 4 + 2)
            if instrument is not None:
                out.append((key_range, inst[instrument * 22:instrument * 22 + 20].split(b"\0")[0].decode("latin1")))
        return sorted(out, key=lambda zone: zone[0] or (0, 0))
    return []


def ranges(path):
    """The key and velocity ranges over every instrument zone, and the generators used."""
    data = open(path, "rb").read()
    igen = chunk(data, b"igen")
    keys, velocities, used = [], [], {}
    for off in range(0, len(igen) - 3, 4):
        op, = struct.unpack("<H", igen[off:off + 2])
        if op == 43:
            keys.append((igen[off + 2], igen[off + 3]))
        elif op == 44:
            velocities.append((igen[off + 2], igen[off + 3]))
        elif op not in (41, 53):
            used.setdefault(GENERATORS.get(op, str(op)), set()).add(struct.unpack("<h", igen[off + 2:off + 4])[0])
    return keys, velocities, used


def midi_file(notes, seconds, velocity):
    """A one-chord MIDI file: `notes` held for `seconds` at 120 BPM (480 ticks a beat), then two beats of rest."""
    def vlq(v):
        out = [v & 0x7f]
        v >>= 7
        while v:
            out.append((v & 0x7f) | 0x80)
            v >>= 7
        return bytes(reversed(out))
    ticks = int(seconds * 960)
    events = b"".join(vlq(0) + bytes([0x90, n, velocity]) for n in notes)
    events += vlq(ticks) + bytes([0x80, notes[0], 0]) + b"".join(vlq(0) + bytes([0x80, n, 0]) for n in notes[1:])
    events += vlq(960) + b"\xff\x2f\x00"
    track = b"MTrk" + struct.pack(">I", len(events)) + events
    return b"MThd" + struct.pack(">IHHH", 6, 0, 1, 480) + track


def render(path, notes, seconds, velocity, bank=None, program=None):
    """Render the chord with fluidsynth and return the RMS of every quarter second (first 6 s);
    with a bank and program, that preset is selected first (as ravving's engine does)."""
    with tempfile.NamedTemporaryFile(suffix=".mid") as mid, tempfile.NamedTemporaryFile(suffix=".wav") as out, tempfile.NamedTemporaryFile(suffix=".txt", mode="w") as commands:
        mid.write(midi_file(notes, seconds, velocity))
        mid.flush()
        extra = []
        if bank is not None and program is not None:
            commands.write("select 0 1 %d %d\n" % (bank, program))
            commands.flush()
            extra = ["-f", commands.name]
        result = subprocess.run(["fluidsynth", "-ni", "-q", "-g", "1", "-r", "48000"] + extra + ["-F", out.name, path, mid.name], capture_output=True, text=True)
        w = wave.open(out.name)
        frames, rate, channels = w.getnframes(), w.getframerate(), w.getnchannels()
        samples = struct.unpack("<%dh" % (frames * channels), w.readframes(frames))
    window = int(rate * 0.25) * channels
    levels = []
    for i in range(0, min(len(samples), int(rate * 6) * channels), window):
        segment = samples[i:i + window]
        levels.append(math.sqrt(sum(x * x for x in segment) / max(1, len(segment))) / 32768)
    warnings = [line for line in (result.stderr + result.stdout).splitlines() if "channel 9" not in line]
    return levels, warnings


CATEGORIES = [
    # the category, and the words in a font's name (lower case) or folder that put it there
    ("Drums", ["drum", "kit", "perc", "808", "909", "linn"]),
    ("Alien", ["ambient", "drone", "atmos", "space", "alien", "chaos", "extrange", "strange", "cristal", "crystal", "glassy", "the thing", "the pulse", "winds", "heeling", "decadence", "falling", "half live", "the heart", "the love", "tubell"]),
    ("Strings", ["string", "violin", "cello", "viola", "ensemble", "orchestra"]),
    ("Organ", ["organ", "b3", "hammond", "farfisa"]),
    ("Keys", ["piano", "rhodes", "wurlitzer", "clav", "keys", "epiano", "e-piano", "harpsi", "vibes", "marimba", "bell", "celest", "glock"]),
    ("Bass", ["bass", "bazz", "sub ", "303"]),
    ("Guitar", ["guitar", "strat", "tele", "nylon", "djent", "banjo", "mandolin", "ukulele"]),
    ("Winds", ["sax", "trumpet", "horn", "brass", "flute", "oboe", "clarinet", "bassoon", "trombone", "tuba", "harmonica", "whistle", "pan pipe", "accordion"]),
    ("Voices", ["voice", "choir", "vox", "vocal", "aah", "ooh"]),
    ("Synth", ["synth", "saw", "square", "lead", "pad", "sync", "laser", "prophet", "oberheim", "juno", "moog", "ob-", "dx7", "fm ", "vangelis", "trance", "dance", "modsynth", "beeper", "sine", "harp"]),
]


def categorise(path):
    """A proposal for one font: (category, display name, [(bank, program, preset name)], mute, note)."""
    import os
    name = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.basename(os.path.dirname(path))
    haystack = (folder + " / " + name).lower()
    category = "Other"
    for candidate, words in CATEGORIES:
        if any(word in haystack for word in words):
            category = candidate
            break
    # the display name: the file's, without the category word repeated as a word of its own
    # ("Ensemble Strings" → "Ensemble", "Funky Guitars" → "Funky", "PhaserOrgan" → "Phaser")
    display = name
    for word in {category, category.rstrip("s")}:
        display = re.sub(r"(?i)\b%ss?\b" % re.escape(word), " ", display)
        display = re.sub(r"(?i)(?<=[a-z])%ss?$" % re.escape(word), "", display)
    display = re.sub(r"\s+", " ", display).strip(" -_·")
    if not display:
        display = name
    found = presets(path)
    keys, velocities, used = ranges(path)
    mute = bool(velocities) and max(v[1] for v in velocities) == 0
    note = "MUTE (velRange 0–0)" if mute else ("%d presets" % len(found) if len(found) > 1 else "")
    return category, display, found, mute, note


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("command", choices=["presets", "ranges", "keys", "render", "categorise"])
    parser.add_argument("--json", action="store_true", help="categorise: print kits.json source entries")
    parser.add_argument("--all-presets", action="store_true", help="categorise --json: one entry per preset of a font that holds several (else its first)")
    parser.add_argument("files", nargs="+")
    parser.add_argument("--notes", default="48,52,55,59")
    parser.add_argument("--seconds", type=float, default=3)
    parser.add_argument("--velocity", type=int, default=96)
    parser.add_argument("--bank", type=int, help="render, keys: the preset's bank (with --program)")
    parser.add_argument("--program", type=int, help="render, keys: the preset's program")
    args = parser.parse_args()
    for path in args.files:
        label = path.split("/soundfonts/")[-1]
        if args.command == "presets":
            print(label, "|", "; ".join("%d:%d %s" % p for p in presets(path)))
        elif args.command == "ranges":
            keys, velocities, used = ranges(path)
            key_text = "keys %d–%d" % (min(k[0] for k in keys), max(k[1] for k in keys)) if keys else "keys all"
            vel_text = "velocity %d–%d" % (min(v[0] for v in velocities), max(v[1] for v in velocities)) if velocities else "velocity all"
            mute = " MUTE (velRange 0–0)" if velocities and max(v[1] for v in velocities) == 0 else ""
            print(label, "|", key_text, "|", vel_text + mute, "|", ", ".join(sorted(used)))
        elif args.command == "keys":
            for key_range, name in preset_keys(path, args.bank or 0, args.program or 0):
                print(label, "|", "keys %d–%d" % key_range if key_range else "keys all", "|", name)
        elif args.command == "render":
            levels, warnings = render(path, [int(n) for n in args.notes.split(",")], args.seconds, args.velocity, args.bank, args.program)
            print(label.ljust(44), " ".join("%.2f" % v for v in levels[:16]), ("| " + " | ".join(warnings)) if warnings else "")
        else:
            category, display, found, mute, note = categorise(path)
            if args.json:
                import json
                if mute:
                    continue
                for bank, program, preset in (found if args.all_presets else found[:1]):
                    source = {"name": "%s · %s" % (category, display if len(found) == 1 or not args.all_presets else preset),
                              "engine": {"type": "fluidsynth", "soundfont": path, "bank": bank, "program": program}}
                    print(json.dumps(source, ensure_ascii=False) + ",")
            else:
                first = "%d:%d" % found[0][:2] if found else "?"
                print(("%s · %s" % (category, display)).ljust(34), "|", label.ljust(50), "|", first, "|", note)
    return 0


if __name__ == "__main__":
    sys.exit(main())
