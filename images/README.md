# images/  (raw input — optional)

Drop your slide images here with **any names** (e.g. exported from your deck).
Then run:

```bash
python3 import_images.py
```

That copies them — in **alphabetical order** — into `../slides/` with an ordering
prefix that keeps the descriptive name (`introduction.png` → `01_introduction.png`,
shown in-game as **“Introduction”**), and rebuilds `../slides.js`.

Your originals here are never modified. If you'd rather manage `slides/`
directly, you can skip this folder entirely and just put files in `slides/`,
then run `python3 build_slides.py`.
