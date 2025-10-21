#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ENHANCED DASHBOARD BUILDER
Construye quirúrgicamente el dashboard mejorado con módulos de admin, localStorage, y cálculo de progreso.
"""

import os
import re

class DashboardBuilder:
    def __init__(self, html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        
        self.original_size = len(self.content)
        self.original_lines = self.content.count('\n') + 1
        self.original_chars = len(self.content)
        
        print(f'📊 BASELINE: {self.original_chars:,} chars | {self.original_lines} lines | {self.original_size:,} bytes')
    
    def insert_before_marker(self, marker, new_code, marker_name=''):
        """Inserta código ANTES de un marcador"""
        pos = self.content.find(marker)
        if pos == -1:
            raise ValueError(f'Marcador no encontrado: {marker_name or marker[:30]}...')
        self.content = self.content[:pos] + new_code + self.content[pos:]
        print(f'✅ Insertado {marker_name or "código"} ({len(new_code)} chars)')
    
    def replace_exact(self, old_str, new_str, name=''):
        """Reemplaza exactamente una sección"""
        if old_str not in self.content:
            raise ValueError(f'No encontrado: {name or old_str[:30]}...')
        self.content = self.content.replace(old_str, new_str, 1)
        delta = len(new_str) - len(old_str)
        print(f'✅ Reemplazado {name or "sección"} (delta: {delta:+d} chars)')
    
    def add_css_styles(self):
        """M3: Agrega estilos CSS para modal y componentes admin"""
        new_styles = """
    /* === ADMIN MODAL STYLES === */
    .modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.7);display:none;align-items:center;justify-content:center;z-index:9999;backdrop-filter:blur(2px)}
    .modal-overlay.active{display:flex}
    .modal-content{background:linear-gradient(180deg,var(--glass),transparent),var(--panel);border:1px solid var(--ring);border-radius:var(--radius);box-shadow:var(--shadow);max-width:900px;width:90%;max-height:85vh;overflow-y:auto;padding:24px;position:relative;animation:slideIn .3s ease}
    @keyframes slideIn{from{opacity:0;transform:translateY(-20px)}to{opacity:1;transform:translateY(0)}}
    .modal-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px;padding-bottom:12px;border-bottom:1px solid var(--ring)}
    .modal-header h2{margin:0;font-size:18px;color:var(--text)}
    .modal-close{appearance:none;background:none;border:none;color:var(--muted);font-size:24px;cursor:pointer;padding:0;width:32px;height:32px;display:flex;align-items:center;justify-content:center}
    .modal-close:hover{color:var(--text)}
    .modal-tabs{display:flex;gap:8px;margin-bottom:20px;border-bottom:1px solid var(--ring);padding-bottom:12px}
    .modal-tab{appearance:none;background:none;border:none;color:var(--muted);padding:8px 12px;cursor:pointer;border-bottom:2px solid transparent;font-size:14px;transition:.2s}
    .modal-tab.active{color:var(--primary);border-bottom-color:var(--primary)}
    .modal-tab:hover{color:var(--text)}
    .modal-tabpanel{display:none}
    .modal-tabpanel.active{display:block}
    .bu-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
    .bu-card{padding:12px;border:1px solid var(--ring);border-radius:10px;background:var(--bg-2);cursor:pointer;transition:.2s;position:relative}
    .bu-card:hover{background:var(--ring);border-color:var(--primary)}
    .bu-card.selected{border-color:var(--primary);background:var(--ring)}
    .bu-card-name{font-weight:700;margin-bottom:4px}
    .bu-card-meta{font-size:12px;color:var(--muted)}
    .bu-card-actions{position:absolute;top:8px;right:8px;display:flex;gap:4px}
    .bu-card-btn{appearance:none;background:none;border:none;color:var(--muted);cursor:pointer;font-size:16px;padding:0;width:24px;height:24px;display:flex;align-items:center;justify-content:center}
    .bu-card-btn:hover{color:var(--primary)}
    .app-table{width:100%;border-collapse:collapse;margin-top:12px}
    .app-table th{text-align:left;padding:8px;border-bottom:1px solid var(--ring);font-size:12px;color:var(--muted);font-weight:700}
    .app-table td{padding:8px;border-bottom:1px solid var(--ring);font-size:13px}
    .app-table tr:hover{background:var(--ring)}
    .app-table input[type=text],.app-table input[type=number],.app-table select{appearance:none;background:var(--bg-2);border:1px solid var(--ring);color:var(--text);padding:4px 6px;border-radius:4px;font-size:12px;width:100%}
    .app-table input:focus,.app-table select:focus{outline:none;border-color:var(--primary);box-shadow:0 0 8px rgba(91,157,255,.3)}
    .form-group{margin-bottom:16px}
    .form-group label{display:block;margin-bottom:6px;font-size:12px;color:var(--muted);font-weight:600}
    .form-group input,.form-group select,.form-group textarea{appearance:none;background:var(--bg-2);border:1px solid var(--ring);color:var(--text);padding:8px 10px;border-radius:8px;font-size:13px;width:100%;font-family:inherit}
    .form-group input:focus,.form-group select:focus,.form-group textarea:focus{outline:none;border-color:var(--primary);box-shadow:0 0 8px rgba(91,157,255,.3)}
    .form-row{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}
    .status-badge{display:inline-block;padding:3px 8px;border-radius:4px;font-size:11px;font-weight:600;text-transform:uppercase}
    .status-tbs{background:rgba(255,95,122,.2);color:var(--danger)}
    .status-wip{background:rgba(255,209,102,.2);color:var(--warn)}
    .status-clo{background:rgba(50,230,133,.2);color:var(--ok)}
    .btn-group{display:flex;gap:8px;margin-top:16px}
    .btn-primary{appearance:none;background:var(--primary);border:none;color:white;padding:10px 16px;border-radius:8px;cursor:pointer;font-weight:600;font-size:13px;transition:.2s}
    .btn-primary:hover{filter:brightness(1.1)}
    .btn-secondary{appearance:none;background:var(--bg-2);border:1px solid var(--ring);color:var(--text);padding:10px 16px;border-radius:8px;cursor:pointer;font-weight:600;font-size:13px;transition:.2s}
    .btn-secondary:hover{background:var(--ring)}
    .btn-danger{appearance:none;background:var(--danger);border:none;color:white;padding:10px 16px;border-radius:8px;cursor:pointer;font-weight:600;font-size:13px;transition:.2s}
    .btn-danger:hover{filter:brightness(1.1)}
    .btn-sm{padding:4px 8px;font-size:12px}
    """
        marker = '</style>'
        self.insert_before_marker(marker, new_styles, 'CSS Admin Modal')
    
    def add_setup_button(self):
        """M7: Agregar botón Setup en los controles"""
        old_button_group = '''        <button id="exportCSV" class="btn pill" title="Exportar CSV">CSV</button>
      </div>'''
        
        new_button_group = '''        <button id="exportCSV" class="btn pill" title="Exportar CSV">CSV</button>
        <button id="setupAdmin" class="btn pill" title="Administration">Setup</button>
      </div>'''
        
        self.replace_exact(old_button_group, new_button_group, 'Setup Button')
    
    def add_modal_html(self):
        """M3: Agregar el HTML de la modal de admin"""
        modal_html = '''
  <!-- ADMIN MODAL -->
  <div id="adminModal" class="modal-overlay">
    <div class="modal-content">
      <div class="modal-header">
        <h2>📊 Project Administration</h2>
        <button class="modal-close" id="closeAdminModal">✕</button>
      </div>
      <div class="modal-tabs">
        <button class="modal-tab active" data-tab="buses">Business Units</button>
        <button class="modal-tab" data-tab="apps">Applications</button>
        <button class="modal-tab" data-tab="settings">Settings</button>
      </div>
      
      <!-- TAB: BUSINESS UNITS -->
      <div class="modal-tabpanel active" id="tab-buses">
        <div style="margin-bottom:16px">
          <button class="btn btn-primary" id="newBUBtn">+ New Business Unit</button>
        </div>
        <div class="bu-list" id="buList"></div>
      </div>
      
      <!-- TAB: APPLICATIONS -->
      <div class="modal-tabpanel" id="tab-apps">
        <div class="form-group">
          <label>Select Business Unit</label>
          <select id="appBUFilter"></select>
        </div>
        <div id="appEditorContainer"></div>
      </div>
      
      <!-- TAB: SETTINGS -->
      <div class="modal-tabpanel" id="tab-settings">
        <h3>Global Settings</h3>
        <div class="form-group">
          <label>Export Data</label>
          <button class="btn btn-secondary" id="exportAdminJSON">📥 Export Config as JSON</button>
        </div>
        <div class="form-group">
          <label>Import Data</label>
          <input type="file" id="importAdminJSON" accept=".json" />
        </div>
        <div class="form-group">
          <label>Clear All Data</label>
          <button class="btn btn-danger" id="clearAllDataBtn">🗑️ Clear All (local storage)</button>
        </div>
      </div>
      
      <div class="btn-group" style="margin-top:24px;border-top:1px solid var(--ring);padding-top:16px">
        <button class="btn btn-primary" id="saveAdminBtn">💾 Save & Close</button>
        <button class="btn btn-secondary" id="cancelAdminBtn">Cancel</button>
      </div>
    </div>
  </div>
'''
        marker = '<script>'
        self.insert_before_marker(marker, modal_html, 'Modal HTML')
    
    def add_storage_module(self):
        """M1: localStorage Manager"""
        storage_code = '''
    /* ========== M1: STORAGE MANAGER ========== */
    const StorageManager = {
      STORAGE_KEY: 'dashboard_config_v1',
      
      init() {
        // Si no hay datos en localStorage, inicializar desde DATA
        if (!localStorage.getItem(this.STORAGE_KEY)) {
          this.saveConfig({
            buses: DATA.map((d, i) => ({
              id: i + 1,
              key: d.key,
              name: d.name,
              domain: 'CORF',
              fullname: d.name + ' Department',
              apps: []
            })),
            apps: [],
            waves: [
              { id: 1, name: 'Wave 1' },
              { id: 2, name: 'Wave 2' },
              { id: 3, name: 'Wave 3' }
            ]
          });
        }
      },
      
      loadConfig() {
        const config = localStorage.getItem(this.STORAGE_KEY);
        return config ? JSON.parse(config) : this.getDefaultConfig();
      },
      
      saveConfig(config) {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(config));
      },
      
      getDefaultConfig() {
        return { buses: [], apps: [], waves: [] };
      },
      
      getBUs() {
        return this.loadConfig().buses || [];
      },
      
      getApps() {
        return this.loadConfig().apps || [];
      },
      
      getAppsByBU(buId) {
        return this.getApps().filter(app => app.buId === buId);
      },
      
      addBU(bu) {
        const config = this.loadConfig();
        bu.id = Math.max(...config.buses.map(b => b.id), 0) + 1;
        config.buses.push(bu);
        this.saveConfig(config);
        return bu;
      },
      
      updateBU(buId, updates) {
        const config = this.loadConfig();
        const bu = config.buses.find(b => b.id === buId);
        if (bu) Object.assign(bu, updates);
        this.saveConfig(config);
      },
      
      deleteBU(buId) {
        const config = this.loadConfig();
        config.buses = config.buses.filter(b => b.id !== buId);
        config.apps = config.apps.filter(a => a.buId !== buId);
        this.saveConfig(config);
      },
      
      addApp(app) {
        const config = this.loadConfig();
        app.id = Math.max(...config.apps.map(a => a.id), 0) + 1;
        config.apps.push(app);
        this.saveConfig(config);
        return app;
      },
      
      updateApp(appId, updates) {
        const config = this.loadConfig();
        const app = config.apps.find(a => a.id === appId);
        if (app) Object.assign(app, updates);
        this.saveConfig(config);
      },
      
      deleteApp(appId) {
        const config = this.loadConfig();
        config.apps = config.apps.filter(a => a.id !== appId);
        this.saveConfig(config);
      }
    };

'''
        marker = 'const DATA = ['
        self.insert_before_marker(marker, storage_code, 'M1: Storage Manager')
    
    def add_progress_calculator(self):
        """M2: Progress Calculator con cálculo ponderado"""
        calc_code = '''
    /* ========== M2: PROGRESS CALCULATOR ========== */
    const ProgressCalculator = {
      
      calculateAppWeight(app) {
        const statusWeights = { TBS: 0, WIP: 0.5, CLO: 1.0 };
        const criticalityWeights = { Low: 1, Medium: 2, High: 3 };
        return (statusWeights[app.status] || 0) * (criticalityWeights[app.criticality] || 1);
      },
      
      calculateBUProgress(buId) {
        const apps = StorageManager.getAppsByBU(buId);
        if (apps.length === 0) return 0;
        
        const weightedSum = apps.reduce((sum, app) => {
          const weight = app.weight || 1;
          const progress = app.progress || 0;
          return sum + (progress * weight);
        }, 0);
        
        const totalWeight = apps.reduce((sum, app) => sum + (app.weight || 1), 0);
        return totalWeight > 0 ? Math.round((weightedSum / totalWeight) * 100) / 100 : 0;
      },
      
      recalculateAllBUsProgress() {
        const buses = StorageManager.getBUs();
        const updated = buses.map(bu => ({
          ...bu,
          computedProgress: this.calculateBUProgress(bu.id)
        }));
        return updated;
      },
      
      getEnhancedDATA() {
        // Devuelve DATA actualizado con progreso computado desde storage
        const buses = this.recalculateAllBUsProgress();
        return buses.map(bu => ({
          key: bu.key,
          name: bu.name,
          progress: bu.computedProgress || 0
        }));
      }
    };

'''
        marker = 'const $ = (s,root=document)'
        self.insert_before_marker(marker, calc_code, 'M2: Progress Calculator')
    
    def add_admin_controller(self):
        """M4, M5, M6: Admin Controller - Gestor de modal y eventos"""
        controller_code = '''
    /* ========== M4,M5,M6: ADMIN CONTROLLER ========== */
    const AdminController = {
      currentBUId: null,
      
      init() {
        this.setupEventListeners();
        this.renderBUList();
      },
      
      setupEventListeners() {
        $('#setupAdmin').addEventListener('click', () => this.openModal());
        $('#closeAdminModal').addEventListener('click', () => this.closeModal());
        $('#cancelAdminBtn').addEventListener('click', () => this.closeModal());
        $('#saveAdminBtn').addEventListener('click', () => this.saveAndClose());
        
        // Tabs
        $$('.modal-tab').forEach(tab => {
          tab.addEventListener('click', (e) => this.switchTab(e.target.dataset.tab));
        });
        
        // BU buttons
        $('#newBUBtn').addEventListener('click', () => this.newBU());
        
        // App filter
        $('#appBUFilter').addEventListener('change', (e) => {
          this.currentBUId = parseInt(e.target.value);
          this.renderAppsEditor();
        });
        
        // Settings
        $('#exportAdminJSON').addEventListener('click', () => this.exportConfig());
        $('#importAdminJSON').addEventListener('change', (e) => this.importConfig(e));
        $('#clearAllDataBtn').addEventListener('click', () => {
          if (confirm('⚠️ Clear all data from localStorage?')) {
            localStorage.removeItem(StorageManager.STORAGE_KEY);
            location.reload();
          }
        });
      },
      
      openModal() {
        $('#adminModal').classList.add('active');
        this.renderBUList();
        this.renderBUFilter();
      },
      
      closeModal() {
        $('#adminModal').classList.remove('active');
      },
      
      switchTab(tabName) {
        $$('.modal-tab').forEach(t => t.classList.remove('active'));
        $$('.modal-tabpanel').forEach(p => p.classList.remove('active'));
        $('[data-tab="' + tabName + '"]').classList.add('active');
        $('#tab-' + tabName).classList.add('active');
      },
      
      renderBUList() {
        const buses = StorageManager.getBUs();
        const container = $('#buList');
        container.innerHTML = '';
        
        buses.forEach(bu => {
          const apps = StorageManager.getAppsByBU(bu.id);
          const progress = ProgressCalculator.calculateBUProgress(bu.id);
          const card = document.createElement('div');
          card.className = 'bu-card';
          card.innerHTML = `
            <div class="bu-card-actions">
              <button class="bu-card-btn" title="Edit">✏️</button>
              <button class="bu-card-btn" title="Delete">🗑️</button>
            </div>
            <div class="bu-card-name">${bu.name}</div>
            <div class="bu-card-meta">${bu.domain} · ${bu.fullname}</div>
            <div class="bu-card-meta">Apps: ${apps.length} · Progress: ${progress.toFixed(1)}%</div>
          `;
          card.addEventListener('click', () => this.selectBU(bu.id, card));
          container.appendChild(card);
        });
      },
      
      selectBU(buId, element) {
        $$('.bu-card').forEach(c => c.classList.remove('selected'));
        element.classList.add('selected');
        this.currentBUId = buId;
      },
      
      newBU() {
        const name = prompt('Business Unit name:');
        if (!name) return;
        StorageManager.addBU({
          key: name.toUpperCase().slice(0, 4),
          name,
          domain: 'CORF',
          fullname: name + ' Department'
        });
        this.renderBUList();
      },
      
      renderBUFilter() {
        const buses = StorageManager.getBUs();
        const select = $('#appBUFilter');
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
        const bu = StorageManager.getBUs().find(b => b.id === this.currentBUId);
        const apps = StorageManager.getAppsByBU(this.currentBUId);
        const container = $('#appEditorContainer');
        
        let html = `<h3>${bu.name} Applications</h3>
          <button class="btn btn-primary" onclick="AdminController.newApp(${this.currentBUId})" style="margin-bottom:12px">+ Add Application</button>
          <table class="app-table">
            <thead>
              <tr>
                <th>App Name</th>
                <th>Status</th>
                <th>Progress %</th>
                <th>Weight</th>
                <th>Criticality</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>`;
        
        apps.forEach(app => {
          html += `
            <tr>
              <td><input type="text" value="${app.name}" onchange="AdminController.updateApp(${app.id}, {name: this.value})"/></td>
              <td><select onchange="AdminController.updateApp(${app.id}, {status: this.value})">
                <option value="TBS" ${app.status === 'TBS' ? 'selected' : ''}>TBS</option>
                <option value="WIP" ${app.status === 'WIP' ? 'selected' : ''}>WIP</option>
                <option value="CLO" ${app.status === 'CLO' ? 'selected' : ''}>CLO</option>
              </select></td>
              <td><input type="number" min="0" max="100" value="${app.progress || 0}" onchange="AdminController.updateApp(${app.id}, {progress: parseInt(this.value)})"/></td>
              <td><input type="number" min="0.5" max="3" step="0.5" value="${app.weight || 1}" onchange="AdminController.updateApp(${app.id}, {weight: parseFloat(this.value)})"/></td>
              <td><select onchange="AdminController.updateApp(${app.id}, {criticality: this.value})">
                <option value="Low" ${app.criticality === 'Low' ? 'selected' : ''}>Low</option>
                <option value="Medium" ${app.criticality === 'Medium' ? 'selected' : ''}>Medium</option>
                <option value="High" ${app.criticality === 'High' ? 'selected' : ''}>High</option>
              </select></td>
              <td><button class="btn btn-danger btn-sm" onclick="AdminController.deleteApp(${app.id})">Delete</button></td>
            </tr>`;
        });
        
        html += '</tbody></table>';
        container.innerHTML = html;
      },
      
      newApp(buId) {
        const name = prompt('Application name:');
        if (!name) return;
        StorageManager.addApp({
          buId,
          name,
          status: 'TBS',
          progress: 0,
          weight: 1,
          criticality: 'Medium'
        });
        this.renderAppsEditor();
      },
      
      updateApp(appId, updates) {
        StorageManager.updateApp(appId, updates);
        this.renderAppsEditor();
      },
      
      deleteApp(appId) {
        if (confirm('Delete this application?')) {
          StorageManager.deleteApp(appId);
          this.renderAppsEditor();
        }
      },
      
      exportConfig() {
        const config = StorageManager.loadConfig();
        const json = JSON.stringify(config, null, 2);
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'dashboard_config_' + new Date().toISOString().slice(0, 10) + '.json';
        a.click();
        URL.revokeObjectURL(url);
      },
      
      importConfig(event) {
        const file = event.target.files[0];
        if (!file) return;
        const reader = new FileReader();
        reader.onload = (e) => {
          try {
            const config = JSON.parse(e.target.result);
            StorageManager.saveConfig(config);
            alert('✅ Configuration imported successfully');
            location.reload();
          } catch (err) {
            alert('❌ Invalid JSON file');
          }
        };
        reader.readAsText(file);
      },
      
      saveAndClose() {
        apply();
        this.closeModal();
        alert('✅ Changes saved');
      }
    };

'''
        marker = 'function filtered(){'
        self.insert_before_marker(marker, controller_code, 'M4,M5,M6: Admin Controller')
    
    def update_data_retrieval(self):
        """Reemplazar DATA en apply() con datos calculados desde storage"""
        old_apply = '''    function apply(){
      const items = filtered();
      const avgGlobal = DATA.reduce((s,d)=>s+d.progress,0)/DATA.length;'''
        
        new_apply = '''    function apply(){
      // Actualizar DATA desde storage con progreso calculado
      const enhancedData = ProgressCalculator.getEnhancedDATA();
      for (let i = 0; i < enhancedData.length; i++) {
        if (DATA[i]) DATA[i].progress = enhancedData[i].progress;
      }
      const items = filtered();
      const avgGlobal = DATA.reduce((s,d)=>s+d.progress,0)/DATA.length;'''
        
        self.replace_exact(old_apply, new_apply, 'Update apply() with storage data')
    
    def add_hero_click_handler(self):
        """M6: Al hacer clic en el indicador principal, mostrar apps de la BU seleccionada"""
        code = '''
    // Click en hero gauge para ver apps detail
    $('#heroGauge').addEventListener('click', () => {
      if (state.pinned) {
        AdminController.currentBUId = DATA.find(d => d.name === state.pinned)?.id || null;
        if (AdminController.currentBUId) {
          AdminController.openModal();
          AdminController.switchTab('apps');
          setTimeout(() => {
            const busSelect = $('#appBUFilter');
            if (busSelect) busSelect.value = AdminController.currentBUId;
            AdminController.renderAppsEditor();
          }, 100);
        }
      }
    });

'''
        marker = '/* ------------- INIT ------------- */'
        self.insert_before_marker(marker, code, 'M6: Hero click handler')
    
    def add_initialization(self):
        """Inicializar módulos al cargar"""
        init_code = '''    // Initialize storage and admin
    StorageManager.init();
    AdminController.init();
'''
        marker = 'apply();'
        self.insert_before_marker(marker, init_code, 'Module initialization')
    
    def validate_output(self):
        """Validar que el archivo de salida sea válido"""
        new_size = len(self.content)
        new_lines = self.content.count('\n') + 1
        new_chars = len(self.content)
        
        print(f'\n📊 VALIDACIÓN DE SALIDA')
        print(f'=' * 70)
        print(f'Original: {self.original_chars:,} chars | {self.original_lines} lines | {self.original_size:,} bytes')
        print(f'Nuevo:    {new_chars:,} chars | {new_lines} lines | {new_size:,} bytes')
        print(f'Delta:    {new_chars - self.original_chars:+,} chars | {new_lines - self.original_lines:+,} lines | {new_size - self.original_size:+,} bytes')
        
        # Validaciones
        if new_size < self.original_size:
            print('⚠️  ADVERTENCIA: Nuevo archivo es más pequeño (revisar que no se perdió código)')
        
        if '</html>' not in self.content:
            raise ValueError('❌ Archivo mal formado: falta </html>')
        
        if '<script>' not in self.content or '</script>' not in self.content:
            raise ValueError('❌ Archivo mal formado: script corrupto')
        
        # Verificar que todos los módulos están presentes
        modules = ['StorageManager', 'ProgressCalculator', 'AdminController', 'adminModal']
        missing = [m for m in modules if m not in self.content]
        if missing:
            raise ValueError(f'❌ Módulos faltantes: {missing}')
        
        print('✅ Validación de estructura: PASSED')
        print('✅ Validación de módulos: PASSED')
    
    def save_output(self, output_path):
        """Guardar el archivo mejorado"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(self.content)
        file_size = os.path.getsize(output_path)
        print(f'\n💾 Archivo guardado en: {output_path}')
        print(f'   Tamaño: {file_size:,} bytes')
    
    def build(self):
        """Ejecutar el pipeline de construcción"""
        print('🚀 INICIANDO CONSTRUCCIÓN DEL DASHBOARD MEJORADO\n')
        
        steps = [
            ('M1: Storage Manager', self.add_storage_module),
            ('M2: Progress Calculator', self.add_progress_calculator),
            ('M4,M5,M6: Admin Controller', self.add_admin_controller),
            ('M3: CSS Styles', self.add_css_styles),
            ('M3: Modal HTML', self.add_modal_html),
            ('M7: Setup Button', self.add_setup_button),
            ('M6: Hero Click Handler', self.add_hero_click_handler),
            ('Update apply()', self.update_data_retrieval),
            ('Initialization', self.add_initialization),
        ]
        
        for step_name, step_fn in steps:
            try:
                print(f'\n📝 {step_name}...')
                step_fn()
            except Exception as e:
                print(f'❌ ERROR en {step_name}: {e}')
                raise
        
        print(f'\n🔍 Validando salida...')
        self.validate_output()
        
        output_path = r'c:\PROYECTOS\Dashboard\dashboard_enhanced.html'
        self.save_output(output_path)
        
        print(f'\n✅ ¡CONSTRUCCIÓN COMPLETADA EXITOSAMENTE!')
        return output_path


if __name__ == '__main__':
    html_path = r'c:\PROYECTOS\Dashboard\dashboard.html'
    builder = DashboardBuilder(html_path)
    output = builder.build()
    print(f'\n📥 Abre el archivo en: {output}')
