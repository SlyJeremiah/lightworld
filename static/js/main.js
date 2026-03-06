/* Light World Engineering – main.js */

// ── Scroll Reveal ─────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const reveals = document.querySelectorAll('.reveal');
  if (!reveals.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          // Stagger siblings slightly
          const siblings = Array.from(entry.target.parentElement?.querySelectorAll('.reveal:not(.visible)') || []);
          const delay = siblings.indexOf(entry.target) * 80;
          setTimeout(() => entry.target.classList.add('visible'), delay);
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  );

  reveals.forEach(el => observer.observe(el));
});

// ── Active nav link ───────────────────────────────────────────
(function () {
  const path = window.location.pathname;
  document.querySelectorAll('.lw-nav-link').forEach(link => {
    if (link.getAttribute('href') === path ||
        (path.startsWith(link.getAttribute('href')) && link.getAttribute('href') !== '/')) {
      link.classList.add('text-warning');
    }
  });
})();

// ── Smooth navbar background on scroll ───────────────────────
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.lw-navbar');
  if (!nav) return;
  if (window.scrollY > 60) {
    nav.style.background = 'rgba(6,14,26,0.98)';
  } else {
    nav.style.background = 'rgba(10,22,40,0.95)';
  }
}, { passive: true });
