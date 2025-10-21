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
  }