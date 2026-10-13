# R&B pack: research notes (2026-10-12)

Contemporary R&B after Jorja Smith and Snoh Aalegra, for `sources/rnb`. The songs'
progressions and tempos are the reference; nothing is quoted (every line, melody and rhythm in
the pack is original). Chord sheets were fetched with
`sources/research/ug-chords.py OUT "artist::title" …` (Ultimate Guitar, most-voted sheet).

## The songs: progressions, keys, tempos

Tempos and keys from two automatic analyses: SongBPM (Spotify's analysis, songbpm.com) and
AcousticBrainz (the low-level descriptors, acousticbrainz.org, looked up by MusicBrainz
recording id). They often disagree by a factor of two; the slow, half-time reading is the
one these songs are felt in (and both sources agree once halved). I could not listen to the
recordings, so the tempos are the analyses', not mine.

| Song | Chord sheet (UG) | On E minor's degrees | Key | BPM |
|---|---|---|---|---|
| Jorja Smith – Be Honest | Cmaj7 B7 Em Em (2800520) | VImaj7 V7 i i | E minor (sheet) | no analysis found |
| Jorja Smith – Teenage Fantasy | Am B7 Em D (2065615) | iv V7 i VII | E minor (sheet; AB says A minor) | 88 (AB); SongBPM 176 = 2 × 88 |
| Jorja Smith – Blue Lights | F G Am G, capo 3 (2723457) | VI VII i VII (on the relative minor) | G major / E minor (SongBPM) | 92 (SongBPM) |
| Jorja Smith – Don't Watch Me Cry | Ab Bbm Gb Db (2239329) | VII i VI III | Bb minor | — |
| Jorja Smith – On My Mind | Am C G D (3056365) | i III VII IV (the Dorian IV) | A minor / Bb minor (AB) | 129.5 (AB): the UK-garage single, not used |
| Jorja Smith – Where Did I Go? | D Fmaj7 G6/9/E Bb/F (1954429) | — (modal mixture, not used) | F major (SongBPM) | 97 (SongBPM) |
| Snoh Aalegra – Fool For You | Em9 F#m(b9) Dmaj7 Bm7 B7 (2452745) | i9 IV13 VIImaj7 v7 V7 (the F#m(b9) shape over A is an A13: the Dorian IV) | E minor (sheet) | 75: AB 150, SongBPM 150, both halved |
| Snoh Aalegra – Situationship | Bm9 C#m11 (4027984) | i9 ii11 (the Dorian ii) | F# minor (SongBPM), Bm on the sheet | 90 (SongBPM) |
| Snoh Aalegra – Whoa | Ebmaj7 D7 Fm Gm7 (3085499) | VImaj7 V7 ♭vii9 i7 (in G minor; the Fm is chromatic) | Bb major / G minor (AB) | 94 (AB, SongBPM) |
| Snoh Aalegra – Lost You | Cm Gm7 Ab Fm7 (3762680) | i v7 VI iv7 | C / F minor | — |
| Snoh Aalegra – I Want You Around | F Em Am Gm7 C (2622450) | VI v i ♭vii7 III (in A minor) | G# minor (AB) | 84 (AB); SongBPM 168 = 2 × 84 |
| Snoh Aalegra – Find Someone Like You | Emaj7 C#m7 Bm7 F#m9 (2832151) | IIImaj7 i7 (♭vii7) iv9 on the relative minor | E major (AB) | 84.9 (AB); SongBPM 169 |
| Snoh Aalegra – Nothing Burns Like the Cold | — | — | — | 69 (SongBPM 138 halved) |
| Daniel Caesar – Best Part | Dmaj7 Am7 Gmaj7 Bbmaj7 (2126075) | (the genre's maj7 colour; not used) | D major | — |
| H.E.R. – Focus | C G A7 Dm7 Fm, capo 4 (2051855) | (not used) | — | — |

**The pack's choice: Natural Minor, E minor, 86 BPM, SWING 56 (16ths).** Most of the
references are minor (Be Honest, Teenage Fantasy, Don't Watch Me Cry, Fool For You, Lost You,
Situationship); the major ones (Blue Lights, Find Someone Like You) sit on the relative minor.
E minor is the key of three of the sheets (Be Honest, Teenage Fantasy, Fool For You). The
tempos cluster at 84–94 (I Want You Around 84, Find Someone 85, Teenage Fantasy 88,
Situationship 90, Blue Lights 92, Whoa 94): 86 is their middle, leaning to the slower ones. A
second template, **R&B · Slow Jam**, sits at Fool For You's 75 with SWING 58 (Nothing Burns
Like the Cold, 69, is slower still). The chromatic chords of the songs (the harmonic V7, the
Dorian IV13 and ii11, Whoa's ♭vii) are chromatic `c` voicings.

## The style

- **Harmony.** Extended chords: maj7/maj9, min9, 11ths, 13ths, the dominant with #9 or b9
  (the sheets above: Em9, F#m(b9), Dmaj7, Bm9, C#m11, Ebmaj7, Gm7, G7#9). Two-chord vamps
  (Situationship) and four-chord loops a bar each.
- **Drums** (neo-soul and contemporary R&B programming): the snare or clap laid back 5–15 ms
  behind a kick and hats kept on the grid; ghost notes at 30–40 % velocity on the 16ths
  before the backbeats, barely audible; hats nudged early against a late snare for the
  push-pull; swing from the groove/quantize; 808 or soft acoustic kicks, rimshots, claps
  ([soundbridge.io](https://www.soundbridge.io/drum-programming-tips-for-producers-of-all-levels);
  [UJAM: neo-soul drums](https://www.ujam.com/tutorials/how-to-make-neo-soul-drums/);
  [Violet Recording: groove and swing](https://violetrecording.com/how-to-add-groove-to-a-beat/);
  [Attack Magazine: ghost notes](https://www.attackmagazine.com/?p=6110);
  [Bonedo: ghost notes tutorial](https://www.bonedo.de/artikel/einzelansicht/drum-programming-tutorial-6.html)).
- **What a ravving drum chart can hold.** A hit or an accented hit, no per-hit velocity or
  nudge (DrumMachine::applyChart), and the accent is the whole step's. So the backbeats are the
  accented steps and the ghosts the plain hits, the lay-back is written by placement (a kick on
  the "a", a ghost a 16th after the snare: the drag) and the template's SWING; the per-note
  nudges (>6–14) go to the bass, the lead and nothing else.
- **Bass.** Sub and synth bass under the root, 808 slides (the 808 · Monosynth glides; the
  soundfont basses only overlap), fretless and finger bass walking between the chords, behind
  the beat.
- **Lead.** Vocal lines: pentatonic melismas (a run of 16ths into a long note), scoops (~),
  grace notes snapped in early, every long note late; voice "oohs", a flute, strings, a Rhodes
  answering in the gaps.
- **Snoh Aalegra's arrangements.** Lush piano and strings over slow, swung drums (the albums
  *Ugh, Those Feels Again*, 2019, and *Temporary Highs in the Violet Skies*, 2021; the sheets'
  maj7 and min9 piano chords): the pack uses the device's warm grand (Full Grands' Warm Grand Rev), the ensemble strings for the
  chords and the GM string section as a lead line, and a warm pad.

## Sounds

New sources in `data/kits.json`, all from soundfonts already on the device, found with
`tools/soundfont.py presets` and rendered there (`render`, peak over 2 s, 2026-10-12):

| Machine | Source | Soundfont, bank:program | Render (chord E3 G3 B3 D4 @90 / one note @80) |
|---|---|---|---|
| chords, lead | Rhodes · Suitcase | jRhodes4.sf3 0:0 | chord 0.18; E4 0.09, E5 0.09 |
| chords | Wurlitzer | DX7 Wurlitzer.sf3 0:0 | chord 0.38 (loud: lower the chords' VOL) |
| chords | Grand · Warm | Full Grands.sf3 0:58 (Warm Grand Rev) | chord 0.26 |
| chords | Pad · Warm | FluidR3Mono_GM 0:89 | chord 0.18 after a 0.5 s swell |
| chords | Pad · Vocal | SFZ Synths/Vocal Padds.sf3 0:0 | chord 0.12; low chords 0.08 |
| lead | Strings | FluidR3Mono_GM 0:48 | E4 0.05, E5 0.05 (quiet: raise the lead's VOL) |

Also looked at and not used: Full Grands' Space Grand and Piano Vib Pad, FM Piano, Slow
Heavens (0.10, slower than Vocal Padds), Dirty Sub, Funky Guitars (one-shot riffs, not
playable tones).
