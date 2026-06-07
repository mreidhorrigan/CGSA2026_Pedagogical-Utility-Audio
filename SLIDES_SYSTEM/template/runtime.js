/* runtime.js — the tiny in-deck navigator inlined into every generated deck.
   Zero dependencies. Works inside the game's slide <iframe> AND when the deck
   .html is opened directly in a browser.

   Navigate by: ← → / PageUp PageDown / Space / Home / End (keyboard works once
   the slide is focused), the on-screen ‹ › arrows, or clicking the left/right
   edge of the slide. The deep-link hash (#3) selects a slide on load.

   NOTE on focus: while a slide is open in the game, the parent page owns the
   keyboard until you click *into* the iframe (a documented project gotcha), so
   we window.focus() on click and provide click / button navigation that never
   needs the keyboard. */
(function () {
  "use strict";
  var slides = [].slice.call(document.querySelectorAll(".slide"));
  if (!slides.length) return;

  var total = slides.length;
  var cur = document.getElementById("cur");
  var bar = document.getElementById("bar");
  var totalEl = document.getElementById("total");
  var hint = document.getElementById("hint");
  var prevBtn = document.querySelector(".nav.prev");
  var nextBtn = document.querySelector(".nav.next");
  if (totalEl) totalEl.textContent = total;

  // Standalone (deck opened on its own) vs embedded (inside the game's kiosk
  // iframe). Standalone gets the keyboard immediately and can go fullscreen;
  // embedded shows the "click to take focus" hint (a documented project gotcha).
  var embedded = true;
  try { embedded = window.self !== window.top; } catch (e) { embedded = true; }
  if (hint) {
    hint.textContent = embedded
      ? "Click the slide, then ← →  ·  or tap the edges"
      : "← → navigate  ·  F for fullscreen  ·  or tap the edges";
  }

  var idx = -1;

  function show(n) {
    n = Math.max(0, Math.min(total - 1, n));
    if (n === idx) return;
    idx = n;
    for (var i = 0; i < total; i++) slides[i].classList.toggle("active", i === idx);
    if (cur) cur.textContent = idx + 1;
    if (bar) bar.style.width = ((idx + 1) / total * 100) + "%";
    if (prevBtn) prevBtn.classList.toggle("disabled", idx === 0);
    if (nextBtn) nextBtn.classList.toggle("disabled", idx === total - 1);
    var h = "#" + (idx + 1);
    if (location.hash !== h) { try { history.replaceState(null, "", h); } catch (e) { location.hash = h; } }
  }
  function next() { show(idx + 1); }
  function prev() { show(idx - 1); }
  function dismissHint() { if (hint) hint.classList.add("gone"); }

  function toggleFullscreen() {
    var d = document, el = d.documentElement;
    var on = d.fullscreenElement || d.webkitFullscreenElement;
    var fn = on ? (d.exitFullscreen || d.webkitExitFullscreen)
               : (el.requestFullscreen || el.webkitRequestFullscreen);
    if (fn) { try { var p = fn.call(on ? d : el); if (p && p.catch) p.catch(function () {}); } catch (_) {} }
  }

  document.addEventListener("keydown", function (e) {
    switch (e.key) {
      case "ArrowRight": case "PageDown": case " ": case "Spacebar":
        next(); e.preventDefault(); break;
      case "ArrowLeft": case "PageUp":
        prev(); e.preventDefault(); break;
      case "Home": show(0); e.preventDefault(); break;
      case "End": show(total - 1); e.preventDefault(); break;
      case "f": case "F": toggleFullscreen(); e.preventDefault(); break;
      default: return;
    }
    dismissHint();
  });

  document.addEventListener("click", function (e) {
    try { window.focus(); } catch (_) {}
    if (e.target.closest && e.target.closest("a, button, .hud, .progress, .hint")) return;
    if (e.clientX < window.innerWidth * 0.3) prev(); else next();
    dismissHint();
  });

  if (prevBtn) prevBtn.addEventListener("click", function (e) { e.stopPropagation(); prev(); dismissHint(); });
  if (nextBtn) nextBtn.addEventListener("click", function (e) { e.stopPropagation(); next(); dismissHint(); });

  var start = parseInt((location.hash || "").slice(1), 10);
  show(isNaN(start) ? 0 : start - 1);
  try { window.focus(); } catch (_) {}
})();
