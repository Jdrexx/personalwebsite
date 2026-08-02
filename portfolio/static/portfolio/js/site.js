(function () {
  "use strict";
  var analyticsId = document.body.dataset.analyticsId;
  if (analyticsId && /^G-[A-Z0-9]+$/.test(analyticsId)) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", analyticsId);
    var analyticsScript = document.createElement("script");
    analyticsScript.async = true;
    analyticsScript.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(analyticsId);
    document.head.appendChild(analyticsScript);
  }
  var html = document.documentElement;
  var themeButton = document.getElementById("theme-toggle");
  if (localStorage.getItem("theme") === "light") {
    html.setAttribute("data-theme", "light");
    if (themeButton) themeButton.textContent = "☀️";
  }
  if (themeButton) themeButton.addEventListener("click", function () {
    var isLight = html.getAttribute("data-theme") === "light";
    if (isLight) html.removeAttribute("data-theme"); else html.setAttribute("data-theme", "light");
    themeButton.textContent = isLight ? "🌙" : "☀️";
    localStorage.setItem("theme", isLight ? "" : "light");
  });

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var animated = document.querySelectorAll(".fade-in");
  if (reducedMotion || !("IntersectionObserver" in window)) {
    animated.forEach(function (element) { element.classList.add("visible"); });
  } else {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add("visible"); observer.unobserve(entry.target); }
      });
    }, { threshold: 0.15 });
    animated.forEach(function (element) { observer.observe(element); });
  }

  var topButton = document.getElementById("back-to-top");
  if (topButton) {
    window.addEventListener("scroll", function () { topButton.classList.toggle("visible", window.scrollY > 300); }, { passive: true });
    topButton.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: reducedMotion ? "auto" : "smooth" }); });
  }

  document.querySelectorAll(".expand-btn").forEach(function (button) {
    button.addEventListener("click", function () {
      var details = button.closest(".project-body").querySelector(".project-details");
      var expanded = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", String(!expanded));
      details.hidden = expanded;
      button.textContent = expanded ? "More details ↓" : "Less details ↑";
    });
  });

  document.querySelectorAll("[data-track]").forEach(function (element) {
    element.addEventListener("click", function () {
      if (typeof window.gtag === "function") window.gtag("event", element.dataset.track, {link_url: element.href || "", page_location: window.location.href});
    });
  });
})();
