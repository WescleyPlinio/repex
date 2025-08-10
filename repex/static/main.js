document.addEventListener('DOMContentLoaded', () => {
  const track = document.getElementById('cardTrack');
  const items = Array.from(track.children);
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');

  let index = 0;
  let visible = 2.5;     // número de "cards" visíveis (2 completos + 0.5)
  let maxIndex = 0;

  function recalc() {
    // adapta visible para mobile
    if (window.innerWidth < 768) visible = 1.25; else visible = 2.5;

    // calcula máximo de index que ainda deixa conteúdo à direita (ceil)
    maxIndex = Math.max(0, items.length - Math.ceil(visible));

    // força index válido
    if (index > maxIndex) index = maxIndex;
    updateButtons();
    move();
  }

  function move() {
    // largura real do item (inclui padding/box-sizing)
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
  // inicializa
  recalc();
});