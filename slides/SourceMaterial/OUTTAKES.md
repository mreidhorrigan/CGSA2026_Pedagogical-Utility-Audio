# Slide outtakes / detritus

Archive of kiosk slides retired when the room was reduced from **14 kiosks to 9**
(2026-06-11, after the first full deck shipped in `0caadb4` / `924aaf5` — those
commits hold the byte-exact originals if this file ever disagrees). Nothing here
is loaded by the game: `build_slides.py` ignores subdirectories of `slides/`.

## The 14-kiosk room (before)

1. Minimum Viable Soundscapes — *kept (kiosk 1)*
2. Minimum Viable Product — *merged with #3 → kiosk 2*
3. Why Audio First — *merged into kiosk 2 (its opening paragraph was dropped as
   redundant with #2's labour/prestige paragraph — original below)*
4. The Audio Training Sequence — *merged with #5 → kiosk 3*
5. Ergatogeny Repeats Phylogeny — *merged into kiosk 3*
6. Problems With The Pipeline — *kept (kiosk 4)*
7. A Timeline Of Audio Control — *kept, deliberately its own kiosk (kiosk 5)*
8. Where The Timeline Comes From — *merged with #9 → kiosk 6*
9. The Linearising Trap — *merged into kiosk 6*
10. The Present Chaosifier — *merged with #11 → kiosk 7*
11. A Longer Genealogy — *merged into kiosk 7*
12. Clod Bathos Superior Machine — *merged with #13 → kiosk 8 (Audio-Led Games)*
13. Autofac Rad Shipping — *merged into kiosk 8*
14. References And Links — *kept (kiosk 9)*

## Why these merges

- **2+3** — the dilemma and audio's answer to it are one argument.
- **4+5** — "ergatogeny repeats phylogeny" is a claim *about* the training
  sequence; it now caps that kiosk.
- **8+9** — the tools' ancestry and the linearising trap it produces are the
  essay's single through-line.
- **10+11** — both are the outline's part three: the disruption now and the
  long view.
- **12+13** — two short examples under one "audio-led games" roof.

To resurrect any slide: copy its HTML below back to a numbered top-level file in
`slides/` and run `python3 build_slides.py`.

---

The full standalone slides follow, verbatim.

## 02_minimum_viable_product.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minimum viable product</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ffd166;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.5em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.04em}
  blockquote p{margin:.2em 0}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Pedagogy · the dilemma</p>
  <h1>Minimum viable product</h1>

  <ul>
    <li>The <strong>least resource-intensive usable version</strong> of an object.</li>
    <li>The more resource-intensive the medium, the more necessary the MVP.</li>
    <li>And <strong>games are the most resource-intensive medium</strong>.</li>
  </ul>

  <p>In popular culture, a videogame's attractiveness and prestige normally result in
  significant part from its detailed, bespoke visual interactive assets — which require
  time-consuming, repetitive labour to design.</p>

  <blockquote>
    <p>For their classes to make the most widely recognizable of good games, instructors
    would have to exploit students as workers; yet, if students do not make good-enough
    games in postsecondary production classes, academic programmes lose the authority by
    which they make crucial, prosocial interventions into game culture.</p>
  </blockquote>

  <p><strong>We need to assign our students minimum viable products that have aesthetic
  value without miring students in prematurely specializing workflows.</strong></p>

  <p class="src">From the conference abstract.</p>
</main>
</body>
</html>
```

## 03_why_audio_first.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Why audio-first?</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ffd166;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.5em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  .turn{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin-top:1.5em}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Pedagogy · the proposal</p>
  <h1>Why audio-first?</h1>

  <p>The games students have played before entering production programs are usually the
  most expensive to produce — and the expense of triple-A-style gamemaking militates for
  hierarchically specialized labour disciplines that undermine the
  <strong>diverse transferability of skills</strong> postsecondary students need.</p>

  <p>Audio changes the economics:</p>
  <ul>
    <li><strong>Smaller storage requirements</strong> correspond with more easily adjustable
        workflows — and thus better teaching scenarios.</li>
    <li>Students can still produce media whose <strong>standard of refinement matches</strong>
        some aspects of the most popular games.</li>
    <li>As a technique, <strong>digital audio is extremely mature</strong>, easing asset
        production.</li>
    <li>As old media continually become the content of the new, the
        <em>obsolescence</em> of assets has value in the pedagogy of their vectors —
        interactive media.</li>
  </ul>

  <p class="turn">But a gap occurs between <strong>visually dominated game engines</strong> and
  <strong>timeline-focused audio engines</strong> — and this gap is a barrier for audio-first
  gamemaking. The next kiosks trace where that gap comes from.</p>

  <p class="src">From the conference abstract and talk notes.</p>
</main>
</body>
</html>
```

## 04_the_audio_training_sequence.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The audio training sequence — traditional</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ffd166;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ol.seq{list-style:none;counter-reset:step;margin:1.2em 0;padding:0}
  ol.seq>li{counter-increment:step;background:var(--panel);border:1px solid var(--line);
            border-radius:10px;padding:.7em .9em .7em 3em;margin:.5em 0;position:relative}
  ol.seq>li::before{content:counter(step);position:absolute;left:.8em;top:.62em;
            color:var(--accent);font-weight:800;font-size:1.15em}
  ol.seq b{color:#fff}
  ol.seq .eg{color:var(--muted);font-size:.9em;display:block;margin-top:.15em}
  strong,em{color:#fff}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">How audio is taught</p>
  <h1>The audio training sequence — traditional</h1>

  <ol class="seq">
    <li><b>Practice</b><span class="eg">music · storytelling (theatre) · tabletop roleplay</span></li>
    <li><b>Recording</b><span class="eg">e.g. soundwalking, performance documentation, actual-play podcast</span></li>
    <li><b>Editing</b><span class="eg">e.g. Audacity</span></li>
    <li><b>Routing</b><span class="eg">e.g. Reaper</span></li>
    <li><b>Control and cueing</b><span class="eg">e.g. Ableton, QLab, Traktor — MIDI manipulation</span></li>
    <li><b>Installation audio; visual / flowchart programming</b><span class="eg">Max — then bespoke software engineering (e.g. the Web Audio SDK)</span></li>
    <li><b>Gaming middleware</b><span class="eg">FMOD, Wwise — visual flowchart programming (e.g. Unreal MetaSounds), then bespoke engineering (e.g. plugin adaptation for Wwise shipping)</span></li>
  </ol>

  <p>Seven rungs, climbed in order, each gated by the one before — and each rung is also a
  <strong>stage in the history of the craft</strong>. That resemblance is the next kiosk's claim.</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```

## 05_ergatogeny_repeats_phylogeny.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ergatogeny repeats phylogeny</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ffd166;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  .def{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin:1.2em 0}
  .def b{color:var(--accent)}
  strong,em{color:#fff}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.12em}
  blockquote p{margin:.2em 0}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">A proposition</p>
  <h1>Ergatogeny repeats phylogeny</h1>

  <p class="def"><b>Ergatogeny</b> — professional ontology: the emergence of a skilled worker
  (<em>ergat-</em>).</p>

  <blockquote>
    <p>A student — who is always already a worker — develops skills according to a sequence
    recapitulating the history of their craft.</p>
  </blockquote>

  <p>After the old biological slogan (“ontogeny recapitulates phylogeny”): the traditional
  training sequence replays, in one student's development, the historical development of
  audio work itself. Practice before recording; recording before editing; cueing before
  middleware.</p>

  <p>So a curriculum is also a <strong>genealogy</strong> — and whatever the history got
  wrong, the curriculum re-teaches.</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```

## 08_where_the_timeline_comes_from.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Where the timeline comes from</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#79e0c4;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.55em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0}
  blockquote p{margin:.2em 0}
  .payoff{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin:1.4em 0}
  figure{margin:1.6em 0 0}
  .card{background:#f6f1e7;border-radius:12px;padding:12px;overflow:auto;
        -webkit-overflow-scrolling:touch;max-height:60vh}
  .card img{width:1054px;max-width:none;height:auto;display:block;border-radius:6px}
  figcaption{color:var(--muted);font-size:.85em;margin-top:.6em;line-height:1.45}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Genealogy</p>
  <h1>Where the timeline comes from</h1>

  <blockquote>
    <p>Game-audio middleware (FMOD, Wwise) and theatrical show-control software (QLab&hellip;)
    are <strong>siblings, not parent-and-child</strong>. They converge on the same control
    vocabulary because they descend from a shared ancestor — <strong>MIDI, 1983</strong> —
    and solved the same problem in parallel. The crossover is real, documented, and
    bidirectional — but the dominant documented flow is <strong>games&nbsp;&rarr;&nbsp;theatre</strong>.</p>
  </blockquote>

  <ul>
    <li><strong>FMOD is demoscene.</strong> “Firelight MODule player” (1995) was born to play
        tracker music; FMOD Studio (2012) is explicitly “designed like a digital audio
        workstation.”</li>
    <li><strong>Wwise is Montréal music-production, not theatre.</strong> Founder Martin H.
        Klein went music &rarr; Ubisoft (1997) &rarr; Audiokinetic (2000) — no theatre at any
        stage.</li>
    <li><strong>The convergence is documented from the other direction:</strong> “An FMOD
        event is akin to a theatrical sound cue” (Swift, USITT 2020) — a game engine adapted
        <em>for</em> theatre.</li>
  </ul>

  <p class="payoff"><strong>The timeline is inherited, twice over</strong> — from the
  tracker/sequencer <em>playlist</em> and from the DAW's <em>fixed media</em>. Both ancestries
  push toward linearity; the explorable-space model has <strong>no strong ancestor in either
  lineage</strong> — which is exactly why exploratory audiogames are “unusual.”</p>

  <figure>
    <div class="card">
      <img src="SourceMaterial/AUDIOGAMES/genealogy.svg"
           alt="Directed graph with MIDI 1.0 (1983) at the root and four branches — theatre/show control, tracker/demoscene, music sequencer/adaptive, and engine/driver abstraction — leading to FMOD, Wwise, QLab and audio games, with arrows marking documented crossovers including games-to-theatre in 2020.">
    </div>
    <figcaption>Four lineages feed modern game audio; only one is theatre — and it is a
    <em>sibling</em> of middleware, not its parent. The graph is full size —
    scroll / drag inside it to pan.</figcaption>
  </figure>

  <p class="src">From the background study, “Audio performance control, from the theatre cue
  to the game engine.”</p>
</main>
</body>
</html>
```

## 09_the_linearising_trap.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The linearising trap</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#79e0c4;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.6em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.08em}
  blockquote p{margin:.2em 0}
  .move{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin:1.4em 0}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Findings · work in progress</p>
  <h1>The linearising trap</h1>

  <p>By emphasizing the <strong>timeline-based editing paradigm</strong> of fixed-media audio
  composition, the most popular game-audio frameworks <strong>struggle to represent
  soundscapes as interactive spaces</strong>.</p>

  <ul>
    <li>Mainstream accessibility features for blind players tend to limit exploration by
        streamlining movement in the <em>“direction of story progression”</em>
        (DeadeyeJediBob, 2024) — repeating the timeline theme.</li>
    <li>Audio description is itself <strong>cue-based show control</strong> — and it remains
        most established for <em>linear</em> scenes (IGDA GASIG, 2023).</li>
    <li>The linearizing effect may explain why <em>Papa Sangre</em> and <em>The Nightjar</em>
        have remained unusual despite their affordances for accessibility (Kirke, 2018) —
        both ran on a bespoke binaural engine, not FMOD or Wwise.</li>
  </ul>

  <blockquote>
    <p>An underappreciated niche exists for <strong>exploratory audiogames</strong>: games that
    use audio to fully support environmental storytelling, beyond directing navigational
    guidance.</p>
  </blockquote>

  <p class="move"><strong>The teaching response:</strong> have students build audio navigation
  as adaptive <em>cue-space</em> — states, parameters, spatialised events — rather than as a
  guided playlist. Teach the cue-as-space, not the cue-as-timeline: the very middleware,
  used <em>against its grain</em>.</p>

  <p class="src">Method: a critical walkthrough (Light, Burgess &amp; Duguay, 2018) of FMOD
  and Wwise, with a literature review of audio accessibility. From the abstract and the
  background study.</p>
</main>
</body>
</html>
```

## 10_the_present_chaosifier.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Present Chaosifier</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#c9a7ff;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  strong,em{color:#fff}
  .nest{list-style:none;margin:1.2em 0;padding:0}
  .nest li{background:var(--panel);border:1px solid var(--line);border-radius:10px;
           padding:.65em .95em;margin:.45em 0}
  .nest li:nth-child(2){margin-left:1.6em}
  .nest li:nth-child(3){margin-left:3.2em}
  .nest b{color:var(--accent)}
  .nest span{color:var(--muted);font-size:.9em}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.1em}
  blockquote p{margin:.2em 0}
  .meta{color:var(--muted);font-size:.9em}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Disruption</p>
  <h1>The Present Chaosifier</h1>

  <p><strong>Vibe (vibration?) coding</strong> as dis- or super-intermediation:</p>

  <ul class="nest">
    <li><b>command-line interface</b> <span>(CLI)</span></li>
    <li><b>model context protocol</b> <span>(MCP)</span></li>
    <li><b>bespoke software</b> <span>— much easier to have; architectural understanding much more important</span></li>
  </ul>

  <blockquote>
    <p>Working with an LLM is a <em>devising</em> process, because of the dialogue and
    randomness involved.</p>
  </blockquote>

  <p>The pipeline's GUI problem inverts: the sequence's final rung — bespoke software
  engineering — comes within early reach, while <strong>architectural understanding matters
  more than ever</strong>.</p>

  <p class="meta">(This room is itself an instance: a build-free, vibe-coded isometric
  poster.)</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```

## 11_a_longer_genealogy.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A longer genealogy</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#c9a7ff;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  strong,em{color:#fff}
  .lead{font-size:1.2em}
  .pair{margin:1.4em 0;padding:0;list-style:none}
  .pair li{background:var(--panel);border:1px solid var(--line);border-radius:10px;
           padding:.9em 1.1em;margin:.5em 0;font-size:1.12em}
  .pair b{color:var(--accent)}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Perspective</p>
  <h1>A longer genealogy</h1>

  <p class="lead">Consider <strong>audio as the fundamental asset type</strong>.</p>

  <ul class="pair">
    <li><b>Storytelling</b> predates <b>writing</b>.</li>
    <li><b>Audio recording</b> predates <b>video recording</b>.</li>
  </ul>

  <p>Audio-first pedagogy leans on the maturity of the oldest layer of the craft: the
  training sequence's first rung — practice: music, storytelling, tabletop — is also its
  most ancient. And as a technique, digital audio is extremely mature, easing asset
  production.</p>

  <p class="src">From the talk notes and the conference abstract.</p>
</main>
</body>
</html>
```

## 12_clod_bathos_superior_machine.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clod Bathos, Superior Machine</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ff9e9e;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.55em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  a{color:var(--accent)}
  .btn{display:inline-block;background:var(--accent);color:#1b1426;font-weight:700;
       padding:.6em 1.1em;border-radius:10px;text-decoration:none;margin:.5em 0 1em}
  .caveat{background:var(--panel);border:1px solid var(--line);border-radius:10px;
          padding:.9em 1.1em;margin:1.4em 0;color:var(--muted)}
  .caveat b{color:var(--ink)}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Audio-led games · example 1</p>
  <h1>Clod Bathos, <em>Superior Machine</em></h1>

  <p><a class="btn" href="https://mreidhorrigan.github.io/Clod-Bathos-Superior-Machine-An-LM-IDN/"
        target="_blank" rel="noopener">Play it in the browser&nbsp;&nearr;</a></p>

  <ul>
    <li>A <strong>text-based, stylized command-line game</strong> — successor to
        choose-your-own-adventure and interactive digital narrative (IDN).</li>
    <li><strong>Twine, disintermediated.</strong> (Sorry, Twine — no support for LLM runtime
        dialogue rewording, or for state-machine navigation.)</li>
    <li>Seeks immersion by <strong>imitating the diegetic medium with the delivery
        medium</strong> — both of them screens.</li>
    <li>Exploits <strong>easy text-to-audio conversion</strong>.</li>
  </ul>

  <p class="caveat"><b>However:</b> LLMs sized for local operability are not (yet) smart
  enough to carry the game on their own.</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```

## 13_autofac_rad_shipping.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Autofac: Rad Shipping</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ff9e9e;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.6em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.6em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  .lead{font-size:1.1em}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Audio-led games · example 2</p>
  <h1>Autofac: <em>Rad Shipping</em></h1>

  <p class="lead">Navigate a <strong>darkfactory</strong> — the “lights-out” factory, a
  corporate concept for a warehouse that requires no humans — as a robot moving in the
  dark.</p>

  <ul>
    <li><strong>Horror:</strong> the robot inherits a vestigial work environment shaped by
        the abuse of the human workers who came before it.</li>
    <li>The warehouse is also <strong>irradiated</strong> — because why not; because the robot
        needs a timer for its tasks; and because of the historical use of robots near failed
        nuclear reactor cores.</li>
  </ul>

  <p>An audio-led game: in a lights-out world, the soundscape carries navigation, interface,
  and story.</p>

  <p class="src">From the talk notes (work in progress).</p>
</main>
</body>
</html>
```
