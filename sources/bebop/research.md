# Bebop pack (the first Solos pack): research notes (2026-10-11)

> The research behind the **Bebop** pack (sources/bebop): the first Solos pack, renamed when Solos became ballads on 2026-10-12.

Six original horn solos for the LEAD machine, in the styles of Charlie Parker (alto), John
Coltrane (tenor, soprano) and Chet Baker (trumpet: the brief took Baker's phrasing for the
lines; the user then asked for his own instrument). Nothing is quoted: their compositions and
recorded solos are copyrighted, so the vocabulary below was studied and the lines, the chord
progressions (plain ii–V–I, rhythm-changes-type and blues-type schemes, a modal vamp) and the
rhythms are written fresh. The pack is `sources/solos`.

## Parker (bebop alto)

- Lines in running eighths that outline the chord tones, with chromatic approach tones (a
  non-diatonic note a half step from a chord tone, resolving into it) and enclosures (the
  target surrounded first from above and below, a whole or half step away):
  [Use bebop scales like a pro (Learn Jazz Standards)](https://www.learnjazzstandards.com/blog/learning-jazz/jazz-theory/use-bebop-scales-like-pro/),
  [Billie's Bounce lesson (jazzguitar.be)](https://www.jazzguitar.be/blog/billies-bounce) (the
  major blues scale, chromatic approach notes and enclosures).
- The "bebop scale" (a chromatic passing tone added to the dominant or major scale so the
  chord tones fall on the beats) was formalised after Parker by David Baker and Barry Harris;
  Parker himself added the passing tones where the line needed them, thinking from the chord
  tones: [The truth about bebop scales (keyboardimprov)](https://keyboardimprov.com/the-truth-about-bebop-scales/).
- Rhythm: the upbeat tied into the next downbeat, the lines leaning on the off-beats; a
  triplet dropped on beat two of an otherwise even eighth-note line; phrases that start and
  stop off the bar line (rhythmic displacement), with breaths between them:
  [Charlie Parker for guitar (Premier Guitar)](https://www.premierguitar.com/lessons/jazz/charlie-parker-for-guitar).
  Thomas Owens's *Bebop: The Music and Its Players* is the systematic study (not consulted).
- Harmony played over: rhythm changes (the I–VI7–ii–V turnaround family, the I7–IV–♯iv°
  bar) and the bop blues with its ii–V turnaround.

In the pack: **Bird Changes** (an 8-bar rhythm-changes A section at 200) and **Bird Blues**
(an 8-bar bop blues at 160), the alto in its middle register, the off-beat eighths a touch
louder (@ +8), chromatic approach notes snapped in a hair early (<8), the blue ♭3 scooped
into the 3 (~).

## Coltrane (tenor and soprano)

- Coltrane changes: the chromatic third-related substitutions he put over common progressions
  (first on *Bags & Trane* and *Cannonball Adderley Quintet in Chicago*, then *Giant Steps*):
  a ii–V–I becomes ii7 ♭III7 | ♭VImaj7 VII7 | IIImaj7 V7 | Imaj7, the "Countdown" reharm:
  [Coltrane changes (Wikipedia)](https://en.wikipedia.org/wiki/Coltrane_changes).
- "Sheets of sound" (Ira Gitler's phrase for the late-50s tenor): rapid passages outlining the
  chords, with harmonic superimpositions; later the modal period:
  [Rutgers Journal of Jazz Studies](https://jjs.libraries.rutgers.edu/index.php/jjs/article/download/317/310/2430).
- The practice patterns over the cycle: the 1-2-3-5 cell on every chord, key centres grouped
  (a user-uploaded study guide, [Scribd](https://www.scribd.com/document/898140091/Understanding-Coltrane-Changes-and-Patterns);
  secondary). The modal vocabulary: minor pentatonics, stacked fourths, a cell repeated and
  transposed, a high note cried over and over.

In the pack: **Trane Countdown** (4 bars at 140, sixteenth-note 1-2-3-5 runs through the
Countdown reharm of a ii–V–I, the tenor swelling to each chord's top) and **Trane Fourths**
(8 bars at 160, a modal vamp on the ii7 with two bars of V7sus, the soprano in pentatonic
cells, fourths and repeated cries over quartal "So What"-type voicings).

## Baker (cool trumpet, as a phrasing reference)

- A sparse, lyrical, "plaintive" style with no interest in playing fast; counterpoint rather
  than doubled lines: [Chet Baker's long goodbye (Hackworth, Substack)](https://martinhackworth.substack.com/p/chet-bakers-long-goodbye).
- Simple melodic phrases built from small stepwise motion around the chord tensions
  (a thesis on his *But Not for Me* solo, [USFQ](https://repositorio.usfq.edu.ec/bitstream/23000/10918/1/128103.pdf));
  passing notes that "beautify" the lines (a thesis on his *Autumn Leaves* solo,
  [USFQ](https://repositorio.usfq.edu.ec/bitstream/23000/10465/1/129947.pdf)).
- The behind-the-beat placement, the near-absence of vibrato and the middle register are
  from listening; the sources above do not discuss them.

In the pack: **Baker Ballad** (8 bars at 64 over I vi ii V iii VI ii V: long tones at @62–80,
every note >10–14 late, a scoop into the fifth, half a bar of air at the end) and **Baker
Cool** (8 bars at 120, a medium swing over a I ii–V iii–vi ii–V IV iv–♭VII iii–VI ii–V, a
narrow sung line in the G3–G5 register, every phrase >8 behind the beat).

## Sounds

Found with `tools/soundfont.py presets` on milo. The General MIDI fonts there hold every sax:
FluidR3Mono_GM 0:64 Soprano, 0:65 Alto (in kits.json), 0:66 Tenor (in kits.json), 0:67
Baritone; Roland SC-88 0:64–67 the same four, and 0:56 Trumpet, 0:59 Mute Trumpt. Rendered on
the device (`render --notes 60 --velocity 90`, peak over 2 s): FluidR3 soprano 0.04, alto
0.07, tenor 0.07, baritone 0.05; SC-88 soprano 0.09, alto 0.07, tenor 0.10, baritone 0.08.
Added: **Soprano sax** (FluidR3 0:64), **Tenor sax · Bright** (SC-88 0:66) and **Trumpet ·
Cool** (SC-88 0:56) to the lead's sources.
