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


---

# 2026-06-12 — condensed for projector legibility

The 9 kiosk slides were rewritten for an overhead-projector context: **light
(cream) background, Verdana, larger type, and aggressively trimmed text** so each
kiosk fits with minimal scrolling. The fuller-prose versions that were live
2026-06-11 → 12 (dark theme, system-font stack) are preserved verbatim below; the
arguments and sources are unchanged, only the wording was tightened. Copy any
block back to its top-level file + rebuild to restore the verbose version.

## 01_minimum_viable_soundscapes.html (verbose, pre-condense)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minimum viable soundscapes</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ffd166;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(17px,2.2vw,21px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.8em,5vw,2.8em);line-height:1.1;margin:.1em 0 .2em;letter-spacing:-.01em}
  .sub{font-size:1.25em;color:var(--ink);margin:.2em 0 .6em;font-weight:600}
  .byline{color:var(--muted);font-size:1em;margin:0 0 1.4em}
  p{margin:.75em 0}
  .lead{font-size:1.1em}
  .hint{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.8em 1em;color:var(--muted);font-size:.92em;margin:1.6em 0}
  .hint b{color:var(--ink)}
  .kw{display:inline-block;background:var(--panel);border:1px solid #3a2d55;border-radius:999px;
      padding:.25em .8em;margin:.18em;font-size:.8em;color:var(--muted)}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">CGSA 2026 · Conference poster</p>
  <h1>Minimum viable soundscapes</h1>
  <p class="sub">Appraising the pedagogical utility of audiogames</p>
  <p class="byline">Matt Horrigan</p>

  <p class="lead">A major dilemma in media production pedagogy is the determination of
  <em>minimum viable products</em> — and the dilemma is especially prevalent for videogames.
  This poster shifts emphasis from the video mode to the audio mode and asks:
  <strong>what are the benefits of audio-first design pedagogy?</strong></p>

  <div class="hint">
    <b>How this room works:</b> each kiosk holds one idea from the talk — wander in any order,
    or press <b>Space</b> to be walked to the next kiosk automatically. Open a kiosk with
    <b>E</b> (or a tap); walk away to leave it; browse a kiosk's pages with <b>&lsaquo;</b> and <b>&rsaquo;</b>.
  </div>

  <p>
    <span class="kw">design pedagogy</span>
    <span class="kw">audiogames</span>
    <span class="kw">minimum viable product</span>
    <span class="kw">technological maturity</span>
    <span class="kw">accessibility</span>
  </p>

  <p class="src">From the conference abstract, “Minimum viable soundscapes: Appraising the
  pedagogical utility of audiogames.”</p>
</main>
</body>
</html>
```

## 02_minimum_viable_product.html (verbose, pre-condense)

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
  h2{font-size:1.15em;color:var(--accent);margin:1.8em 0 .5em}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.5em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.04em}
  blockquote p{margin:.2em 0}
  .turn{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin-top:1.5em}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Pedagogy · the dilemma and the proposal</p>
  <h1>Minimum viable product</h1>

  <ul>
    <li>The <strong>least resource-intensive usable version</strong> of an object.</li>
    <li>The more resource-intensive the medium, the more necessary the MVP.</li>
    <li>And <strong>games are the most resource-intensive medium</strong>.</li>
  </ul>

  <p>In popular culture, a videogame's attractiveness and prestige normally result in
  significant part from its detailed, bespoke visual interactive assets — which require
  time-consuming, repetitive labour to design. The expense of triple-A-style gamemaking
  militates for hierarchically specialized labour disciplines that undermine the
  <strong>diverse transferability of skills</strong> postsecondary students need.</p>

  <blockquote>
    <p>For their classes to make the most widely recognizable of good games, instructors
    would have to exploit students as workers; yet, if students do not make good-enough
    games in postsecondary production classes, academic programmes lose the authority by
    which they make crucial, prosocial interventions into game culture.</p>
  </blockquote>

  <p><strong>We need to assign our students minimum viable products that have aesthetic
  value without miring students in prematurely specializing workflows.</strong></p>

  <h2>Why audio-first?</h2>

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

  <p class="src">From the conference abstract.</p>
</main>
</body>
</html>
```

## 03_the_audio_training_sequence.html (verbose, pre-condense)

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
  h2{font-size:1.15em;color:var(--accent);margin:1.8em 0 .5em}
  p{margin:.75em 0}
  ol.seq{list-style:none;counter-reset:step;margin:1.2em 0;padding:0}
  ol.seq>li{counter-increment:step;background:var(--panel);border:1px solid var(--line);
            border-radius:10px;padding:.7em .9em .7em 3em;margin:.5em 0;position:relative}
  ol.seq>li::before{content:counter(step);position:absolute;left:.8em;top:.62em;
            color:var(--accent);font-weight:800;font-size:1.15em}
  ol.seq b{color:#fff}
  ol.seq .eg{color:var(--muted);font-size:.9em;display:block;margin-top:.15em}
  strong,em{color:#fff}
  .def{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin:1.2em 0}
  .def b{color:var(--accent)}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.08em}
  blockquote p{margin:.2em 0}
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
  <strong>stage in the history of the craft</strong>:</p>

  <h2>Ergatogeny repeats phylogeny</h2>

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

## 04_problems_with_the_pipeline.html (verbose, pre-condense)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Problems with the pipeline</title>
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
  .next{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:.9em 1.1em;margin-top:1.5em}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Critique</p>
  <h1>Problems with the pipeline</h1>

  <ul>
    <li><strong>Timelines aren't playtime.</strong> The perception persists that timelines are
        easier than cyclic playtime — but the fixed-medium timeline mindset, useful for
        replicable data (annotation, reference), is <em>wrong for user experience</em>.
        Linear time is also ethnocentric.</li>
    <li><strong>Middleware nudges students</strong> to specialize in audio — underpaid — and
        separates them from the interactive logic of the games they score.</li>
    <li><strong>GUIs impair software-architecture awareness</strong>, blocking access to
        transferable and generalizable tools.</li>
    <li><strong>The sequence ranks teachers above learners</strong> — it artificially places
        instructors ahead of students in a linear development process.</li>
  </ul>

  <p class="next">These tools have a history. The <strong>next kiosk</strong> holds the full
  1972–2020 timeline of audio performance control, at a size you can scroll.</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```

## 05_a_timeline_of_audio_control.html (verbose, pre-condense)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A timeline of audio control</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#79e0c4;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(16px,2vw,20px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(14px,2.5vw,32px)}
  .copy{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.6em,4vw,2.4em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  p{margin:.7em 0}
  strong,em{color:#fff}
  .hint{color:var(--muted);font-size:.88em}
  .pane{background:#f6f1e7;border-radius:12px;padding:10px;margin:1.2em 0 0;
        overflow:auto;-webkit-overflow-scrolling:touch;max-height:70vh}
  .pane img{width:1412px;max-width:none;height:auto;display:block;border-radius:6px}
  .src{color:var(--muted);font-size:.82em;margin-top:1.4em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
  <div class="copy">
    <p class="kicker">Genealogy · the data</p>
    <h1>A timeline of audio control</h1>
    <p>Fifty years of audio performance control, 1972–2020, in six lanes — theatre show
    control, tracker/demoscene, music sequencers, engine middleware, standardization, audio
    games — all descending from <strong>MIDI&nbsp;1.0 (1983)</strong>. ★ marks documented
    convergences: MIDI Show Control (1991), Wwise and QLab shipping the same year (2006),
    FMOD adapted for theatre (2020).</p>
    <p class="hint">The chart is shown at full size so the type stays legible —
    <strong>scroll / drag inside it</strong> to pan across the decades.</p>
  </div>

  <div class="pane">
    <img src="SourceMaterial/AUDIOGAMES/timeline_vega.svg"
         alt="Swim-lane timeline of audio performance control from 1972 to 2020: events in six lanes — theatre/show control, tracker/demoscene, music sequencer/adaptive, engine/middleware, standardization, and audio games/accessibility — all descending from MIDI 1.0 in 1983. Stars mark convergences such as MIDI Show Control in 1991, Wwise and QLab both shipping in 2006, and FMOD adapted for theatre in 2020.">
  </div>

  <div class="copy">
    <p class="src">Figure from the background study, generated from
    <code>timeline_data.json</code> in this room's source material.</p>
  </div>
</body>
</html>
```

## 06_where_the_timeline_comes_from.html (verbose, pre-condense)

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
  h2{font-size:1.15em;color:var(--accent);margin:1.8em 0 .5em}
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
  <p class="kicker">Genealogy · findings</p>
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

  <h2>The linearising trap</h2>

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

  <p class="payoff"><strong>The teaching response:</strong> have students build audio navigation
  as adaptive <em>cue-space</em> — states, parameters, spatialised events — rather than as a
  guided playlist. Teach the cue-as-space, not the cue-as-timeline: the very middleware,
  used <em>against its grain</em>.</p>

  <p class="src">From the background study, “Audio performance control, from the theatre cue
  to the game engine,” and the conference abstract. Method: a critical walkthrough (Light,
  Burgess &amp; Duguay, 2018) of FMOD and Wwise, with a literature review of audio
  accessibility. Findings are work in progress.</p>
</main>
</body>
</html>
```

## 07_the_present_chaosifier.html (verbose, pre-condense)

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
  h2{font-size:1.15em;color:var(--accent);margin:1.8em 0 .5em}
  p{margin:.75em 0}
  strong,em{color:#fff}
  .nest{list-style:none;margin:1.2em 0;padding:0}
  .nest li{background:var(--panel);border:1px solid var(--line);border-radius:10px;
           padding:.65em .95em;margin:.45em 0}
  .nest li:nth-child(2){margin-left:1.6em}
  .nest li:nth-child(3){margin-left:3.2em}
  .nest b{color:var(--accent)}
  .nest span{color:var(--muted);font-size:.9em}
  .pair{margin:1.2em 0;padding:0;list-style:none}
  .pair li{background:var(--panel);border:1px solid var(--line);border-radius:10px;
           padding:.8em 1.1em;margin:.5em 0;font-size:1.08em}
  .pair b{color:var(--accent)}
  blockquote{margin:1.4em 0;padding:1em 1.2em;background:var(--panel);
             border-left:4px solid var(--accent);border-radius:0 10px 10px 0;font-size:1.1em}
  blockquote p{margin:.2em 0}
  .meta{color:var(--muted);font-size:.9em}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Disruption · perspective</p>
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

  <h2>A longer genealogy</h2>

  <p>Consider <strong>audio as the fundamental asset type</strong>.</p>

  <ul class="pair">
    <li><b>Storytelling</b> predates <b>writing</b>.</li>
    <li><b>Audio recording</b> predates <b>video recording</b>.</li>
  </ul>

  <p>Audio-first pedagogy leans on the maturity of the oldest layer of the craft: the
  training sequence's first rung — practice: music, storytelling, tabletop — is also its
  most ancient.</p>

  <p class="meta">(This room is itself an instance: a build-free, vibe-coded isometric
  poster.)</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```

## 08_audio_led_games.html (verbose, pre-condense)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Audio-led games</title>
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
  h2{font-size:1.2em;color:var(--accent);margin:1.8em 0 .5em}
  h2 em{color:var(--accent)}
  p{margin:.75em 0}
  ul{padding-left:1.3em;margin:.8em 0}
  li{margin:.55em 0}
  li::marker{color:var(--accent)}
  strong,em{color:#fff}
  a{color:var(--accent)}
  .btn{display:inline-block;background:var(--accent);color:#1b1426;font-weight:700;
       padding:.6em 1.1em;border-radius:10px;text-decoration:none;margin:.3em 0 .8em}
  .caveat{background:var(--panel);border:1px solid var(--line);border-radius:10px;
          padding:.9em 1.1em;margin:1.2em 0;color:var(--muted)}
  .caveat b{color:var(--ink)}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Audio-led games · two examples</p>
  <h1>Audio-led games</h1>

  <h2>Example 1 — Clod Bathos, <em>Superior Machine</em></h2>

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

  <h2>Example 2 — Autofac: <em>Rad Shipping</em></h2>

  <p>Navigate a <strong>darkfactory</strong> — the “lights-out” factory, a corporate concept
  for a warehouse that requires no humans — as a robot moving in the dark.</p>

  <ul>
    <li><strong>Horror:</strong> the robot inherits a vestigial work environment shaped by
        the abuse of the human workers who came before it.</li>
    <li>The warehouse is also <strong>irradiated</strong> — because why not; because the robot
        needs a timer for its tasks; and because of the historical use of robots near failed
        nuclear reactor cores.</li>
  </ul>

  <p>In a lights-out world, the soundscape carries navigation, interface, and story.</p>

  <p class="src">From the talk notes (Autofac is work in progress).</p>
</main>
</body>
</html>
```

## 09_references_and_links.html (verbose, pre-condense)

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>References &amp; links</title>
<style>
  :root{--bg:#15101f;--panel:#201734;--ink:#f2edf7;--muted:#bdb1d6;--accent:#ffd166;--line:#322747}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font:400 clamp(16px,2vw,19px)/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       padding:clamp(20px,4vw,56px)}
  main{max-width:46rem;margin:0 auto}
  .kicker{color:var(--accent);font-size:.78em;letter-spacing:.18em;text-transform:uppercase;font-weight:700;margin:0 0 .9em}
  h1{font-size:clamp(1.7em,4.5vw,2.4em);line-height:1.12;margin:.1em 0 .45em;letter-spacing:-.01em}
  h2{font-size:1.05em;color:var(--accent);margin:1.6em 0 .5em}
  p{margin:.7em 0}
  ul{padding-left:1.2em;margin:.6em 0}
  li{margin:.55em 0}
  li::marker{color:var(--accent)}
  em{color:#fff}
  a{color:var(--accent);word-break:break-word}
  .btn{display:inline-block;background:var(--accent);color:#1b1426;font-weight:700;
       padding:.55em 1em;border-radius:10px;text-decoration:none;margin:.3em 0}
  .kw{display:inline-block;background:var(--panel);border:1px solid #3a2d55;border-radius:999px;
      padding:.22em .75em;margin:.16em;font-size:.78em;color:var(--muted)}
  .src{color:var(--muted);font-size:.82em;margin-top:2.2em;border-top:1px solid var(--line);padding-top:.9em}
</style>
</head>
<body>
<main>
  <p class="kicker">Bibliography</p>
  <h1>References &amp; links</h1>

  <p><a class="btn" href="https://mreidhorrigan.github.io/Clod-Bathos-Superior-Machine-An-LM-IDN/"
        target="_blank" rel="noopener">Play <em>Clod Bathos, Superior Machine</em>&nbsp;&nearr;</a></p>

  <h2>Works cited</h2>
  <ul>
    <li>DeadeyeJediBob (2024). <em>Guy Born Blind Plays The Last of Us Part I — 1: The
        Beginning.</em> <a href="https://www.youtube.com/watch?v=ndodaE6OlSk"
        target="_blank" rel="noopener">YouTube</a>.</li>
    <li>Ford-Williams, G., Graham, L., Grammenos, D., Hamilton, I., Headstrong Games, Lee, E.,
        Manion, J., &amp; Westin, T. (n.d.). <em>Game Accessibility Guidelines.</em>
        <a href="https://gameaccessibilityguidelines.com/full-list/"
        target="_blank" rel="noopener">gameaccessibilityguidelines.com</a>.</li>
    <li>Fritsch, J., Karaturhan, P., Jørgensen, S. M. H., Ada, A. A., &amp; Knudsen, S. L.
        (2025). “Towards a Framework for Exploring Synthetic Voices in VUI Design.”
        <em>Proceedings of DIS '25</em>, 724–739.
        <a href="https://doi.org/10.1145/3715336.3735729" target="_blank"
        rel="noopener">doi:10.1145/3715336.3735729</a>.</li>
    <li>IGDA GASIG (2023). <em>“Showering the Ground with Gore”: The Audio Description of
        Mortal Kombat 1.</em> <a href="https://www.youtube.com/watch?v=tZ1H2RXuCCA"
        target="_blank" rel="noopener">YouTube</a>.</li>
    <li>Kirke, A. (2018). “When the Soundtrack Is the Game: From Audio-Games to Gaming the
        Music.” In <em>Emotion in Video Game Soundtracking</em>, 65–83.
        <a href="https://doi.org/10.1007/978-3-319-72272-6_7" target="_blank"
        rel="noopener">doi:10.1007/978-3-319-72272-6_7</a>.</li>
    <li>Light, B., Burgess, J., &amp; Duguay, S. (2018). “The walkthrough method: An approach
        to the study of apps.” <em>New Media &amp; Society</em>, 20(3), 881–900.
        <a href="https://doi.org/10.1177/1461444816675438" target="_blank"
        rel="noopener">doi:10.1177/1461444816675438</a>.</li>
  </ul>

  <h2>From the genealogy study</h2>
  <ul>
    <li>Swift, S. (2020). “FMOD, an Audio Engine for Video Games, Adapted for Theater.”
        USITT Sound Commission.</li>
    <li>Land, M. Z., &amp; McConnell, P. N. (1994). <em>US Patent 5,315,057</em> — the iMUSE
        patent, the urtext of adaptive game audio.
        <a href="https://patents.google.com/patent/US5315057A/en" target="_blank"
        rel="noopener">patents.google.com</a>.</li>
  </ul>

  <p>Background research is catalogued in Zotero (collection <em>CLAUDE_AUDIOGAMES</em>,
  41 items); the genealogy and timeline figures in this room are generated from
  <em>timeline_data.json</em> in the poster's source material.</p>

  <p>
    <span class="kw">design pedagogy</span>
    <span class="kw">audiogames</span>
    <span class="kw">minimum viable product</span>
    <span class="kw">technological maturity</span>
    <span class="kw">accessibility</span>
  </p>

  <p class="src">“Minimum viable soundscapes: Appraising the pedagogical utility of
  audiogames” · Matt Horrigan · CGSA 2026.</p>
</main>
</body>
</html>
```


---

## 2026-06-13 — Slide 02 retired: "Minimum viable product"

Displaced when slide 02 became **Questions & intuitions** during the slide-by-slide
rebuild. This is the production (light-theme, Verdana) MVP slide as it stood. The MVP
argument may well return on a later kiosk — recover it from here if so.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minimum viable product</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(18px,2.4vw,29px);line-height:1.5;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .7em}
  h1{font-size:clamp(30px,5vw,50px);line-height:1.08;margin:0 0 .4em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.22em;display:inline-block}
  h2{font-size:clamp(20px,2.5vw,26px);color:var(--accent);margin:1.3em 0 .3em}
  p{margin:.6em 0}
  .def{font-size:1.05em}
  ul{padding-left:1.15em;margin:.6em 0}
  li{margin:.45em 0}
  li::marker{color:var(--accent)}
  strong{font-weight:700}
  .box{background:var(--card);border-left:6px solid var(--accent);border-radius:0 10px 10px 0;
       padding:.8em 1.05em;margin:1em 0;box-shadow:0 1px 0 var(--rule);font-weight:700}
  .src{color:var(--soft);font-size:.7em;margin-top:1.4em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">The dilemma, and the proposal</p>
  <h1>Minimum viable product</h1>

  <p class="def">The <strong>least resource-intensive usable version</strong> of a thing.</p>
  <ul>
    <li>The costlier the medium, the more an MVP matters.</li>
    <li><strong>Games are the costliest medium</strong> — prestige rests on bespoke visual
        assets and repetitive labour.</li>
    <li>That pressure forces <strong>specialized labour</strong>, undermining the transferable
        skills students actually need.</li>
  </ul>

  <p class="box">Assign minimum viable products with real aesthetic value — without miring
  students in prematurely specialized workflows.</p>

  <h2>Why audio?</h2>
  <ul>
    <li>Smaller assets &rarr; flexible workflows &rarr; better teaching.</li>
    <li>Digital audio is a <strong>mature craft</strong>, so a high standard of refinement is
        within reach.</li>
  </ul>

  <p class="src">From the conference abstract.</p>
</main>
</body>
</html>
```


---

## 2026-06-13 — Slide 03 retired: "The audio training sequence"

Displaced when slide 03 became **Methods** during the slide-by-slide rebuild. This is the
production (light-theme) version. It's the worked example of *ergatogeny repeats phylogeny*
(slide 02's intuition) — the 7-step Practice → Game-middleware genealogy — so it may well
return on a later kiosk. Recover from here.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The audio training sequence</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(17px,2.15vw,27px);line-height:1.45;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .7em}
  h1{font-size:clamp(28px,4.6vw,46px);line-height:1.08;margin:0 0 .4em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.22em;display:inline-block}
  ol.seq{list-style:none;counter-reset:step;margin:.9em 0;padding:0}
  ol.seq>li{counter-increment:step;padding:.28em 0 .28em 2.1em;position:relative;
            border-top:1px solid var(--rule)}
  ol.seq>li:first-child{border-top:0}
  ol.seq>li::before{content:counter(step);position:absolute;left:0;top:.28em;
            color:var(--accent);font-weight:700;font-size:1.05em}
  ol.seq b{font-weight:700}
  ol.seq .eg{color:var(--soft);font-size:.85em}
  strong{font-weight:700}
  .box{background:var(--card);border-left:6px solid var(--accent);border-radius:0 10px 10px 0;
       padding:.8em 1.05em;margin:1em 0 0;box-shadow:0 1px 0 var(--rule)}
  .box b{color:var(--accent)}
  .src{color:var(--soft);font-size:.72em;margin-top:1.2em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">How audio is taught — traditionally</p>
  <h1>The audio training sequence</h1>

  <ol class="seq">
    <li><b>Practice</b> <span class="eg">— music, theatre, tabletop</span></li>
    <li><b>Recording</b> <span class="eg">— soundwalks, documentation, podcasts</span></li>
    <li><b>Editing</b> <span class="eg">— Audacity</span></li>
    <li><b>Routing</b> <span class="eg">— Reaper</span></li>
    <li><b>Control &amp; cueing</b> <span class="eg">— Ableton, QLab, Traktor (MIDI)</span></li>
    <li><b>Installation / visual programming</b> <span class="eg">— Max</span></li>
    <li><b>Game middleware</b> <span class="eg">— FMOD, Wwise</span></li>
  </ol>

  <p class="box"><b>Ergatogeny repeats phylogeny.</b> A student replays their craft's whole
  history, in order — so a curriculum is also a <strong>genealogy</strong>, and it re-teaches
  whatever that history got wrong.</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```


---

## 2026-06-13 — Slide 04 retired: "Problems with the pipeline"

Displaced when slide 04 became **Findings** during the slide-by-slide rebuild. The critique
bullets (timelines aren't playtime; middleware nudges students into underpaid audio; GUIs hide
architecture; the sequence ranks instructors above learners) may belong on a later "critique"
kiosk. Recover from here.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Problems with the pipeline</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(18px,2.4vw,29px);line-height:1.5;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .7em}
  h1{font-size:clamp(30px,5vw,50px);line-height:1.08;margin:0 0 .4em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.22em;display:inline-block}
  ul{padding-left:1.15em;margin:.7em 0}
  li{margin:.6em 0}
  li::marker{color:var(--accent)}
  strong{font-weight:700}
  .next{background:var(--card);border-left:6px solid var(--accent);border-radius:0 10px 10px 0;
        padding:.8em 1.05em;margin:1.1em 0 0;box-shadow:0 1px 0 var(--rule);font-size:.92em}
  .src{color:var(--soft);font-size:.72em;margin-top:1.3em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">Critique</p>
  <h1>Problems with the pipeline</h1>

  <ul>
    <li><strong>Timelines aren't playtime.</strong> Fixed-media linearity suits annotation and
        reference, not lived experience — and linear time is ethnocentric.</li>
    <li><strong>Middleware nudges students</strong> into audio — underpaid — and splits them
        from the game's interactive logic.</li>
    <li><strong>GUIs hide software architecture</strong>, blocking transferable, generalizable
        tools.</li>
    <li><strong>The sequence ranks instructors above learners</strong> by default.</li>
  </ul>

  <p class="next">Next kiosk &rarr; the full <strong>1972–2020 timeline</strong> of these
  tools, at a size you can scroll.</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>
```


---

## 2026-06-13 — Slide 05 retired: "A timeline of audio control" (standalone)

The timeline figure now lives embedded (scrollable) on slide 04 "Descriptive findings", so the
dedicated full-size kiosk was retired and slide 05 became **Normative findings**. The standalone
framing/copy is preserved here; the figure asset itself is still in use at
slides/SourceMaterial/AUDIOGAMES/timeline_vega.svg.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>A timeline of audio control</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(17px,2.05vw,25px);line-height:1.45;
       -webkit-text-size-adjust:100%;padding:clamp(16px,3vw,36px)}
  .copy{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .6em}
  h1{font-size:clamp(26px,4.2vw,42px);line-height:1.08;margin:0 0 .35em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.2em;display:inline-block}
  p{margin:.55em 0}
  strong{font-weight:700}
  .hint{color:var(--soft);font-size:.9em}
  .pane{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:10px;margin:.9em 0 0;
        overflow:auto;-webkit-overflow-scrolling:touch;max-height:72vh}
  .pane img{width:1412px;max-width:none;height:auto;display:block;border-radius:4px}
  .src{color:var(--soft);font-size:.74em;margin-top:1em}
</style>
</head>
<body>
  <div class="copy">
    <p class="kicker">Genealogy · the data</p>
    <h1>A timeline of audio control</h1>
    <p>1972–2020, six lanes — theatre show control, trackers, music sequencers, engine
    middleware, standardization, audio games — all descending from <strong>MIDI (1983)</strong>.
    <strong>★</strong> marks documented convergences.</p>
    <p class="hint"><strong>Scroll / drag inside the chart</strong> to pan across the decades.</p>
  </div>

  <div class="pane">
    <img src="SourceMaterial/AUDIOGAMES/timeline_vega.svg"
         alt="Swim-lane timeline of audio performance control from 1972 to 2020...">
  </div>

  <div class="copy">
    <p class="src">Figure from the background study, generated from
    <code>timeline_data.json</code>.</p>
  </div>
</body>
</html>
```


---

## 2026-06-13 — Slide 06 retired: "Where the timeline comes from"

The MIDI-genealogy FIGURE was moved to slide 04 "Descriptive findings" (below the timeline), and
slide 06 became **Conceptual discussion**. The genealogy.svg asset is still in use (now on slide 04).
The prose below (siblings-not-parent-child framing; FMOD/Wwise one-liners; the "inherited twice →
guided rail" critique) is preserved here in case it wants a future kiosk.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Where the timeline comes from</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(17px,2.15vw,27px);line-height:1.45;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .7em}
  h1{font-size:clamp(28px,4.6vw,46px);line-height:1.08;margin:0 0 .4em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.22em;display:inline-block}
  p{margin:.55em 0}
  ul{padding-left:1.15em;margin:.6em 0}
  li{margin:.45em 0}
  li::marker{color:var(--accent)}
  strong{font-weight:700}
  .box{background:var(--card);border-left:6px solid var(--accent);border-radius:0 10px 10px 0;
       padding:.8em 1.05em;margin:.9em 0;box-shadow:0 1px 0 var(--rule)}
  figure{margin:1em 0 0}
  .card{background:var(--card);border:1px solid var(--rule);border-radius:10px;padding:10px;
        overflow:auto;-webkit-overflow-scrolling:touch;max-height:62vh}
  .card img{width:1054px;max-width:none;height:auto;display:block;border-radius:4px}
  figcaption{color:var(--soft);font-size:.82em;margin-top:.5em;line-height:1.45}
  .src{color:var(--soft);font-size:.72em;margin-top:1.2em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">Genealogy, and the trap it sets</p>
  <h1>Where the timeline comes from</h1>

  <p class="box"><strong>FMOD &amp; Wwise and theatre cue software are siblings, not
  parent-and-child</strong> — both descend from <strong>MIDI (1983)</strong>. The busiest
  documented traffic runs <strong>games &rarr; theatre</strong>, not the reverse.</p>

  <ul>
    <li><strong>FMOD</strong> = a demoscene tracker player (1995); FMOD Studio (2012) is
        "designed like a DAW."</li>
    <li><strong>Wwise</strong> = Montréal music production, never theatre.</li>
  </ul>

  <figure>
    <div class="card">
      <img src="SourceMaterial/AUDIOGAMES/genealogy.svg" alt="...">
    </div>
    <figcaption>Four lineages feed game audio; only one is theatre — a sibling, not a parent.
    Scroll / drag to pan.</figcaption>
  </figure>

  <p class="box">The timeline is <strong>inherited twice</strong> — from the tracker playlist
  and the DAW. Linearity has deep roots; explorable space has none. So exploratory audiogames
  stay rare — and blind-accessibility often collapses into a <strong>guided rail</strong>.</p>

  <p class="src">Background study, "Audio performance control, from the theatre cue to the game
  engine." Method: a critical walkthrough (Light, Burgess &amp; Duguay, 2018) of FMOD and Wwise.</p>
</main>
</body>
</html>
```


---

## 2026-06-13 — Slide retired (deck trimmed to this chat's build): "The present chaosifier"

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The present chaosifier</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(17px,2.2vw,28px);line-height:1.45;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .7em}
  h1{font-size:clamp(28px,4.6vw,46px);line-height:1.08;margin:0 0 .4em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.22em;display:inline-block}
  h2{font-size:clamp(19px,2.4vw,25px);color:var(--accent);margin:1.2em 0 .25em}
  p{margin:.55em 0}
  ul.steps{list-style:none;margin:.7em 0;padding:0}
  ul.steps li{padding:.3em 0 .3em 1.4em;position:relative}
  ul.steps li::before{content:"\2192";position:absolute;left:0;color:var(--accent);font-weight:700}
  ul.steps b{font-weight:700}
  .pair{margin:.6em 0;padding:0;list-style:none}
  .pair li{margin:.3em 0}
  .pair b{color:var(--accent)}
  strong{font-weight:700}
  .box{background:var(--card);border-left:6px solid var(--accent);border-radius:0 10px 10px 0;
       padding:.8em 1.05em;margin:.9em 0;box-shadow:0 1px 0 var(--rule)}
  .meta{color:var(--soft);font-size:.85em;margin-top:.9em}
  .src{color:var(--soft);font-size:.72em;margin-top:1em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">Disruption, and the long view</p>
  <h1>The present chaosifier</h1>

  <p><strong>Vibe coding</strong> as dis- or super-intermediation:</p>
  <ul class="steps">
    <li><b>CLI</b> — command-line interface</li>
    <li><b>MCP</b> — model context protocol</li>
    <li><b>Bespoke software</b> — now easy to have; architecture matters more than ever</li>
  </ul>

  <p class="box">Working with an LLM is a <strong>devising</strong> process — shaped by
  dialogue and randomness.</p>

  <h2>A longer genealogy</h2>
  <p>Treat <strong>audio as the fundamental asset</strong>:</p>
  <ul class="pair">
    <li><b>Storytelling</b> predates <b>writing</b>.</li>
    <li><b>Audio recording</b> predates <b>video recording</b>.</li>
  </ul>

  <p class="meta">(This room is itself an instance: a build-free, vibe-coded isometric poster.)</p>

  <p class="src">From the talk notes.</p>
</main>
</body>
</html>

```


---

## 2026-06-13 — Slide retired (deck trimmed to this chat's build): "Audio-led games"

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Audio-led games</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(17px,2.15vw,27px);line-height:1.45;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.64em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .7em}
  h1{font-size:clamp(28px,4.6vw,46px);line-height:1.08;margin:0 0 .4em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.22em;display:inline-block}
  h2{font-size:clamp(19px,2.4vw,25px);margin:1.1em 0 .2em}
  h2 em{font-style:italic}
  p{margin:.5em 0}
  ul{padding-left:1.15em;margin:.45em 0}
  li{margin:.35em 0}
  li::marker{color:var(--accent)}
  strong{font-weight:700}
  a{color:var(--accent);text-decoration:underline}
  .btn{display:inline-block;background:var(--accent);color:#fff;font-weight:700;
       padding:.5em 1em;border-radius:9px;text-decoration:none;margin:.3em 0 .5em}
  .caveat{background:var(--card);border-left:6px solid var(--accent);border-radius:0 10px 10px 0;
          padding:.65em 1em;margin:.6em 0;font-size:.9em;box-shadow:0 1px 0 var(--rule)}
  .src{color:var(--soft);font-size:.72em;margin-top:1.1em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">Two examples</p>
  <h1>Audio-led games</h1>

  <h2>1 · Clod Bathos, <em>Superior Machine</em></h2>
  <p><a class="btn" href="https://mreidhorrigan.github.io/Clod-Bathos-Superior-Machine-An-LM-IDN/"
        target="_blank" rel="noopener">Play in the browser &nearr;</a></p>
  <ul>
    <li>A text-based, stylized <strong>command-line game</strong> — successor to
        choose-your-own-adventure and IDN.</li>
    <li><strong>Twine, disintermediated:</strong> adds LLM runtime rewording and state-machine
        navigation. Immersion by matching diegetic and delivery media — both screens.</li>
  </ul>
  <p class="caveat"><strong>Caveat:</strong> locally-runnable LLMs aren't yet smart enough to
  carry it alone.</p>

  <h2>2 · Autofac: <em>Rad Shipping</em></h2>
  <ul>
    <li>Navigate a lights-out <strong>“darkfactory”</strong> as a robot moving in the dark.</li>
    <li><strong>Horror:</strong> the robot inherits a work environment shaped by the human
        workers' abuse — and the place is irradiated (it needs a task timer).</li>
    <li>Sound carries <strong>navigation, interface, and story</strong>.</li>
  </ul>

  <p class="src">From the talk notes (Autofac is work in progress).</p>
</main>
</body>
</html>

```


---

## 2026-06-13 — Slide retired (deck trimmed to this chat's build): "References & links"

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>References &amp; links</title>
<style>
  :root{--bg:#fbf9f4;--ink:#16161a;--soft:#44444d;--rule:#ddd7c9;--accent:#0a5247;--card:#fff}
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);
       font-family:Verdana,Tahoma,Geneva,"DejaVu Sans",sans-serif;
       font-size:clamp(15px,1.7vw,23px);line-height:1.45;
       -webkit-text-size-adjust:100%;padding:clamp(22px,4vw,52px)}
  main{max-width:min(64rem,92vw);margin:0 auto}
  .kicker{color:var(--accent);font-size:.66em;letter-spacing:.1em;text-transform:uppercase;font-weight:700;margin:0 0 .6em}
  h1{font-size:clamp(26px,4.2vw,42px);line-height:1.08;margin:0 0 .35em;font-weight:700;
     border-bottom:5px solid var(--accent);padding-bottom:.2em;display:inline-block}
  h2{font-size:1.05em;color:var(--accent);margin:1.2em 0 .35em}
  p{margin:.55em 0}
  ul{padding-left:1.1em;margin:.45em 0}
  li{margin:.4em 0}
  li::marker{color:var(--accent)}
  em{font-style:italic}
  a{color:var(--accent);text-decoration:underline;word-break:break-word}
  .btn{display:inline-block;background:var(--accent);color:#fff;font-weight:700;
       padding:.5em 1em;border-radius:9px;text-decoration:none;margin:.3em 0 .2em}
  .src{color:var(--soft);font-size:.82em;margin-top:1.4em;border-top:1px solid var(--rule);padding-top:.7em}
</style>
</head>
<body>
<main>
  <p class="kicker">Bibliography</p>
  <h1>References &amp; links</h1>

  <p><a class="btn" href="https://mreidhorrigan.github.io/Clod-Bathos-Superior-Machine-An-LM-IDN/"
        target="_blank" rel="noopener">Play <em>Clod Bathos, Superior Machine</em> &nearr;</a></p>

  <h2>Works cited</h2>
  <ul>
    <li>DeadeyeJediBob (2024). <em>Guy Born Blind Plays The Last of Us Part I.</em>
        <a href="https://www.youtube.com/watch?v=ndodaE6OlSk" target="_blank" rel="noopener">YouTube</a>.</li>
    <li>Ford-Williams, G., et al. (n.d.). <em>Game Accessibility Guidelines.</em>
        <a href="https://gameaccessibilityguidelines.com/full-list/" target="_blank" rel="noopener">gameaccessibilityguidelines.com</a>.</li>
    <li>Fritsch, J., et al. (2025). “Towards a Framework for Exploring Synthetic Voices in VUI
        Design.” <em>DIS '25</em>, 724–739.
        <a href="https://doi.org/10.1145/3715336.3735729" target="_blank" rel="noopener">doi.org/10.1145/3715336.3735729</a>.</li>
    <li>IGDA GASIG (2023). <em>The Audio Description of Mortal Kombat 1.</em>
        <a href="https://www.youtube.com/watch?v=tZ1H2RXuCCA" target="_blank" rel="noopener">YouTube</a>.</li>
    <li>Kirke, A. (2018). “When the Soundtrack Is the Game.” In <em>Emotion in Video Game
        Soundtracking</em>, 65–83.
        <a href="https://doi.org/10.1007/978-3-319-72272-6_7" target="_blank" rel="noopener">doi.org/10.1007/978-3-319-72272-6_7</a>.</li>
    <li>Light, B., Burgess, J., &amp; Duguay, S. (2018). “The walkthrough method.”
        <em>New Media &amp; Society</em>, 20(3), 881–900.
        <a href="https://doi.org/10.1177/1461444816675438" target="_blank" rel="noopener">doi.org/10.1177/1461444816675438</a>.</li>
    <li>Swift, S. (2020). “FMOD, an Audio Engine for Video Games, Adapted for Theater.” USITT.</li>
    <li>Land, M. Z., &amp; McConnell, P. N. (1994). <em>US Patent 5,315,057</em> (iMUSE).
        <a href="https://patents.google.com/patent/US5315057A/en" target="_blank" rel="noopener">patents.google.com</a>.</li>
  </ul>

  <p class="src">Background research catalogued in Zotero (<em>CLAUDE_AUDIOGAMES</em>, 41 items);
  figures generated from <code>timeline_data.json</code>. · “Minimum viable soundscapes” ·
  Matt Horrigan · CGSA 2026.</p>
</main>
</body>
</html>

```
