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
  
  selectBU(buId, element) {
    Array.from(document.querySelectorAll('.bu-card')).forEach(c => c.classList.remove('selected'));
    element.classList.add('selected');
    this.currentBUId = buId;
  },
  
  newBU() {
    const name = prompt('Business Unit name:');
    if (!name) return;
    Dashboard.StorageManager.addBU({
      key: name.toUpperCase().slice(0, 4),
      name,
      domain: 'CORF',
      fullname: name + ' Department'
    });
    this.renderBUList();
  },
  
  renderBUFilter() {
    const buses = Dashboard.StorageManager.getBUs();
    const select = document.querySelector('#appBUFilter');
    select.innerHTML = '<option value="">-- Select BU --</option>';
    buses.forEach(bu => {
      const opt = document.createElement('option');
      opt.value = bu.id;
      opt.textContent = bu.name;
      select.appendChild(opt);
    });
  },
  
  renderAppsEditor() {
    if (!this.currentBUId) return;
    const bu = Dashboard.StorageManager.getBUs().find(b => b.id === this.currentBUId);
    const apps = Dashboard.StorageManager.getAppsByBU(this.currentBUId);
    const container = document.querySelector('#appEditorContainer');
    
    let html = `<h3>${bu.name} Applications</h3>
      <button class="btn btn-primary" onclick="Dashboard.AdminController.newApp(${this.currentBUId})" style="margin-bottom:12px">+ Add Application</button>
      <table class="app-table">
        <thead>
          <tr>
            <th>App Name</th>
            <th>Status</th>
            <th>Progress %</th>
            <th>Weight <small>(Auto)</small></th>
            <th>Criticality</th>
            <th>Business Impact</th>
            <th>Priority</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>`;
    
    apps.forEach(app => {
      html += `
        <tr>
          <td><input type="text" value="${app.name}" onchange="Dashboard.AdminController.updateApp(${app.id}, {name: this.value})"/></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {status: this.value})">
            <option value="TBS" ${app.status === 'TBS' ? 'selected' : ''}>TBS</option>
            <option value="WIP" ${app.status === 'WIP' ? 'selected' : ''}>WIP</option>
            <option value="CLO" ${app.status === 'CLO' ? 'selected' : ''}>CLO</option>
          </select></td>
          <td><input type="number" min="0" max="100" value="${app.progress || 0}" onchange="Dashboard.AdminController.updateApp(${app.id}, {progress: parseInt(this.value)})"/></td>
          <td><span class="auto-weight">${Dashboard.ProgressCalculator.calculateAppWeight(app).toFixed(2)}</span></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {criticality: this.value})">
            <option value="Low" ${app.criticality === 'Low' ? 'selected' : ''}>Low</option>
            <option value="Medium" ${app.criticality === 'Medium' ? 'selected' : ''}>Medium</option>
            <option value="High" ${app.criticality === 'High' ? 'selected' : ''}>High</option>
          </select></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {businessImpact: this.value})">
            <option value="Low" ${app.businessImpact === 'Low' ? 'selected' : ''}>Low</option>
            <option value="Medium" ${(app.businessImpact === 'Medium' || !app.businessImpact) ? 'selected' : ''}>Medium</option>
            <option value="High" ${app.businessImpact === 'High' ? 'selected' : ''}>High</option>
          </select></td>
          <td><select onchange="Dashboard.AdminController.updateApp(${app.id}, {priority: this.value})">
            <option value="Low" ${app.priority === 'Low' ? 'selected' : ''}>Low</option>
            <option value="Medium" ${(app.priority === 'Medium' || !app.priority) ? 'selected' : ''}>Medium</option>
            <option value="High" ${app.priority === 'High' ? 'selected' : ''}>High</option>
          </select></td>
          <td><button class="btn btn-danger btn-sm" onclick="Dashboard.AdminController.deleteApp(${app.id})">Delete</button></td>
        </tr>`;
    });
    
    html += '</tbody></table>';
    container.innerHTML = html;
  },
  
  newApp(buId) {
    const name = prompt('Application name:');
    if (!name) return;
    Dashboard.StorageManager.addApp({
      buId,
      name,
      status: 'TBS',
      progress: 0,
      criticality: 'Medium',
      businessImpact: 'Medium',
      priority: 'Medium'
    });
    this.renderAppsEditor();
  },
  
  updateApp(appId, updates) {
    Dashboard.StorageManager.updateApp(appId, updates);
    this.renderAppsEditor();
    // Refresh main dashboard when weight-affecting factors change
    if (updates.criticality || updates.businessImpact || updates.priority || updates.progress) {
      Dashboard.UIController.apply();
    }
  },
  
  deleteApp(appId) {
    if (confirm('Delete this application?')) {
      Dashboard.StorageManager.deleteApp(appId);
      this.renderAppsEditor();
    }
  },
  
  exportConfig() {
    const config = Dashboard.StorageManager.loadConfig();
    
    // Enrich buses with calculated progress
    const enrichedConfig = {
      ...config,
      buses: config.buses.map(bu => ({
        ...bu,
        calculatedProgress: Dashboard.ProgressCalculator.calculateBUProgress(bu.id),
        appCount: config.apps.filter(app => app.buId === bu.id).length,
        weightedMetrics: this.calculateBUWeightedMetrics(bu.id)
      })),
      apps: config.apps.map(app => ({
        ...app,
        buName: config.buses.find(b => b.id === app.buId)?.name || 'Unknown',
        calculatedWeight: app.weight || 1,
        calculatedProgress: app.progress || 0
      })),
      exportMetadata: {
        exportedAt: new Date().toISOString(),
        version: '2.0',
        schema: 'dashboard_config_v1_enriched',
        totalBUs: config.buses.length,
        totalApps: config.apps.length,
        totalWaves: config.waves.length
      }
    };
    
    const json = JSON.stringify(enrichedConfig, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'dashboard_config_' + new Date().toISOString().slice(0, 10) + '.json';
    a.click();
    URL.revokeObjectURL(url);
  },
  
  calculateBUWeightedMetrics(buId) {
    const apps = Dashboard.StorageManager.getAppsByBU(buId);
    if (apps.length === 0) return { totalWeight: 0, weightedSum: 0, averageProgress: 0 };
    
    const totalWeight = apps.reduce((sum, app) => sum + (app.weight || 1), 0);
    const weightedSum = apps.reduce((sum, app) => sum + ((app.progress || 0) * (app.weight || 1)), 0);
    const averageProgress = totalWeight > 0 ? Math.round((weightedSum / totalWeight) * 100) / 100 : 0;
    
    return {
      totalWeight,
      weightedSum,
      averageProgress
    };
  },
  
  importConfig(event) {
    const file = event.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const importedConfig = JSON.parse(e.target.result);
        
        // Validate schema
        if (!importedConfig.buses || !importedConfig.apps || !importedConfig.waves) {
          throw new Error('Invalid configuration schema. Missing required fields: buses, apps, or waves');
        }
        
        // Extract only the essential data (remove calculated fields)
        const cleanConfig = {
          buses: importedConfig.buses.map(bu => ({
            id: bu.id,
            key: bu.key,
            name: bu.name,
            domain: bu.domain,
            fullname: bu.fullname,
            color: bu.color || '#5b9dff',
            manager: bu.manager || ''
          })),
          apps: importedConfig.apps.map(app => ({
            id: app.id,
            buId: app.buId,
            name: app.name,
            status: app.status || 'TBS',
            progress: app.progress || 0,
            weight: app.weight || 1,
            criticality: app.criticality || 'Medium'
          })),
          waves: importedConfig.waves.map(wave => ({
            id: wave.id,
            name: wave.name
          }))
        };
        
        // Validate data integrity
        const appBUIds = new Set(cleanConfig.apps.map(a => a.buId));
        const buIds = new Set(cleanConfig.buses.map(b => b.id));
        
        for (let buId of appBUIds) {
          if (!buIds.has(buId)) {
            throw new Error(`Invalid reference: app references non-existent Business Unit ID ${buId}`);
          }
        }
        
        // Save configuration
        Dashboard.StorageManager.saveConfig(cleanConfig);
        
        // Verify import
        const verifyConfig = Dashboard.StorageManager.loadConfig();
        console.log('✅ Configuration imported successfully', {
          busesCount: verifyConfig.buses.length,
          appsCount: verifyConfig.apps.length,
          wavesCount: verifyConfig.waves.length
        });
        
        alert('✅ Configuration imported successfully:\n\n' +
              `  • Business Units: ${verifyConfig.buses.length}\n` +
              `  • Applications: ${verifyConfig.apps.length}\n` +
              `  • Waves: ${verifyConfig.waves.length}`);
        
        location.reload();
      } catch (err) {
        console.error('Import error:', err);
        alert('❌ Import failed:\n\n' + err.message);
      }
    };
    reader.readAsText(file);
  },
  
  saveAndClose() {
    this.closeModal();
    Dashboard.UIController.apply();
    alert('✅ Changes saved');
  },
  
  clearAllData() {
    // Double confirmation to prevent accidents
    const confirmed = confirm('⚠️ DANGER ZONE ⚠️\n\nThis will permanently delete ALL data:\n• Business Units\n• Applications\n• Waves\n\nThis action CANNOT be undone.\n\nAre you sure?');
    
    if (!confirmed) return;
    
    const secondConfirmation = confirm('⚠️ FINAL WARNING ⚠️\n\nType OK to confirm deletion of all data.');
    if (secondConfirmation === false) return;
    
    try {
      // Mark as cleared BEFORE deletion
      Dashboard.StorageManager.markAsCleared();
      
      // Clear localStorage
      localStorage.removeItem(Dashboard.StorageManager.STORAGE_KEY);
      
      // Verify deletion
      const verification = localStorage.getItem(Dashboard.StorageManager.STORAGE_KEY);
      if (verification !== null) {
        throw new Error('Failed to clear localStorage - data still exists');
      }
      
      // Clear all cached variables
      this.currentBUId = null;
      
      console.log('✅ All data cleared successfully from localStorage');
      
      alert('✅ All data has been permanently deleted.\n\nThe dashboard will now reload with empty state (cleared data will be preserved).');
      
      // Reload after showing success message
      location.reload();
    } catch (err) {
      console.error('Clear All Data Error:', err);
      alert('❌ Error clearing data:\n\n' + err.message + '\n\nPlease try again or contact support.');
    }
  }
};

// Export module for namespace compatibility
(function(app) {
  app.AdminController = AdminController;
})(window.Dashboard = window.Dashboard || {});