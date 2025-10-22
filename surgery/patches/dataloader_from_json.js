  async loadData() {
    try {
      console.log('🚀 [DataLoader] Fetching data from data/tables.json...');
      
      // FETCH from external JSON file (no hardcodes)
      const response = await fetch('./data/tables.json');
      if (!response.ok) {
        console.error('❌ [DataLoader] Failed to fetch data/tables.json:', response.statusText);
        return { businessUnits: [], apps: [], waves: [] };
      }
      
      const jsonData = await response.json();
      console.log('✅ [DataLoader] JSON loaded successfully');
      
      // Transform Business Units
      const businessUnits = (jsonData.business_units_catalog || []).map(bu => ({
        id: bu.BU_ID,
        key: bu.BU_DOMAIN,
        name: bu.BU_NAME,
        domain: bu.BU_DOMAIN,
        fullname: bu.BU_FULLNAME,
        apps: []
      }));
      
      // Transform Applications
      const apps = (jsonData.apps_catalog || []).map(app => ({
        id: app.APP_ID,
        buId: app.BU_ID,
        wave: `Wave ${app.WAVE_ID}`,
        name: app.APP_NAME,
        status: app.APP_STATUS === "Completed" ? "CLO" : app.APP_STATUS === "WIP" ? "WIP" : "TBS",
        progress: app.APP_COMPLETION_PROGRESS || 0,
        criticality: app.APP_CRITICALITY || "Medium",
        impact: app.APP_BUSINESS_IMPACT || "Medium",
        priority: app.APP_PRIORITY || "Medium",
        order: app.APP_ID
      }));
      
      // Transform Waves
      const waves = (jsonData.waves_catalog || []).map(wave => ({
        id: wave.WAVE_ID,
        name: wave.DESCRIPTION
      }));
      
      // PERSIST to localStorage (single source of truth)
      Dashboard.StorageManager.saveConfig({
        buses: businessUnits,
        apps: apps,
        waves: waves
      });
      
      console.log('✅ [DataLoader] Data persisted to localStorage:', { 
        buses: businessUnits.length, 
        apps: apps.length, 
        waves: waves.length 
      });
      return { businessUnits, apps, waves };
    } catch (error) {
      console.error("❌ [DataLoader] Error loading data:", error);
      return { businessUnits: [], apps: [], waves: [] };
    }
  }
