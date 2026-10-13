# Making a genre pack

How the pattern packs (`sources/<pack>`, writing into the shared `ravving/presets` tree) are
researched, written, checked and tried, as the folk, heavy metal, black metal, post-punk and
Gregorian packs were. The pack format and every pack are in the repository's `README.md`, the
token syntax at the top of `sources/patternkit.py`. A pack's research notes go beside its
script, in `sources/<pack>/research.md`. Paths below are this repository's; `tools/…` and
`data/…` are ravving's (the packs are its `data/packs` submodule).

## 1. Research

- **The bands' own harmony.** `ug-chords.py OUT "artist::title" "TAB:artist::title" …` saves
  the most voted chord sheet (or tab, for riffs) of each song from Ultimate Guitar;
  `ug-chords.py OUT --summary` prints each one's chord sequence. Ten to fifteen reference songs
  per genre, by the well-known bands; read the tabs' first staff lines for the riffs. Always
  give the artist: the search goes by title, and an unfiltered result is often another song.
- **Public-domain melodies** (chant, traditional tunes): find a MIDI file (mfiles.co.uk,
  IMSLP, the Mutopia project) and read it with `midi-notes.py FILE` (as downloaded data:
  `python3 -I`). Quote only what is public domain; for anything else take the progression and
  write the line.
- **The rhythms and the playing**: web sources for the genre's drum patterns and techniques
  (the blast beat, the gallop, the jig's 1 and 4), cited in the pack's README section.
- **Set each song on the pack's scale**: one scale per pack (Major, Natural Minor, Dorian…, as
  Rave.qml lists them), each song moved to its degrees (A Forest's Am C F D is i III VI IV;
  Love Will Tear Us Apart's D A Bm Em, in B minor, is III VII i iv). Notes outside the scale
  take ♭/♯ (ALTER), chords outside the key chromatic voicings.

## 2. Sounds

- Look for fitting instruments among the soundfonts on the device:
  `tools/soundfont.py presets FILE` (bank:program and name), `keys FILE` (a kit's drums by
  key), `render FILE --bank B --program P --notes …` (that it speaks, and how loud). Copy the
  script to the device first (ravving's `tools/device.sh tools`, or `scp`).
- Add what the pack needs to `data/kits.json`: a machine's `sources`, or a drum kit in
  `presetKits` (a General MIDI kit with keys picked for the rows: "…#128:8?TOM=41&PERC=54"). A
  pack's drums may also name any kit in the kit folder.
- Register new kits in `sources/patternkit.py`'s KITS.

## 3. Write

`sources/<pack>/build.py`, on `patternkit.Pack`: five presets each of drums, bass,
lead and chords (names unique within the genre), each a short comment saying what it is and
where it comes from. Use the per-note settings where the style plays them: `@velocity`
(palm-muting, tremolo strokes, a bow's push), `<n` / `>n` nudges (grace notes early, a dub bass
late), lengths (`_`), and `mods=` for the sound's MODS. 6/8 and 3/4: four 12-step bars in three
16-step bars.

End with the pack's template, `pack.template(bpm, root, scale, swing=…, phaser=…, echo=…, heavy=…,
about=…)`: the tempo, swing, key and LIVE FX the pack plays best at (the projects dialog's
TEMPLATES; `pack.done()` refuses a pack without one). Add its row to the README's table.

## 4. Check, try, document

- `python3 build.py` (in the pack's folder: it first removes what its `files.txt` lists, so a
  renamed preset leaves no stale file), then `python3 ../validate.py`: no errors, no two
  presets of an instrument nearly the same, no file two packs write.
- Deploy the kits.json change (`tools/device.sh deploy`), copy the presets to the stick
  (`tar -cf - ravving | ssh root@<device> 'tar --no-same-owner -xf - -C /media/root/<stick>'`, from the repository's root)
  and load the presets from SOURCE · USB with WITH ITS SOUND and WITH ITS MODS.
- `README.md`, the published packs page, written to `docs/writing-the-guide.md`
  (`python3 tools/check-guide-style.py --strict` passes): the pack's section (scale and key,
  "### The songs" as a table, "### The playing" as points, a table of every preset with its
  bars, tempo and sound, "### References" as a list), its scale in the scales list, its swing if
  not straight, its template row.
- `notes/pack-sounds.md`: the new sources and kits, their soundfont programs and render checks.
- The packs page is translated: `sh tools/i18n-extract.sh`, then fill the pack's new and
  fuzzy entries in po-site/es and po-site/ja (preset, sound and song names stay as they are),
  and `python3 tools/site-i18n.py render`. ctest translations-current fails until they're done.
- Commit and push here, cut a release with a tag (`git tag vN && git push origin vN`: the
  workflow validates and attaches ravving-packs.zip), then move ravving's `data/packs`
  submodule to that commit and commit that in ravving with the regenerated site pages.
