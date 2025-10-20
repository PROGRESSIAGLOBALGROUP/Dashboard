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
  }