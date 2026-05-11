// Scroll-fade reveal — adds .is-visible when elements enter the viewport.
// Stagger via data-reveal-index attribute (set in CSS as --reveal-index).
// Respects prefers-reduced-motion (CSS handles the no-op).

(() => {
  const els = document.querySelectorAll(".reveal");
  if (!els.length) return;

  if (!("IntersectionObserver" in window)) {
    els.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -8% 0px" }
  );

  els.forEach((el) => {
    const idx = el.dataset.revealIndex;
    if (idx) el.style.setProperty("--reveal-index", idx);
    io.observe(el);
  });
})();
