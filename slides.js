// Manifest intentionally left EMPTY so the game falls back to its five built-in
// demo kiosks (PLACEHOLDER_SLIDES in game.js) — one kiosk per slide, for testing.
// slides/placeholder.html is untouched on disk.
//
// To restore the bundled deck (one kiosk):   python3 build_slides.py
// To get one kiosk per real slide: drop image/PDF/HTML/embed files into slides/
// (the placeholder auto-drops) and run:        python3 build_slides.py
window.SLIDES_MANIFEST = [];
