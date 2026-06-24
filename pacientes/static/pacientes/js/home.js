/* ── Nav mobile ── */
const hamburger = document.querySelector('.nav__hamburger');
const mobileMenu = document.getElementById('mobile-menu');

if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    const open = hamburger.getAttribute('aria-expanded') === 'true';

    hamburger.setAttribute('aria-expanded', String(!open));
    mobileMenu.setAttribute('aria-hidden', String(open));

    mobileMenu.classList.toggle('nav__mobile--open');
    hamburger.classList.toggle('nav__hamburger--open');
  });
}

/* ── Nav sticky ── */
const nav = document.getElementById('nav');

if (nav) {
  window.addEventListener(
    'scroll',
    () => {
      nav.classList.toggle('nav--scrolled', window.scrollY > 40);
    },
    { passive: true }
  );
}

/* ── Smooth scroll ── */
document.querySelectorAll('a[href^="#"]').forEach((a) => {
  a.addEventListener('click', (e) => {
    const id = a.getAttribute('href');

    if (id === '#') return;

    const target = document.querySelector(id);

    if (target) {
      e.preventDefault();

      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });

      if (
        mobileMenu &&
        hamburger &&
        mobileMenu.classList.contains('nav__mobile--open')
      ) {
        hamburger.click();
      }
    }
  });
});

/* ── Reveal on scroll ── */
if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.1,
      rootMargin: '0px 0px -60px 0px',
    }
  );

  document.querySelectorAll('.reveal').forEach((el) => {
    observer.observe(el);
  });
} else {
  document.querySelectorAll('.reveal').forEach((el) => {
    el.classList.add('revealed');
  });
}

/* ── Parallax Hero ── */
window.addEventListener(
  'scroll',
  () => {
    const scroll = window.scrollY;

    const dashboard = document.querySelector('.hero-dashboard');
    const brain = document.querySelector('.hero-brain');
    const apple = document.querySelector('.fruit--apple');
    const kiwi = document.querySelector('.fruit--kiwi');
    const avocado = document.querySelector('.fruit--avocado');
    const strawberry = document.querySelector('.fruit--strawberry');

    if (dashboard) {
      dashboard.style.transform =
        `translateY(${scroll * 0.08}px)`;
    }

    if (brain) {
      brain.style.transform =
        `translateY(${scroll * -0.15}px)`;
    }

    if (apple) {
      apple.style.transform =
        `translateY(${scroll * 0.25}px)`;
    }

    if (kiwi) {
      kiwi.style.transform =
        `translateY(${scroll * -0.18}px)`;
    }

    if (avocado) {
      avocado.style.transform =
        `translateY(${scroll * 0.12}px)`;
    }

    if (strawberry) {
      strawberry.style.transform =
        `translateY(${scroll * -0.22}px)`;
    }
  },
  { passive: true }
);