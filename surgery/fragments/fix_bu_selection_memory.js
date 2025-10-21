/* ========== Admin Controller Module ========== */
const AdminController = {
  currentBUId: null,
  
  init() {
    this.setupEventListeners();
    this.renderBUList();
  },
  
  setupEventListeners() {
    document.querySelector('#setupAdmin').addEventListener('click', () => this.openModal());
    document.querySelector('#closeAdminModal').addEventListener('click', () => this.closeModal());
    document.querySelector('#cancelAdminBtn').addEventListener('click', () => this.closeModal());
    document.querySelector('#saveAdminBtn').addEventListener('click', () => this.saveAndClose());
    
    // Tabs
    Array.from(document.querySelectorAll('.modal-tab')).forEach(tab => {
      tab.addEventListener('click', (e) => this.switchTab(e.target.dataset.tab));
    });
    
    // BU buttons
    document.querySelector('#newBUBtn').addEventListener('click', () => this.newBU());
    
    // App filter
    document.querySelector('#appBUFilter').addEventListener('change', (e) => {
      this.currentBUId = parseInt(e.target.value);
      this.renderAppsEditor();
    });
    
    // Settings
    document.querySelector('#exportAdminJSON').addEventListener('click', () => this.exportConfig());
    document.querySelector('#importAdminJSON').addEventListener('change', (e) => this.importConfig(e));
    document.querySelector('#clearAllDataBtn').addEventListener('click', () => this.clearAllData());
  },
  
  openModal() {
    document.querySelector('#adminModal').classList.add('active');
    this.renderBUList();
    this.renderBUFilter();
    
    // Si hay una BU seleccionada, actualizar el dropdown para reflejarla
    if (this.currentBUId) {
      const buFilter = document.querySelector('#appBUFilter');
      buFilter.value = this.currentBUId;
      
      // También marcar la tarjeta correspondiente como seleccionada
      const buCards = document.querySelectorAll('.bu-card');
      buCards.forEach(card => {
        const buId = parseInt(card.getAttribute('data-bu-id') || '0');
        if (buId === this.currentBUId) {
          card.classList.add('selected');
        }
      });
      
      // Actualizar la vista de aplicaciones
      this.renderAppsEditor();
    }
  },
  
  closeModal() {
    document.querySelector('#adminModal').classList.remove('active');
  },
  
  switchTab(tabName) {
    Array.from(document.querySelectorAll('.modal-tab')).forEach(t => t.classList.remove('active'));
    Array.from(document.querySelectorAll('.modal-tabpanel')).forEach(p => p.classList.remove('active'));
    document.querySelector('[data-tab="' + tabName + '"]').classList.add('active');
    document.querySelector('#tab-' + tabName).classList.add('active');
  },
  
  renderBUList() {
    const buses = Dashboard.StorageManager.getBUs();
    const container = document.querySelector('#buList');
    container.innerHTML = '';
    
    buses.forEach(bu => {
      const apps = Dashboard.StorageManager.getAppsByBU(bu.id);
      const progress = Dashboard.ProgressCalculator.calculateBUProgress(bu.id);
      const card = document.createElement('div');
      card.className = 'bu-card';
      // Añadir data-bu-id para facilitar la selección al reabrir el modal
      card.setAttribute('data-bu-id', bu.id);
      card.innerHTML = `
        <div class="bu-card-actions">
          <button class="bu-card-btn" title="Edit">✏️</button>
          <button class="bu-card-btn" title="Delete">🗑️</button>
        </div>
        <div class="bu-card-name">${bu.name}</div>
        <div class="bu-card-meta">${bu.domain} · ${bu.fullname}</div>
        <div class="bu-card-meta">Apps: ${apps.length} · Progress: ${progress.toFixed(1)}%</div>
      `;
      // Marcar como seleccionada si coincide con currentBUId
      if (this.currentBUId === bu.id) {
        card.classList.add('selected');
      }
      card.addEventListener('click', () => this.selectBU(bu.id, card));
      container.appendChild(card);
    });
  },