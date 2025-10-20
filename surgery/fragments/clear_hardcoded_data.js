// REPLACEMENT FOR HARDCODED DATA ARRAY
// This is now DYNAMICALLY built from StorageManager, not hardcoded
// The old const DATA = [...] is REMOVED entirely

const DATA = [];  // Empty by default, populated from StorageManager

// Function to rebuild DATA from storage (single source of truth)
function rebuildDATAFromStorage() {
  DATA.length = 0;  // Clear array
  const buses = Dashboard.StorageManager.getBUs();
  
  buses.forEach(bus => {
    const apps = Dashboard.StorageManager.getAppsByBU(bus.id);
    let progress = 0;
    
    if (apps.length > 0) {
      const totalWeight = apps.reduce((sum, app) => sum + (app.weight || 1), 0);
      const weightedSum = apps.reduce((sum, app) => {
        return sum + ((app.progress || 0) * (app.weight || 1));
      }, 0);
      progress = totalWeight > 0 ? Math.round((weightedSum / totalWeight) * 100) / 100 : 0;
    }
    
    DATA.push({
      key: bus.key,
      name: bus.name,
      progress: progress
    });
  });
  
  console.log('🔄 [DATA] Rebuilt from storage:', JSON.stringify(DATA));
  return DATA;
}
