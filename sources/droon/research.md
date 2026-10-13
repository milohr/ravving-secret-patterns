# Droon pack: research notes (2026-10-12)

"Droon" is a pack after **Sonder**, the R&B trio of Brent Faiyaz (vocals) and the producers
Dpat and Atu, for `sources/droon`. Their progressions and tempos are the
reference; every line, riff and rhythm in the pack is original.

## The records

- ***Into*** (EP, 27 January 2017), seven tracks, about 25 minutes: Feel, Lovely, Sirens,
  Too Fast, Baldwin Park, Searchin', Care
  ([Album of the Year](https://www.albumoftheyear.org/album/70743-sonder-into.php);
  [Hypebeast](https://hypebeast.com/2017/2/sonder-into-ep-release-354)). Then the single
  *What You Heard* (2018).
- **How it was made**, from the band's track-by-track
  ([The Line of Best Fit](https://www.thelineofbestfit.com/features/track-by-track/sonder-into)):
  Sirens kept "minimal so that his songwriting could really be processed", its second half
  harder; Lovely went through "over 5 different versions"; Baldwin Park is built round sampled
  background vocals from an unfinished session, kept bare; Los Hendrix played most of the
  instruments on Too Fast's outro; Care "came out of nowhere".
- **The sound** in reviews: "spotless guitars and ghostly backing vocals" that change inside
  the songs (Too Fast, Feel); claps, snaps and choirs, a 90s R&B sweetness; "introspection,
  melancholy and smoothness", "a subtle darkness" in the backing tracks; cinematic, layered
  and warm, "a masterclass in restraint"
  ([highclouds](https://highclouds.org/rb-trio-sonder-release-their-90s-and-groovy-debut-ep-into/);
  [Okayplayer](https://www.okayplayer.com/sonder-brings-soulful-sultry-rb-with-new-into-ep/427549);
  [Free Press Houston](https://freepresshouston.com/sonder-drops-sultry-debut/);
  [Hypebeast](https://hypebeast.com/2017/2/sonder-into-ep-release-354)).
  No source describes the drums or the reverb; "spacious, moody, reverbed" is the brief's and
  the reviews' mood, written as sparse patterns and the template's ECHO.

## Keys and tempos

Two automatic analyses: SongBPM (songbpm.com, Spotify's analysis, with its "beats per bar")
and AcousticBrainz (acousticbrainz.org, by MusicBrainz recording id). I could not listen to
the recordings.

| Song | SongBPM | AcousticBrainz | Reading |
|---|---|---|---|
| Too Fast | 99, E minor, 3 beats a bar | 75.0, E minor (chords key), G major (key) | **74–75 in E minor**: 99 × 3/4 = 74, the triplet reading of the same pulse |
| Care | 127, A#/Bb minor, 3 a bar | 114.6, A# minor | **Bb minor**; the tempo is uncertain (half of 127 ≈ 64, half of 114.6 ≈ 57; a slow pulse with a triplet subdivision either way) |
| Feel | 132, F# minor | 132.1, E major | half time, 66 |
| Lovely | 144, G#/Ab minor, 3 a bar | 143.5 | half time, 72 |
| Sirens | 82, G#/Ab minor | 163.9 | 82 |
| Searchin' | 104, A#/Bb minor | 104.0, A# minor | 104 (or 52 felt in half time) |
| Baldwin Park | 125, F minor, 3 a bar | 125.0, F minor | half time, 62.5 |
| What You Heard | 137 | — | (A minor on the sheet) |

Every Into song is in a minor key; the felt tempos run 62–82. **The pack: Natural Minor, E
minor (Too Fast's key), 74 BPM (Too Fast's tempo, the middle of the EP's half-time pulses),
SWING 58 on the 16ths.** A second template, **Droon · Care**, is in Bb minor (Care's and
Searchin's key) at 64 with SWING 62 on the eighths: SongBPM's three-beat reading of Care,
Too Fast, Lovely and Baldwin Park points at a triplet subdivision, which swung eighths
approximate on the 16-step grid.

## Chord sheets and tabs (ug-chords.py)

- **Too Fast** (UG 2155579, 14 votes, E minor): refrain Em D Em | Bm Em D Bm, ending Em C
  (i VII i | v i VII v, … i VI); verse Em D Am Em G Bm (i VII iv i III v); intro
  Am Em C F#m Em Bm Em (iv i VI ii i v i: the F#m is the Dorian ii, chromatic in natural minor);
  the interlude Em C Am C G Am G Em, then Am Em Gm A C G (chromatic).
- **Care** (UG tab 5376447, half a step down, Bb minor): the verse lick is Bb minor pentatonic
  with hammer-ons, a trill, slides and vibrato on the 3rd and 4th strings; the chorus guitar
  arpeggiates three shapes, Em-shape (iv add9 with the hammered 2nd), F#m-shape (v) and
  Bm7/F#-shape (i7), in Bb minor iv – v – i7, broken in a 3-3-2 rhythm.
- **What You Heard** (UG 5197296): Fmaj7 Cmaj7 Fmaj7 Cmaj7 | Dm E7 (in A minor: VImaj7 IIImaj7
  | iv V7), later D#m7 A#m7 Bmaj7 Ddim (a step up).
- No sheets on Ultimate Guitar for Feel, Lovely, Sirens, Searchin', Baldwin Park, One Way or
  I Wanna See You Dance: those songs gave their keys and tempos only.

On E minor's degrees, the pack uses Too Fast's refrain, intro and interlude, Care's chorus
(iv add9 – v – i7) and What You Heard's VImaj7 – IIImaj7 – iv – V7.

## Sounds

All from `data/kits.json`; the R&B pack added Rhodes · Suitcase (jRhodes4), Grand · Warm
(Full Grands' Warm Grand Rev) and Pad · Vocal (Vocal Padds, for the "ghostly backing
vocals"), rendered on milo (`sources/rnb/research.md`). Guitars: Guitar · Chorus (the
Stratocaster font's chorus preset) and Guitar · Clean for Into's clean, chorused guitars.
Bass: 808 · Monosynth (it glides), Finger bass, Fretless, Synth bass, Sine sub. Drums: TR808
with its LENGTH up, SP1200, the Black Pearl and Red Zeppelin acoustic kits and the GM room
kit, each darkened with the kit's TONE.
