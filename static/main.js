document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.carousel-shell').forEach(shell => {
    const track = shell.querySelector('.carousel-track');
    if (!track) return;

    let items = Array.from(track.children);
    const prevBtn = shell.querySelector('.carousel-prev');
    const nextBtn = shell.querySelector('.carousel-next');

    let index = 0;
    let visible = 2.5;
    let itemWidth = 0;

    const clonesBefore = items.slice(-3).map(el => el.cloneNode(true));
    const clonesAfter = items.slice(0, 3).map(el => el.cloneNode(true));

    clonesBefore.forEach(clone => track.prepend(clone));
    clonesAfter.forEach(clone => track.append(clone));

    items = Array.from(track.children);

    index = 3;

    function recalc() {
      visible = window.innerWidth < 768 ? 1.25 : 2.5;
      itemWidth = items[0]?.getBoundingClientRect().width || 0;
      move(true);
    }

    function move(skipTransition = false) {
      if (skipTransition) {
        track.style.transition = 'none';
      } else {
        track.style.transition = 'transform 0.3s ease';
      }

      const translateX = index * itemWidth;
      track.style.transform = `translateX(-${translateX}px)`;
    }

    function checkLoop() {
      if (index >= items.length - 3) {
        index = 3;
        move(true); 
      }

      if (index < 3) {
        index = items.length - 6;
        move(true); 
      }
    }

    prevBtn.addEventListener('click', () => {
      index--;
      move();
      setTimeout(checkLoop, 310);
    });

    nextBtn.addEventListener('click', () => {
      index++;
      move();
      setTimeout(checkLoop, 310);
    });

    window.addEventListener('resize', recalc);
    recalc();
  });
});
