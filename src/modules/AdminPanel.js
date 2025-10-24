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
    
    // Initialize waves editor (for settings tab)
    this.renderWavesEditor();
    
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

  /**
   * Validate progress input - Must be integer 0-100
   */
  validateProgressInput(value) {
    // Type check
    if (typeof value !== 'number') {
      return { valid: false, error: 'Progress must be a number' };
    }
    
    // Must be integer (no decimals)
    if (!Number.isInteger(value)) {
      return { valid: false, error: 'Progress must be a whole number (0-100)' };
    }
    
    // Range check
    if (value < 0 || value > 100) {
      return { valid: false, error: 'Progress must be between 0 and 100' };
    }
    
    // NaN check
    if (isNaN(value)) {
      return { valid: false, error: 'Progress is not a valid number' };
    }
    
    return { valid: true, error: null };
  },

  /**
   * Detect transition type based on old and new progress values
   * Returns: { type, requiresPopup, celebration?, sadness? }
   */
  detectProgressTransition(oldProgress, newProgress) {
    // Validation first
    const validation = this.validateProgressInput(newProgress);
    if (!validation.valid) {
      return { type: 'INVALID', requiresPopup: true, error: validation.error };
    }
    
    // No change
    if (oldProgress === newProgress) {
      return { type: 'NONE', requiresPopup: false };
    }
    
    // START: 0 → X (where 0 < X ≤ 100)
    if (oldProgress === 0 && newProgress > 0) {
      return { type: 'START', requiresPopup: true };
    }
    
    // COMPLETION: X → 100 (where 0 ≤ X < 100)
    // Includes reaching 100 from any value, triggers celebration
    if (oldProgress < 100 && newProgress === 100) {
      return { type: 'COMPLETION', requiresPopup: true, celebration: true };
    }
    
    // REOPEN: 100 → Y (where Y < 100)
    if (oldProgress === 100 && newProgress < 100) {
      return { type: 'REOPEN', requiresPopup: true, sadness: true };
    }
    
    // RESET: X → 0 (where X > 0)
    if (oldProgress > 0 && newProgress === 0) {
      return { type: 'RESET', requiresPopup: true };
    }
    
    // INTERMEDIATE: X → Y (both between 1-99 inclusive)
    // No popup, direct apply
    if (oldProgress > 0 && oldProgress < 100 && newProgress > 0 && newProgress < 100) {
      return { type: 'UPDATE', requiresPopup: false };
    }
    
    // Unknown/invalid transition
    return { type: 'INVALID', requiresPopup: true, error: 'Invalid progress transition' };
  },

  /**
   * Show progress confirmation popup with 4 types
   * Returns promise that resolves with user choice
   */
  showProgressPopup(type, oldProgress, newProgress, app) {
    return new Promise((resolve) => {
      const backdrop = document.createElement('div');
      backdrop.style.cssText = 'position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,0.7);display:flex;align-items:center;justify-content:center;z-index:10000';
      
      const popup = document.createElement('div');
      popup.style.cssText = 'background:var(--panel);border:2px solid var(--ring);border-radius:16px;padding:24px;max-width:400px;min-width:300px;box-shadow:0 10px 40px rgba(0,0,0,0.5)';
      
      let title, message, confirmText, confirmStyle, themeColor;
      
      switch (type) {
        case 'START':
          title = '🚀 Start Activity';
          message = `Change status from 'To Be Started' to 'In Progress'? (${oldProgress}% → ${newProgress}%)`;
          confirmText = 'Start Task';
          confirmStyle = 'background:var(--primary);color:white';
          themeColor = 'var(--primary)';
          break;
          
        case 'COMPLETION':
          title = '🎉 Congratulations!';
          message = `You've completed this task! Confirm to mark as Completed? (${oldProgress}% → 100%)`;
          confirmText = 'Celebrate & Complete';
          confirmStyle = 'background:#FFD700;color:black;font-weight:bold';
          themeColor = '#FFD700';
          break;
          
        case 'REOPEN':
          title = '😢 Reopening Completed Task';
          message = `Are you sure? This will change status back to 'In Progress'. (100% → ${newProgress}%)`;
          confirmText = 'Reopen Task';
          confirmStyle = 'background:var(--text);color:var(--bg);opacity:0.8';
          themeColor = 'var(--text)';
          break;
          
        case 'RESET':
          title = '⚠️ Reset Activity to Zero';
          message = `This will mark the task as 'Not Started' and remove all progress. (${oldProgress}% → 0%)`;
          confirmText = 'Reset to Zero';
          confirmStyle = 'background:#FF9500;color:white';
          themeColor = '#FF9500';
          break;
          
        default:
          resolve(false);
          return;
      }
      
      popup.innerHTML = `
        <div style="border-bottom:3px solid ${themeColor};margin-bottom:16px;padding-bottom:12px">
          <h3 style="margin:0;color:var(--text);font-size:20px">${title}</h3>
          <p style="margin:8px 0 0 0;color:var(--text);opacity:0.7;font-size:14px;font-weight:normal">App: <strong>${app.name}</strong></p>
        </div>
        <p style="color:var(--text);margin:16px 0;line-height:1.5">${message}</p>
        <div style="display:flex;gap:12px;margin-top:24px;justify-content:flex-end">
          <button id="popupCancel" style="padding:8px 16px;border:1px solid var(--ring);background:transparent;color:var(--text);border-radius:8px;cursor:pointer;font-size:14px">Cancel</button>
          <button id="popupConfirm" style="padding:8px 16px;border:none;${confirmStyle};border-radius:8px;cursor:pointer;font-size:14px;font-weight:bold">✓ ${confirmText}</button>
        </div>
      `;
      
      backdrop.appendChild(popup);
      document.body.appendChild(backdrop);
      
      const cleanup = () => {
        backdrop.remove();
      };
      
      popup.querySelector('#popupCancel').addEventListener('click', () => {
        cleanup();
        resolve(false);
      });
      
      popup.querySelector('#popupConfirm').addEventListener('click', () => {
        cleanup();
        resolve(true);
      });
      
      // Click backdrop to cancel
      backdrop.addEventListener('click', (e) => {
        if (e.target === backdrop) {
          cleanup();
          resolve(false);
        }
      });
      
      // ESC to cancel
      const escHandler = (e) => {
        if (e.key === 'Escape') {
          document.removeEventListener('keydown', escHandler);
          cleanup();
          resolve(false);
        }
      };
      document.addEventListener('keydown', escHandler);
    });
  },

  /**
   * Handle progress cell edit - orchestrates validation, popup, and save
   */
  async onProgressEdit(appId, newProgressValue) {
    const app = Dashboard.StorageManager.getApps().find(a => a.id === appId);
    if (!app) {
      Dashboard.UIController.showToast('App not found', 'error');
      return;
    }
    
    const oldProgress = app.progress || 0;
    const newProgress = parseInt(newProgressValue, 10);
    
    // Validate input
    const validation = this.validateProgressInput(newProgress);
    if (!validation.valid) {
      Dashboard.UIController.showToast(`❌ ${validation.error}`, 'error');
      return;
    }
    
    // Detect transition type
    const transition = this.detectProgressTransition(oldProgress, newProgress);
    
    // Handle invalid transition
    if (transition.type === 'INVALID') {
      Dashboard.UIController.showToast(`❌ ${transition.error || 'Invalid progress change'}`, 'error');
      return;
    }
    
    // Handle NONE (no change)
    if (transition.type === 'NONE') {
      Dashboard.UIController.showToast('Progress unchanged', 'info');
      return;
    }
    
    // For transitions that require popup
    if (transition.requiresPopup) {
      const confirmed = await this.showProgressPopup(transition.type, oldProgress, newProgress, app);
      if (!confirmed) {
        Dashboard.UIController.showToast('Progress change cancelled', 'info');
        this.renderAppsEditor(); // Refresh to reset input
        return;
      }
    }
    
    // Calculate new status based on transition
    let newStatus = app.status;
    if (transition.type === 'START') {
      newStatus = 'WIP';
    } else if (transition.type === 'COMPLETION') {
      newStatus = 'CLO';
    } else if (transition.type === 'REOPEN') {
      newStatus = 'WIP';
    } else if (transition.type === 'RESET') {
      newStatus = 'TBS';
    } else if (transition.type === 'UPDATE') {
      // Keep existing status (should be WIP)
      newStatus = 'WIP';
    }
    
    // Apply changes
    const updates = {
      progress: newProgress,
      status: newStatus,
      updatedAt: new Date().toISOString(),
      updatedBy: 'Local Edit'
    };
    
    Dashboard.StorageManager.updateApp(appId, updates);
    
    // Show appropriate feedback
    let message = '';
    if (transition.type === 'START') {
      message = `✅ Task started! Progress: ${newProgress}%`;
    } else if (transition.type === 'COMPLETION') {
      message = `🏆 Task completed! Great job!`;
      // Trigger celebration animation
      Dashboard.UIController.showCelebration();
    } else if (transition.type === 'REOPEN') {
      message = `↩️ Task reopened`;
      Dashboard.UIController.showSadness();
    } else if (transition.type === 'RESET') {
      message = `🔄 Activity reset to zero`;
    } else if (transition.type === 'UPDATE') {
      message = `✅ Progress updated: ${newProgress}%`;
    }
    
    Dashboard.UIController.showToast(message, 'success');
    
    // Refresh UI
    this.renderAppsEditor();
    Dashboard.UIController.apply();
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
          <td><input type="number" min="0" max="100" value="${app.progress || 0}" onchange="Dashboard.AdminController.onProgressEdit(${app.id}, parseInt(this.value))"/></td>
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
  },
  
  /**
   * Waves CRUD Operations
   */
  renderWavesEditor() {
    const waves = Dashboard.StorageManager.getWaves();
    const container = document.querySelector('#waveEditorContainer');
    
    if (!container) return;
    
    let html = `<h3>Waves Management</h3>
      <button class="btn btn-primary" onclick="Dashboard.AdminController.newWave()" style="margin-bottom:12px">+ Add Wave</button>
      <table class="wave-table" style="width:100%;border-collapse:collapse;margin-top:12px">
        <thead style="background:rgba(91,157,255,0.1);border-bottom:2px solid var(--ring)">
          <tr>
            <th style="padding:12px;text-align:left;font-size:12px;font-weight:600;color:#aaa">ID</th>
            <th style="padding:12px;text-align:left;font-size:12px;font-weight:600;color:#aaa">Wave Name</th>
            <th style="padding:12px;text-align:left;font-size:12px;font-weight:600;color:#aaa">Apps Count</th>
            <th style="padding:12px;text-align:center;font-size:12px;font-weight:600;color:#aaa">Actions</th>
          </tr>
        </thead>
        <tbody>`;
    
    waves.forEach(wave => {
      const appCount = Dashboard.StorageManager.getApps().filter(a => a.waveId === wave.id).length;
      html += `
        <tr style="border-bottom:1px solid var(--ring);transition:background 0.2s">
          <td style="padding:12px;font-size:13px;color:var(--text)">${wave.id}</td>
          <td style="padding:12px">
            <input type="text" value="${wave.name}" onchange="Dashboard.AdminController.updateWave(${wave.id}, {name: this.value})" style="width:100%;padding:6px;background:rgba(91,157,255,0.05);border:1px solid var(--ring);border-radius:6px;color:var(--text);font-size:13px"/>
          </td>
          <td style="padding:12px;font-size:13px;color:var(--text)">${appCount}</td>
          <td style="padding:12px;text-align:center">
            ${appCount > 0 ? 
              `<button class="btn btn-sm" disabled style="opacity:0.5;cursor:not-allowed" title="Cannot delete: wave has ${appCount} app(s)">Delete</button>` :
              `<button class="btn btn-danger btn-sm" onclick="Dashboard.AdminController.deleteWave(${wave.id})">Delete</button>`
            }
          </td>
        </tr>`;
    });
    
    html += '</tbody></table>';
    html += `<div style="margin-top:16px;padding:12px;background:rgba(91,157,255,0.05);border:1px solid var(--ring);border-radius:8px;font-size:12px;color:#aaa">
      <strong>ℹ️ Total Waves:</strong> ${waves.length} | <strong>Total Apps:</strong> ${Dashboard.StorageManager.getApps().length}
    </div>`;
    
    container.innerHTML = html;
  },
  
  newWave() {
    const name = prompt('Wave name (e.g., "Wave Q4 2025"):');
    if (!name) return;
    
    try {
      Dashboard.StorageManager.addWave({ name });
      this.renderWavesEditor();
    } catch (err) {
      alert('❌ Error adding wave:\n\n' + err.message);
    }
  },
  
  updateWave(waveId, updates) {
    try {
      Dashboard.StorageManager.updateWave(waveId, updates);
      this.renderWavesEditor();
    } catch (err) {
      alert('❌ Error updating wave:\n\n' + err.message);
    }
  },
  
  deleteWave(waveId) {
    if (!confirm('Delete this wave? This action cannot be undone.')) return;
    
    try {
      Dashboard.StorageManager.deleteWave(waveId);
      this.renderWavesEditor();
    } catch (err) {
      alert('❌ Cannot delete wave:\n\n' + err.message);
    }
  }
};

// Export module for namespace compatibility
(function(app) {
  app.AdminController = AdminController;
})(window.Dashboard = window.Dashboard || {});