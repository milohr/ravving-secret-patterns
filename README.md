# Secret pattern packs

Sixteen genre packs plus the jazz pack: classical, hip-hop, pop, rock, trap, reggaeton, punk,
tropical, cumbia, folk, heavy metal, black metal, post-punk, Gregorian (old gothic), vuelo
(Flight Facilities' nu-disco) and solos (six ballad solos after Coltrane's *Ballads* and Chet Baker). Each
has five pattern presets for each of the drums, the bass, the lead and the chords (solos six).
A smaller style pack, piig, has three of each. They are not installed with ravving. To play one, copy a
pack's `ravving` folder to the root of a USB stick: the presets dialog's **SOURCE · USB**
plays them straight from there (`PresetExchange::stickPatterns` / `loadStickPattern`), and
the USB page can import them.

```
data/secret/<genre>-presets/build.py                     the generator (python3 build.py)
data/secret/<genre>-presets/ravving/presets/<drums|bass|lead|chords>/patterns/<Genre> · <Name>.json
data/secret/patternkit.py                                shared by the genre build.py files (not the jazz one)
data/secret/validate.py                                  checks every pack against ravving's parsers
```

Each file is `{"ravving": "preset", "type": "pattern", "library": "<x>-presets.json",
"preset": {"name", "genre", "chart", "sound"}}`. The chart is the shipped libraries' format.
`sound` is the sound the pattern was written for: `{"soundSource": …}` for the bass, lead and
chords, `{"kit": …}` for the drums (a subset of `Machine::soundState()`).

**The notes are scale degrees.** They follow the session's root and scale. Each genre is
written for one scale, so its four instruments play together:

- Natural Minor: hip-hop, trap, reggaeton, piig, heavy metal, black metal, post-punk, vuelo.
- Major: classical, pop, rock, punk, tropical, cumbia, folk, solos.
- Dorian: Gregorian.
- Tropical's minor styles (salsa, bachata) and cumbia's (villera, chicha) sit on degree 6,
  the relative minor, so each pack stays in one key. In C major they play in A minor.

Notes from outside the scale use ALTER (for example rock's ♭3/♭7, trap's ♭2 and raised 7th).
Chords from outside the key use chromatic `c` voicings.

**Tempo and swing are not stored** in a pattern. The tables give each preset's tempo, in
quarter-note BPM on the 16-step grid. Every preset plays straight (SWING 50) except these:

| Preset | SWING |
|---|---|
| Hip-Hop · Golden Era Swing | 58–62 |
| Hip-Hop · Boom Bap, Lo-Fi Lazy and their bass, lead and chords | 54–60 if wanted; straight works |
| Hip-Hop · Jazz Rap, Jazz Rap Walk | 60–66 |
| Rock · Half-Time Shuffle | about 66, the triplet shuffle |
| Piig · every preset | 56–60, the lazy MPC swing |
| Solos · every preset | 54–58 with SWING on the EIGHTHS (the templates set it), a ballad's lilt; straight works |

Set the same swing on every machine playing along.

**Each pack ships a template, or more** (`pack.template(…)`, `patternkit.write_template()`; the
projects dialog's TEMPLATES, `ravving/presets/templates/<genre>.json` on the stick, a second one
under its own `name=`): the tempo, swing, key and LIVE FX its presets are best played with.
Choosing one starts a new project with them. The tempo is the middle of the pack's preset
tempos; the key is the one a pack was made for where it says so, else a usual key of the style.

| Pack | Tempo | Key | Swing | PHASER · ECHO · HEAVY |
|---|---|---|---|---|
| Classical | 100 | C major | 50 | 0 · 0.2 · 0 |
| Hip-Hop | 90 | C minor | 56 | 0 · 0.15 · 0.35 |
| Pop | 116 | C major | 50 | 0 · 0.15 · 0.25 |
| Rock | 122 | E major | 50 | 0 · 0.05 · 0.35 |
| Trap | 140 | F minor | 50 | 0 · 0.15 · 0.45 |
| Reggaeton | 93 | A minor | 50 | 0 · 0.1 · 0.4 |
| Punk | 170 | A major | 50 | 0 · 0 · 0.5 |
| Tropical | 130 | C major | 50 | 0 · 0.1 · 0.2 |
| Cumbia | 95 | G major | 50 | 0.15 · 0.3 · 0.2 |
| Piig | 79 | D minor | 58 | 0.15 · 0.25 · 0.3 |
| Folk | 110 | G major | 50 | 0 · 0.1 · 0 |
| Metal | 150 | E minor | 50 | 0 · 0.05 · 0.6 |
| Black Metal | 170 | E minor | 50 | 0 · 0.25 · 0.55 |
| Post-Punk | 142 | A minor | 50 | 0.3 · 0.3 · 0.3 |
| Gregorian | 70 | D Dorian | 50 | 0 · 0.5 · 0 |
| Jazz | 120 | C minor | 62 | 0 · 0.1 · 0 |
| Vuelo | 120 | A minor | 50 | 0.1 · 0.15 · 0.3 |
| Vuelo · Crave | 120 | C# minor | 52 | 0 · 0.25 · 0.25 |
| Solos | 64 | Eb major | 56 (eighths) | 0 · 0.35 · 0 |
| Solos · Late Night | 58 | Eb major | 54 (eighths) | 0 · 0.45 · 0 |

**The notes may carry their own velocity and nudge** (SELECT's knobs 2 and 3, the chart's
`VELOCITY` and `NUDGE` lanes by step): patternkit writes them from a note token's `@64` and
`<10` / `>10` (10 % of a step early / late). The packs made since use them: palm-muted chugs,
tremolo down- and up-strokes, a fiddle's bow, grace notes snapped in early, a dub bass behind the
beat, a chant's swell. A note's LENGTH is its `_` steps (HOLD), as before.

**6/8 and 3/4 in the new packs** work as the waltz trio does (below): three 16-step bars hold
four 12-step bars, and the tempo counts a quarter of four steps (a jig at a dotted quarter of
110 is "165").

**The waltz trio is in 3/4.** Classical · Waltz, Waltz Oom and Waltz Pah-Pah are three
16-step bars long, which hold four 12-step waltz bars, so the three loop together.

## Sounds

Every sound named is a source in `data/kits.json` (or a kit path), and `validate.py` checks
this. I added two kinds of entries to `kits.json`, all from the FluidR3Mono_GM.sf3 already on
the device (`/zynthian/zynthian-data/soundfonts/SF2 Instruments/`):

- **Chords sources:** Harpsichord 0:6, Guitar · Clean 0:27, Guitar · Overdrive 0:29,
  Guitar · Distortion 0:30, Marimba 0:12, Steel drums 0:114, Accordion 0:21,
  Brass section 0:61, Pizzicato strings 0:45.
- **Bass sources:** Picked bass 0:34, Slap bass 0:36, Sine sub 8:80, Contrabass 0:43,
  Cello 0:42.
- **Lead sources:** Violin 0:40, Harpsichord 0:6, Trumpet 0:56, Guitar · Overdrive 0:29,
  Marimba 0:12, Steel drums 0:114, Pan flute 0:75, Accordion 0:21, Music box 0:10,
  Guitar · Clean 0:27 (champeta's soukous lead).
- **Bass source "808 · Monosynth":** a `jalv` source on Calf Monosynth, the lead machine's
  own engine (a second instance on the bass track). Its controls are real port values,
  checked against the plugin's lv2info dump in
  `engine-mods/calf_monosynth_mod/docs/engine-symbols.txt`:
  - Sound: osc 1 Sine (`o1_wave` 3), plus 15 % of a triangle an octave up (`o2_wave` 4,
    `o2_xpose` 12, `o12_mix` 0.15) for the harmonics an 808's saturation gives.
  - Filter: 12 dB low-pass at 400 Hz that follows the key, opened by a 60 ms filter envelope
    (`env2cutoff` 2400 cents): the click of the attack.
  - Amp envelope: 1 ms attack, 1.8 s decay to 0.3, 250 ms release.
  - Glide: `legato` 3 (Fingered Legato) with `portamento` 80 ms, so only overlapping notes
    (a SLIDE) glide.
  - Off: LFO-to-pitch, LFO-to-filter, the mod wheel; `master` 0.5.
  - What it cannot do:
    - **No pitch drop.** The Monosynth's modulation matrix is LV2 state, not ports (the mod's
      RESEARCH.md), so kits.json can't set a pitch envelope.
    - **No drive port.** Turn on the bass machine's DRIVE for the saturation.
    - The bass page's knobs (Nekobi's) don't apply to it.
- **presetKits:**
  - Power `#128:16`
  - Orchestra `#128:48?TOM=48&HAT=43&OPEN=81&CYMBAL=57&PERC=54`. The rows land on:

    | Row | Sound |
    |---|---|
    | KICK | concert bass drum |
    | SNARE | concert (field) snare |
    | CLAP | castanets |
    | TOM | timpani on C (key 48) |
    | HAT | timpani on G below (key 43) |
    | OPEN | triangle |
    | CYMBAL | concert crash (clash cymbals) |
    | PERC | tambourine |

    The timpani suit a key of C: drum kits don't follow the session's key.
  - Cumbia · timbal `#128:0?PERC=73&TOM=65&CYMBAL=56&CLAP=63`: PERC the güiro, TOM the high
    timbale, CYMBAL the cowbell (campana), CLAP the high conga (llamador).
  - Cumbia · room `#128:8?PERC=74&TOM=66&CYMBAL=56&CLAP=63`: the room kit, with the long güiro
    and the low timbale.
  - Latin · congas `#128:0?SNARE=63&CLAP=62&TOM=64&HAT=75&OPEN=70&CYMBAL=56&PERC=73`, for
    salsa: SNARE open conga, CLAP conga slap, TOM tumba, HAT claves, OPEN maracas, CYMBAL
    cowbell (campana), PERC güiro; KICK stays the kick.
  - Latin · güira `#128:0?SNARE=60&TOM=61&CLAP=62&OPEN=64&HAT=70&CYMBAL=56&PERC=69`, for
    merengue and bachata: SNARE high bongo, TOM low bongo, CLAP conga slap, OPEN tumba (the
    tambora's low stroke), HAT maracas, CYMBAL cowbell, PERC cabasa (the metal güira).
  - All the Latin keys were named from the font and rendered; every one sounds.

**Nothing needs installing on the device.** The device's font is MuseScore 2.3.2's
FluidR3Mono_GM.sf3. It matches by sha256
`cfcd66d89e8386823400eca64934b14fbea7bf48ba1f00d21189af1262794ec2`, the hash in zynthbox-qml's
`config/soundfonts.json`, entry SF_00022. A byte-identical copy is in
`~/Downloads/ravving-soundfonts/fluidr3mono/`, from
<https://github.com/musescore/MuseScore/raw/v2.3.2/share/sound/FluidR3Mono_GM.sf3>. Its
licence is MIT (Frank Wen 2000–2002, mono version Michael Cowgill 2014–16; see
`LICENSE-FluidR3Mono.md` there).

**How the new sounds were checked.** Every new preset was rendered offline from that copy
with `tools/soundfont.py render`. All of them sound, with peak levels from 0.02 to 0.20 and
none silent. The kit rows were also worked out with a port of `DrumKit::fromSoundfont`.
`validate.py` checks that every FluidR3Mono bank:program in kits.json exists, whenever the
copy is present.

**Limits of these sounds:** FluidSynth sources don't glide; a SLIDE only overlaps the notes.
The 808 lines therefore use "808 · Monosynth", which does glide. "Sine sub" (8:80) stays
registered, but no preset uses it any more.

### Added with the folk, metal, black metal, post-punk and Gregorian packs (2026-10-10)

Sources from soundfonts already on milo (`SF2 Instruments/`; each preset found with
`tools/soundfont.py presets` and rendered there: peaks 0.02–0.31 like the others, except
**Organ · Plein jeu**, 0.66: lower its machine's VOL):

| Machine | Source | Soundfont, bank:program |
|---|---|---|
| chords | Guitar · Heavy rhythm | Heavy Guitars 0:0 |
| chords, lead | Guitar · Chorus | Stratocaster 0:3 (STRAT VS chorus) |
| chords | Guitar · 12-string, Guitar · Acoustic | Acoustic Guitars 0:8, 0:0 |
| chords | Organ · Vox humana, Organ · Plein jeu | Pipe Organ 0:45, 0:114 |
| chords, lead | Harp | FluidR3Mono_GM 0:46 |
| bass | Squier bass | Squierbass 0:0 |
| bass | Organ · Bourdon 16 | Pipe Organ 0:59 |
| bass, lead | Guitar · Heavy muted | Heavy Guitars 0:4 (palm-muted) |
| lead | Guitar · Heavy lead, Guitar · Valve OD | Heavy Guitars 0:2, Valve OD Guitar 0:0 |
| lead | Choir, Voice oohs | FluidR3Mono_GM 0:52, 0:53 |
| lead | Fiddle, Banjo, Bagpipe, Recorder | FluidR3Mono_GM 0:110, 0:105, 0:109, 0:74 |
| lead | Organ · Krummhorn | Pipe Organ 0:124 |

Kits (`presetKits`, and the kit folder's machines the packs name):

- **Black Pearl 5**, **Red Zeppelin 5**: the AVL acoustic kits, the soundfonts inside their
  FluidPlug LV2s (`/zynthian/zynthian-plugins/lv2/<kit>.lv2/FluidPlug.sf2`; the `sf2/` links to
  them are broken, their names hold a literal `*`). Velocity-layered, mapped by General MIDI
  key (their samples are unnamed); rendered: kick 0.09, snare 0.05, a little under the drum
  machines. DrumKit names such a kit after its bundle ("Black Pearl 5", not "FluidPlug").
- **Folk · bodhrán**: FluidR3's Room kit with TOM the low floor tom (the bodhrán), PERC the
  tambourine, CYMBAL the ride.
- **Orchestra · D**: the orchestra kit with its timpani on D (TOM, key 50) and the A below
  (HAT, key 45), a D tonic and dominant.
- From the kit folder: Boss DR55 (the Sisters of Mercy's Doktor Avalanche), Roland CR78.
  `validate.py` knows the folder's files as listed on milo.

### Added with the Solos pack (2026-10-11)

Lead sources, found with `tools/soundfont.py presets` on milo and rendered there (`render
--notes 60 --velocity 90`, peak over 2 s), see `tools/genre-research/solos.md`:

| Machine | Source | Soundfont, bank:program | Peak |
|---|---|---|---|
| lead | Soprano sax | FluidR3Mono_GM 0:64 | 0.04 (quiet: raise the lead's VOL) |
| lead | Tenor sax · Bright | Roland SC-88 (Roand_SC-88.sf3) 0:66 | 0.10 |
| lead | Trumpet · Cool | Roland SC-88 0:56 | 0.06, decaying to 0.04 (FluidR3's Trumpet 0.04, its Muted trumpet 0.06, the SC-88 mute 0.07) |

The existing Alto sax and Tenor sax (FluidR3 0:65, 0:66) rendered at 0.07, the SC-88's alto
0.07, soprano 0.09, baritone 0.08 (FluidR3's baritone 0.05).

## Classical: Major

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Waltz | drums | 3 (3/4) | Viennese waltz: timpani C/G on the I and V downbeats, triangle on the "pah-pah", bass drum and cymbals on the first one, snare roll into the phrase | 160–190 | Orchestra kit |
| March | drums | 2 | orchestral march in 2/4: field-snare rudiments, bass drum and clash cymbals on the strong beats, timpani tonic and dominant | 110–120 | Orchestra kit |
| Galop | drums | 2 | Offenbach galop (can-can): the snare's "ta-ta-ta", bass drum "oom" and cymbal "pah", triangle, stop-time V–I on the timpani | 140–160 | Orchestra kit |
| Habanera | drums | 2 | the habanera rhythm (dotted 8th, 16th, two 8ths) on castanets, tambourine, timpani tonic then dominant | 70–90 | Orchestra kit |
| Timpani Cadence | drums | 4 | maestoso: timpani alternating tonic and dominant, a dominant roll into the final tonic stroke with bass drum and cymbals | 70–90 | Orchestra kit |
| Alberti Bass | bass | 4 | low–high–middle–high eighths over I, IV6/4, V6/5 (Mozart K. 545 texture) | 110–140 | Cello |
| Pachelbel Ground | bass | 2 | Pachelbel's eight-note ground, in quarter notes | 50–70 | Cello |
| Lament Bass | bass | 4 | chromatic descending tetrachord from 1 to 5 in half notes, then IV–ii–V | 60–80 | Contrabass |
| Waltz Oom | bass | 3 (3/4) | the "oom" on each downbeat: I, IV, V, I | 160–190 | Upright |
| Octave Continuo | bass | 2 | Baroque octave-leaping eighths down the scale (after the Air, BWV 1068) | 55–70 | Contrabass |
| Prelude Arpeggio | lead | 4 | Bach WTC I C-major prelude figure, bars 1–3 and 5 | 60–80 | Harpsichord |
| Classical Phrase | lead | 4 | a period's antecedent, ending on a half cadence | 90–120 | Violin |
| Ode Theme | lead | 4 | Beethoven's Ode to Joy, first four bars | 100–120 | Oboe |
| Baroque Sequence | lead | 2 | turning sixteenth figure stepping down each beat | 90–110 | Flute |
| Fanfare | lead | 2 | dotted triad calls rising to the octave | 100–120 | Trumpet |
| Chorale Cadence | chords | 4 | four-part SATB: I vi IV ii6 I6/4 V7 I, with strict voice leading | 60–80 | Choir |
| Pachelbel Progression | chords | 2 | I V vi iii IV I IV V, with the upper voices stepping down | 50–70 | Strings · Ensemble |
| Waltz Pah-Pah | chords | 3 (3/4) | chords on beats 2 and 3: I, IV6/4, V7, I | 160–190 | Pizzicato strings |
| Prinner Pulse | chords | 2 | the galant Prinner (IV–I6–vii°6–I) in repeated eighths | 90–120 | Strings · Bowed |
| Circle of Fifths | chords | 4 | I IV vii° iii vi ii V I in half notes | 70–100 | Harpsichord |

References: [Lament bass (Wikipedia)](https://en.wikipedia.org/wiki/Lament_bass);
[Music theory behind Canon in D](https://musiciangoods.com/blogs/music-theory/music-theory-behind-canon-in-d);
[The art of the ostinato](https://thelistenersclub.com/2012/04/15/the-listeners-club-the-art-of-the-ostinato/);
R. Gjerdingen, *Music in the Galant Style* (the Prinner).

The public-domain scores, on IMSLP: Bach BWV 846 and BWV 1068, Pachelbel's Canon, Beethoven
Symphony 9, Mozart K. 545, Bizet *Carmen*.

## Hip-Hop: Natural Minor

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Boom Bap | drums | 2 | kick on 1 and pushes, snare 2 and 4, eighth hats, ghost snare, open hat | 85–95 | SP1200 1 |
| Golden Era Swing | drums | 2 | sixteenth hats to swing (SWING 58–62), skipping kick, rim ghosts | 88–98 | LINN9000 1 |
| Lo-Fi Lazy | drums | 2 | soft, off-beat hats only, late kick, rim clicks | 70–85 | SP1200 1 |
| Old School 808 | drums | 2 | electro-rap kick, claps 2 and 4, cowbell | 95–110 | Roland TR808 |
| Jazz Rap | drums | 2 | ride "ding, ding-a" and hi-hat foot over boom bap | 85–95 | Jazz · ride kit |
| Boom Bap Root | bass | 2 | roots on the kick, i→iv, VI walking back | 85–95 | Finger bass |
| Jazz Rap Walk | bass | 2 | upright walking i–iv with pickups | 85–95 | Upright |
| G-Funk Glide | bass | 2 | Moog-style gliding octave and pentatonic line | 90–96 | Nekobi |
| Lo-Fi Sub | bass | 4 | long notes under i–VI–iv–v with pickups | 70–85 | Fretless |
| Electro Funk | bass | 2 | sixteenth octave pops with a slide | 100–112 | Nekobi |
| Rhodes Riff | lead | 2 | minor-pentatonic riff with a falling answer | 80–95 | Rhodes |
| Horn Stabs | lead | 2 | chopped-soul horn hits and falls | 85–95 | Muted trumpet |
| Vibes Loop | lead | 2 | eighth arpeggios of i and iv | 75–90 | Vibes |
| G-Funk Whistle | lead | 2 | high portamento whistle line | 90–96 | Calf Monosynth |
| Flute Loop | lead | 2 | flute falling from the octave, turning on the third | 80–95 | Flute |
| Boom Bap Keys | chords | 2 | chopped i, then iv / III / VII stabs (CHORD SET sevenths) | 85–95 | Rhodes |
| Soul Loop | chords | 2 | i7–iv7–VII–III, half a bar each | 80–95 | Strings · Ensemble |
| Lo-Fi Ninths | chords | 4 | im9–ivm9–VImaj9–v7, each a 16th late | 70–85 | Upright piano |
| Dark Strings | chords | 4 | i (two bars) – VI – v triads | 80–95 | Strings · Bowed |
| Organ Vamp | chords | 2 | soul-jazz i7–IV7 (Dorian IV) stabs | 90–100 | Jazz organ |

References: [Best drum patterns for hip hop](https://violetrecording.com/best-drum-patterns-for-hip-hop/);
[What is boom bap (Native Instruments)](https://blog.native-instruments.com/what-is-boom-bap/);
[How to make a boom bap beat](https://violetrecording.com/how-to-make-a-boom-bap-beat/);
[Boom bap in FL Studio](https://www.audeobox.com/learn/fl-studio/how-to-make-boom-bap-beats-in-fl-studio/).

## Pop: Major

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Four on the Floor | drums | 2 | dance pop: kick every beat, claps 2 and 4, off-beat open hats | 118–128 | Roland TR909 |
| Half-Time Ballad | drums | 2 | one snare a bar on 3 | 130–150 (felt half) | Standard kit |
| 80s Gated | drums | 2 | big 2 and 4 snare, doubled kick, tom run | 110–125 | LINN9000 1 |
| 808 Pop | drums | 2 | half-time claps, sparse kicks, hat rolls | 130–150 (felt half) | Roland TR808 |
| Motown Stomp | drums | 2 | snare on all four beats, tambourine on 2 and 4 | 120–135 | Room kit |
| Axis Eighths | bass | 4 | pumping eighths on I–V–vi–IV | 100–130 | Finger bass |
| Synth Octaves | bass | 4 | octave-jumping eighths on vi–IV–I–V | 110–128 | Synth bass |
| Ballad Descent | bass | 4 | I–V/7–vi–IV descending bass, walk-up home | 60–80 | Fretless |
| Funk-Pop Sixteenths | bass | 2 | syncopated sixteenths with octave pops | 105–120 | Slap bass |
| Motown Walk | bass | 2 | melodic pickups into I–vi–IV–V | 110–130 | Finger bass |
| Axis Hook | lead | 2 | sung-style hook: repeated notes, leap to the fifth | 100–128 | Calf Monosynth |
| Piano Ostinato | lead | 2 | sixteenth ostinato grouped 3+3+2 | 110–130 | Grand piano |
| Sax Hook | lead | 2 | 80s sax hook up to the octave | 100–120 | Alto sax |
| Pluck Arp | lead | 4 | sixteenth arpeggios over I–V–vi–IV | 110–128 | Vibes |
| Ballad Melody | lead | 4 | long notes, ends open on 2 | 60–80 | Rhodes |
| Axis Quarters | chords | 4 | I–V–vi–IV in quarter notes | 90–120 | Grand piano |
| Minor-Start Pulse | chords | 4 | vi–IV–I–V pulsing eighths | 110–128 | TAL NoiseMaker |
| Doo-Wop Changes | chords | 2 | 50s I–vi–IV–V triads | 60–80 | Upright piano |
| Royal Road | chords | 4 | IV–V–iii–vi, each bar pushed 3+3+2 | 90–110 | Rhodes |
| Ballad Strings | chords | 4 | I–V/7–vi–IV–V with the stepping bass voiced in | 60–80 | Strings · Ensemble |

References: [Hooktheory chord trends](https://www.hooktheory.com/blog/chord-progression-search-patterns-and-trends/);
[Common pop progressions (Mixed In Key)](https://mixedinkey.com/captain-plugins/common-chord-progressions-pop-music/);
[15 common drum beats](https://thedrumninja.com/common-drum-beats/);
[Drum patterns (muted.io)](https://muted.io/drum-patterns/).

## Rock: Major, with ♭3, ♭7 and ♭VI/♭VII borrowed

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Straight Backbeat | drums | 2 | kick 1 and 3, snare 2 and 4, eighth hats | 100–140 | Power kit |
| Arena Ride | drums | 2 | driving eighths on the ride, doubled kicks | 110–140 | Power kit |
| Half-Time Shuffle | drums | 2 | backbeat on 3 with ghost notes (SWING about 66) | 80–95 | Room kit |
| Bo Diddley Toms | drums | 2 | 3-2 "shave and a haircut" on toms, maracas | 100–125 | Room kit |
| Gallop | drums | 2 | eighth plus two sixteenths on the kick every beat | 140–180 | Power kit |
| Root Eighths | bass | 4 | pumping eighths I–♭VII–IV–I | 110–150 | Picked bass |
| Boogie Walk | bass | 4 | 1-3-5-6-♭7 boogie over I–IV–I–V | 140–170 | Finger bass |
| Blues-Rock Riff | bass | 2 | minor-pentatonic unison riff with ♯4 | 90–120 | Finger bass |
| Gallop Bass | bass | 4 | gallop on I–♭VI–♭VII–I | 140–180 | Picked bass |
| Root–Fifth Two-Beat | bass | 4 | country-rock root–fifth with a walk home | 100–130 | Acoustic bass |
| Pentatonic Lick | lead | 2 | blues-rock lick, ♭3 sliding into 3 | 90–120 | Guitar · Overdrive |
| Honking Sax | lead | 2 | rock'n'roll honks with a ♭7 growl | 140–170 | Tenor sax |
| Anthem Hook | lead | 4 | arena "whoa-oh" long notes | 110–140 | Guitar · Overdrive |
| Clean Arpeggio | lead | 4 | open-chord picking Iadd9–IV–vi–Vsus | 70–100 | Nylon guitar |
| Boogie Piano | lead | 2 | 3–5 tremolo, then a run down with a ♭3–3 crush | 140–170 | Grand piano |
| Power I–♭VII–IV | chords | 4 | chugged power chords | 110–150 | Guitar · Distortion |
| Organ Pushes | chords | 2 | R&B-rock organ holds with stabs | 100–125 | Jazz organ |
| ♭VI–♭VII–I | chords | 2 | Aeolian rock cadence, parallel triads | 100–140 | Guitar · Overdrive |
| Piano Pump | chords | 4 | I–IV–V–IV in a "1 2 3, 1 2 3, 1 2" push | 120–150 | Grand piano |
| Clean Strum | chords | 4 | strummed I–V–IV–V, guitar voicings | 90–120 | Guitar · Clean |

References: [15 common drum beats (shuffle, half-time shuffle)](https://thedrumninja.com/common-drum-beats/);
[Basic drum beats (Gear4music)](https://www.gear4music.com/blog/?p=43811);
[Rock and disco drum patterns](https://c.enwp.org/wiki/File:Characteristic_rock_and_disco_drum_patterns.png);
the Bo Diddley beat (Wikipedia).

## Trap: Natural Minor, with harmonic-minor 7 and Phrygian ♭2

The drum grid is sixteenths at the track's tempo, with the clap on beat 3: a half-time feel.

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Classic Trap | drums | 2 | clap on 3, eighth hats with sixteenth rolls, open hat | 130–150 | Roland TR808 |
| Triplet Flow | drums | 2 | hats grouped in threes against the beat | 130–150 | Roland TR808 |
| Drill | drums | 2 | snare on 3 plus a late one, 3-3-2 skipping hats | 140–145 | Roland TR808 |
| Phonk Cowbell | drums | 2 | cowbell riff, claps 2 and 4, Memphis kick | 120–140 | Roland TR808 |
| Sparse Snap | drums | 2 | quarter hats with one roll, snap on 3 | 140–160 | SP1200 1 |
| 808 Root Glide | bass | 2 | long root gliding up the octave, VII sliding home | 130–150 | 808 · Monosynth |
| Triplet 808 | bass | 2 | 808 hits in threes | 130–150 | 808 · Monosynth |
| Drill Slides | bass | 2 | slides through the ♭2 and the leading note | 140–145 | 808 · Monosynth |
| Phonk Bounce | bass | 2 | short punchy hits | 120–140 | 808 · Monosynth |
| Harmonic Minor 808 | bass | 2 | raised 7th pulling to the root | 130–150 | 808 · Monosynth |
| Flute Riff | lead | 2 | pentatonic flute riff, 3-3-2 | 130–150 | Flute |
| Bell Melody | lead | 2 | sixteenth music-box figure | 130–150 | Music box |
| Dark Piano | lead | 2 | sparse piano, leading tone to octave | 130–150 | Grand piano |
| Triplet Synth | lead | 2 | synth lead in threes | 130–150 | Calf Monosynth |
| Phrygian Riff | lead | 2 | drill string riff on the ♭2 | 140–145 | Violin |
| i–VI Pad | chords | 4 | i and VI, two bars each | 130–150 | Strings · Ensemble |
| i–iv–VI–V Stabs | chords | 4 | stab and echo; V major (chromatic) | 130–150 | Grand piano |
| Choir i–VII–VI–VII | chords | 4 | a bar each | 130–150 | Choir |
| Drill Pizzicato | chords | 2 | i and ♭II plucked 3-3-2 | 140–145 | Pizzicato strings |
| Glassy Stabs | chords | 2 | i–v–VI–VII, each half bar 3-3-2 | 130–150 | Alien · Glassy |

References: [Best drum patterns for trap](https://violetrecording.com/best-drum-patterns-for-trap/);
[Creating trap rhythms (Cubase seminar)](https://sleepfreaks-dtm.com/en/produce-recipe/cubase-pro-10-musicseminar-1);
[MPC modern trap workflow](https://www.audeobox.com/learn/mpc-software/modern-trap-workflow/);
[How to make trap beats](https://thedrumninja.com/how-to-make-trap-beats/).

## Reggaeton: Natural Minor

The dembow: the kick on every beat, the snare on steps 4, 7, 12 and 15 (3-3-2 twice a bar).

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Dembow Clásico | drums | 2 | the dembow ("Dem Bow" riddim) | 88–98 | Roland TR808 |
| Perreo Lento | drums | 2 | kick 1 and 3, claps on the "and"s, off-beat hats | 85–92 | Roland TR808 |
| Dembow Timbal | drums | 2 | dembow with a cowbell line and a timbal roll | 90–98 | Roland TR808 |
| Dembow Dominicano | drums | 2 | faster, doubled snare, sixteenth hats, claps 2 and 4 | 115–130 | Roland TR808 |
| Moombahton | drums | 2 | dembow under house claps and open hats | 105–110 | Roland TR909 |
| Dembow 808 | bass | 4 | tresillo roots i–VI–III–VII | 88–98 | 808 · Monosynth |
| Perreo Sub | bass | 2 | held root sliding down through VII | 85–95 | 808 · Monosynth |
| Syncopated Synth | bass | 2 | off-beat octave synth bass | 90–100 | Synth bass |
| Romántico Walk | bass | 2 | eighth walk i–iv–VII–III | 85–95 | Finger bass |
| Offbeat Pump | bass | 2 | Dominican off-beat eighths | 115–130 | 808 · Monosynth |
| Pluck Hook | lead | 2 | tresillo synth hook | 88–98 | Calf Monosynth |
| Guitarra Romántica | lead | 2 | Andalusian 3-2-1 with the raised 7 | 85–95 | Nylon guitar |
| Flauta Perreo | lead | 2 | short syncopated high flute | 88–98 | Flute |
| Marimba Dembow | lead | 2 | marimba in the dembow's rhythm | 90–98 | Marimba |
| Sax Romántico | lead | 2 | long sax notes, turn into the leading tone | 85–95 | Alto sax |
| i–VI–III–VII Dembow | chords | 4 | stabs in 3+3+2 | 88–98 | TAL NoiseMaker |
| Romántico Piano | chords | 4 | i–iv–VII–III held | 85–95 | Grand piano |
| Andalusian Strum | chords | 4 | i–VII–VI–V strummed (V chromatic) | 88–98 | Nylon guitar |
| Pad VI–VII–i | chords | 4 | sustained pad | 88–98 | Strings · Digital |
| Organ Offbeats | chords | 4 | off-beat stabs i–VI–i–v | 105–110 | Organ · House |

References: [How to make reggaeton beats](https://violetrecording.com/how-to-make-reggaeton-beats/);
[Reggaetón Lento (Hooktheory)](https://www.hooktheory.com/theorytab/view/cnco/reggaeton-lento-(bailemos));
[Reggaeton chord progressions](https://unison.audio/reggaeton-chord-progressions/);
Wikipedia's "Dembow" (Shabba Ranks' "Dem Bow", Steely & Clevie's "Poco Man Jam" riddim).

## Punk: Major, with ♭3, ♭7 and ♭VI/♭VII borrowed

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Skate Beat | drums | 2 | polka: kick on the beats, snare on every "and" | 170–200 | Power kit |
| D-Beat | drums | 2 | Discharge beat: kick 1, &1, &2, 3, &3, &4; crash eighths, no hat | 150–190 | Room kit |
| Straight Eighths | drums | 2 | Ramones-style eighth hats and backbeat | 160–190 | Standard kit |
| Half-Time Breakdown | drums | 2 | pop-punk breakdown with crash quarters and a tom fill | 140–180 | Power kit |
| Ska Offbeat | drums | 2 | off-beat hats, snare 2 and 4 | 150–180 | Standard kit |
| Pop-Punk Eighths | bass | 4 | down-picked staccato eighths, I–V–vi–IV | 160–190 | Picked bass |
| Skate Walk-Up | bass | 4 | eighths with walk-ups, I–IV–V–I | 170–200 | Picked bass |
| D-Beat Riff | bass | 2 | crust riff with ♭3 and ♯4 | 150–180 | Picked bass |
| Ska Walk | bass | 4 | walking quarters I–vi–IV–V | 140–170 | Finger bass |
| New Wave Octaves | bass | 4 | octave eighths I–IV–I–V | 140–160 | Synth bass |
| Pop-Punk Hook | lead | 2 | repeated-note hook up to the fifth | 160–190 | Guitar · Overdrive |
| Ska Horns | lead | 2 | off-beat horn pushes and a fall | 150–180 | Trumpet |
| Street Riff | lead | 2 | Oi!/street-punk single-note riff | 150–180 | Guitar · Overdrive |
| Gang Chant | lead | 2 | "whoa-oh" long notes | 150–180 | Calf Monosynth |
| Piano Pounding | lead | 2 | high octave and fifth pounding eighths | 160–190 | Grand piano |
| Power I–IV–V | chords | 4 | I–I–IV–V chugged eighths | 160–200 | Guitar · Distortion |
| Pop-Punk Pushes | chords | 4 | I–V–vi–IV, each change an eighth early | 160–190 | Guitar · Distortion |
| Ska Upstrokes | chords | 4 | off-beat chops I–vi–IV–V | 150–180 | Guitar · Clean |
| Crust I–♭VI–♭VII | chords | 2 | chugged I, then ♭VI–♭VII | 150–190 | Guitar · Overdrive |
| Piano Bash | chords | 4 | straight eighth triads I–IV–I–V | 160–190 | Grand piano |

References: [D-beat (Wikipedia)](https://en.wikipedia.org/wiki/D-beat);
[Punk drum beats and rhythms](https://drumhelper.com/learning-drums/punk-drum-beats-and-rhythms/);
[The history of the punk beat in 10 songs](https://www.pastemagazine.com/music/punk/the-history-of-the-punk-beat-in-10-songs).

## Tropical: Major, with salsa and bachata on the relative minor (degree 6)

Latin "música tropical" without cumbia, which has its own pack below. Five styles, one preset
per style for each instrument: salsa, merengue, bachata, vallenato, champeta. All play
straight (SWING 50).

| Preset | Part | Bars | What it is | Tempo · swing | Sound |
|---|---|---|---|---|---|
| Salsa | drums | 2 | 2-3 son clave; conga marcha (slap on 2, open tones on 4 and its "and"), tumba answer; campana on the beats; bombo on the 3-side's "and" of 2 | 170–200, straight | Latin · congas |
| Merengue | drums | 2 | güira on every beat with its "and-a"; tambora hand and stick strokes, the quintillo into beat 3; orquesta kick on every beat | 130–160, straight | Latin · güira |
| Bachata | drums | 2 | bongo martillo eighths, low-bongo open tone on 4, güira keeping time | 120–140, straight | Latin · güira |
| Vallenato | drums | 2 | paseo: caja hand strokes and rim slaps, guacharaca scrape | 90–110, straight | Cumbia · room |
| Champeta | drums | 2 | drum machine up front, kick on 1, &2 and 3, snare on 2 and 4, soukous cavacha sixteenths on the hats | 110–125, straight | Roland TR808 |
| Salsa Tumbao | bass | 4 | tresillo off-beats only (the "and" of 2, beat 4 held over the bar line), relative-minor i–iv–V–i | 170–200, straight | Upright |
| Merengue Bass | bass | 4 | on the beat and the "and" of 2, I and V | 130–160, straight | Finger bass |
| Bachata Bass | bass | 4 | root–fifth syncopations, relative-minor i–iv–V–i | 120–140, straight | Acoustic bass |
| Vallenato Paseo | bass | 4 | root and fifth with pickups, I–IV–V–I | 90–110, straight | Picked bass |
| Champeta Bass | bass | 4 | fast octave sixteenths, I–IV–V–IV | 110–125, straight | Synth bass |
| Mambo Horns | lead | 2 | syncopated horn call and answer, leading tone (♯5) | 170–200, straight | Trumpet |
| Sax Jaleo | lead | 2 | merengue's running sixteenth arpeggio, I then V7 | 130–160, straight | Alto sax |
| Requinto | lead | 2 | bachata lead-guitar arpeggios on i then V | 120–140, straight | Nylon guitar |
| Acordeón Paseo | lead | 2 | accordion paseo melody, V then I | 90–110, straight | Accordion |
| Sebene Guitar | lead | 2 | soukous sebene picking high on the neck | 110–125, straight | Guitar · Clean |
| Piano Montuno | chords | 4 | syncopated montuno stabs, relative-minor i–iv–V7–i | 170–200, straight | Grand piano |
| Merengue Brass | chords | 4 | off-beat hits, I–I–V7–V7 | 130–160, straight | Brass section |
| Segunda Strum | chords | 4 | strummed on each beat, the 4th held, relative-minor i–iv–V–i | 120–140, straight | Guitar · Clean |
| Vallenato Guitar | chords | 4 | strum pattern, I–IV–V–I | 90–110, straight | Nylon guitar |
| Champeta Stabs | chords | 4 | synth stabs on the "e" after each beat, I–IV–V–IV | 110–125, straight | TAL NoiseMaker |

References:
- Salsa: [Tumbao (Wikipedia)](https://www.wikipedia.org/wiki/Tumbao);
  [Tumbao (Soundbrenner)](https://www.soundbrenner.com/blogs/articles/tumbao);
  [Latin and counting (TalkBass)](https://www.talkbass.com/threads/latin-and-counting.366625/)
- Merengue: [Merengue rhythm (Soundbrenner)](https://www.soundbrenner.com/blogs/articles/merengue-rhythm);
  [Merengue music (Wikipedia)](https://www.wikipedia.org/wiki/Merenque);
  [Merengue típico (Wikipedia)](https://www.wikipedia.com/wiki/Perico_Ripiao)
- Bachata: [Breaking down bachata, part 1](https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/4JGuRsatSHe2lZ4XuGxuUF/breaking-down-bachata-part-1-overview)
  and [part 3, guitars](https://www.ubisoft.com/en-us/game/rocksmith/plus/news-updates/42YP2fih1AY3wVyZhWhLrZ/breaking-down-bachata-part-3-guitars)
- Vallenato: the Colombian university theses on paseo bass lines
  ([UPN](https://repositorio.upn.edu.co/bitstreams/a8d7eb05-b98d-43b9-8c23-10c73eb38508/download),
  [Unireformada](https://repository.unireformada.edu.co/bitstreams/235e80db-ab95-4fed-be63-fb1fa7493731/download))
- Champeta: [Champeta (Wikipedia)](https://en.wikipedia.org/wiki/Champeta);
  [Palenque Records guide (Bandcamp Daily)](https://daily.bandcamp.com/lists/palaneque-records-label-guide)

## Cumbia: Major, with the minor styles on the relative minor (degree 6)

The drums play the "Cumbia" kits: PERC güiro, CLAP conga (llamador), TOM timbale, CYMBAL
cowbell (campana). The güiro plays "chu-chucu": a stroke on the beat, then down-up on its
"and-a".

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Colombiana | drums | 2 | tambora on 1 and 3, llamador on 2 and 4, güiro every beat, the alegre answering | 85–100 | Cumbia · room |
| Sonidera | drums | 2 | slower; kick with a pickup, llamador on every "and", campana quarters, timbal fill | 80–92 | Cumbia · timbal |
| Villera | drums | 2 | harder: snare cracking on 2 and 4, kick on 1, the "a" of 2 and 3, timbal rolls | 95–105 | Cumbia · timbal |
| Chicha | drums | 2 | timbales' pattern over the güiro, conga off-beat eighths | 90–100 | Cumbia · room |
| Digital | drums | 2 | drum-machine cumbia: hats playing the güiro figure, claps on 2 and 4 | 90–105 | Roland TR808 |
| Root–Fifth Tumbao | bass | 2 | root for a dotted quarter, fifth anticipating; I then V | 85–100 | Finger bass |
| Tónica-Dominante | bass | 4 | root on 1, fifth on 3, a pickup into each chord, I–IV–V–I | 85–100 | Acoustic bass |
| Sonidera Walk | bass | 2 | round bass walking I up to IV and back | 80–92 | Fretless |
| Villera i–VII | bass | 2 | repeating keyboard bass on the relative minor's i–VII | 95–105 | Synth bass |
| Digital 808 | bass | 4 | the tumbao rhythm on an 808 over vi–IV–I–V, gliding into each root | 90–105 | 808 · Monosynth |
| Acordeón | lead | 2 | accordion eighth runs | 85–100 | Accordion |
| Caña de Millo | lead | 2 | sixteenth trills, the cumbia's original cane flute | 85–100 | Flute |
| Chicha Guitar | lead | 2 | tremolo-picked pairs in the relative minor, the raised 7th to the tonic | 90–100 | Guitar · Overdrive |
| Villera Lead | lead | 2 | sharp keyboard lead around the relative minor | 95–105 | Calf Monosynth |
| Orquesta Brass | lead | 2 | 1950s big-band cumbia call and answer | 90–105 | Trumpet |
| Accordion Offbeats | chords | 4 | off-beat accordion chords I–V–V–I | 85–100 | Accordion |
| Sonidera Organ | chords | 4 | combo organ on the "and" of 1 and 3, held; I–IV–V–I | 80–92 | Jazz organ |
| Villera Stabs | chords | 4 | two quick stabs each half bar, relative minor i–VII (vi–V) | 95–105 | TAL NoiseMaker |
| Chicha Surf | chords | 4 | surf guitar strums: i–VII–i–V of the relative minor (V major, chromatic) | 90–100 | Guitar · Clean |
| Orquesta Hits | chords | 4 | brass hits on the "and" of 2 and on 4, I–IV–V–I | 90–105 | Brass section |

References:
- [Cumbia villera (Wikipedia)](https://en.wikipedia.org/wiki/Cumbia_villera);
  [Cumbia santafesina (Wikipedia)](https://en.wikipedia.org/wiki/Cumbia_santafesina);
  [Guacharaca (Wikipedia)](https://en.wikipedia.org/wiki/Guacharaca)
- [Latin Beats: cumbia on a drum kit and congas (Reverb)](https://reverb.com/news/latin-beats-how-to-play-the-cumbia-style);
  [What is cumbia (Orphiq)](https://orphiq.com/resources/what-is-cumbia)
- The Jamzone cumbia lesson, which gives the güira's down, down-up figure; its PDF link is now
  dead.
- Sergio Martín's gaita / porro / cumbia analysis in the [Berklee archive](https://archives.berklee.edu/node/50311/ocr)
- Chicha: [MasterClass chicha guide](https://www.masterclass.com/articles/chicha-music-guide);
  [My Hot Chicha Summer](https://newdirectionsinmusic.substack.com/p/my-hot-chicha-summer);
  [Cumbia is just like techno](https://globalbassstudies.substack.com/p/im-here-to-convince-you-that-cumbia)

## Piig: Natural Minor, with the Dorian IV and the harmonic V

After the candle-lit lo-fi hip-hop and neo-soul of Biig Piig's early EPs (*Big Fan of the
Sesh*, *A World Without Snooze*, *No Place for Patience*): lazy 2- and 4-bar loops, muted
drums (rim, shaker, brushes, soft kicks), a round legato bass, Rhodes and jazz-guitar 7th and
9th chords, and saxes in the background. **Play it in D minor at 79 BPM**, the key and tempo
of *24K* (songbpm.com; chord sites that say 150 count it in double time), with SWING 56–60.

Three families, one preset of each instrument in each. A family's four presets share their
chord changes, so they play together; the 2-bar drums loop under the 4-bar parts. The
progressions come from the songs (Ultimate Guitar's chord sheets), and every line is original:

| Family | Progression | From |
|---|---|---|
| Smoke | i – IV – iv – VI VII (Dm G Gm Bb C) | *24K*: the Dorian IV (B natural) falling to the minor iv |
| Lay Here | i7 – V7 | *Perdida* (Gm7 D7 there): the V's raised third |
| Daffodil | VII – iv – i – i | *Sunny* (Dm Am Em there) |

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Smoke Dust | drums | 2 | dusty boom bap: kick on one and the "a" of two, sixteenth hats with holes, rim ghosts, an open hat turning bar two | 76–84 | SP1200 1 |
| Lay Here Bossa | drums | 2 | a lazy bossa: surdo-like kick, side stick on the bossa clave, closed hat as the shaker | 76–84 | Standard kit |
| Daffodil Brushes | drums | 2 | ride "ding, ding-a", hat foot on 2 and 4, feathered kick, brush snare | 76–84 | Brush · ride |
| Smoke Sub | bass | 4 | round sustained sub gliding between roots, B natural under the IV, B flat under the iv | 76–84 | 808 · Monosynth |
| Lay Here Upright | bass | 2 | bossa root and fifth, the raised 7th leading home | 76–84 | Upright |
| Daffodil Walk | bass | 4 | held roots walking into each change | 76–84 | Finger bass |
| Smoke Alto | lead | 4 | background alto rising to the octave, then the same fall over IV and iv | 76–84 | Alto sax |
| Lay Here Tenor | lead | 2 | a tenor answering late in the bar, the V's third resolving | 76–84 | Tenor sax |
| Daffodil Alto | lead | 4 | long alto tones between the chords and a falling answer | 76–84 | Alto sax |
| Smoke Rhodes | chords | 4 | i9 – IV9 – iv9 – VImaj7 VIIadd9, each a sixteenth late with a pushed re-hit | 76–84 | Rhodes |
| Lay Here Guitar | chords | 2 | i7 – V7 comped in the bossa's eighths | 76–84 | Jazz guitar |
| Daffodil Keys | chords | 4 | VIIadd9 – iv9 – i9 – i11, laid late and touched again | 76–84 | Upright piano |

The texture the records have (vinyl crackle, a 12-bit sampler's grit, the tape's wobble, a
low-pass on the chords) is not in a pattern: the machines' FX (a low-pass, DRIVE, a little
reverb) get part of the way.

References: [24K, tempo and key (songbpm)](https://songbpm.com/@biig-piig/24k);
[Biig Piig chords and tabs (Ultimate Guitar)](https://www.ultimate-guitar.com/artist/biig_piig_618029):
*Perdida*, *Sunny*, *Switch*, *Oh No*, *Feels Right*.

## Folk: Major, the modal tunes on degree 2 (Dorian)

Made for **G major**. The chords are the songs' (Ultimate Guitar): Knockin' on Heaven's Door
(G D Am | G D C), The Times They Are A-Changin' in 3/4 (G Em C G | G Am C D), The House of the
Rising Sun in 6/8 (Am C D F Am E Am E: the F and the E major from outside the key), Dirty Old
Town and Whiskey in the Jar (I IV I | V vi), Scarborough Fair and Matty Groves (A Dorian in G
major: ii I ii IV | ii IV V ii). Drunken Sailor is the traditional tune (public domain).

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Dylan Shuffle | drums | 2 | folk rock's train beat, the tambourine on the off-beats | 68–80 | Folk · bodhrán |
| Bodhran Jig | drums | 3 (6/8) | the bodhrán's eighths, 1 and 4 strong | 150–170 | Folk · bodhrán |
| Reel Stomp | drums | 2 | a foot on every beat, bodhrán eighths, claps, tambourine sixteenths | 110–125 | Folk · bodhrán |
| Changin' Waltz | drums | 3 (3/4) | kick on one, the snare on two and three, the ride | 85–95 | Folk · bodhrán |
| Whiskey Gallop | drums | 2 | driving eighths, the backbeat, a tom roll | 120–140 | Folk · bodhrán |
| Heaven's Door Roots | bass | 2 | root and fifth under I V ii / I V IV | 68–75 | Acoustic bass |
| Jig Bass | bass | 3 (6/8) | root on 1, fifth on 4, the strong one louder | 150–170 | Upright |
| Rising Sun Walk | bass | 6 (8 of 6/8) | falling with the eight chords | 110–120 | Contrabass |
| Changin' Oom-Pah | bass | 3 (3/4) | the root, then the fifth twice | 85–95 | Acoustic bass |
| Dorian Drone | bass | 4 | the A held, stepping to G, swelling and easing | 60–90 | Contrabass |
| Fiddle Jig | lead | 3 (6/8) | eighths in threes, the bow leaning on each first, a grace note snapped in early | 150–170 | Fiddle |
| Banjo Roll | lead | 2 | a Scruggs roll 3 + 3 + 2 over I and IV, accented | 100–120 | Banjo |
| Whistle Air | lead | 4 | a slow air, each long note led in by a cut played early | 60–75 | Recorder |
| Drunken Sailor | lead | 4 | the traditional shanty, in the Dorian of degree 2 | 100–120 | Bagpipe |
| Rising Sun Harp | lead | 6 (8 of 6/8) | the song's picking: root, fifth, octave, third, fifth, octave | 110–120 | Harp |
| Heaven's Door Strum | chords | 4 | G D Am / G D C strummed, down-up-down | 68–75 | Guitar · Acoustic |
| Changin' 12-String | chords | 6 (8 of 3/4) | G Em C G / G Am C D, on one, two and three | 85–95 | Guitar · 12-string |
| Rising Sun Accordion | chords | 6 (8 of 6/8) | the eight chords held a 6/8 bar each | 110–120 | Accordion |
| Dirty Old Town Pah | chords | 4 | I IV I / V vi, the accordion's off-beat "pah" | 100–120 | Accordion |
| Scarborough Harp | chords | 4 | ii I ii IV / ii IV V ii (A Dorian), held | 60–90 | Harp |

## Heavy Metal: Natural Minor, with the ♭2, the ♭5 and the raised 7th

Made for **E minor**. From Ultimate Guitar's tabs and chord sheets: Black Sabbath's Paranoid
(Em D G D Em) and Iron Man (B D D E E, G F♯ G F♯ G F♯ D D E E); Iron Maiden's The Trooper
(E5 D G D, C5 D) and Fear of the Dark (Dm B♭ C: i VI VII); Judas Priest; Metallica's Master of
Puppets (the chromatic fall from E); Motörhead's Ace of Spades. The drums are on the AVL kits.

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Paranoid Drive | drums | 2 | eighth hats, backbeat, the kick pushing the "and"s | 160–165 | Black Pearl 5 |
| Maiden Gallop | drums | 2 | the gallop on the kick, sixteenth hats (Clive Burr's) | 160–180 | Black Pearl 5 |
| Doom Half-Time | drums | 2 | Sabbath's half time, the ride's quarters, a tom roll | 70–80 | Black Pearl 5 |
| Double Kick | drums | 2 | sixteenth double bass, backbeat, crashes | 110–140 | Black Pearl 5 |
| Speed Rock | drums | 2 | the kick on every eighth, the ride driving | 135–145 | Red Zeppelin 5 |
| Paranoid Eighths | bass | 2 | i VII III VII i in eighths, picked hard on the beat | 160–165 | Picked bass |
| Harris Gallop | bass | 4 | Steve Harris's gallop under i VI VII i, the eighth louder | 160–180 | Picked bass |
| Iron Riff | bass | 4 | after Iron Man, slow, a slide into the first note | 70–80 | Guitar · Heavy muted |
| Thrash Chromatic | bass | 2 | a palm-muted E in sixteenths (@72–78), accented notes falling E D♯ D C♯ | 180–200 | Guitar · Heavy muted |
| Anthem Octaves | bass | 2 | i VI VII in eighths jumping octaves | 140–160 | Picked bass |
| Trooper Twin Lead | lead | 4 | a gallop melody climbing and falling | 160–175 | Guitar · Heavy lead |
| Iron Theme | lead | 4 | Iron Man's riff an octave up | 70–80 | Guitar · Heavy lead |
| Pentatonic Lick | lead | 2 | a blues lick, slides into the bend notes, ringing out | 80–110 | Guitar · Valve OD |
| Harmonic Run | lead | 2 | sixteenth arpeggios of i and the major V | 100–130 | Guitar · Heavy lead |
| Dark Anthem | lead | 4 | long notes over i VI VII with pickups | 140–160 | Guitar · Heavy lead |
| Paranoid Power | chords | 2 | Em D G D Em in palm-muted eighths | 160–165 | Guitar · Heavy rhythm |
| Trooper Gallop | chords | 2 | E5 D C5 galloping (two voicings alternate so each hit sounds) | 160–175 | Guitar · Heavy rhythm |
| Iron Doom | chords | 2 | B5 D5 E5, G5 F♯5, held | 70–80 | Guitar · Heavy rhythm |
| Anthem i-VI-VII | chords | 4 | i VI VII, struck twice a bar | 140–160 | Guitar · Heavy rhythm |
| Chromatic Fall | chords | 2 | E5 D♯5 D5 C♯5, then the ♭II | 180–200 | Guitar · Heavy rhythm |

## Black Metal: Natural Minor, with the Phrygian ♭2 and the ♭5

Made for **E minor**. From Ultimate Guitar's tabs: Darkthrone's Transilvanian Hunger (a falling
tremolo line over an open pedal), Burzum's Dunkelheit (Em arpeggios moving a half step up),
Mayhem's Freezing Moon, Emperor's I Am the Black Wizards, Bathory's One Rode to Asa Bay
(i VII … VI). The blast beat after Wikipedia's: the kick and the snare alternating sixteenths,
a cymbal with each kick; the hammer blast all three together; the skank beat. SyncTimer stops
at 200 BPM: the fastest presets sit just under it.

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Traditional Blast | drums | 2 | kick and snare alternating sixteenths, the crash with the kick | 180–200 | Black Pearl 5 |
| Hammer Blast | drums | 2 | kick, snare and cymbal together on the eighths | 180–200 | Black Pearl 5 |
| Skank Beat | drums | 2 | kick on the beat, snare on its "and" | 160–190 | Black Pearl 5 |
| Frozen March | drums | 2 | sixteenth double kick, the snare on three | 100–130 | Black Pearl 5 |
| Viking March | drums | 2 | Bathory's slow epic, the floor toms answering | 80–100 | Black Pearl 5 |
| Tremolo Roots | bass | 2 | i VI VII in eighths | 160–200 | Picked bass |
| Pedal Swell | bass | 2 | the root in sixteenths swelling 70→118 and back | 160–200 | Picked bass |
| Phrygian Crawl | bass | 4 | i and ♭II in half notes, the ♭5 passing | 100–180 | Picked bass |
| Symphonic Drone | bass | 4 | i VI VII i held, swelling (Emperor's keyboards) | any | Organ · Bourdon 16 |
| Viking Walk | bass | 4 | i VII i VII VI under the march | 80–100 | Picked bass |
| Hunger Tremolo | lead | 4 | after Transilvanian Hunger: a falling line, each note tremolo-picked a beat (down 112, up 86) | 160–200 | Guitar · Heavy lead |
| Dunkelheit Arpeggio | lead | 4 | Em arpeggio in eighths, then a half step up (F) | 100–130 | Guitar · Heavy lead |
| Frozen Melody | lead | 4 | slow notes tremolo-picked half a bar each | 160–200 | Guitar · Heavy lead |
| Symphonic Choir | lead | 4 | long sung notes over the drone | any | Choir |
| Tritone Riff | lead | 2 | root, ♭2 and ♭5 in accented sixteenths | 140–180 | Guitar · Heavy lead |
| Hunger Chords | chords | 4 | i VI VII i held | 160–200 | Guitar · Heavy rhythm |
| Phrygian Dread | chords | 4 | i for two bars, the ♭II, back | any | Guitar · Heavy rhythm |
| Symphonic Strings | chords | 4 | i iv V i, slow strings | any | Strings · Bowed |
| Dunkelheit Shapes | chords | 4 | Em, then F (the ♭II), two bars each | 100–130 | Guitar · Heavy rhythm |
| Cathedral Organ | chords | 4 | i iv i V, in full | 60–90 | Organ · Plein jeu |

## Post-Punk: Natural Minor, with the Dorian IV

Made for **A minor**. The progressions are the bands' (Ultimate Guitar), each on its degrees of
a minor key: The Cure's A Forest (Am C F D: i III VI IV, the Dorian major IV), Lullaby (i VI) and
Boys Don't Cry (A Bm C♯m D in F♯ minor: III iv v VI); Joy Division's Love Will Tear Us Apart
(D A Bm Em in B minor: III VII i iv), Disorder and She's Lost Control; Siouxsie and the Banshees'
Spellbound (D Dorian: i7 VII IV); The Sisters of Mercy's Temple of Love (i III IV) and Lucretia My
Reflection (i III iv); Bauhaus's Bela Lugosi's Dead. The bass leads (Peter Hook), high and
melodic, some notes a little late (NUDGE).

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Lost Control | drums | 2 | sixteenth hats, the snare cracking, a syncopated kick | 140–150 | Room kit |
| Tribal Toms | drums | 2 | a floor-tom figure instead of the backbeat | 130–160 | Room kit |
| Doktor Avalanche | drums | 2 | the Sisters' drum machine: four on the floor, open hats on the "and" | 125–140 | Boss DR55 |
| Forest Run | drums | 2 | A Forest's beat, an open hat on the "and" of four | 130–140 | Roland CR78 |
| Undead Dub | drums | 2 | Bela Lugosi's rim-click clave, soft hats, toms | 115–125 | Room kit |
| Hook Melody | bass | 4 | the bass carrying the melody over III VII i iv, off-beats late | 145–150 | Squier bass |
| Forest Pulse | bass | 4 | A Forest's eighth-note pulse on i III VI IV | 130–140 | Squier bass |
| Undead Dub Bass | bass | 2 | a falling dub figure, all behind the beat | 115–125 | Squier bass |
| Disorder Run | bass | 2 | busy eighths climbing the minor | 155–165 | Squier bass |
| Boys Walk | bass | 2 | III iv v VI in eighths, up the scale | 155–170 | Squier bass |
| Forest Arpeggio | lead | 4 | a chorused arpeggio on i III VI IV | 130–140 | Guitar · Chorus |
| Tear Apart Synth | lead | 4 | a falling, singing synth figure | 145–150 | Calf Monosynth |
| Spellbound Sixteenths | lead | 4 | fast arpeggios on i VII IV | 145–150 | Guitar · Chorus |
| Temple Chime | lead | 2 | high ringing eighths over i III IV | 135–145 | Guitar · Valve OD |
| Lullaby Creep | lead | 2 | plucked notes tiptoeing, some early | 110–120 | Guitar · Clean |
| Forest Chords | chords | 4 | Am C F D(add9), struck and pushed | 130–140 | Guitar · Chorus |
| Tear Apart Strings | chords | 4 | III VII i iv on the string synth | 145–150 | Strings · Fat |
| Boys Strum | chords | 2 | III iv v VI in eighth strums | 155–170 | Guitar · Clean |
| Spellbound Dorian | chords | 4 | i7 VII IV i7–VII | 145–150 | Guitar · 12-string |
| Lucretia Gloom | chords | 4 | i III iv on the organ's vox humana | 125–135 | Organ · Vox humana |

## Gregorian (old gothic): Dorian

Made for **D Dorian** (SCALE Dorian, ROOT D), the chant's first mode. The Dies Irae (13th
century, public domain) is the three phrases of the mfiles.co.uk MIDI: F E F D E C D D |
F F G F E D C E | F E D A C D D. **Organum Above** (lead) and **Organum Below** (bass) sing it a
perfect fifth over and a perfect fourth under, note for note, in its rhythm (organum's parallel
fifths and fourths, after the Musica enchiriadis): any two of the three loop together. Dead Can
Dance's i v VII IV (In Power We Entrust the Love Advocated: Am Em G D), a saltarello in 6/8, the
drone under the chant, and a breakbeat under it the 90s way. The chant's notes swell to the
phrase's middle (80–98) and lean a hair early or late.

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Processional | drums | 2 | timpani D on one, A on three, the bass drum, a cymbal swell | 55–70 | Orchestra · D |
| Saltarello | drums | 3 (6/8) | tambourine eighths (1 and 4 strong), the frame drum leaping | 150–170 | Folk · bodhrán |
| Chant Breakbeat | drums | 2 | a lazy break under the chant | 92–100 | SP1200 1 |
| Wrath Timpani | drums | 2 | the D, the A, a roll into the bar, the cymbal | 55–70 | Orchestra · D |
| Ritual Frame | drums | 2 | the frame drum's 3 + 3 + 2, the tambourine's shimmer | 70–90 | Folk · bodhrán |
| Ison Drone | bass | 4 | the final held, the fifth a bar, a breath | 50–80 | Organ · Bourdon 16 |
| Organum Below | bass | 8 | the Dies Irae a fourth under | 60–80 | Cello |
| Open Fifths | bass | 4 | D and A, two bars each, swelling | 50–80 | Contrabass |
| Ostinato Pulse | bass | 4 | quarters on D growing 40→110, the A falling back | 60–90 | Contrabass |
| Dorian Ground | bass | 4 | i v VII IV, roots held, a step into each | 60–90 | Cello |
| Dies Irae | lead | 8 | the chant, sung | 60–80 | Choir |
| Organum Above | lead | 8 | the Dies Irae a fifth over | 60–80 | Voice oohs |
| Krummhorn Estampie | lead | 4 | a lively Dorian dance in eighths | 100–120 | Organ · Krummhorn |
| Kyrie Melisma | lead | 4 | one syllable over many notes, rising to the fifth | 55–70 | Choir |
| Saltarello Recorder | lead | 3 (6/8) | leaping eighths, 1 and 4 leaned on | 150–170 | Recorder |
| Organum Fifths | chords | 8 | open fifths D C A D, two bars each, sung | 55–80 | Choir |
| Dorian Cadence | chords | 4 | i IV VII i (the mode's major IV) | 55–80 | Organ · Pipe 16+8+4 |
| Gothic Choir | chords | 4 | i v VII IV, held | 60–90 | Choir |
| Vox Humana | chords | 4 | Dsus2 Dm Dsus4 Dm | 50–80 | Organ · Vox humana |
| Harp Psalter | chords | 3 (6/8) | i and VII on the dotted quarters | 150–170 | Harp |

References for the five packs:
[Ultimate Guitar](https://www.ultimate-guitar.com) (each song's chord sheet or tab, found with
`tools/genre-research/ug-chords.py`);
[Blast beat (Wikipedia)](https://en.wikipedia.org/wiki/Blast_beat);
[Organum (Wikipedia)](https://en.wikipedia.org/wiki/Organum);
[Dies Irae, score and MIDI (mfiles)](https://www.mfiles.co.uk/scores/gregorian-dies-irae.htm);
[The jig rhythm (Soundbrenner)](https://www.soundbrenner.com/blogs/articles/jig-rhythm);
[A Matter of Life and Drums (Invisible Oranges)](https://www.invisibleoranges.com/?p=44567)
(Clive Burr's sixteenth hats).

## Solos: Major (ballads after Coltrane's *Ballads* and Chet Baker)

Made for **Eb major** (a tenor's ballad key; the lead's degree 1 is Eb4, so the tenor sings
"5-".."1+" and cries up to "2+", the soprano floats "5".."3+", the trumpet stays "7-".."6").
The minor moods sit on degree 6 (C minor), and Devotion vamps on degree 2 (F Dorian). Six
original ballad solos for the LEAD, each with the brushes, the bass and the chords it is heard
over. They are moody, prolonged and passionate, with no fast passages. The model is the John
Coltrane Quartet's *Ballads* (Impulse!, 1962/63: Tyner, Garrison, Jones), plus Baker's slow
trumpet. Nothing is quoted: the album's standards and the recorded solos are copyrighted. The
style was studied (`tools/genre-research/solos.md`), and every line, progression and rhythm is
new.

The playing:

- Tempo 56–70.
- Long held notes, 6–12 steps, with a beat or half a bar of air between phrases.
- A swell written across each phrase in velocities: @60 rising to @100–110 and falling back.
  The MODS soften each note's attack (ATTACK +2400 timecents on the sax, +3600 on the
  trumpet) and lengthen the release.
- Every long note sits 8–16 % of a step late, the rubato lean.
- Flurries only as ornaments: three or four sixteenths pushed early and climbing into a long
  note.
- A scoop or slur (~) into a long tone.

The chords are Tyner-style: rootless 9ths and 13ths, the So What fourths, fourths planed over
a pedal, Lydian clusters, the minor iv (Abm6) and the backdoor Db9, each held a bar or half a
bar and then re-voiced. The bass is Garrison's two-feel, whole notes and pedal. The drums are
brushes only, darkened with TONE/CUTOFF, with a crash rolled up into the downbeat for the
cymbal swell.

| Preset | Part | Bars | What it is | Tempo | Sound |
|---|---|---|---|---|---|
| Vow Brushes | drums | 2 | brushes swept in eighths, the slap and the foot on 2 and 4, a feathered kick, the ride entering at the end | 62–70 | Brush · ride |
| Lament Swells | drums | 2 | slow brushes, the slap on 2 and 4, a crash rolled up over two beats into the accented downbeat | 54–60 | Brush · crash |
| Devotion Mallets | drums | 2 | the ride skipping, toms rolling around the pedal, a brush slap closing the loop | 66–72 | Brush · ride |
| Nocturne Whisper | drums | 2 | the ride on 1 and 3, the foot, two brush taps, one click | 56–64 | Brush · ride |
| Twilight Swirl | drums | 2 | the swirl as soft sixteenth taps, the slap on 2 and 4, the two-feel kick | 58–66 | Brush · ride |
| Rain Brushes | drums | 2 | brushes in 3 + 3 + 2, the slap only on 4, a soft crash on the loop's top | 54–62 | Brush · crash |
| Vow Two | bass | 8 | half notes behind the beat, a chromatic eighth into each change | 62–70 | Upright |
| Lament Pedal | bass | 8 | the C held under the line cliché, half notes, a G back into it | 54–60 | Upright |
| Devotion Pedal | bass | 8 | the F pedal with its fifth and a push for four bars; Ab, G, F; C7 held, E into the F | 66–72 | Upright |
| Nocturne Roots | bass | 8 | a note a bar under the floating line | 56–64 | Upright |
| Twilight Two | bass | 8 | the two-feel, root and fifth or third, D into the Eb | 58–66 | Acoustic bass |
| Rain Long Tones | bass | 8 | whole notes, an A into the Bb, the backdoor Db | 54–62 | Acoustic bass |
| Trane Vow | lead | 8 | a warm major ballad (I vi ii V, iii VI7 ii iv, I VI7alt ii V) paraphrased in long tones: the minor iv's Cb sliding down, a chromatic climb into the high Eb cried | 62–70 | Tenor sax |
| Trane Lament | lead | 8 | C minor over the line cliché and the minor ii–V: a beat of silence, the G held, a flurry up G7's b9 arpeggio into a long Eb5 cry, the D sighing to C | 54–60 | Tenor sax |
| Trane Devotion | lead | 8 | the passionate one: from a soft low F over the F pedal, climbing for eight bars to F5, cried three times (@104–110), C7alt home | 66–72 | Tenor sax · Bright |
| Soprano Nocturne | lead | 8 | the soprano floating over IV iii ii I (the Lydian #11), the Cb of the minor iv, a turn up to the G5 | 56–64 | Soprano sax |
| Baker Twilight | lead | 8 | Baker's major ballad (I #i°7 ii V, iii VI7 ii V, I vi ii V): few notes, low and soft (@60–76), all late, a scoop into the G | 58–66 | Trumpet · Cool |
| Baker Rain | lead | 8 | Baker in the minor: half a bar of silence, the Eb, the backdoor iv–bVII7 with its Cb, a scoop, the B of G7 | 54–62 | Trumpet · Cool |
| Vow Voicings | chords | 8 | lush rootless voicings held, re-voiced on 3 (Ebmaj9 to 6/9, Cm11 to Cm9, Bb13sus to b9) | 62–70 | Grand piano |
| Lament Line | chords | 8 | Cm with C B Bb A under a held D, Dø G7alt, Abmaj7#11 clusters, Cm(maj9) | 54–60 | Grand piano |
| Devotion Fourths | chords | 8 | fourths planed over the F pedal, the Lydian IV, Gm11, C7alt to C7#9 | 66–72 | Grand piano |
| Nocturne Floating | chords | 8 | one chord a bar, Abmaj9#11 Gm11 Fm11 Eb6/9, then the minor iv and a ii–V | 56–64 | Grand piano |
| Twilight Piano | chords | 8 | I #i°7 ii V iii VI7 ii V I vi ii V, each held and re-voiced | 58–66 | Upright piano |
| Rain Rhodes | chords | 8 | Cm9 Abmaj9 Fm9 Bb13, Ebmaj9, Abm6 Db9, Ebmaj9 Cm7, Dø G7b9 | 54–62 | Rhodes |

No sounds were added; the MODS (ATTACK, RELEASE, vibrato, TONE/CUTOFF) need a render check on
milo (see the research notes). The first version (bebop: Bird Changes, Bird Blues, Trane
Countdown, Trane Fourths, Baker Ballad, Baker Cool, and their drums, bass and chords, in Bb
major) is in commit 3d3f71f.

References: [Ballads (Wikipedia)](https://en.wikipedia.org/wiki/Ballads_(John_Coltrane_album));
[Ballads review (Positive Feedback)](https://positive-feedback.com/reviews/music-reviews/john-coltrane-quartet-ballads/);
[Ballads review (MusicWeb International)](https://musicweb-international.com/jazz/2002/Apr02/Coltrane_ballads.htm);
[Balladen, die zweite Seele des John Coltrane (SRF)](https://www.srf.ch/kultur/musik/musik-balladen-die-zweite-seele-des-john-coltrane);
[Ballads, editorial notes (Apple Music)](https://music.apple.com/album/1440747672);
[You Don't Know What Love Is (Michael's jazz blog)](https://michaelsjazzblog.com/?p=32);
[Quartal voicings (Piano with Willie)](https://pianowithwillie.com/quartal-fourth-voicings/);
[McCoy Tyner (jazz.com)](https://jazz.com/encyclopedia/tyner-mccoy);
[Chet Baker: My Funny Valentine (jazz.com)](https://jazz.com/music/chet-baker-my-funny-valentine-1952);
[Chet Baker's long goodbye (Hackworth)](https://martinhackworth.substack.com/p/chet-bakers-long-goodbye).

## Jazz

The original pack. It has no `sound` field. See `jazz-presets/build.py`.

## Vuelo (Flight Facilities)

Natural Minor; A minor is Arty Boy's key, C# minor Crave You's (the two templates, both at
120: Crave You is 120 on every listing, Arty Boy's groove sits there too). The band's own
progressions from their chord sheets (Ultimate Guitar, 2026-10-11): Arty Boy's verse F Am Em C
(VI i v III) in its timing (the first chord a bar and a half, the second the last two beats:
| F F F F | F F Am Am |), its pre-chorus F Am Dm E (VI i iv V, the major V chromatic), its
chorus F Em (VI v); Crave You's C#m7 Gdim7 F#m7 B7sus4 (i7, a chromatic ♯iv°7, iv7, a chromatic
VII7sus4), one bar each; Need You's Am G F G (i VII VI VII); Two Bodies' F C Am G (VI III i
VII); Stranded's Gmaj7 A Em7 A Bm (VI VII iv VII i). The lines are original: nu-disco drums
(a 909 four on the floor with claps and open hats on the off-beats, an 808 for Crave You's
laid-back pulse, a Linn disco shuffle with 16th hats, a build with a snare roll into a
crash), octave disco basses riding between the kicks, a slap riff, a sub with slides, the
funk guitar riff with muted 16ths (@42), a Rhodes hook, a string rise written as a velocity
swell, an 80s synth lead on slides, a lazy sax behind the beat (>8).

| Preset | Bars | BPM | Sound |
|---|---|---|---|
| Vuelo · Four On The Floor | 2 | 118–124 | TR909 (MODS: the kit's TONE down a little) |
| Vuelo · Crave Groove | 2 | 116–122 | TR808 |
| Vuelo · Disco Shuffle | 2 | 118–124 | LINN9000 |
| Vuelo · Arty Funk | 2 | 116–122 | TR909 (MODS: the kit's LENGTH shorter) |
| Vuelo · Build And Crash | 2 | 118–124 | TR909 |
| Vuelo · Crave Walk | 4 | 116–122 | Finger bass |
| Vuelo · Arty Pulse | 4 | 116–122 | Synth bass |
| Vuelo · Octave Disco | 4 | 118–124 | Picked bass |
| Vuelo · Sub Pulse | 4 | 116–122 | Sine sub |
| Vuelo · Slap Riff | 2 | 116–122 | Slap bass |
| Vuelo · Guitar Riff | 2 | 116–122 | Guitar · Clean |
| Vuelo · Rhodes Hook | 2 | 116–122 | Rhodes |
| Vuelo · String Rise | 2 | 116–124 | Violin |
| Vuelo · Synth Slide | 2 | 116–122 | Calf Monosynth |
| Vuelo · Sax Line | 2 | 116–122 | Alto sax |
| Vuelo · Arty Verse | 4 | 116–122 | Guitar · Chorus |
| Vuelo · Arty Pre | 4 | 116–122 | Rhodes |
| Vuelo · Crave Loop | 4 | 116–122 | Jazz guitar |
| Vuelo · Chorus Stabs | 2 | 118–124 | Organ · House |
| Vuelo · String Pads | 4 | 116–122 | Strings · Ensemble |

References: the chord sheets (ug-chords.py: Arty Boy 2137129, Crave You 1132236, Need You
5587641, Stranded 3235883, Two Bodies 1931097), the user's charts of Arty Boy's strumming
timing and Crave You's groove (minimal struck chords in the verse, a down-up rhythm in the
chorus), SongBPM's 120 for Crave You, the band on their own sound (70s disco grooves, 909
rhythms, slinky basslines: Boss Hunting and Mixmag interviews, 2017–2024).
