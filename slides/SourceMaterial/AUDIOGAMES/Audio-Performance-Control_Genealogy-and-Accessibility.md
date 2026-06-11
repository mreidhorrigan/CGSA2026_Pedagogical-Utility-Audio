# Audio performance control, from the theatre cue to the game engine

### A sourced genealogy of FMOD and Wwise, an evaluation of the "Montreal-theatre → Wwise" hypothesis, and its bearing on accessibility

*Background research for "Minimum viable soundscapes: Appraising the pedagogical utility of audiogames." Sources are catalogued in the Zotero collection **`CLAUDES_NOTES → CLAUDE_AUDIOGAMES`** (41 items across 5 sub-collections) with cross-linked, YAML-headed annotation notes. Machine-generated and unverified — tertiary sources (Wikipedia/Grokipedia) are flagged; verify against primaries before publication.*

---

## 0. Headline finding (the honest answer)

Your hypothesis — **"Wwise developed through the Montreal theatre scene, adapting conventions from playlist-based theatrical sound design"** — is **not supported as a direct, causal/personnel genealogy**, and I'd advise against asserting it in that form. The evidence points to something more defensible and, I think, more interesting for your paper:

> Game-audio middleware (FMOD, Wwise) and theatrical show-control software (QLab, Stage Research SFX, Richmond Sound Design) are **siblings, not parent-and-child**. They converge on the same control vocabulary — discrete, triggerable, parameterised sound *events/cues* sequenced in *lists/playlists* — because they descend from a **shared ancestor (MIDI and MIDI-era sequencing, c. 1983)** and solved the same problem (responsive sound for live/interactive performance) in parallel. The crossover is real, documented, and **bidirectional** — but the dominant documented flow is actually **games → theatre**, the *reverse* of the hypothesis.

Two specifics that decide it:

1. **Audiokinetic's founder came from music, then games — not theatre.** Per a primary biography (zú Montréal), Martin H. Klein was "formally trained in music and law… established himself as a musician and composer, then focused on sound design and music production," worked as "a producer, publisher, arranger, and record label director with… top record labels, film companies and advertising agencies," and **"joined Ubisoft Entertainment in 1997 as Executive Audio Producer and Artistic Director"** before founding Audiokinetic in 2000. The path is **music/recording → games**, with **no theatre** at any point. No pre‑Wwise product, no theatre product, and **no patents** located for Audiokinetic or Firelight. (zú Montréal; `About Audiokinetic`; *The Story of Wwise*.)
2. **FMOD's lineage is the demoscene/tracker scene**, and the other major middleware lineages (Miles, iMUSE, DirectMusic) are **driver-abstraction** and **music-sequencer** lineages. None originate in theatre.

The payoff for your abstract: the **"timeline/linearising" tendency you critique in FMOD/Wwise is inherited**, and we can now say *from where* — from music sequencers and trackers (the "playlist") and from screen/cue automation (the "cue") — which is exactly why these tools default to fixed-media, linear representations rather than explorable spaces. See §7.

---

## 1. The four genealogical threads feeding modern game audio

Modern game-audio middleware is a confluence. Keeping the threads separate is what lets you evaluate the hypothesis cleanly.

| Thread | Core metaphor | Origin | Carried into games by |
|---|---|---|---|
| **A. Theatre / show control** | the **cue** + the **GO** button; cue stack | Richmond Sound Design (1972); MIDI Show Control (1991) | conceptual convergence; FMOD "event ≈ cue" |
| **B. Tracker / demoscene** | the **pattern playlist** ("order list") | Ultimate Soundtracker (1987) | **FMOD** (Brett Paterson, 1995) |
| **C. Music sequencer / adaptive** | **branch/marker** score-following; segments | iMUSE (1991); Blue Ribbon SoundWorks → DirectMusic | iMUSE, Microsoft DirectMusic, Wwise/FMOD music systems |
| **D. Engine / driver abstraction** | unified **API** over sound hardware | Miles AIL (1991) | Miles → FMOD → Wwise as a software *category* |

The crucial observation: **threads B, C, and D are all software/engineering lineages; only A is theatre.** Wwise and FMOD sit at the junction of B/C/D. Theatre (A) **meets** them later, as a peer, not as an ancestor.

### Why "playlist" vs "cue" matters terminologically
Your hypothesis uses the phrase *"playlist-based theatrical sound design."* In fact theatre practice is **cue-list-based** (a *cue stack* advanced by an operator pressing **GO**), while **"playlist"** is native to **music software** — the tracker "order list" that sequences patterns "into complete songs via a playlist editor" (`Ultimate Soundtracker`, 1987), and later iTunes/DJ/broadcast senses. This maps cleanly onto the two middlewares' own vocabularies:

- **"Cue" → theatre/show-control → FMOD "event."** FMOD's own practitioners say it outright: *"An FMOD event is akin to a theatrical sound cue"* (Swift).
- **"Playlist" → tracker/sequencer → Wwise "Music Playlist Container."** Wwise's interactive-music hierarchy is literally built on *Music Playlist Containers* (Sequence/Random Continuous) and *Music Switch Containers*.

So the "playlist" in Wwise descends from **trackers and sequencers**, and the "cue" affinity in FMOD is a **convergence** with theatre — not a borrowing *from* theatre into Wwise.

---

## 2. Sourced timeline of audio performance control

Lineage key: **SC** show-control/theatre · **TR** tracker/demoscene · **MS** music-sequencer/adaptive · **MW** engine/middleware · **STD** standardisation · **AG/ACC** audio games/accessibility.

| Year | Event | Thread | Source |
|---|---|---|---|
| 1972 | Richmond Sound Design founded (Charlie Richmond), Canada — theatre sound + show control | SC | Huntington, *MSC History* |
| 1983 | MIDI 1.0 ratified; instantly adopted by sound industry — the shared ancestor | (root) | Huntington |
| 1987 | **Ultimate Soundtracker** (Karsten Obarski, Amiga): first music tracker; patterns sequenced "via a **playlist editor**" | TR | Wikipedia |
| 1988 | Todor Fay co-founds **Blue Ribbon SoundWorks** (Amiga: Bars&Pipes sequencer, SuperJAM! auto-composition) | MS | Game Developer; ITHistory |
| 1989 | "MIDI Mania" panel, LDI Nashville; Andy Meldrum (Vari\*Lite) proposes a standard SysEx for show control; Dec 1989 Richmond opens MMA "Theatre Messages" working group on USITT Callboard | SC | Huntington |
| 1989–90 | NoiseTracker (1989), **ProTracker** (1990) — tracker culture spreads through the demoscene | TR | Wikipedia |
| 1991 | **MIDI Show Control v1.0** becomes a standard (summer 1991); Richmond Sound Design ships **Stage Manager**, first MSC software | SC/STD | Huntington; MSC (Wikipedia) |
| 1991 | **Miles AIL** (John Miles): first commercial game-audio **middleware** (unified API over DOS sound cards) | MW | RAD Game Tools; Wikipedia |
| 1991 | **iMUSE** debuts in *Monkey Island 2* (SCUMM v5); patent filed 25 Nov 1991 | MS | US 5,315,057; Strank |
| 1994 | iMUSE patent **granted** (US 5,315,057, 24 May 1994) — foundational adaptive-audio IP | MS | US 5,315,057 |
| 1994 | **IASIG** formed within the MIDI Association (games-audio standards body) | STD | IASIG |
| 1994 | Huntington, *Control Systems for Live Entertainment* (1st ed.) — first book on show control | SC | Huntington |
| 1995 | **FMOD** debuts (Brett Paterson, 6 Mar 1995): tracker-module player for DOS/Gravis Ultrasound (.mod/.s3m/.xm/.it) | TR/MW | FMOD (Wikipedia) |
| 1995 | Microsoft acquires Blue Ribbon SoundWorks; RAD acquires Miles Design | MS/MW | Game Developer; RAD |
| late 1990s | Microsoft **DirectMusic / DirectX Audio** (Todor Fay leads IMA then DirectMusic) | MS | Game Developer; Fay |
| **2000** | **Audiokinetic founded in Montreal** by **Martin H. Klein** (music/film/games veterans) | MW | About Audiokinetic |
| 2002 | **Firelight Technologies** incorporated (Melbourne); FMOD becomes commercial middleware | MW | Grokipedia/Wikipedia |
| ~2005–06 | FMOD Ex / **FMOD Designer** (event-based authoring); IASIG releases **iXMF** public-preview draft | MW/STD | FMOD docs; IASIG |
| **2006** | **Wwise released** (Audiokinetic). Same year: **QLab v1.0** (Figure 53, Chris Ashworth) — the theatrical cue standard | MW / SC | Audiokinetic; Figure 53/QLab |
| 2010 | **Papa Sangre** (Somethin' Else): "video game with no video," binaural, bespoke *Papa Engine* (not FMOD/Wwise) | AG/ACC | Papa Sangre (Wikipedia) |
| 2011 | **The Nightjar** (Somethin' Else) | AG/ACC | Papa Sangre (Wikipedia) |
| ~2011–12 | iMUSE patent (filed 1991) reaches end of ~20-yr term — adaptive-audio techniques enter the commons | MS | (analysis; cf. US 5,315,057) |
| 2012 | **FMOD Studio** announced at GDC (DAW-styled successor to Designer); Huntington renames book *Show Networks and Control Systems* | MW/SC | Business Wire; Huntington |
| 2013 | FMOD Studio 1.0; Collins, *Playing with Sound* | MW / scholarship | FMOD; Collins |
| 2019 | **Sony Interactive Entertainment acquires Audiokinetic** — Wwise becomes platform infrastructure | MW | Sony |
| 2020 | **Swift, "FMOD … Adapted for Theater" (USITT)** — documented games → theatre crossover | SC↔MW | Swift |

---

## 3. FMOD: a demoscene/tracker genealogy

FMOD is the clearest case *against* a theatre origin and *for* a music-software one.

- **Person & place:** Brett Paterson, while studying computing at Monash University (Melbourne, B.Comp. 1992–95), wrote FMOD as a personal project. (FMOD/Grokipedia.)
- **Name & function:** FMOD = **"Firelight MODule player."** Its 6 March 1995 debut played **tracker modules** (`.mod`, `.s3m`, `.xm`, `.it`) on DOS via the Gravis Ultrasound — i.e., it was born to play **demoscene music**. (FMOD/Wikipedia.)
- **Company:** Firelight Technologies incorporated Jan 2002 (Melbourne); FMOD became commercial middleware. (Grokipedia.)
- **The timeline turn:** FMOD Designer (event-based, mid-2000s) → **FMOD Studio** (GDC 2012; 1.0 in 2013), explicitly **"designed like a digital audio workstation"** (Pro Tools/Logic). (Business Wire; Swift.)

**Reading for your abstract:** FMOD's "playlist" thinking (the *scatterer* instrument literally has a sample **playlist**) is a **tracker inheritance**, and FMOD Studio's DAW timeline is a **fixed-media inheritance**. The tool is *genetically* a music-playback engine that grew adaptivity, which is precisely why its interface "struggles to represent soundscapes as interactive spaces."

---

## 4. Wwise / Audiokinetic, and the hypothesis tested

### What the evidence says
- **Founding:** Audiokinetic, Montreal, **2000**, by **Martin H. Klein** (President/CEO) and a team of veterans **"from the music, film, and gaming industries."** First office 2003 (Old Port); Quebec digital-industry funding 2003; **Wwise launched 2006**; **Sony acquired Audiokinetic in 2019**. (`About Audiokinetic`; Sony.)
- **Klein's background (now confirmed from a primary source):** "formally trained in music and law," he "established himself as a musician and composer, then focused on sound design and music production," and built a track record "as a producer, publisher, arranger, and record label director with the industry's top record labels, film companies and advertising agencies." He then **"joined Ubisoft Entertainment in 1997 as Executive Audio Producer and Artistic Director,"** and founded Audiokinetic in 2000. So the "major developer" where he saw the games-audio tooling gap was **Ubisoft** (Montréal's flagship game studio) — a *games* role, reached via a *music/recording* career. **No theatre at any stage.** (zú Montréal, "Alliances — with Martin Klein"; *The Story of Wwise*, Audiokinetic.)
- **No pre-Wwise product; no theatre product.** Searches surface no Audiokinetic product before Wwise, and no theatre/show-control product.
- **No patents.** Google Patents searches return **no patents assigned to Audiokinetic or Firelight Technologies** — unlike LucasArts' iMUSE. Wwise/FMOD competed on engineering and ecosystem, not IP. *(Negative finding; phrase as "no patents located," not "none exist.")*

### Where the hypothesis likely came from (and how to salvage it)
The intuition is reasonable because **Wwise's vocabulary really does rhyme with theatre**: containers, states, switches, **playlists**, events. But:

- **Montreal's media-tech scene that fed Audiokinetic is the music/recording and film/VFX/games scene** (think Softimage/Discreet, Ubisoft Montréal, a deep recording-studio culture) — **not** a theatre-sound pipeline.
- The genuinely **Canadian** node in this story is on the **theatre** side and it's in **British Columbia**, not Montreal: **Charlie Richmond / Richmond Sound Design**, who *chaired the MIDI Show Control standardisation* (1989–91). If you want a Canadian through-line, it runs **BC theatre show control (Richmond) ∥ Montréal game audio (Audiokinetic)** as **parallel** Canadian contributions to performance-control software — a cleaner and still-striking claim. (Huntington.)

### Recommended reframing
> *Wwise did not emerge from theatre; it emerged from Montréal's music-production milieu and the existing lineage of game-audio middleware (Miles, iMUSE, DirectMusic). Its convergence with theatrical cue-and-playlist paradigms is evidence of a shared MIDI-era ancestry and of active, **bidirectional** traffic between the game-audio and theatre-sound communities — most visibly games → theatre.*

---

## 5. The keystone: documented convergence (and its direction)

The single best primary source is a **theatre-technology** paper that imports a **game engine** into live theatre — the opposite of the hypothesis, and proof the two worlds share one vocabulary:

**Stephen Swift, "FMOD, an Audio Engine for Video Games, Adapted for Theater"** (USITT Sound Commission). A sound designer uses **FMOD** to run the score/sound for the Rogue Artists Ensemble production *Wood Boy Dog Fish* (composer Adrien Prévost), because the director wanted performance "organic, open to improvisation, and **not … locked to a track**." Swift translates directly between the domains:

- > "An **FMOD event is akin to a theatrical sound cue**; it is the container that holds the audio files and related settings."
- > "A **scatterer instrument is similar to a QLab group cue set to random mode**."
- > "The FMOD Studio interface will be comfortable to anyone familiar with a **Digital Audio Workstation (DAW)** such as Pro Tools or Logic Pro."

This source does triple duty for you: (1) it **confirms the timeline/DAW paradigm** you critique; (2) it shows the **non-linear escape hatches** (scatterers, **sustain points**, parameters, transition regions) that let an expert *defeat* linearity — implying the linearising effect is an **interface default**, not an absolute limit; and (3) it demonstrates the **games→theatre** flow that inverts the hypothesis.

**Institutional clincher.** The same standards body underlies both worlds: the **MIDI Manufacturers Association** ratified **MIDI Show Control** (theatre, 1991) *and* houses the **IASIG** (games, 1994). And **Michael Land** appears in *both* the adaptive-music patent (iMUSE) *and* the games-audio standardisation effort (iXMF, begun with George Sanger at Project Bar‑B‑Q). MIDI is the common grandparent.

---

## 6. Patents (checked)

| Patent | What it claims | Why it matters | Source |
|---|---|---|---|
| **US 5,315,057 A** — "Method and apparatus for dynamically composing music and sound effects using a computer entertainment system" (Land & McConnell; **LucasArts**; filed 1991-11-25, granted 1994-05-24) | Real-time composition driven by unpredictable game events: **"decision points"** for conditional branching between musical sequences; embedded **hooks/markers** for transposition/volume/instrument changes | **The urtext of adaptive game audio.** A *music-sequencer* logic (branch/marker), not a theatre-cue logic. Every later middleware re-implements it | US 5,315,057 |
| **US 6,700,640 B2** — "Apparatus and method for cueing a theatre automation system" (Morley et al.; **Qualcomm**; filed 2001-03-02, granted 2004-03-02) | Digital-cinema automation: operators build a **"playlist"** sequencing programs with embedded **"cues"** that trigger lights/curtains | Shows the **"playlist + cue"** model crystallising in *screen-entertainment* IP exactly as game middleware adopts events/playlist-containers | US 6,700,640 |
| **(absent)** Audiokinetic / Firelight | — | **No patents located** for either company; the dominant middlewares are not patent-driven (contrast iMUSE) | Google Patents searches |

A nice analytical aside: the **iMUSE patent (filed 1991) lapsed ~2011–12**, just as **FMOD Studio (2012)** and mature interactive-music systems proliferated. Treat as suggestive correlation, not proven causation.

---

## 7. How this maps onto your abstract

Your draft argues that FMOD/Wwise "emphasi[ze] the timeline-based editing paradigm of fixed-media audio composition" and so "struggle to represent soundscapes as interactive spaces," with a "linearising effect" that also shapes accessibility (movement in the "direction of story progression"). The genealogy **explains the mechanism**:

1. **The timeline is inherited, twice over.** From **trackers/sequencers** (the "playlist/order-list," thread B/C → FMOD/Wwise) and from **screen/DAW fixed media** (FMOD Studio = a DAW). The tools *look like* music software because they *are* descended from it.
2. **The "cue" is the convergence point with theatre,** and theatre's cue is *also* fundamentally sequential (a stack advanced by GO). So both ancestries push toward linearity; the explorable-space model has **no strong ancestor** in either lineage — which is exactly why exploratory audiogames are "unusual."
3. **Tool criticism / walkthrough angle (Light, Burgess & Duguay):** a walkthrough of FMOD/Wwise can now name their **"environment of expected use"** as a *fixed-media, music-production* ideology — DAW timelines, playlist containers, "events" — that interpellates students into linear thinking *before they design a single sound*. That is your platform-studies/ocularcentrism argument, sharpened: the linearity is **sonic and infrastructural**, not merely visual.
4. **MVP pedagogy:** if the dominant tools bias toward the timeline, the *minimum viable soundscape* exercise should foreground the **non-linear escape hatches** (Wwise States/RTPCs/Switch Containers; FMOD parameters/scatterers/sustain points) — i.e., teach the **cue-as-space**, not the cue-as-timeline.

---

## 8. Accessibility synthesis

Performance-control software and accessibility are tightly linked, in three ways your paper can use.

**(a) Audio description (AD) is itself cue-based show control.** AD — born in theatre and screen — is *descriptions fired against time/events*, i.e., a **cue list** running alongside the primary performance. Its migration into games (`Xbox Accessibility Guideline 111`; Larreina‑Morales & Mangiron 2024; Mangiron & Zhang 2016; the live `Mortal Kombat 1` AD) is the **same cue/event infrastructure** repurposed for access. This is the most direct bridge between your two halves: **the thing that makes a game accessible (a controllable stream of discrete, well-timed audio events) is exactly what performance-control software is for.** And it inherits the linearity: AD "is most established for linear scenes" (your abstract; IGDA GASIG), because cue lists are sequential.

**(b) The "linearising" trap is an accessibility trap.** Because middleware foregrounds the timeline, mainstream blind-accessibility tends to **streamline movement** "in the direction of story progression" (your DeadeyeJediBob example) — turning exploration into a guided rail. The genealogy says this isn't a failure of will but a **path-dependency** of the tools. Naming it lets you argue for **exploratory** audio access as a design *and* tooling problem.

**(c) Exploratory audio games historically needed bespoke engines.** *Papa Sangre* / *The Nightjar* rendered explorable space in **binaural sound on a custom "Papa Engine," not FMOD/Wwise** — and even then hit accessibility friction (Apple VoiceOver "was not flexible enough to work at the same time as the sound engine," forcing a separate UI). This is concrete evidence for your claim that the **affordances for accessibility are real but under-tooled**: the spatial/exploratory audio game sits *outside* the mainstream middleware's comfort zone (Kirke; Röber & Masuch; Garcia & Neris).

**Constructive implication.** The accessible, exploratory audiogame your abstract calls for is, in genealogical terms, an attempt to build the **branch/space** model (iMUSE's "decision points," generalised from music to *navigation*) on tools that default to the **playlist/timeline** model. The pedagogical MVP, then, is to have students implement **audio navigation as adaptive cue-space** (states/parameters/spatialised events) rather than as a guided playlist — using the very middleware, but **against its grain**.

---

## 9. Reference list (with identifiers)

*All items are in Zotero → `CLAUDE_AUDIOGAMES`. ✚ = added in this pass; ◆ = already in your library. Zotero item keys in brackets.*

**Scholarship — game audio & adaptive music**
- ◆ Collins, K. (2008). *Game Sound: An Introduction to the History, Theory, and Practice of Video Game Music and Sound Design.* MIT Press. ISBN 9780262033787. [9LL9HCIU]
- ✚ Collins, K. (2013). *Playing with Sound: A Theory of Interacting with Sound and Music in Video Games.* MIT Press. ISBN 9780262018678. [TU57M95C]
- ✚ Strank, W. (2013). The Legacy of iMuse: Interactive Video Game Music in the 1990s. In P. Moormann (Ed.), *Music and Game* (pp. 81–91). Springer VS. DOI 10.1007/978-3-531-18913-0_4. [PCFWNT93]
- ✚ Moormann, P. (Ed.) (2013). *Music and Game: Perspectives on a Popular Alliance.* Springer VS. DOI 10.1007/978-3-531-18913-0. [C69PTRN3]
- ◆ Grimshaw, M. (Ed.) (2011). *Game Sound Technology and Player Interaction.* IGI Global. ISBN 9781616928285. [2Q36MU62]
- ◆ Kirke, A. (2018). When the Soundtrack Is the Game. DOI 10.1007/978-3-319-72272-6_7. [CEEMUMSG]
- ◆ Röber, N., & Masuch, M. (2005). Audio games: new perspectives on game audio. DOI 10.1145/1067343.1067361. [F5PCH5QZ]

**Industry & primary — middleware**
- ✚ Fay, T. M., Selfon, S., & Fay, T. J. (2004). *DirectX 9 Audio Exposed: Interactive Audio Development.* Wordware. ISBN 9781556222887. [F75KN8WB]
- ✚ "DirectMusic for the Masses." *Game Developer* (Gamasutra). [THIAMC2A]
- ✚ "The Miles Sound System." RAD Game Tools. https://www.radgametools.com/miles.htm [RUBT7ZDN]
- ✚ "Ultimate Soundtracker." Wikipedia *(tertiary)*. [W5NJQURP]
- ✚ "About Audiokinetic." Audiokinetic. https://www.audiokinetic.com/en/about/ [NIA76EBA]
- ✚ "Firelight Technologies Announces … FMOD Studio at GDC 2012." Business Wire, 7 Mar 2012. [5ETT9RC7]
- ✚ "Sony Interactive Entertainment to Acquire Audiokinetic" (2019). [VHWWFVFF]
- ✚ zú Montréal. "Alliances — with Martin Klein (Wwise & Audiokinetic)" — **primary founder biography** (music→records→Ubisoft 1997→Audiokinetic 2000). [VR8FVFVS]
- ✚ Audiokinetic. *The Story of Wwise* (video; company origin account). [RX98D7XZ]

**Industry & primary — theatre / show control**
- ✚ Huntington, J. (2017). *Show Networks and Control Systems* (formerly *Control Systems for Live Entertainment*, Focal Press, 1994). Zircon Designs Press. ISBN 9780692958735. [MZHEVVQR]
- ✚ Huntington, J. (2023). "A Bit of MIDI Show Control History." Controlgeek.net. [AJ2CTAZF]
- ✚ Brown, R. (2010). *Sound: A Reader in Theatre Practice.* Palgrave Macmillan. [FW9FWGPM]
- ✚ Deiorio, V. (2018). *The Art of Theatrical Sound Design: A Practical Guide.* Methuen Drama. ISBN 9781474257800. [4IV6J26S]
- ✚ **Theatre-playback peers (the cue-software field):** **QLab** (Figure 53; Ashworth & Kriss; macOS; v1.0 2006) [GNDSXR5M] · **SFX** (Stage Research / Timeline Theatrics; Guc & Rembielak; Windows) [FJXUJJMV] · **Show Cue System / SCS** (Show Cue Systems, AU; Windows) [KDJ2BEGC] · **MultiPlay** (da-share; Windows; free) [I7KEUHHA] · **Richmond Sound Design** — Stage Manager / AudioBox / SoundMan-Server (Charlie Richmond; 1972; Vancouver BC) [D2EGE9WF].

**Convergence (keystone)**
- ✚ Swift, S. (2020). "FMOD, an Audio Engine for Video Games, Adapted for Theater." USITT Sound Commission. [NFZZW5G7]
- ✚ "Introducing the Interactive XMF Audio File Format." *Game Developer* / IASIG. [5H9R6UWQ]

**Patents**
- ✚ Land, M. Z., & McConnell, P. N. (1994). *US 5,315,057 A.* LucasArts. https://patents.google.com/patent/US5315057A/en [TZ6C9ZMU]
- ✚ Morley, S. A., et al. (2004). *US 6,700,640 B2.* Qualcomm. https://patents.google.com/patent/US6700640B2/en [VFJPUVTR]

**Accessibility & audio games**
- ✚ Larreina‑Morales, M. E., & Mangiron, C. (2024). Audio description in video games? *Universal Access in the Information Society.* DOI 10.1007/s10209-023-01036-4. [RVFHDDM8]
- ✚ Mangiron, C., & Zhang, X. (2016). Game Accessibility for the Blind … DOI 10.1057/978-1-137-56917-2_5. [DT6K9JR2]
- ✚ "Xbox Accessibility Guideline 111: Audio descriptions." Microsoft Learn. [Z97BUP6Q]
- ✚ "Papa Sangre." Wikipedia *(tertiary; for Papa Sangre / The Nightjar / Papa Engine)*. [47R8F66G]
- ◆ Garcia, F. E., & de Almeida Neris, V. P. (2013). Design Guidelines for Audio Games. DOI 10.1007/978-3-642-39262-7_26. [ZFBRLP9C]
- ◆ Light, B., Burgess, J., & Duguay, S. (2018). The walkthrough method. DOI 10.1177/1461444816675438. [RQS67WJX]
- ◆ Fritsch, J., et al. (2025). Towards a Framework for Exploring Synthetic Voices in VUI Design. DOI 10.1145/3715336.3735729. [85UIL4HS]
- ◆ Game Accessibility Guidelines [HJ9YTED6]; ◆ GAG & WCAG 2.0 Gap Analysis, DOI 10.1007/978-3-319-94277-3_43 [A4TWVFIC]; ◆ TLOU II accessibility [II2G4GXC]; ◆ Mortal Kombat 1 AD (IGDA GASIG) [PXWRT8KZ].

**Still worth adding (not yet in Zotero):** Collins, *Game Sound in the Mechanical Arcades* (Game Studies 16(1), open access); Kaye & LeBrecht, *Sound and Music for the Theatre*; the IASIG iXMF specification document itself; Ableton Live as a theatre-playback tool (per Swift). The theatrical-playback peers (QLab, SFX, SCS, MultiPlay, Richmond Sound Design) are **now in the collection**.

---

## 10. Caveats & verification notes

- **Founder biography — resolved.** Now corroborated by a primary source: the zú Montréal "Alliances — with Martin Klein" bio gives the music→records→**Ubisoft (1997)**→Audiokinetic (2000) path explicitly, and Audiokinetic's *The Story of Wwise* video is the company's own origin account. For an even stronger citation, transcribe Klein's spoken remarks in those talks. (The earlier aggregator bios — Crunchbase/The Org — agree.)
- **FMOD Designer date** appears variously as 2005/2006/2010 across sources; "mid-2000s" is safe. FMOD Studio: announced GDC **2012**, 1.0 in **2013**.
- **Tertiary sources** (Wikipedia, Grokipedia) are used for tracker history, Papa Sangre, and some FMOD dates; treat as pointers and confirm against primaries (Demozoo/pouët; developer postmortems).
- **Negative patent finding** = "none located in Google Patents," not a proof of non-existence.
- The **iMUSE-patent-expiry ↔ FMOD-Studio** timing is an *observation*, not a demonstrated cause.

---

## 11. What was done in your Zotero (`CLAUDE_AUDIOGAMES`) & local deliverables

**Zotero — `CLAUDES_NOTES → CLAUDE_AUDIOGAMES` (41 items):**
- **29 new items created** — scholarship (DOIs via CrossRef), books (ISBNs via OpenLibrary/Google Books), **2 patents**, industry/primary web sources, **5 theatre-playback peers** (QLab, SFX, SCS, MultiPlay, Richmond Sound Design, as `computerProgram` items), and **2 primary Klein sources** (zú talk; *The Story of Wwise*).
- **12 existing** accessibility/audio-games items added non-destructively, co-locating the genealogy and accessibility halves.
- **5 thematic sub-collections** for navigation: **1 · Theatre & show control** (11) · **2 · Middleware, adaptive music & tracker roots** (13) · **3 · Convergence & standardization** (6) · **4 · Accessibility & audio games** (13) · **5 · Method & game-audio scholarship** (4). *(Your own seed note sits at the collection top level, untouched.)*
- **30 child-note annotations**, each with a **YAML header** (`annotation_by`, `themes`, `relates_to`, `key_claim`, `status`) and prose cross-linking related items via clickable `zotero://select` URIs.
- **Thematic tags** for clustering (`theme:show-control`, `theme:middleware-history`, `theme:adaptive-audio`, `theme:standardization`, `theme:accessibility-AD`, `theme:audio-games`, `theme:theatre-sound`, `theme:games-theatre-convergence`, `theme:canadian-audio`, `theme:tracker-demoscene`, `theme:patent`, `theme:DAW-timeline-paradigm`), plus `CLAUDE_AUDIOGAMES-2026` and `CLAUDE-annotation`.

**Local files (this folder):**
- `Audio-Performance-Control_Genealogy-and-Accessibility.md` — this report.
- `Timeline-Tooling-Recommendations.md` — open-source methods for a beautiful HTML + PDF timeline.
- `timeline/` — a runnable, data-driven scaffold that already produced `timeline.pdf`, `genealogy.pdf`, and a self-contained `index.html` (re-render: `bash timeline/render.sh`).
