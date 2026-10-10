document.documentElement.classList.add('js');
const header = document.querySelector('.site-header');
const navToggle = document.querySelector('.nav-toggle');
const navLinks = document.querySelectorAll('.main-nav a');
const desktopQuery = window.matchMedia('(min-width: 981px)');
// Preserve the complete photo catalogue when JavaScript is unavailable.
const serviceSection = document.querySelector('.services');
const serviceButtons = [...document.querySelectorAll('[data-service-select]')];
const servicePanels = [...document.querySelectorAll('[data-service-panel]')];
if (serviceSection && serviceButtons.length && serviceButtons.length === servicePanels.length) {
  serviceSection.classList.add('services-enhanced');
  serviceButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const selected = button.dataset.serviceSelect;
      serviceButtons.forEach((control) => control.setAttribute('aria-pressed', String(control === button)));
      servicePanels.forEach((panel) => {
        const active = panel.dataset.servicePanel === selected;
        panel.hidden = !active;
        panel.classList.toggle('preview-enter', active);
      });
    });
  });
}
function setNavState(open, restoreFocus = false) {
  if (!header || !navToggle) return;
  header.classList.toggle('nav-open', open);
  navToggle.setAttribute('aria-expanded', String(open));
  navToggle.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
  if (restoreFocus) navToggle.focus();
}
navToggle?.addEventListener('click', () => setNavState(navToggle.getAttribute('aria-expanded') !== 'true'));
navLinks.forEach((link) => link.addEventListener('click', () => {
  setNavState(false);
  if (!desktopQuery.matches) {
    const section = document.querySelector(link.hash);
    if (section) { section.setAttribute('tabindex', '-1'); section.focus({ preventScroll: true }); }
  }
}));
document.addEventListener('click', (event) => { if (header && !header.contains(event.target)) setNavState(false); });
document.addEventListener('keydown', (event) => { if (event.key === 'Escape' && header?.classList.contains('nav-open')) setNavState(false, true); });
header?.addEventListener('focusout', (event) => { if (event.relatedTarget && !header.contains(event.relatedTarget)) setNavState(false); });
desktopQuery.addEventListener('change', () => setNavState(false));
// Observe sections instead of running work on every scroll event.
if ('IntersectionObserver' in window) {
  const sections = [...navLinks].map((link) => link.hash === '#top' ? document.querySelector('.hero') : document.querySelector(link.hash)).filter(Boolean);
  const activeSections = new Set();
  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => { if (entry.isIntersecting) activeSections.add(entry.target); else activeSections.delete(entry.target); });
    const activeSection = sections.filter((section) => activeSections.has(section)).sort((a, b) => b.getBoundingClientRect().top - a.getBoundingClientRect().top)[0];
    const activeId = activeSection?.classList.contains('hero') ? 'top' : activeSection?.id;
    navLinks.forEach((link) => { if (link.hash === `#${activeId}`) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
  }, { rootMargin: '-20% 0px -65% 0px', threshold: 0 });
  sections.forEach((section) => sectionObserver.observe(section));
}
const menuDialog = document.querySelector('.menu-dialog');
const menuLink = document.querySelector('[data-menu-open]');
if (menuDialog && typeof menuDialog.showModal === 'function') {
  menuLink?.addEventListener('click', (event) => { event.preventDefault(); menuDialog.showModal(); document.body.classList.add('dialog-open'); });
  menuDialog.querySelector('.dialog-close')?.addEventListener('click', () => menuDialog.close());
  menuDialog.addEventListener('click', (event) => {
    if (event.target !== menuDialog) return;
    const bounds = menuDialog.getBoundingClientRect();
    if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) menuDialog.close();
  });
  menuDialog.addEventListener('close', () => { document.body.classList.remove('dialog-open'); menuLink?.focus({ preventScroll: true }); });
}
const studioVideo = document.querySelector('.gallery-video video');
const playButton = document.querySelector('.video-play');
if (studioVideo && playButton) {
  playButton.hidden = false;
  playButton.addEventListener('click', async () => {
    playButton.hidden = true;
    try { await studioVideo.play(); }
    catch { studioVideo.controls = true; }
  });
  studioVideo.addEventListener('play', () => { playButton.hidden = true; });
  studioVideo.addEventListener('ended', () => { playButton.hidden = false; });
  studioVideo.addEventListener('error', () => { playButton.hidden = true; });
}
