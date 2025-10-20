const StorageManager = {
  STORAGE_KEY: 'dashboard_config_v1',
  CLEARED_FLAG: 'dashboard_user_cleared_v1',
  
  init() {
    // Check if user intentionally cleared data
    const wasCleared = sessionStorage.getItem(this.CLEARED_FLAG);
    
    if (wasCleared) {
      // User cleared data intentionally - don't auto-recreate
      sessionStorage.removeItem(this.CLEARED_FLAG);
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
  
  markAsCleared() {
    sessionStorage.setItem(this.CLEARED_FLAG, 'true');
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
  }