document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.carousel-shell').forEach(shell => {
    const track = shell.querySelector('.carousel-track');
    if (!track) return;

    const items = Array.from(track.children);
    const prevBtn = shell.querySelector('.carousel-prev');
    const nextBtn = shell.querySelector('.carousel-next');

    let index = 0;
    let visible = 2.5;
    let maxIndex = 0;

    function recalc() {
      visible = window.innerWidth < 768 ? 1.25 : 2.5;

      maxIndex = Math.max(0, items.length - Math.ceil(visible));

      // força index válido
      if (index > maxIndex) index = maxIndex;
      updateButtons();
      move();
    }

    function move() {
      const itemWidth = items[0]?.getBoundingClientRect().width || 0;
      const translateX = index * itemWidth;
      track.style.transform = `translateX(-${translateX}px)`;
    }

    function updateButtons() {
      prevBtn.style.visibility = index > 0 ? 'visible' : 'hidden';
      nextBtn.style.visibility = index < maxIndex ? 'visible' : 'hidden';
    }

    prevBtn.addEventListener('click', () => {
      index = Math.max(0, index - 1);
      move();
      updateButtons();
    });

    nextBtn.addEventListener('click', () => {
      index = Math.min(maxIndex, index + 1);
      move();
      updateButtons();
    });

    window.addEventListener('resize', recalc);
    recalc();
  });
});
