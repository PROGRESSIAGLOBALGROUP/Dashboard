// Automatic Weight Calculation Implementation
// Business-grade formula: (Criticality × Business Impact × Priority) ÷ 27 * 3

const ProgressCalculator = {
  /**
   * Calculates automatic weight based on business factors
   * Formula: (Criticality × Business Impact × Priority) ÷ 27 * 3
   * Range: 0.11 to 3.0 (enterprise-grade scaling)
   */
  calculateAppWeight(app) {
    // Business factor weights (enterprise standard)
    const criticalityWeights = { Low: 1, Medium: 2, High: 3 };
    const businessImpactWeights = { Low: 1, Medium: 2, High: 3 };
    const priorityWeights = { Low: 1, Medium: 2, High: 3 };
    
    // Get values with defaults
    const criticality = criticalityWeights[app.criticality] || 2;
    const businessImpact = businessImpactWeights[app.businessImpact] || 2;
    const priority = priorityWeights[app.priority] || 2;
    
    // Automatic weight calculation: normalized to 0.11-3.0 range
    const rawWeight = (criticality * businessImpact * priority) / 27 * 3;
    
    // Round to 2 decimals for precision
    return Math.round(rawWeight * 100) / 100;
  },
  
  calculateBUProgress(buId) {
    const apps = Dashboard.StorageManager.getAppsByBU(buId);
    if (apps.length === 0) return 0;
    
    // Filter out TBS apps (not started yet)
    const activeApps = apps.filter(app => app.status !== 'TBS');
    if (activeApps.length === 0) return 0;
    
    const weightedSum = activeApps.reduce((sum, app) => {
      const weight = this.calculateAppWeight(app); // Use automatic weight
      const progress = app.progress || 0;
      return sum + (progress * weight);
    }, 0);
    
    const totalWeight = activeApps.reduce((sum, app) => {
      return sum + this.calculateAppWeight(app); // Use automatic weight
    }, 0);
    
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