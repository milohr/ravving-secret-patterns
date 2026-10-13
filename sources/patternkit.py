#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Camilo Higuita <milo.h@aol.com>
# SPDX-License-Identifier: GPL-3.0-or-later
#
# What every genre pack's build.py (sources/<pack>/build.py) writes its presets with: the same
# files as the jazz pack (sources/jazz/build.py), one per preset, into the repository's one
# ravving/presets tree, laid out as a USB stick holds them (PresetExchange), so the repository's
# root copied to a stick's root is read as it is:
#
#     ravving/presets/<drums|bass|lead|chords>/patterns/<Genre> · <Name>.json
#     ravving/presets/templates/<Genre>.json (and "<Genre> · <Groove>.json")
#
# Each pack lists the files it wrote in its files.txt (Outputs), which validate.py reads to
# find each pack's presets and to refuse a file two packs write.
#     {"ravving": "preset", "type": "pattern", "library": "<x>-presets.json",
#      "preset": {"name", "genre", "chart", "sound"}}
#
# "sound" is the sound the pattern is meant for, a subset of Machine::soundState():
# {"soundSource": "<a source of the machine>"} for the bass, lead and chords (kits.json's
# machines[].sourceName or sources[].name), {"kit": "<kit path>"} for the drums
# (DrumMachine::kitPath()). validate.py checks the names against kits.json.
#
# A bass, lead or chords preset may bring MODS for its source too (mods={"CARD/KNOB": value}),
# written in the engine's own units as data/engines.json gives each knob's min and max (the
# soundfonts' FILTER/CUTOFF in cents, -8400 to 0), or a choice knob by its label: they go in as
# the knob positions the machine keeps (0-1), under "sourceSound" for a soundfont source (one
# set for all of a machine's soundfonts) or "sourceSounds"/<source> for a synth source (the
# 808 · Monosynth). A drums preset's MODS are its kit's (engines.json's kitSound: TONE, SHAPE,
# PITCH on the whole kit), under "sound". Loading the preset WITH ITS SOUND + MODS puts that
# set back whole (its other knobs at rest); a preset without MODS leaves the machine's alone.
#
# The patterns are written as step grids that read like a tracker, one token or character a
# 16th, "|" and spaces only for the eye:
#
#   drums   one string per role (KICK SNARE CLAP TOM HAT OPEN CYMBAL PERC): x a hit, X an
#           accented one. An accent is the whole step's (DrumMachine::setAccent), so every
#           hit on an accented step is written X, as the machine's own chart() writes it.
#   mono    (bass, lead) tokens: "." a rest, "_" the note before still sounding (HOLD), or a
#           note: [b|#]<degree 1-7>[+|-][!][~][@velocity][<|>nudge]: b/# a semitone down/up
#           (written as the degree below plus ALTER, as MonoMachine::chart() does), +/- an
#           octave, ! an accent, ~ a slide into the next note (which must start where this one
#           ends), @64 the note's own velocity (1-127, SELECT's knob 2), <10 / >10 the note
#           played that % of a step early / late (SELECT's NUDGE, at most 50): the chart's
#           VELOCITY and NUDGE lanes, by step.
#   chords  tokens: "." nothing, "=" the chord before goes on, "1"-"7" the chord on that
#           degree (stacked in thirds, as the CHORD SET says), "@name" a voicing of the
#           pack's own: ("x", scale degrees from degree I, 0-based) or ("c", semitones from
#           the chord base). Two hits of the same chord need a "." between them, or they
#           are one held chord (ChordMachine::writePattern).

import json
import math
import os
import re

STEPS = 16
MAJOR = [0, 2, 4, 5, 7, 9, 11]
MINOR = [0, 2, 3, 5, 7, 8, 10]  # the "Natural Minor" of Rave.qml's scales
# Rave.qml's scales by name (a template names its scale; Templates::scaleNames())
SCALES = {"Natural Minor": MINOR, "Major": MAJOR, "Dorian": [0, 2, 3, 5, 7, 9, 10],
          "Phrygian": [0, 1, 3, 5, 7, 8, 10], "Lydian": [0, 2, 4, 6, 7, 9, 11],
          "Mixolydian": [0, 2, 4, 5, 7, 9, 10], "Harmonic Minor": [0, 2, 3, 5, 7, 8, 11]}
ROOTS = {"C": 0, "C#": 1, "Db": 1, "D": 2, "D#": 3, "Eb": 3, "E": 4, "F": 5, "F#": 6, "Gb": 6,
         "G": 7, "G#": 8, "Ab": 8, "A": 9, "A#": 10, "Bb": 10, "B": 11}
ROLES = ["KICK", "SNARE", "CLAP", "TOM", "HAT", "OPEN", "CYMBAL", "PERC"]

# the sounds, by their names in data/kits.json (the drum kits by their paths, as kitPath()
# gives them: the machines' default soundfonts, a demo's, and kits.json's presetKits)
DRUM_MACHINES = "/zynthian/zynthian-data/soundfonts/SFZ Drum Machines/"
GM = "/zynthian/zynthian-data/soundfonts/SF2 Instruments/FluidR3Mono_GM.sf3"
KITS = {
    "TR909": DRUM_MACHINES + "Roland TR909.sf3",
    "TR808": DRUM_MACHINES + "Roland TR808.sf3",
    "LINN": DRUM_MACHINES + "LINN9000 1.sf3",
    "SP1200": DRUM_MACHINES + "SP1200 1.sf3",
    "STANDARD": GM + "#128:0",
    "ROOM": GM + "#128:8",
    "JAZZ": GM + "#128:32?CYMBAL=51&HAT=44",
    "BRUSH": GM + "#128:40",
    "BRUSH_RIDE": GM + "#128:40?CYMBAL=51&HAT=44",  # kits.json presetKits "Brush · ride"
    "POWER": GM + "#128:16",      # kits.json presetKits, added with these packs
    # the orchestra kit: KICK concert bass drum, SNARE concert snare, TOM timpani C, HAT timpani
    # G (the dominant below), OPEN triangle, CYMBAL concert crash, PERC tambourine, CLAP castanets
    "ORCHESTRA": GM + "#128:48?TOM=48&HAT=43&OPEN=81&CYMBAL=57&PERC=54",
    # cumbia: PERC güiro, TOM timbale, CYMBAL cowbell (the campana), CLAP conga (the llamador)
    "CUMBIA": GM + "#128:0?PERC=73&TOM=65&CYMBAL=56&CLAP=63",
    "CUMBIA_ROOM": GM + "#128:8?PERC=74&TOM=66&CYMBAL=56&CLAP=63",
    # salsa / son: SNARE open conga, CLAP conga slap, TOM tumba, HAT claves, OPEN maracas,
    # CYMBAL cowbell (campana), PERC güiro; KICK the kit's kick
    "CONGAS": GM + "#128:0?SNARE=63&CLAP=62&TOM=64&HAT=75&OPEN=70&CYMBAL=56&PERC=73",
    # merengue / bachata: SNARE high bongo, TOM low bongo, CLAP conga slap, OPEN tumba (the
    # tambora's low stroke), HAT maracas, CYMBAL cowbell, PERC cabasa (the metal güira)
    "GUIRA": GM + "#128:0?SNARE=60&TOM=61&CLAP=62&OPEN=64&HAT=70&CYMBAL=56&PERC=69",
    # the kit folder's machines (the kit picker lists them all): post-punk's and the 80s'
    "DR55": DRUM_MACHINES + "Boss DR55.sf3",
    "CR78": DRUM_MACHINES + "Roland CR78.sf3",
    "HR16": DRUM_MACHINES + "Alesis HR16.sf3",
    "SIMMONS": DRUM_MACHINES + "Simmons.sf3",
    "TR606": DRUM_MACHINES + "Roland TR606.sf3",
    # kits.json presetKits, added with the folk / metal / post-punk / gothic packs: the AVL
    # acoustic kits (their LV2s' soundfonts) and the folk room kit (TOM a low floor tom for the
    # bodhrán, PERC the tambourine, CYMBAL the ride)
    "BLACK_PEARL": "/zynthian/zynthian-plugins/lv2/Black_Pearl_5.lv2/FluidPlug.sf2",
    "RED_ZEPPELIN": "/zynthian/zynthian-plugins/lv2/Red_Zeppelin_5.lv2/FluidPlug.sf2",
    "FOLK": GM + "#128:8?TOM=41&PERC=54&CYMBAL=51",
    # the orchestra kit with its timpani on D (TOM) and A below (HAT): a D-minor or D-Dorian
    # tonic and dominant, for the Gregorian pack
    "ORCHESTRA_D": GM + "#128:48?TOM=50&HAT=45&OPEN=81&CYMBAL=57&PERC=54",
}

LIBRARY = {"drums": "drum-presets.json", "bass": "bass-presets.json",
           "lead": "lead-presets.json", "chords": "chord-presets.json"}

SOURCES = os.path.dirname(os.path.abspath(__file__))  # sources/: the packs' scripts
REPO = os.path.dirname(SOURCES)                         # the repository's root, a stick's root
STICK = os.path.join(REPO, "ravving", "presets")        # where a stick's presets are, shared by every pack
MANIFEST = "files.txt"                                  # a pack's list of the files it writes


def ravving_data():
    """ravving's data/ folder, where the sounds the packs name are listed (kits.json,
    engines.json, demos/): $RAVVING_DATA when set, else the folder above the repository (the
    packs as ravving's data/packs submodule), else a ravving clone beside the repository, else
    the snapshot of those files in sources/ravving-data (refresh it when ravving's change)."""
    if os.environ.get("RAVVING_DATA"):
        candidates = [os.environ["RAVVING_DATA"]]
    else:
        candidates = [os.path.dirname(REPO), os.path.join(os.path.dirname(REPO), "ravving", "data"),
                      os.path.join(SOURCES, "ravving-data")]
    for folder in candidates:
        if os.path.isfile(os.path.join(folder, "kits.json")):
            return folder
    raise SystemExit("ravving's data/ folder (kits.json, engines.json) not found in "
                     + " or ".join(candidates) + ": clone https://github.com/ravving/ravving beside "
                     "this repository, or set RAVVING_DATA to its data/ folder")


DATA = None


def _load(name):
    global DATA
    DATA = DATA or ravving_data()
    with open(os.path.join(DATA, name)) as f:
        return json.load(f)


def source_mods(machine, source):
    """Where a source's MODS go in a sound ("sourceSound", or "sourceSounds" for a synth
    source; "sound" for a drum kit) and its knobs as engines.json gives them, as
    EngineProfiles::profileFor finds the profile: by the engine's type, a jalv by its URI (a
    kit: the soundfont profile's kitSound, EngineProfiles::resolveKit)."""
    if machine == "drums":
        profile = next(p for p in _load("engines.json")["engines"] if p["type"] == "fluidsynth")
        return "sound", profile["kitSound"]
    for entry in _load("kits.json")["machines"]:
        if entry["key"] != machine:
            continue
        for candidate in entry.get("sources", []):
            if candidate["name"] != source:
                continue
            engine = candidate["engine"]
            for profile in _load("engines.json")["engines"]:
                if profile["type"] == engine["type"] and (engine["type"] != "jalv" or profile.get("uri") == engine.get("uri")):
                    return ("sourceSound" if engine["type"] == "fluidsynth" else "sourceSounds"), profile["sound"]
            raise ValueError(f"{source}: no engine profile in engines.json")
    raise ValueError(f"{machine} has no source {source!r} with MODS")


def knob_position(knob, value):
    """A knob's position (0-1) for a value in the engine's units, or a choice by its label."""
    choices = knob.get("choices")
    if choices:
        labels = [c["label"] for c in choices]
        return labels.index(value) / (len(labels) - 1)
    low, high = knob.get("min", 0.0), knob.get("max", 1.0)
    if not min(low, high) <= value <= max(low, high):
        raise ValueError(f"{knob['name']}: {value} is outside {low}..{high}")
    if knob.get("curve") == "log" and low > 0:
        return round(math.log(value / low) / math.log(high / low), 4)
    return round((value - low) / (high - low), 4)


def mods_state(machine, source, mods):
    """The sound's MODS part for `mods` ({"CARD/KNOB": value}): {"sourceSound": {...}} or
    {"sourceSounds": {source: {...}}}."""
    where, cards = source_mods(machine, source)
    positions = {}
    for key, value in mods.items():
        card_title, knob_name = key.split("/", 1)
        knob = next((k for c in cards if c["title"] == card_title for k in c["knobs"] if k["name"] == knob_name), None)
        if knob is None:
            raise ValueError(f"{source}: no MODS knob {key}")
        positions[key] = knob_position(knob, value)
    return {where: {source: positions}} if where == "sourceSounds" else {where: positions}


def _grid(text):
    return re.sub(r"[\s|]", "", text)


def _tokens(text):
    return [t for t in re.split(r"[\s|]+", text) if t]


class Outputs:
    """The files a pack's build.py writes into the shared ravving/presets tree, listed in the
    pack's files.txt so validate.py can tell that no two packs write the same file. A build
    first removes what its last run wrote, so a renamed preset leaves no file behind."""

    def __init__(self, here):
        self.manifest = os.path.join(here, MANIFEST)
        self.files = []
        if os.path.exists(self.manifest):
            with open(self.manifest, encoding="utf-8") as f:
                for line in f:
                    old = os.path.join(REPO, line.rstrip("\n"))
                    if line.strip() and os.path.isfile(old):
                        os.remove(old)

    def path(self, *parts):
        """Where a file under ravving/presets goes (`parts` below it), recorded as the pack's."""
        path = os.path.join(STICK, *parts)
        relative = os.path.relpath(path, REPO).replace(os.sep, "/")
        if relative in self.files:
            raise ValueError(f"{relative}: written twice")
        self.files.append(relative)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        return path

    def save(self):
        with open(self.manifest, "w", encoding="utf-8") as f:
            f.write("".join(name + "\n" for name in sorted(self.files)))
        return len(self.files)


class Pack:
    def __init__(self, genre, here, scale):
        self.genre = genre
        self.outputs = Outputs(here)
        self.scale = scale
        self.names = set()

    def _write(self, group, name, chart, sound):
        full = f"{self.genre} · {name}"
        if full in self.names:
            raise ValueError(f"{full}: written twice")
        self.names.add(full)
        if re.search(r'[/\\:*?"<>|]', full):
            raise ValueError(f"{full}: not a FAT file name (PresetExchange fileNameOf)")
        document = {"ravving": "preset", "type": "pattern", "library": LIBRARY[group],
                    "preset": {"name": full, "genre": self.genre, "chart": chart, "sound": sound}}
        with open(self.outputs.path(group, "patterns", full + ".json"), "w") as f:
            json.dump(document, f, indent=4, ensure_ascii=False)
            f.write("\n")

    @staticmethod
    def _length(name, length):
        if length % STEPS or not 1 <= length // STEPS <= 8:
            raise ValueError(f"{name}: {length} steps is not 1-8 bars of {STEPS}")

    # --- drums ------------------------------------------------------------------------------
    def drums(self, name, kit, rows, mods=None):
        rows = {role: _grid(line) for role, line in rows.items()}
        lengths = {len(line) for line in rows.values()}
        if len(lengths) != 1:
            raise ValueError(f"{name}: rows of different lengths {lengths}")
        length = lengths.pop()
        self._length(name, length)
        for role, line in rows.items():
            if role not in ROLES or set(line) - set(".xX"):
                raise ValueError(f"{name}: bad role or characters in {role}")
        accented = {i for line in rows.values() for i, c in enumerate(line) if c == "X"}
        chart = {}
        for role in ROLES:  # in the kit's order
            if role in rows:
                chart[role] = "".join("." if c == "." else ("X" if i in accented else "x")
                                      for i, c in enumerate(rows[role]))
        sound = {"kit": KITS[kit]}
        if mods:
            sound.update(mods_state("drums", KITS[kit], mods))
        self._write("drums", name, chart, sound)

    # --- bass and lead ----------------------------------------------------------------------
    def _note(self, token):
        m = re.fullmatch(r"([#b]?)([1-7])([+-]?)([!~]*)(?:@(\d{1,3}))?(?:([<>])(\d{1,2}))?", token)
        if not m:
            raise ValueError(f"bad note token {token!r}")
        shift, degree, octave, flags, velocity, way, nudge = m.groups()
        self._extra = (int(velocity) if velocity else None,
                       (-1 if way == "<" else 1) * int(nudge) if nudge else 0)
        if self._extra[0] is not None and not 1 <= self._extra[0] <= 127:
            raise ValueError(f"{token!r}: velocity out of 1-127")
        if abs(self._extra[1]) > 50:
            raise ValueError(f"{token!r}: nudge past half a step")
        semitones = self.scale[int(degree) - 1] + {"+": 12, "-": -12, "": 0}[octave] + {"#": 1, "b": -1, "": 0}[shift]
        octave = semitones // 12
        pc = semitones - 12 * octave
        if octave not in (-1, 0, 1):
            raise ValueError(f"{token!r} is out of the chart's three octaves")
        d = max(i for i, s in enumerate(self.scale) if s <= pc)
        return d + 1, octave, pc - self.scale[d], "!" in flags, "~" in flags

    def _sound(self, group, source, mods):
        sound = {"soundSource": source}
        if mods:
            sound.update(mods_state(group, source, mods))  # the groups are the machines' keys
        return sound

    def _mono(self, group, name, source, text, mods=None):
        tokens = _tokens(text)
        length = len(tokens)
        self._length(name, length)
        lanes = {lane: ["."] * length for lane in ("NOTES", "OCTAVE", "ACCENT", "SLIDE", "HOLD", "ALTER")}
        sounding = False
        starts = []
        velocities, nudges = {}, {}
        for i, token in enumerate(tokens):
            if token == ".":
                sounding = False
            elif token == "_":
                if not sounding:
                    raise ValueError(f"{name}: a hold at step {i} with no note before it")
                lanes["HOLD"][i] = "x"
            else:
                degree, octave, alter, accent, slide = self._note(token)
                lanes["NOTES"][i] = str(degree)
                lanes["OCTAVE"][i] = "+" if octave > 0 else "-" if octave < 0 else "."
                if alter:
                    lanes["ALTER"][i] = str(alter)
                lanes["ACCENT"][i] = "x" if accent else "."
                lanes["SLIDE"][i] = "x" if slide else "."
                velocity, nudge = self._extra
                if velocity is not None:
                    velocities[str(i)] = velocity
                if nudge:
                    nudges[str(i)] = nudge
                sounding = True
                starts.append(i)
        # a slide glides into the note that starts where it ends
        for i in starts:
            if lanes["SLIDE"][i] == "x":
                end = i + 1
                while end < length and lanes["HOLD"][end] == "x":
                    end += 1
                if lanes["NOTES"][end % length] == ".":  # past the end: the loop's first step
                    raise ValueError(f"{name}: the slide at step {i} glides into nothing")
        chart = {lane: "".join(chars) for lane, chars in lanes.items()}
        # the shipped charts leave out lanes with nothing in them (MonoMachine::chart())
        for lane in ("HOLD", "ALTER"):
            if set(chart[lane]) == {"."}:
                del chart[lane]
        # the notes' own velocity and nudge (MonoMachine::applyChart), by step
        if velocities:
            chart["VELOCITY"] = velocities
        if nudges:
            chart["NUDGE"] = nudges
        self._write(group, name, chart, self._sound(group, source, mods))

    def bass(self, name, source, text, mods=None):
        self._mono("bass", name, source, text, mods)

    def lead(self, name, source, text, mods=None):
        self._mono("lead", name, source, text, mods)

    # --- chords -----------------------------------------------------------------------------
    def chords(self, name, source, text, voicings=None, mods=None):
        voicings = voicings or {}
        tokens = _tokens(text)
        length = len(tokens)
        self._length(name, length)
        line, chart_voicings = [], {}
        current = None  # the voicing sounding at the step before
        for i, token in enumerate(tokens):
            if token == ".":
                line.append(".")
                current = None
                continue
            if token == "=":
                if current is None:
                    raise ValueError(f"{name}: '=' at step {i} with no chord before it")
                voicing = current
            elif re.fullmatch(r"[1-7]", token):
                voicing = ("d", token)
                if voicing == current:
                    raise ValueError(f"{name}: chord {token} at step {i} would merge with the one before")
            elif token.startswith("@"):
                kind, notes = voicings[token[1:]]
                voicing = (kind, tuple(notes))
                if voicing == current:
                    raise ValueError(f"{name}: {token} at step {i} would merge with the one before")
            else:
                raise ValueError(f"{name}: bad chord token {token!r}")
            if voicing[0] == "d":
                line.append(voicing[1])
            else:
                line.append(voicing[0])
                chart_voicings[str(i)] = list(voicing[1])
            current = voicing
        chart = {"CHORDS": "".join(line)}
        if chart_voicings:
            chart["VOICINGS"] = chart_voicings
        self._write("chords", name, chart, self._sound("chords", source, mods))

    def template(self, bpm, root, scale, name=None, **settings):
        """A template of the pack (write_template()); its scale must be the pack's own. A pack
        has one at least, named after it; more take a `name` of their own ("Vuelo · Crave")."""
        if SCALES.get(scale) != self.scale:
            raise ValueError(f"{self.genre}: the template's {scale} is not the scale the pack is written in")
        write_template(self.outputs, name or self.genre, bpm, root, scale, genre=self.genre, **settings)
        self.has_template = True

    def done(self):
        if not getattr(self, "has_template", False):
            raise ValueError(f"{self.genre}: no template (pack.template(…) before pack.done())")
        print(f"{self.genre}: {self.outputs.save()} files under {STICK}")


def write_template(outputs, name, bpm, root, scale, swing=50, phaser=0.0, echo=0.0, heavy=0.0,
                   about="", swing_eighths=False, genre=None):
    """A pack's project template (src/backend/templates.h): the tempo, swing, key and LIVE
    FX its presets are best played with, at ravving/presets/templates/<name>.json (`outputs`
    the pack's Outputs; `name` the pack's, or a template's own, with `genre` the pack's). `root`
    a note name ("E", "F#"), `scale` a name of SCALES, `swing` as the header shows it
    (50–75 %), the LIVE FX knobs 0..1."""
    genre = genre or name
    if scale not in SCALES:
        raise ValueError(f"{name}: no scale {scale!r} (one of {', '.join(SCALES)})")
    if root not in ROOTS:
        raise ValueError(f"{name}: no root {root!r}")
    if not 30 <= bpm <= 300 or not 50 <= swing <= 75:
        raise ValueError(f"{name}: {bpm} BPM, SWING {swing} out of range")
    for knob, value in (("phaser", phaser), ("echo", echo), ("heavy", heavy)):
        if not 0 <= value <= 1:
            raise ValueError(f"{name}: {knob} {value} is not 0..1")
    template = {"name": name, "genre": genre, "about": about, "bpm": bpm, "swing": swing,
                "swingEighths": swing_eighths, "root": ROOTS[root], "scale": scale,
                "phaser": phaser, "echo": echo, "heavy": heavy}
    with open(outputs.path("templates", name + ".json"), "w") as f:
        json.dump({"ravving": "preset", "type": "template", "template": template}, f, indent=4, ensure_ascii=False)
        f.write("\n")


def N(token, length=1, gap=0):
    """A note held `length` steps, then `gap` steps of rest: N("5-", 3, 1) → "5- _ _ ."."""
    return " ".join([token] + ["_"] * (length - 1) + ["."] * gap)


def C(token, length=1, gap=0):
    """A chord held `length` steps, then `gap` steps of nothing: C("@I", 3, 1) → "@I = = ."."""
    return " ".join([token] + ["="] * (length - 1) + ["."] * gap)


def R(steps):
    """`steps` steps of rest."""
    return " ".join(["."] * steps)


def power(degree):
    """A power chord on a scale degree (0-based): root, fifth, octave, in scale degrees."""
    return ("x", [degree, degree + 4, degree + 7])


def cpower(semitones):
    """A power chord on a chromatic root (semitones from the key's root): a ♭VII in major."""
    return ("c", [semitones, semitones + 7, semitones + 12])
