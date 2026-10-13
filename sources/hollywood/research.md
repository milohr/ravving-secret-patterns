# Hollywood pack: research notes (2026-10-12)

The pack is `sources/hollywood`: Lana Del Rey's beats and riffs with an
old-Hollywood orchestral sound (violins, cellos, string sections, harp arpeggios, celesta), a
vintage, cinematic, melancholic vibe. Nothing is quoted: her songs are copyrighted. The chord
progressions and tempos below are reference material; every line, melody and rhythm in the pack
is new.

## The songs

The chord sheets were fetched with `sources/research/ug-chords.py` (the most voted sheet of
each song on Ultimate Guitar; a capo is applied below to give the sounding chords). The tempos
and keys come from Wikipedia where it gives them (from the published sheet music), else from
SongBPM's audio analysis, which often doubles or halves a slow tempo: both readings are given.
A chord's degree is in the song's own minor key (her songs are nearly all minor, or major songs
that lean on the relative minor).

| Album | Song | Tempo | Key | Progression (sounding) | Degrees |
|---|---|---|---|---|---|
| *Born to Die* (2012) | Video Games | 123, felt as 61 half-time (Wikipedia) | F# minor (Wikipedia) | F#m A F#m A C#m D (capo 2 on Em G Bm C); bridge C#m D E Esus4 | i III i III v VI; v VI VII |
| | Born to Die | about 86 (Chordu's reading of the official audio; SongBPM says 75) | E minor on the sheet (SongBPM: E minor) | chorus C Em D C; verse G D C Em | VI i VII VI; III VII VI i |
| | Blue Jeans | about 86 (Musiciwant; SongBPM 118 / 59) | F minor (fan wiki; the sheet's standard tuning) | Fm Eb Bb (Wikipedia: "a basic chord progression of Fm–E♭–B♭") | i VII IV (the Dorian major IV) |
| | Summertime Sadness | 112, half-time 56 (SongBPM); Wikipedia 125 | C# minor (Wikipedia) | A C#m B F#m (capo 4 on F Am G Dm) | VI i VII iv |
| | Dark Paradise | 120 / 60 (SongBPM) | C# minor | A C#m, then B F#m (capo 4 on F Am G Dm) | VI i VII iv |
| *Ultraviolence* (2014) | Ultraviolence | 79 in 3/4 (SongBPM) | D minor | Dm F Am/C G; Dm Bb G; Bb Dm C G | i III v IV; i VI IV; VI i VII IV |
| | Shades of Cool | 138 / 69 in 3/4 (SongBPM) | D minor | Dm Bb Bm Bb Dm; G Gm Dm; Bb C F Cm | i VI ♯vi VI i; IV iv i; VI VII III vii |
| | West Coast | 123 / 62 (SongBPM) | F# minor | F#m E D Bm (capo 2 on Em D C Am) | i VII VI iv |
| *Honeymoon* (2015) | Honeymoon | 75 in 3/4, double 150 (SongBPM) | F minor (SongBPM; the sheet capo 1) | Fm Db Fm Cm Abmaj7 C5; Bbm6 C7 Fm (capo 1 on Em C Em Bm Gmaj7 B5, Am6 B7 Em) | i VI i v IIImaj7 V; iv6 V7 i (the harmonic V7) |
| | Terrence Loves You | 102, half 51 (SongBPM) | G major listed; the sheet vamps on D | D C D, C Bm, D Am7 | I ♭VII I, ♭VII vi, I v7 (Mixolydian) |
| *Lust for Life* (2017) | Lust for Life | not found | C minor (capo 3 on Am) | Cm Bb Ab Bb; Eb Gm Cm Bb (capo 3 on Am G F G; C Em Am G) | i VII VI VII; III v i VII |
| | Young and Beautiful (*The Great Gatsby*, 2013) | 115 / 58 (SongBPM) | B minor | G A Bm D | VI VII i III |
| *Norman Fucking Rockwell!* (2019) | Mariners Apartment Complex | 76 (SongBPM) | B minor (capo 2 on Am) | Bm A E (capo 2 on Am G D) | i VII IV (the Dorian major IV) |
| | Venice Bitch | 79 (SongBPM) | F major (the sheet) | Fsus2 G; Em F Am G; C C7 F Fm6 | I II; vii I iii II; V V7 I i6 (the minor plagal: IV iv6 in C) |
| | The Greatest | 78 (SongBPM) | F major (the sheet) | Bb F C; Dm/A Gm; F C C#dim Dm | IV I V; vi ii; I V ♯V° vi (a chromatic passing diminished) |
| *Chemtrails over the Country Club* (2021) | Chemtrails over the Country Club | not found | E minor | C D Em Em7/D | VI VII i i7/♭7 |

What the progressions share:

- **Minor keys, looped four-chord progressions**, one chord a bar or two, almost never a
  dominant cadence: **VI–i–VII–iv** (Summertime Sadness, Dark Paradise), **i–VII–VI–iv**
  (West Coast), **VI–VII–i–III** (Young and Beautiful), **VI–i–VII–VI** (Born to Die),
  **i–III–v–VI** (Video Games).
- **The Dorian major IV in a minor key:** Blue Jeans' Fm Eb Bb, Mariners' Am G D,
  Ultraviolence's G under Dm. In a Natural Minor pack it is a chromatic chord (the raised 6th).
- **The minor iv and the major–minor IV swap**, the old Hollywood move: Shades of Cool's G Gm,
  Venice Bitch's F Fm6, Honeymoon's iv6.
- **The harmonic-minor V7** for a cadence when one comes (Honeymoon's B7 → Em).
- **Chromatic passing chords:** The Greatest's C#dim, Shades of Cool's Bm between two Bbs.
- **Tempo:** slow. Most of the songs sit at 60–90 felt in quarter notes; the 110–125 readings
  are the half-time hip-hop beats counted double (Video Games, Summertime Sadness, West Coast,
  Dark Paradise). Honeymoon, Shades of Cool and Ultraviolence sway in three.

## Her drums

- ***Born to Die*:** trip-hop and hip-hop beats under the strings; the album is "predominantly
  baroque pop and trip hop", "pop ballads with hip-hop beats" (Pitchfork, via Wikipedia), a
  "lush-strings-meet-hard-beats" sound; Emile Haynie produced and played the drums on most of
  it. The title track has "hip hop-influenced beats and string arrangements", its "whipping
  strings" compared to John Barry. Blue Jeans' beat is "minimalist" and "hip-hop influenced".
  Summertime Sadness and Dark Paradise run a half-time beat at about 56–60 under a 112–120
  pulse.
- ***Ultraviolence*:** a live seven-piece band with Dan Auerbach, "more guitar-based", desert
  rock and slowcore, "the whole album proceeds at the same, somnambulant pace" (The Guardian):
  slow live drums in a reverberant room.
- ***Honeymoon*:** "sweeping strings and stuttering snares" (The Verge on the title track),
  noir, "a sound close to the golden age of jazz" (Del Rey): brushes, sparse, slow, often in 3.
- ***Norman Fucking Rockwell!*:** Jack Antonoff on the drums, soft rock, "Laurel Canyon '70s
  soft-rock fantasies" (Rolling Stone): soft live kit, brushes and sparse fills.

## Her bass

Sustained and simple: the root held through each chord, often doubled an octave up by the cellos
or the low strings; a sub-bass under the hip-hop beats of *Born to Die* (long roots, a slide into
the change); a slow-burn bass line on *Ultraviolence* (Shades of Cool, "a chiming guitar,
slow-burn bass line, and swelling orchestra"). In the orchestral arrangements the bass line is
the contrabass and cello section, bowed, and in the old-Hollywood way it walks chromatically
down under a held minor chord (the lament bass, the line cliché).

## Her orchestration

- **String pads:** "dramatic strings" on Video Games and Born to Die (Wikipedia, *Born to Die*);
  "swirls of cinematic strings" on *Honeymoon*; "swooning strings and swirling synths" on
  *Norman Fucking Rockwell!* (Entertainment Weekly). Larry Gold arranged and conducted the
  strings on Born to Die and Summertime Sadness; Dan Heath arranged Blue Jeans and, by his
  agency's account, most of the album.
- **Pizzicato:** Alexis Petridis on Video Games' "ballooning orchestration and pizzicato
  strings".
- **Harp:** Video Games' producer added "strings, harps and synth arpeggios" to the piano demo
  (Wikipedia); "flourishes of harp and overly romantic swoops of violin" (The Singles Jukebox).
- **Cello lines:** Phillip Peterson plays cello (and flugelhorn) on *Norman Fucking Rockwell!*.
- **Tremolo violins and swells:** the "swooping" violins, the string swells rising over Blue
  Jeans' refrain ("low fidelity string instruments").
- **Glockenspiel and celesta colour:** the "synth arpeggios" and the music-box shimmer of the
  *Born to Die* singles; in Hollywood scoring, Herrmann's "solo colours such as celesta, chimes,
  and double harps".
- **The 1950s/60s film-score sound:** "a cinematic sound reminiscent of the 1950s", compared to
  James Bond soundtracks; Del Rey's own "Hollywood sadcore"; "those first string sweeps are
  straight out of *Imitation of Life*" (Douglas Sirk, 1959); the closing Nina Simone cover read as
  "classical '60s Hollywood melodrama". Everything drenched in reverb.

## The old-Hollywood scoring vocabulary

- **Lush string voicings:** added 9ths and major 7ths, spread wide (cellos on the root, violas
  and violins on the 3rd, 7th and 9th), long bows, slow attacks, swells.
- **The minor line cliché:** a minor chord held while one voice falls chromatically, i –
  i(maj7) – i7 – i6, the "suspense motif" of the Bond theme (Monty Norman's theme in John
  Barry's arrangement: "a line cliché of four smooth E minor chords", and its final Em(maj9),
  the "James Bond chord"). Under it, the lament bass walking down to the dominant.
- **Chromatic cello lines** and the half-step sigh (Herrmann's descending semitones in the low
  strings).
- **Tremolo strings** for suspense, swelling and fading; **ostinatos and swirling harp and
  string arpeggios** (Vertigo: "swirling harps and strings", "circular ostinatos", "a
  simultaneous ascending and descending arpeggiated chord").
- **The minor iv in a major key, the major IV in a minor one** (above).
- **Timpani** on the tonic and the dominant, a roll into the downbeat, the cymbal crash.

## The device's sounds

`tools/soundfont.py presets` over every `SF2 Instruments` font on milo, then `render` (2026-10-12,
offline, `--seconds 3 --velocity 90`, peak level):

| Instrument | Candidates (font bank:program) | Peak | Pick |
|---|---|---|---|
| String section | FluidR3 Strings 0:48 (0.10), Slow Strings 0:49 (0.14), Dry Strings 1:48; SC-88 Strings 1 0:48 (0.20), Strings 2 0:49; Hip Hop Combo Mood Strings 0:54 (0.17); SFZ Synths Ensemble Strings, BowString | | **Strings** (FluidR3 0:48, already in kits.json) with a slow ATTACK for the pads; new **Strings · Mood** (Hip Hop Combo 0:54) for *Born to Die*'s sampled-strings stabs |
| Tremolo strings | FluidR3 Tremolo 0:44 (0.11); SC-88 Tremolo Strings 0:44 (0.18) | 0.18 | new **Strings · Tremolo** (SC-88 0:44) |
| Piano with strings | SC-88 Piano+Strings 0:2 (0.24, the piano decaying, the strings under it) | 0.24 | new **Piano + strings**; the **Grand piano** (Fazioli) for the plain piano |
| Violin | FluidR3 Violin 0:40 (0.05), Slow Violin 8:40 (0.06); SC-88 Violin 0:40 (0.15) | 0.15 | new lead **Violin · Warm** (SC-88); the existing **Violin** (FluidR3) for the tremolo |
| Cello | FluidR3 Cello 0:42 (0.06 at F2, 0.07 at F3); SC-88 Cello 0:42 (0.10 at F2 and C4) | 0.10 | bass: the existing **Cello** (FluidR3); new lead **Cello** (SC-88) for the cello lines |
| Contrabass | FluidR3 0:43 (0.07 at F2); SC-88 0:43 (0.11) | 0.07 | the existing **Contrabass**; **Upright** (ACBass) for the pizzicato bass |
| Harp | FluidR3 Harp 0:46 (0.05, gone in 0.75 s); SC-88 Harp 0:46 (0.11 at F4 and C5) | 0.11 | new lead **Harp · Concert** (SC-88) |
| Celesta | FluidR3 0:8 (0.05, gone in 0.5 s); SC-88 0:8 (0.11, rings 2 s) | 0.11 | new lead **Celesta** (SC-88) |
| Glockenspiel | FluidR3 0:9 (0.03); SC-88 0:9 (0.05, 0.25 s) | 0.05 | not added: too short and quiet on both; the celesta covers the colour |
| Pizzicato | FluidR3 Pizzicato Section 0:45 (already chords **Pizzicato strings**) | | existing |
| Timpani | FluidR3's Orchestra kit (128:48): timpani on keys 41–53, F2 0.12, C3 0.10, F3 0.09 | | new presetKit **Orchestra · F**: TOM the F (key 53), HAT the C below (key 48) |
| Sub | the existing **808 · Monosynth** (it glides), **Sine sub** | | 808 · Monosynth |

Drums: SP1200 and TR808 from the kit folder for the *Born to Die* beats; **Brush · ride** for
the brushes; **Black Pearl 5** (the AVL acoustic kit) for the *Ultraviolence* room; the new
**Orchestra · F** for the timpani.

## Into the pack

- **One scale: Natural Minor, made for F minor.** It is the key of Blue Jeans and Honeymoon
  (and a semitone from Born to Die's E minor and Video Games' F# minor), it puts the contrabass's
  and the cello's low F and C (tonic and dominant) under the strings, and FluidR3's timpani reach
  F. Every song above moves onto its degrees; the Dorian major IV (Bb major's D natural), the
  harmonic V7 (C7's E natural) and the line cliché's E and D take ALTER or chromatic voicings.
- **Tempo:** the presets sit at 56–88, the half-time beats written at their felt tempo. The
  template is **72** (the middle), **SWING 52** (a hair of lazy hip-hop swing under straight
  strings), ECHO 0.4 (the reverb-drenched room; the strings' RELEASE MODS add the tail),
  HEAVY 0.15 (to glue the beats), no PHASER. A second template, **Hollywood · Video Games**, is
  62 in F# minor, the half-time ballad with ECHO 0.45.
- **The playing:** velocity swells across each bowed phrase, long holds, the strings and cellos
  a little behind the beat (>6–10), a written tremolo (sixteenths swelling @40 → @104 and back),
  harp sweeps rising in velocity to a held top note, the celesta's grace notes snapped in early.
  MODS: slow attacks on the strings (ATTACK 2400–4800 timecents), long releases (2400–4000),
  the filter down (CUTOFF −1200 to −1800 cents) for the vintage tone, a little vibrato on the
  solo strings; the drum kits darkened (TONE) and the SP1200 tuned down two semitones.

## Sources

- The chord sheets on [Ultimate Guitar](https://www.ultimate-guitar.com): Video Games 1083902,
  Born to Die 1117902, Blue Jeans 1095078, Summertime Sadness 1129189, Dark Paradise 1128935,
  Ultraviolence 1490387, Shades of Cool 1487802, West Coast 1476802, Honeymoon 1769581,
  Terrence Loves You 1761280, Lust for Life 1983685, Young and Beautiful 1244052, Mariners
  Apartment Complex (capo 2), Venice Bitch 2474754, The Greatest 2801963, Chemtrails over the
  Country Club.
- [Video Games (Wikipedia)](https://en.wikipedia.org/wiki/Video_Games_(Lana_Del_Rey_song)): F♯
  minor, 123 BPM, "strings, harps and synth arpeggios", "pizzicato strings".
- [Summertime Sadness (Wikipedia)](https://en.wikipedia.org/wiki/Summertime_Sadness): C♯ minor,
  125 BPM, Larry Gold's strings.
- [Blue Jeans (Wikipedia)](https://en.wikipedia.org/wiki/Blue_Jeans_(Lana_Del_Rey_song)): Fm–E♭–B♭,
  the hip-hop-influenced beat, Dan Heath's strings;
  [Lana Del Rey Wiki](https://lanadelrey.fandom.com/wiki/Blue_Jeans_(song)) (F minor),
  [Musiciwant](https://www.musiciwant.com/song/blue-jeans-lana-del-rey) (86 BPM).
- [Born to Die (song, Wikipedia)](https://en.wikipedia.org/wiki/Born_to_Die_(Lana_Del_Rey_song)),
  [Born to Die (album, Wikipedia)](https://en.wikipedia.org/wiki/Born_to_Die_(album)),
  [Chordu](https://chordu.com/chords-tabs-lana-del-rey-born-to-die-official-audio--id_eGR1iDuKabU) (85.95 BPM).
- [Ultraviolence (Wikipedia)](https://en.wikipedia.org/wiki/Ultraviolence_(album)),
  [Honeymoon (Wikipedia)](https://en.wikipedia.org/wiki/Honeymoon_(Lana_Del_Rey_album)),
  [Norman Fucking Rockwell! (Wikipedia)](https://en.wikipedia.org/wiki/Norman_Fucking_Rockwell!).
- SongBPM's pages for each song ([songbpm.com/@lana-del-rey](https://songbpm.com/@lana-del-rey)).
- [The Singles Jukebox on Born to Die](https://thesinglesjukebox.com/?p=2305),
  [Daniel Heath (GSA Music)](https://www.gsamusic.com/clients/daniel-heath/).
- The Bond theme's line cliché and chord: [The James Bond chord (Sciencebase)](https://www.sciencebase.com/science-blog/?p=58635),
  [The James Bond Theme (jazzguitar.be)](https://www.jazzguitar.be/blog/james-bond-theme/),
  [quizbowlstats on the Bond theme](https://quizbowlstats.com/buzzpoints/set/2024-chicago-open/tossup/james-bond-theme).
- Herrmann: [The thrilling scores of Bernard Herrmann (Cleveland Orchestra)](https://www.clevelandorchestra.com/posts/the-thrilling-scores-of-bernard-herrmann),
  [Vertigo's return (SFCV)](https://www.sfcv.org/articles/review/symphony-accompanies-vertigos-return-sf),
  [Herrmann's film music (Royal Holloway)](https://www.royalholloway.ac.uk/research-and-education/subjects/music/about-us/teacherhubmusic/bernard-herrmanns-film-music-psycho-and-others).
