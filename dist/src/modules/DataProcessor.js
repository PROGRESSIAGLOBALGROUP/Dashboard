/* ========== Progress Calculator Module ========== */
const DATA = [
  {key:'GDPA', name:'GDPA', progress:30},
  {key:'P&S', name:'P&S', progress:25},
  {key:'SPP', name:'SPP', progress:20},
  {key:'ACC', name:'ACC', progress:15},
  {key:'SMKG', name:'SMKG', progress:9},
  {key:'INV', name:'INV', progress:0},
  {key:'PSC', name:'PSC', progress:0},
  {key:'CUST I', name:'CUST I', progress:0},
  {key:'CUST II', name:'CUST II', progress:0},
  {key:'PAY', name:'PAY', progress:100},
  {key:'HR', name:'HR', progress:100},
  {key:'COMM', name:'COMM', progress:100},
];

const ProgressCalculator = {
  calculateAppWeight(app) {
    const statusWeights = { TBS: 0, WIP: 0.5, CLO: 1.0 };
    const criticalityWeights = { Low: 1, Medium: 2, High: 3 };
    return (statusWeights[app.status] || 0) * (criticalityWeights[app.criticality] || 1);
  },
  
  calculateBUProgress(buId) {
    const apps = Dashboard.StorageManager.getAppsByBU(buId);
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
    const buses = Dashboard.StorageManager.getBUs();
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

// Export module for namespace compatibility
(function(app) {
  app.ProgressCalculator = ProgressCalculator;
  app.DATA = DATA;
})(window.Dashboard = window.Dashboard || {});