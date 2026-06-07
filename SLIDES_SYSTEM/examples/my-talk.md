---
title: Walkable Posters
theme: isometric
paginate: true
---

<!-- _class: lead -->

# Walkable Posters

## Turning a paper poster into a game you can stroll through

A worked example deck — edit this file, run `md2deck.py`, walk in.

<!-- Speaker note: breathe, smile, point at the ghost. (Notes never render.) -->

---

## What you'll see

- **Markdown in, a slideshow kiosk out** — one self-contained `.html`
- Walk the room, open this kiosk, then arrow through the slides
- Works offline from `file://`; no Node, no build step
- Re-themeable with a tiny CSS file

---

## The problem

Conference posters are static. People glance and move on.

> "A poster you can *walk inside* invites people to stay, explore, and ask
> better questions."

So we render the talk as an isometric room and let visitors browse.

---

## The method

1. Author slides as plain Markdown (this file)
2. `md2deck.py` splits on `---` and lays each slide out beautifully
3. The deck lands in `slides/` as **one kiosk** in the room
4. `build_slides.py` picks it up — nothing else to wire

Inline niceties: `code`, **bold**, _italic_, ~~struck~~, and [links](https://marp.app).

---

## A little code

```python
def greet(name: str) -> str:
    # fenced code keeps its spacing & is syntax-safe
    return f"hello, {name} <welcome>"

print(greet("visitor"))
```

---

## Results at a glance

| Metric            | Before | After |
|:------------------|:------:|------:|
| Time at poster    |  20 s  |  95 s |
| Questions asked   |   1    |   6   |
| "That's cool!" 🎉 |  rare  | often |

---

<!-- _class: invert -->

# One idea per slide

Big, calm, legible — even on a tiny kiosk screen.

---

<!-- _class: center -->

## Thanks for walking through

Find the source & build instructions in **SLIDES_SYSTEM/** ·
press **C** to change your ghost · enjoy the room.
