const header = document.querySelector('.site-header');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.main-nav a');
const revealItems = document.querySelectorAll('.reveal');

const setHeaderState = () => {
  if (!header) return;
  header.classList.toggle('scrolled', window.scrollY > 20);
};

const setNavState = (isOpen) => {
  if (!header || !navToggle) return;
  header.classList.toggle('nav-open', isOpen);
  navToggle.setAttribute('aria-expanded', String(isOpen));
};

if (navToggle) {
  navToggle.addEventListener('click', () => {
    const isOpen = header && header.classList.contains('nav-open');
    setNavState(!isOpen);
  });
}

navLinks.forEach((link) => {
  link.addEventListener('click', () => setNavState(false));
});

window.addEventListener('scroll', setHeaderState, { passive: true });
window.addEventListener('resize', () => {
  if (window.innerWidth > 980) {
    setNavState(false);
  }
});

setHeaderState();

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.15,
  }
);

revealItems.forEach((item) => revealObserver.observe(item));

const pointerTarget = document.querySelector('.hero-inner');
if (pointerTarget && window.innerWidth > 768) {
  pointerTarget.addEventListener('pointermove', (event) => {
    const rect = pointerTarget.getBoundingClientRect();
    const offsetX = (event.clientX - rect.left) / rect.width - 0.5;
    const offsetY = (event.clientY - rect.top) / rect.height - 0.5;
    pointerTarget.style.transform = `translate3d(${offsetX * 10}px, ${offsetY * 8}px, 0)`;
  });

  pointerTarget.addEventListener('pointerleave', () => {
    pointerTarget.style.transform = 'translate3d(0, 0, 0)';
  });
}
