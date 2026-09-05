/* Loaded synchronously in <head> (no defer) so the saved/scheme theme is
   applied before first paint — CSP forbids inline scripts, so this is the
   CSP-correct FOUC fix. Must stay tiny: it blocks rendering by design. */
(function () {
  var theme;
  var stored = null;
  try {
    stored = localStorage.getItem("theme");
  } catch (e) {
    /* private mode or storage disabled: fall through to scheme preference */
  }
  if (stored === "light" || stored === "dark") {
    theme = stored;
  } else {
    theme = window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }
  document.documentElement.dataset.theme = theme;
  document.documentElement.style.colorScheme = theme;
  document.documentElement.classList.add("js");
})();