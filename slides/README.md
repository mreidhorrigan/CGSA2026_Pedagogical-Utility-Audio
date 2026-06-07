# slides/  (the game's slide folder)

Put the files you want shown here, then run `python3 build_slides.py` to
regenerate `../slides.js`. Supported per-slide formats:

| Type  | Extensions                          | Shown as                |
|-------|-------------------------------------|-------------------------|
| image | png jpg jpeg gif webp svg avif bmp  | fitted 16:9 image       |
| pdf   | pdf                                 | scrollable document     |
| html  | html htm                            | scrollable document     |
| embed | url embed video yt                  | 16:9 iframe (file = URL)|

Ordering is a natural sort of filenames, so name them `1.png`, `2.pdf`,
`3.html`, … (or `01`, `02`, …). Titles are derived from the filenames.

**Embed a video / web page:** make a tiny text file whose contents is just a URL
— e.g. `3.url` (or `.embed` / `.yt`) holding
`https://www.youtube.com/watch?v=…` or `https://vimeo.com/…`. It shows as a 16:9
iframe; YouTube/Vimeo watch links are auto-converted to their embed form. (An
`.html` slide can *also* contain an embedded `<iframe>` — that scrolls as a
document; an `embed` slide *is* the video.)

This README is ignored by `build_slides.py` (it isn't a slide type).
