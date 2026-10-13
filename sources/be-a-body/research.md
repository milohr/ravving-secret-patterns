# Body pack: research notes (2026-10-12)

The pack is `sources/be-a-body`: Grimes' **Be a Body (侘寂)**, track 8 of *Visions*
(4AD / Arbutus, 2012, 4:20), with its intro as the heart of the pack. The song is copyrighted:
its key, tempo, progression, arrangement shape and sound were studied; every line, melody and
rhythm in the pack is new.

## Key and tempo

| Source | Tempo | Key |
|---|---|---|
| [SongBPM](https://songbpm.com/@grimes/be-a-body) | 140 | (blank) |
| AcousticBrainz, recording `6b0ef67d-361f-4751-b900-d3ed492bbdba`, 99 submissions (read 11: n = 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 80) | 139.8–140.9 in every one | F minor (n 0–1), F major (the other nine); key strength 0.69–0.73; chords key F major |
| [Hooktheory TheoryTab](https://www.hooktheory.com/theorytab/view/grimes/be-a-body) (chorus) | 140, 4/4 | Eb major, chorus `ii7 V7 vi7 ii7 V7 vi7`, melody range G4–Eb5 |
| Chordu, album audio ([Q713eHNFvuU](https://chordu.com/chords-tabs-grimes-be-a-body-%E4%BE%98%E5%AF%82-video--id_Q713eHNFvuU)) | 139 | Cm (its guess; the chords say F) |
| Chordu, official instrumental ([P7GvNMYC1o4](https://chordu.com/chords-tabs-grimes-be-a-body-%E4%BE%98%E5%AF%82-official-instrumental--id_P7GvNMYC1o4)) | 140 | Fm |
| Tunebat | refused the request (403) | |
| The store previews (iTunes and Deezer, 30 s each), `style.py` + a phase/tempo fit of the Basic Pitch onsets | 140 (the fit's error has a sharp minimum at 140.0 between 138 and 142; librosa alone said 92.3, a 2/3 reading caused by the dotted-8th delay) | music21: F minor 0.67–0.69; Chordino: Fm6 Bb7 Cm7, Fm Bb C Gm Cm |

No double/half-time doubt: every source agrees on 140, quarter-note pulse, 4/4.

**The key is F Dorian.** Hooktheory's Eb major with ii7 as the most used chord is the same
seven notes centred on F: Fm7 Bb7 Cm7 = i7 IV7 v7, the Bb7's D natural (and Chordino's Fm6)
the Dorian 6th. AcousticBrainz flips between F minor and F major because the tunes avoid the
3rd: the previews' Basic Pitch notes use C 38–41 %, Bb 22–23 %, F 12–16 %, Eb 9–10 %, G 3–9 %,
D 3–6 %, and **no Ab at all**. The outro does go to F major (Chordu reads F Bb C from about
2:00 to the end).

## The chords

Ultimate Guitar has no sheet for the song (`ug-chords.py` found none, nor does its Grimes
search list one), and no other chord site turned one up (e-chords, Songsterr, web searches). The harmony comes from Chordu's beat-by-beat chord
timelines (beats at 140) and Hooktheory's chorus, cross-checked with Chordino on the previews.

Album audio (Chordu, beat numbers):

| Beats | Chords | Degrees in F Dorian | Section |
|---|---|---|---|
| 1–16 | Fm, Bb, Eb (two bars) | i IV VII VII | the intro's opening (the instrumental reads no chord here: the motif alone) |
| 17–64 | Fm Bb C C, three times | i IV v v (Chordu's C is the Cm7 of Hooktheory) | the intro's loop |
| 65–80 | Ab Bb, Fm Bb | III IV, i IV | the turnaround, then a break (no chord, beats 68–79 on the instrumental) |
| 81–144 | Fm Bb C, Gm Bb Cm, Fm Bb Cm, Gm Bb Cm | i IV v v, ii IV v v | the verse |
| 145–240 | Fm Bb Cm, then Bb Cm two bars each, Ab Bb C | i IV v; IV v IV v…; III IV V | the middle, lifting on the C major |
| 241–280 | Fm Bb Cm | i IV v | the chorus (Hooktheory: ii7 V7 vi7 in Eb) |
| 281–593 | F Bb C | I IV V | the outro, in F major |

## What the intro is made of

- **An opening synth motif** "that could hail from a mainstream radio rocker, perhaps by Van
  Halen in the Eighties" ([The Arts Desk](https://theartsdesk.com/new-music/cd-grimes-visions)),
  over Fm Bb Eb; "kicking off like a '90s suburban rave anthem"
  ([The Line of Best Fit](https://www.thelineofbestfit.com/reviews/albums/grimes-visions-85691)).
- **The Juno-G presets** on this song, from Reverb Machine's author (a reader comment under
  [Grimes Synth Sounds](https://reverbmachine.com/blog/grimes-synth-sounds/)): guitar "Wet
  Nylon", bass "Big Mini", lead "SH101 Bs1". The same article on the album: the Juno-G's
  "X-Cultural" harp across *Visions*, a "Theramax" saw lead with delayed vibrato (Genesis), a
  synced 1/8 delay at 30 % with feedback "that defines the Visions sound", piano with a 1/4
  delay at 40 %, drums from Vengeance packs or the Juno-G's rhythm kits.
- **The voice:** multitracked, high, "honey-sweet vocal tics and melodic effects" (The Arts
  Desk); "the half-understandable chorus" in "broken English" (RA,
  [Visions review](https://ra.co/reviews/10473)), "a hissing cloud of voices".
- **The beat** turns "inside out as it progresses, developing a driving and very modern
  nightclub pulse" (The Arts Desk); "the clubbiest track on the album … owes a bit to early
  Madonna" ([Cool Dad Music](https://www.cooldadmusic.com/2012/04/sunday-run-album-review_29.html)).
- **The album:** made in GarageBand in about three weeks, on a Roland Juno-G, vocal pedals and
  a sampler ([Wikipedia](https://en.wikipedia.org/wiki/Visions_(Grimes_album))).

From the previews' note and onset analysis (study only, nothing transcribed into the pack):

- The bass sits in F1–C2 and leaps the octave (F1/F2, Bb1/Bb2), in syncopated sixteenths
  close to 3-3-2 (hits on steps 0, 3, 6, 8, 11).
- The high line sits around Bb4–Eb5 (Hooktheory's G4–Eb5), on the 5th, 7th and 6th.
- The chords change a bar each at 140 (1.71 s), the v held two bars.
- The drum onsets were too mixed with the bass and the delay echoes to read a pattern; the
  low band hit on two and the "and"s of two and three, the bright band on two and four.

## MIDI

No MIDI transcription of the song was found: BitMidi, MuseScore (behind a challenge page),
Online Sequencer (behind a challenge page), Hooktheory (its MIDI export needs an account) and
web searches turned up nothing. Instead, the two 30-second store previews (the public iTunes
and Deezer preview URLs) were read with `~/.local/share/music-analysis-venv/style.py` and
Basic Pitch, and the notes printed on a 140-BPM sixteenth grid, to study register, rhythm
density and the missing 3rd. No full recording was used (a YouTube download failed with 403). The previews and
their MIDI stayed in the session's scratch folder.

## How the pack uses it

- The scale is Dorian; the template F Dorian at 140, straight.
- The intro presets follow the intro's harmony: i IV VII VII (Intro Stabs, Intro Sub, Intro
  Harp, Intro Chops, Intro Haze's first half), the loop i IV v v (Intro Haze's second half),
  the III IV turnaround (Intro Bells).
- The lines leave the 3rd out, as the song's do: the 5th, 7th, 6th, 9th and 4th.
- The 1/8 delay is the templates' ECHO, and written into Intro Harp and Verse Bounce (the
  note again two steps later at about 55 % velocity).
- Sounds after the Juno-G: the Roland SC-88's synth brass, polysynth, choir pad, square lead
  and synth voice; FluidR3's Synth Bass 2 for the "Big Mini"; the concert harp for the
  album's harp; Calf Monosynth for the "Theramax".
