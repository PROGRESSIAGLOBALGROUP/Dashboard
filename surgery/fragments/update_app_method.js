  updateApp(appId, updates) {
    Dashboard.StorageManager.updateApp(appId, updates);
    this.renderAppsEditor();
    // Refresh main dashboard when weight-affecting factors change
    if (updates.criticality || updates.businessImpact || updates.priority || updates.progress) {
      Dashboard.UIController.apply();
    }
  },