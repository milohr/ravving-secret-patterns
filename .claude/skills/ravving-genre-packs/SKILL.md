---
name: ravving-genre-packs
description: Research and build a new genre pack (or a custom requested pattern pack, or a template) of pattern presets for ravving in this repository - fetch the well-known bands' chord sheets and tabs, read public-domain melodies from MIDI files, pick sounds ravving already has, write sources/<pack>/build.py with per-note velocity, nudge and length, validate, try it from a USB stick and release it with a tag. Use when asked for new pattern presets in a style, genre, song or mood, or to research a style's chords and rhythms for ravving.
---

# ravving genre packs

This repository is laid out like a USB stick: `ravving/presets/…` at the root is what ravving
reads from a stick (one shared tree for every pack); everything else (`sources/`, `.claude/`,
`.github/`, `README.md`) is ignored by the device. Never put audio, soundfont, MIDI or `.ravv`
files anywhere in the repository: the USB page would list them (validate.py refuses them).

Read first:
- **`sources/research/README.md`**, the recipe (research, sounds, write, check, try, document).
- **`README.md`**, the pack format and every pack so far (scale, key, tempos, references). It is
  also published as ravving's packs page, so it follows ravving's `docs/writing-the-guide.md`:
  talk to the reader, short paragraphs, no dates, no smoke-test numbers or stories.
- The token syntax at the top of **`sources/patternkit.py`** (`@velocity`, `<nudge`, `_` holds,
  `~` slides, chord voicings), and a recent pack's `build.py` as the model
  (`sources/gregorian/build.py`, `sources/metal/build.py`). Some packs keep their research in
  `sources/<pack>/research.md`: write one for a new pack.

Tools (all in this repository):
- `sources/research/ug-chords.py OUT "artist::title" "TAB:artist::title" …` and `--summary`
- `sources/research/midi-notes.py FILE` (public-domain melodies; run with `python3 -I`, and
  keep the MIDI file outside the repository)
- `sources/research/soundfont.py presets | keys | render` (on the device, for the soundfonts it has)
- `sources/validate.py` (every pack against ravving's readers, and the stick tree)
- `sources/build-zip.py` (the release zip; the workflow runs it on a tag)

The sounds a preset may name come from ravving's `data/kits.json` and `data/engines.json`:
`patternkit.ravving_data()` takes `$RAVVING_DATA`, else ravving's `data/` when this repository
is its `data/packs` submodule, else a ravving clone beside it, else the snapshot in
`sources/ravving-data/` (refresh it from ravving when its sounds change). A new sound goes into
ravving's kits.json first.

Rules of thumb:
- One scale per pack; move every song onto its degrees; say the suggested ROOT, SCALE and BPM.
- `pack = Pack("<Genre>", HERE, SCALE)`: every preset is "<Genre> · <Name>", so packs never share
  a file name. The build writes into the shared `ravving/presets` tree and lists its files in
  `sources/<pack>/files.txt` (it removes what that list held first, so renames leave nothing).
- Every pack ships a template: `pack.template(bpm, root, scale, swing=, phaser=, echo=, heavy=, about=)`
  before `pack.done()` (it refuses without one); a second one takes `name="Pack · Groove"`. A
  template on its own: a `sources/<name>/build.py` with `Outputs` and `write_template` (README,
  "Add a template on its own"). Add the rows to README.md's templates table.
- Five presets per instrument (three or six also pass, the same for all four).
- Wrap every bar in a 16-token check (vuelo's `bar()` helper): a miscount is the usual slip; a
  chord re-struck right after itself must leave a gap step (else "would merge"); the lead's own
  engine (Calf Monosynth) takes no `mods=` in a pack (no kits.json source entry).
- The bands' progressions, original lines; quote melodies only when public domain.
- Use the per-note settings where the style plays them, and MODS for the sound.
- `python3 sources/validate.py` must end with 0 errors before a commit.
- Try it: copy the repository's `ravving` folder to a stick's root, SOURCE · USB in a preset
  dialog, each preset WITH ITS SOUND; start a project from its template under TEMPLATES.
- Release: commit and push, then `git tag vN && git push origin vN`; the workflow validates and
  attaches `ravving-packs.zip` (ravving/ at its root), and
  `releases/latest/download/ravving-packs.zip` follows. ravving then moves its `data/packs`
  submodule to the tag and re-renders and translates its packs page (its own
  ravving-translations skill).
- Commits are the author's own: no Claude attribution.
