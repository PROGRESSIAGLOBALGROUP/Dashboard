/* ========== Storage Manager Module ========== */
const StorageManager = {
  STORAGE_KEY: 'dashboard_config_v1',
  CLEARED_FLAG: 'dashboard_user_cleared_v1',
  
  init() {
    // Si el usuario ha borrado intencionalmente los datos, no recrear
    if (sessionStorage.getItem(this.CLEARED_FLAG)) {
      console.log('✅ Data was intentionally cleared - keeping empty state');
      return;
    }
    
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
    if (app) {
      // Add timestamp and update marker if not already in updates
      if (!updates.updatedAt) {
        updates.updatedAt = new Date().toISOString();
      }
      if (!updates.updatedBy) {
        updates.updatedBy = 'Local Edit';
      }
      Object.assign(app, updates);
    }
    this.saveConfig(config);
  },
  
  deleteApp(appId) {
    const config = this.loadConfig();
    config.apps = config.apps.filter(a => a.id !== appId);
    this.saveConfig(config);
  },
  
  getWaves() {
    return this.loadConfig().waves || [];
  },
  
  addWave(wave) {
    const config = this.loadConfig();
    wave.id = Math.max(...config.waves.map(w => w.id), 0) + 1;
    config.waves.push(wave);
    this.saveConfig(config);
    return wave;
  },
  
  updateWave(waveId, updates) {
    const config = this.loadConfig();
    const wave = config.waves.find(w => w.id === waveId);
    if (wave) Object.assign(wave, updates);
    this.saveConfig(config);
  },
  
  deleteWave(waveId) {
    const config = this.loadConfig();
    // Validate: wave cannot have active apps
    const appsInWave = config.apps.filter(a => a.waveId === waveId);
    if (appsInWave.length > 0) {
      throw new Error(`Cannot delete Wave ${waveId}: ${appsInWave.length} application(s) still assigned`);
    }
    config.waves = config.waves.filter(w => w.id !== waveId);
    this.saveConfig(config);
  },
  
  markAsCleared() {
    // Mark in sessionStorage so page reload doesn't auto-recreate data
    sessionStorage.setItem(this.CLEARED_FLAG, 'true');
  }
};

// Export module for namespace compatibility
(function(app) {
  app.StorageManager = StorageManager;
})(window.Dashboard = window.Dashboard || {});