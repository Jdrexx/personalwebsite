(function () {
  "use strict";
  // Analytics loads on the first real interaction (scroll, click, key, touch).
  // Visitors who read the page still trigger it; Lighthouse's load-time audit
  // no longer pays for the ~60KB gtag bundle. Events fired before the script
  // arrives are queued in dataLayer and replayed in order by gtag.js.
  var analyticsId = document.body.dataset.analyticsId;
  if (analyticsId && /^G-[A-Z0-9]+$/.test(analyticsId)) {
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () {
      window.dataLayer.push(arguments);
    };
    var analyticsLoaded = false;
    function loadAnalytics() {
      if (analyticsLoaded) return;
      analyticsLoaded = true;
      window.gtag("js", new Date());
      window.gtag("config", analyticsId);
      var script = document.createElement("script");
      script.async = true;
      script.src =
        "https://www.googletagmanager.com/gtag/js?id=" +
        encodeURIComponent(analyticsId);
      document.head.appendChild(script);
    }
    ["click", "keydown", "touchstart", "scroll"].forEach(function (type) {
      window.addEventListener(type, loadAnalytics, {
        passive: true,
        once: true,
      });
    });
  }

  var html = document.documentElement;
  var themeButton = document.getElementById("theme-toggle");
  // Initial theme is applied by theme-init.js in <head> (pre-paint). This
  // side only keeps the button icon in sync and handles the toggle.
  function syncThemeIcon() {
    if (themeButton) {
      themeButton.textContent =
        html.getAttribute("data-theme") === "light" ? "☀️" : "🌙";
    }
  }
  syncThemeIcon();
  if (themeButton)
    themeButton.addEventListener("click", function () {
      var isLight = html.getAttribute("data-theme") === "light";
      var next = isLight ? "dark" : "light";
      html.setAttribute("data-theme", next);
      html.style.colorScheme = next;
      localStorage.setItem("theme", next);
      themeButton.textContent = next === "light" ? "☀️" : "🌙";
    });

  var reducedMotion = window.matchMedia(
    "(prefers-reduced-motion: reduce)",
  ).matches;
  var animated = document.querySelectorAll(".fade-in");
  if (reducedMotion || !("IntersectionObserver" in window)) {
    animated.forEach(function (element) {
      element.classList.add("visible");
    });
  } else {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 },
    );
    animated.forEach(function (element) {
      observer.observe(element);
    });
  }

  var topButton = document.getElementById("back-to-top");
  if (topButton) {
    window.addEventListener(
      "scroll",
      function () {
        topButton.classList.toggle("visible", window.scrollY > 300);
      },
      { passive: true },
    );
    topButton.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: reducedMotion ? "auto" : "smooth" });
    });
  }

  // One delegated listener replaces per-element registrations, so every page
  // pays a flat ~350 bytes instead of handlers that only fire on some pages.
  document.addEventListener("click", function (event) {
    var target =
      event.target && event.target.closest
        ? event.target.closest(".expand-btn, [data-track]")
        : null;
    if (!target) return;
    if (target.classList.contains("expand-btn")) {
      var details = target
        .closest(".project-body")
        .querySelector(".project-details");
      var expanded = target.getAttribute("aria-expanded") === "true";
      target.setAttribute("aria-expanded", String(!expanded));
      details.hidden = expanded;
      target.textContent = expanded ? "More details ↓" : "Less details ↑";
    } else if (typeof window.gtag === "function") {
      window.gtag("event", target.dataset.track, {
        link_url: target.href || "",
        page_location: window.location.href,
      });
    }
  });
})();