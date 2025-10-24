/* ========== UI Controller Module ========== */
const UIController = {
  state: { q: '', status: 'all', sort: 'progress', theme: 'dark', pinned: null },

  init() {
    this.setupEventListeners();
    this.apply();
  },

  setupEventListeners() {
    // Controls
    document.querySelector('#q').addEventListener('input', e => {
      this.state.q = e.target.value;
      this.apply();
    });

    document.querySelector('#status').addEventListener('change', e => {
      this.state.status = e.target.value;
      this.apply();
    });

    Array.from(document.querySelectorAll('button[data-sort]')).forEach(b => b.addEventListener('click', e => {
      this.state.sort = e.target.dataset.sort;
      this.apply();
    }));

    document.querySelector('#theme').addEventListener('change', e => {
      const theme = e.target.checked ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', theme);
      this.state.theme = theme;
      this.apply();
    });

    document.querySelector('#cinema').addEventListener('click', () => document.body.classList.toggle('cinematic'));
    document.querySelector('#exitCinema').addEventListener('click', () => {
      document.body.classList.remove('cinematic');
    });

    document.addEventListener('keydown', (ev) => {
      if (ev.key === '/' && document.activeElement.id !== 'q') {
        ev.preventDefault();
        document.querySelector('#q').focus();
      }
      if (ev.key === 'Enter' && document.activeElement.id === 'q') {
        ev.preventDefault();
        document.querySelector('#q').value = '';
        this.state.q = '';
        this.apply();
      }
      if (ev.key === 's') {
        this.state.sort = (this.state.sort === 'name' ? 'progress' : 'name');
        this.apply();
      }
      if (ev.key === 'x') {
        document.body.classList.toggle('cinematic');
      }
      // FIX: ESC primero limpia selección; si no hay selección, sale del modo cinemático
      if (ev.key === 'Escape') {
        if (this.state.pinned) {
          this.state.pinned = null;
          this.apply();
        } else if (document.body.classList.contains('cinematic')) {
          document.body.classList.remove('cinematic');
        }
      }
    });

    document.querySelector('#exportBars').addEventListener('click', () => this.svgToPNG(document.querySelector('#bars'), 2400, 1000, 'ranking_avance.png'));
    document.querySelector('#exportSVG').addEventListener('click', () => {
      const svg = document.querySelector('#bars').cloneNode(true);
      const sty = document.createElement('style');
      sty.textContent = `text{fill:${this.getCSS('--text')};font-family:${getComputedStyle(document.body).fontFamily}}`;
      svg.insertBefore(sty, svg.firstChild);
      const s = `<?xml version="1.0"?>` + new XMLSerializer().serializeToString(svg);
      this.download('ranking_avance.svg', s, 'image/svg+xml');
    });
    
    document.querySelector('#exportCSV').addEventListener('click', () => {
      const rows = Dashboard.DATA.map(d => `${d.name},${d.progress}`).join('\n');
      this.download('avance_por_area.csv', 'area,progress\n' + rows, 'text/csv');
    });

    // Click en hero gauge para ver apps detail
    document.querySelector('#heroGauge').addEventListener('click', () => {
      if (this.state.pinned) {
        const pinned = Dashboard.DATA.find(d => d.name === this.state.pinned);
        if (pinned) {
          const buId = Dashboard.StorageManager.getBUs().find(bu => bu.name === pinned.name)?.id;
          if (buId) {
            Dashboard.AdminController.currentBUId = buId;
            Dashboard.AdminController.openModal();
            Dashboard.AdminController.switchTab('apps');
            setTimeout(() => {
              const busSelect = document.querySelector('#appBUFilter');
              if (busSelect) busSelect.value = Dashboard.AdminController.currentBUId;
              Dashboard.AdminController.renderAppsEditor();
            }, 100);
          }
        }
      }
    });
  },

  getCSS(v) {
    return getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  },

  /**
   * Show celebration animation when task is completed (100%)
   */
  showCelebration() {
    const celebration = document.createElement('div');
    celebration.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      z-index: 9999;
    `;
    document.body.appendChild(celebration);
    
    // Create confetti particles
    for (let i = 0; i < 50; i++) {
      const confetti = document.createElement('div');
      const delay = Math.random() * 0.2;
      const duration = 2 + Math.random() * 1;
      const size = 8 + Math.random() * 8;
      const color = ['#FFD700', '#FFA500', '#FF69B4', '#00CED1', '#32CD32'][Math.floor(Math.random() * 5)];
      
      confetti.style.cssText = `
        position: absolute;
        width: ${size}px;
        height: ${size}px;
        background: ${color};
        left: ${Math.random() * 100}%;
        top: -10px;
        border-radius: 50%;
        animation: fall ${duration}s linear ${delay}s forwards;
      `;
      celebration.appendChild(confetti);
    }
    
    // Add animation keyframes if not already present
    if (!document.querySelector('#celebration-animations')) {
      const style = document.createElement('style');
      style.id = 'celebration-animations';
      style.textContent = `
        @keyframes fall {
          to {
            transform: translateY(100vh) rotateZ(360deg);
            opacity: 0;
          }
        }
      `;
      document.head.appendChild(style);
    }
    
    // Remove after animation
    setTimeout(() => celebration.remove(), 3500);
  },

  /**
   * Show sadness animation when task is reopened (100% → Y)
   */
  showSadness() {
    const sadness = document.createElement('div');
    sadness.style.cssText = `
      position: fixed;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      background: rgba(0, 0, 0, 0.8);
      color: white;
      padding: 24px 32px;
      border-radius: 12px;
      font-size: 24px;
      z-index: 9999;
      text-align: center;
      animation: fadeOut 2s ease-in-out forwards;
    `;
    sadness.textContent = '😢';
    document.body.appendChild(sadness);
    
    // Add fadeOut animation if not present
    if (!document.querySelector('#sadness-animations')) {
      const style = document.createElement('style');
      style.id = 'sadness-animations';
      style.textContent = `
        @keyframes fadeOut {
          0% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
          50% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
          100% { opacity: 0; transform: translate(-50%, -50%) scale(0.9); }
        }
      `;
      document.head.appendChild(style);
    }
    
    // Remove after animation
    setTimeout(() => sadness.remove(), 2000);
  },

  /**
   * Show toast notification (success, error, info)
   */
  showToast(message, type = 'info', duration = 3000) {
    const toastContainer = document.getElementById('toast-container') || (() => {
      const container = document.createElement('div');
      container.id = 'toast-container';
      container.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 10000;
        display: flex;
        flex-direction: column;
        gap: 10px;
        pointer-events: none;
      `;
      document.body.appendChild(container);
      return container;
    })();
    
    const toast = document.createElement('div');
    const bgColor = type === 'success' ? '#32e685' : type === 'error' ? '#ff5f7a' : '#5b9dff';
    const textColor = '#ffffff';
    
    toast.style.cssText = `
      background: ${bgColor};
      color: ${textColor};
      padding: 12px 16px;
      border-radius: 8px;
      font-size: 14px;
      font-weight: 500;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
      animation: slideIn 0.3s ease-out;
      pointer-events: auto;
      cursor: pointer;
      max-width: 300px;
      word-break: break-word;
      line-height: 1.4;
    `;
    toast.textContent = message;
    
    // Inject animation if not present
    if (!document.querySelector('#toast-animations')) {
      const style = document.createElement('style');
      style.id = 'toast-animations';
      style.textContent = `
        @keyframes slideIn {
          from {
            transform: translateX(400px);
            opacity: 0;
          }
          to {
            transform: translateX(0);
            opacity: 1;
          }
        }
        @keyframes slideOut {
          to {
            transform: translateX(400px);
            opacity: 0;
          }
        }
      `;
      document.head.appendChild(style);
    }
    
    toastContainer.appendChild(toast);
    
    // Auto-remove
    const timeout = setTimeout(() => {
      toast.style.animation = 'slideOut 0.3s ease-out forwards';
      setTimeout(() => {
        toast.remove();
        if (toastContainer.children.length === 0) {
          toastContainer.remove();
          document.getElementById('toast-container')?.remove();
        }
      }, 300);
    }, duration);
    
    // Click to dismiss
    toast.addEventListener('click', () => {
      clearTimeout(timeout);
      toast.style.animation = 'slideOut 0.3s ease-out forwards';
      setTimeout(() => {
        toast.remove();
        if (toastContainer.children.length === 0) {
          toastContainer.remove();
          document.getElementById('toast-container')?.remove();
        }
      }, 300);
    });
  },

  fmt(n) {
    return `${n.toFixed(0)}%`;
  },

  color(p) {
    if (p === 100) return this.getCSS('--ok');
    if (p === 0) return this.getCSS('--danger');
    if (p >= 50) return this.getCSS('--warn');
    return this.getCSS('--low');
  },

  filtered() {
    let arr = Dashboard.DATA.filter(d => d.name.toLowerCase().includes(this.state.q.toLowerCase()));
    if (this.state.status === 'done') arr = arr.filter(d => d.progress === 100);
    if (this.state.status === 'wip') arr = arr.filter(d => d.progress > 0 && d.progress < 100);
    if (this.state.status === 'todo') arr = arr.filter(d => d.progress === 0);

    if (this.state.sort === 'name') arr.sort((a, b) => a.name.localeCompare(b.name));
    if (this.state.sort === 'progress') arr.sort((a, b) => b.progress - a.progress || a.name.localeCompare(b.name));
    return arr;
  },

  drawHero(avg) {
    const svg = document.querySelector('#heroGauge');
    svg.innerHTML = '';
    const W = 360, H = 360, cx = W / 2, cy = H / 2, r = 130, sw = 28, C = 2 * Math.PI * r;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

    const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
    const lg = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
    lg.id = 'g';
    lg.setAttribute('x1', '0');
    lg.setAttribute('y1', '0');
    lg.setAttribute('x2', '1');
    lg.setAttribute('y2', '1');
    const stops = [['0%', '#4fd1ff'], ['50%', '#7affb3'], ['100%', '#ffd166']];
    stops.forEach(([o, c]) => {
      const s = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
      s.setAttribute('offset', o);
      s.setAttribute('stop-color', c);
      lg.appendChild(s);
    });
    const f = document.createElementNS('http://www.w3.org/2000/svg', 'filter');
    f.id = 'glow';
    f.innerHTML = '<feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>';
    defs.appendChild(lg);
    defs.appendChild(f);
    svg.appendChild(defs);

    const track = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    track.setAttribute('cx', cx);
    track.setAttribute('cy', cy);
    track.setAttribute('r', r);
    track.setAttribute('fill', 'none');
    track.setAttribute('stroke', this.getCSS('--ring'));
    track.setAttribute('stroke-width', sw);
    svg.appendChild(track);

    // grid
    for (let i = 0; i <= 10; i++) {
      const a = (i / 10) * Math.PI * 2 - Math.PI / 2, R = r + sw / 2, r2 = R + 8;
      const x1 = cx + Math.cos(a) * R, y1 = cy + Math.sin(a) * R, x2 = cx + Math.cos(a) * r2, y2 = cy + Math.sin(a) * r2;
      const L = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      L.setAttribute('x1', x1);
      L.setAttribute('y1', y1);
      L.setAttribute('x2', x2);
      L.setAttribute('y2', y2);
      L.setAttribute('stroke', this.getCSS('--grid'));
      L.setAttribute('stroke-width', (i % 5 === 0) ? 2 : 1);
      svg.appendChild(L);
    }

    const arc = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    arc.setAttribute('cx', cx);
    arc.setAttribute('cy', cy);
    arc.setAttribute('r', r);
    arc.setAttribute('fill', 'none');
    arc.setAttribute('stroke', 'url(#g)');
    arc.setAttribute('stroke-width', sw);
    arc.setAttribute('stroke-linecap', 'round');
    arc.setAttribute('transform', `rotate(-90 ${cx} ${cy})`);
    const target = C * (1 - avg / 100);
    const t0 = performance.now();
    const dur = 800;
    function step(t) {
      const k = Math.min(1, (t - t0) / dur);
      const ease = .5 * (1 - Math.cos(Math.PI * k));
      arc.setAttribute('stroke-dasharray', `${C} ${C}`);
      arc.setAttribute('stroke-dashoffset', target + (C - target) * (1 - ease));
      requestAnimationFrame(step);
    }
    arc.setAttribute('filter', 'url(#glow)');
    svg.appendChild(arc);

    const comet = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
    comet.setAttribute('r', '6');
    comet.setAttribute('fill', '#ffffff');
    comet.setAttribute('opacity', '.9');
    svg.appendChild(comet);

    function step2() {
      const ang = -Math.PI / 2 + 2 * Math.PI * (avg / 100);
      const rr = r;
      const x = cx + Math.cos(ang) * rr, y = cy + Math.sin(ang) * rr;
      comet.setAttribute('cx', x);
      comet.setAttribute('cy', y);
      requestAnimationFrame(step2);
    }
    requestAnimationFrame(step);
    requestAnimationFrame(step2);
  },

  orbTile(d) {
    const wrap = document.createElement('div');
    wrap.className = 'tile';
    wrap.dataset.name = d.name;
    wrap.dataset.progress = d.progress;

    const svgNS = 'http://www.w3.org/2000/svg';
    const svg = document.createElementNS(svgNS, 'svg');
    svg.setAttribute('viewBox', '0 0 100 100');
    svg.setAttribute('class', 'orb');

    const defs = document.createElementNS(svgNS, 'defs');
    const g = document.createElementNS(svgNS, 'linearGradient');
    g.id = 'g-' + d.name.replace(/\W/g, '');
    g.setAttribute('x1', '0');
    g.setAttribute('y1', '0');
    g.setAttribute('x2', '1');
    g.setAttribute('y2', '1');
    [['0%', '#5bdcff'], ['50%', this.color(Math.max(1, d.progress))], ['100%', '#ffd166']].forEach(([o, c]) => {
      const s = document.createElementNS(svgNS, 'stop');
      s.setAttribute('offset', o);
      s.setAttribute('stop-color', c);
      g.appendChild(s);
    });
    defs.appendChild(g);
    svg.appendChild(defs);

    const r = 34, cx = 50, cy = 50, sw = 10, C = 2 * Math.PI * r;
    const track = document.createElementNS(svgNS, 'circle');
    track.setAttribute('cy', cy);
    track.setAttribute('cx', cx);
    track.setAttribute('r', r);
    track.setAttribute('fill', 'none');
    track.setAttribute('stroke', this.getCSS('--ring'));
    track.setAttribute('stroke-width', sw);
    svg.appendChild(track);

    const fg = document.createElementNS(svgNS, 'circle');
    fg.setAttribute('cy', cy);
    fg.setAttribute('cx', cx);
    fg.setAttribute('r', r);
    fg.setAttribute('fill', 'none');
    fg.setAttribute('stroke', `url(#${g.id})`);
    fg.setAttribute('stroke-width', sw);
    fg.setAttribute('stroke-linecap', 'round');
    fg.setAttribute('transform', `rotate(-90 ${cx} ${cy})`);
    const target = C * (1 - d.progress / 100);
    const t0 = performance.now();
    const dur = 600 + d.progress * 2;
    function anim(t) {
      const k = Math.min(1, (t - t0) / dur);
      const ease = .5 * (1 - Math.cos(Math.PI * k));
      fg.setAttribute('stroke-dashoffset', target + (C - target) * (1 - ease));
      if (k < 1) requestAnimationFrame(anim);
    }
    fg.setAttribute('stroke-dasharray', `${C} ${C}`);
    svg.appendChild(fg);
    requestAnimationFrame(anim);

    const sat = document.createElementNS(svgNS, 'circle');
    sat.setAttribute('r', '3');
    sat.setAttribute('fill', '#fff');
    svg.appendChild(sat);
    function anim2() {
      const ang = -Math.PI / 2 + 2 * Math.PI * (d.progress / 100);
      const x = cx + Math.cos(ang) * r, y = cy + Math.sin(ang) * r;
      sat.setAttribute('cx', x);
      sat.setAttribute('cy', y);
      requestAnimationFrame(anim2);
    }
    requestAnimationFrame(anim2);

    const info = document.createElement('div');
    info.innerHTML = `<div class="name">${d.name}</div><div class="meta">${d.progress}%</div>`;
    const spot = document.createElement('div');
    spot.className = 'spot';
    wrap.appendChild(svg);
    wrap.appendChild(info);
    wrap.appendChild(spot);

    wrap.addEventListener('mouseenter', () => this.spotlight(d.name, true));
    wrap.addEventListener('mouseleave', () => this.spotlight(d.name, false));
    wrap.addEventListener('click', () => {
      this.state.pinned = (this.state.pinned === d.name ? null : d.name);
      this.apply();
    });

    return wrap;
  },

  spotlight(name, on) {
    if (this.state.pinned) return; // si hay selección, ignorar hover
    Array.from(document.querySelectorAll('#tiles .tile')).forEach(t => {
      t.style.opacity = on ? (t.dataset.name === name ? '1' : '.25') : '1';
    });
  },

  drawBars(items) {
    const svg = document.querySelector('#bars');
    svg.innerHTML = '';
    const W = 1100, H = 460, M = { t: 40, r: 24, b: 40, l: 150 };
    const w = W - M.l - M.r, h = H - M.t - M.b;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

    // grid + etiquetas
    for (let i = 0; i <= 10; i++) {
      const x = M.l + (i / 10) * w;
      const L = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      L.setAttribute('x1', x);
      L.setAttribute('y1', M.t);
      L.setAttribute('x2', x);
      L.setAttribute('y2', M.t + h);
      L.setAttribute('stroke', this.getCSS('--grid'));
      L.setAttribute('stroke-width', (i % 2 === 0) ? 2 : 1);
      svg.appendChild(L);

      const T = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      T.setAttribute('x', x);
      T.setAttribute('y', M.t - 10);
      T.setAttribute('text-anchor', 'middle');
      T.setAttribute('font-size', '11');
      T.textContent = (i * 10) + '%';
      T.setAttribute('fill', this.getCSS('--text'));
      svg.appendChild(T);
    }

    const barH = Math.min(26, h / items.length - 10);
    items.forEach((d, i) => {
      const y = M.t + i * (barH + 10);

      const lab = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      lab.setAttribute('x', M.l - 12);
      lab.setAttribute('y', y + barH / 2);
      lab.setAttribute('text-anchor', 'end');
      lab.setAttribute('dominant-baseline', 'middle');
      lab.setAttribute('font-size', '13');
      lab.textContent = d.name;
      lab.setAttribute('fill', this.getCSS('--text'));
      svg.appendChild(lab);

      const track = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      track.setAttribute('x', M.l);
      track.setAttribute('y', y);
      track.setAttribute('width', w);
      track.setAttribute('height', barH);
      track.setAttribute('rx', '8');
      track.setAttribute('fill', this.getCSS('--ring'));
      svg.appendChild(track);

      const defs = svg.querySelector('defs') || document.createElementNS('http://www.w3.org/2000/svg', 'defs');
      if (!svg.querySelector('defs')) svg.appendChild(defs);
      const gid = 'gb' + i;
      const gr = document.createElementNS('http://www.w3.org/2000/svg', 'linearGradient');
      gr.id = gid;
      gr.setAttribute('x1', '0');
      gr.setAttribute('y1', '0');
      gr.setAttribute('x2', '1');
      gr.setAttribute('y2', '0');
      [['0%', this.color(Math.max(1, d.progress))], ['100%', '#ffd166']].forEach(([o, c]) => {
        const s = document.createElementNS('http://www.w3.org/2000/svg', 'stop');
        s.setAttribute('offset', o);
        s.setAttribute('stop-color', c);
        gr.appendChild(s);
      });
      defs.appendChild(gr);

      const bar = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      bar.setAttribute('x', M.l);
      bar.setAttribute('y', y);
      bar.setAttribute('width', '0');
      bar.setAttribute('height', barH);
      bar.setAttribute('fill', `url(#${gid})`);
      bar.style.filter = 'drop-shadow(0 2px 10px rgba(0,0,0,.2))';
      bar.dataset.target = w * d.progress / 100;
      svg.appendChild(bar);

      const gloss = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      gloss.setAttribute('x', M.l);
      gloss.setAttribute('y', y);
      gloss.setAttribute('width', '0');
      gloss.setAttribute('height', Math.max(2, barH * 0.35));
      gloss.setAttribute('rx', '6');
      gloss.setAttribute('fill', '#fff');
      gloss.setAttribute('opacity', '0.18');
      svg.appendChild(gloss);

      const v = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      v.setAttribute('x', M.l + 4);
      v.setAttribute('y', y + barH / 2);
      v.setAttribute('dominant-baseline', 'middle');
      v.setAttribute('font-size', '12');
      v.setAttribute('fill', this.getCSS('--text'));
      v.textContent = this.fmt(d.progress);
      svg.appendChild(v);
    });

    // ✅ FIX: seleccionar solo las barras animables por su data-attribute
    const bars = Array.from(svg.querySelectorAll('rect[data-target]'));
    const glosses = Array.from(svg.querySelectorAll('rect[rx="6"]'));
    bars.forEach((el, idx) => {
      const target = +el.dataset.target;
      const t0 = performance.now();
      const dur = 600;
      function step(t) {
        const k = Math.min(1, (t - t0) / dur);
        const ease = 1 - Math.pow(1 - k, 3);
        const w = target * ease;
        el.setAttribute('width', w);
        if (glosses[idx]) glosses[idx].setAttribute('width', Math.max(0, w - 6));
        if (k < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  },

  updateKPIs(items) {
    const done = items.filter(d => d.progress === 100).length;
    const wip = items.filter(d => d.progress > 0 && d.progress < 100).length;
    const todo = items.filter(d => d.progress === 0).length;
    const avg = Dashboard.DATA.reduce((s, d) => s + d.progress, 0) / Dashboard.DATA.length;
    document.querySelector('#kpiDone').textContent = done;
    document.querySelector('#kpiWip').textContent = wip;
    document.querySelector('#kpiTodo').textContent = todo;
    document.querySelector('#kpiAvg').textContent = avg.toFixed(2) + '%';
  },

  renderTiles(items) {
    const box = document.querySelector('#tiles');
    box.innerHTML = '';
    items.forEach(d => box.appendChild(this.orbTile(d))); // posiciones fijas
    if (this.state.pinned) {
      Array.from(document.querySelectorAll('#tiles .tile')).forEach(t => t.style.opacity = (t.dataset.name === this.state.pinned ? '1' : '.18'));
    }
  },

  apply() {
    // Actualizar DATA desde storage con progreso calculado
    const enhancedData = Dashboard.ProgressCalculator.getEnhancedDATA();
    for (let i = 0; i < enhancedData.length; i++) {
      if (Dashboard.DATA[i]) Dashboard.DATA[i].progress = enhancedData[i].progress;
    }
    const items = this.filtered();
    const avgGlobal = Dashboard.DATA.reduce((s, d) => s + d.progress, 0) / Dashboard.DATA.length;
    let heroValue = avgGlobal;
    let heroText = 'Avg';
    if (this.state.pinned) {
      const sel = Dashboard.DATA.find(d => d.name === this.state.pinned);
      if (sel) {
        heroValue = sel.progress;
        heroText = sel.name;
      }
    }
    this.drawHero(heroValue);
    document.querySelector('#heroPct').textContent = this.fmt(heroValue);
    document.querySelector('#heroCaption').textContent = heroText;

    this.renderTiles(items);
    this.drawBars(items);
    this.updateKPIs(items);
  },

  download(filename, text, type = 'text/plain') {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type }));
    a.download = filename;
    a.click();
    URL.revokeObjectURL(a.href);
  },

  svgToPNG(svgEl, w = 2200, h = 920, filename = 'chart.png') {
    const svg = new XMLSerializer().serializeToString(svgEl);
    const img = new Image();
    img.onload = function() {
      const c = document.createElement('canvas');
      c.width = w;
      c.height = h;
      const ctx = c.getContext('2d');
      ctx.fillStyle = UIController.getCSS('--bg');
      ctx.fillRect(0, 0, w, h);
      ctx.drawImage(img, 0, 0, w, h);
      c.toBlob(b => {
        const a = document.createElement('a');
        a.href = URL.createObjectURL(b);
        a.download = filename;
        a.click();
        URL.revokeObjectURL(a.href);
      }, 'image/png');
    };
    img.src = 'data:image/svg+xml;base64,' + btoa(unescape(encodeURIComponent(svg)));
  }
};

// Export module for namespace compatibility
(function(app) {
  app.UIController = UIController;
})(window.Dashboard = window.Dashboard || {});