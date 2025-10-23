// ========== BU ANALYTICS EXPORT/IMPORT - JAVASCRIPT FUNCTIONS ==========

// Initialize BU Analytics
initBUAnalytics() {
  this.buAnalyticsData = null;
  this.setupBUAnalyticsEventListeners();
  this.populateBUSelectDropdown();
},

setupBUAnalyticsEventListeners() {
  // Export
  document.getElementById('buAnalyticsExportSelect')?.addEventListener('change', (e) => {
    this.onBUSelectForExport(parseInt(e.target.value));
  });
  
  document.getElementById('exportBUAnalyticsBtn')?.addEventListener('click', () => {
    this.showBUAnalyticsExportModal();
  });
  
  document.getElementById('downloadBUAnalyticsBtn')?.addEventListener('click', () => {
    this.downloadBUAnalytics();
  });
  
  // Import
  const dropZone = document.getElementById('importDropZone');
  if (dropZone) {
    dropZone.addEventListener('click', () => {
      document.getElementById('importBUAnalyticsFile').click();
    });
    
    dropZone.addEventListener('dragover', (e) => {
      e.preventDefault();
      dropZone.classList.add('drag-over');
    });
    
    dropZone.addEventListener('dragleave', () => {
      dropZone.classList.remove('drag-over');
    });
    
    dropZone.addEventListener('drop', (e) => {
      e.preventDefault();
      dropZone.classList.remove('drag-over');
      if (e.dataTransfer.files.length) {
        this.handleBUAnalyticsFileImport(e.dataTransfer.files[0]);
      }
    });
  }
  
  document.getElementById('importBUAnalyticsFile')?.addEventListener('change', (e) => {
    if (e.target.files.length) {
      this.handleBUAnalyticsFileImport(e.target.files[0]);
    }
  });
  
  document.getElementById('confirmBUImportBtn')?.addEventListener('click', () => {
    this.confirmBUAnalyticsImport();
  });
},

populateBUSelectDropdown() {
  const select = document.getElementById('buAnalyticsExportSelect');
  if (!select) return;
  
  const buses = Dashboard.StorageManager.getBUs();
  select.innerHTML = '<option value="">-- Choose a Business Unit --</option>';
  
  buses.forEach(bu => {
    const opt = document.createElement('option');
    opt.value = bu.id;
    opt.textContent = `${bu.name} (${bu.key})`;
    select.appendChild(opt);
  });
},

onBUSelectForExport(buId) {
  const btn = document.getElementById('exportBUAnalyticsBtn');
  const previewBox = document.getElementById('exportPreviewBox');
  
  if (!buId) {
    btn.disabled = true;
    previewBox.style.display = 'none';
    return;
  }
  
  const bu = Dashboard.StorageManager.getBUs().find(b => b.id === buId);
  const apps = Dashboard.StorageManager.getAppsByBU(buId);
  
  const completed = apps.filter(a => a.status === 'CLO').length;
  const avgProgress = apps.length > 0
    ? Math.round(apps.reduce((sum, a) => sum + (a.progress || 0), 0) / apps.length)
    : 0;
  
  const jsonStr = JSON.stringify({ bu, apps }, null, 2);
  const fileSize = (new Blob([jsonStr]).size / 1024).toFixed(1);
  
  document.getElementById('exportPreviewApps').textContent = apps.length;
  document.getElementById('exportPreviewProgress').textContent = avgProgress + '%';
  document.getElementById('exportPreviewSize').textContent = fileSize + ' KB';
  
  previewBox.style.display = 'block';
  btn.disabled = false;
  this.buAnalyticsData = { bu, apps };
},

showBUAnalyticsExportModal() {
  if (!this.buAnalyticsData) return;
  
  const { bu, apps } = this.buAnalyticsData;
  const completed = apps.filter(a => a.status === 'CLO').length;
  const wip = apps.filter(a => a.status === 'WIP').length;
  const avgProgress = apps.length > 0
    ? Math.round(apps.reduce((sum, a) => sum + (a.progress || 0), 0) / apps.length)
    : 0;
  
  document.getElementById('exportBUName').textContent = bu.name;
  document.getElementById('exportBUMeta').textContent = `${bu.domain} • ${bu.manager || 'No manager'}`;
  document.getElementById('exportStatApps').textContent = apps.length;
  document.getElementById('exportStatComplete').textContent = completed;
  document.getElementById('exportStatWIP').textContent = wip;
  document.getElementById('exportStatProgress').textContent = avgProgress + '%';
  
  document.getElementById('buAnalyticsExportModal').classList.add('active');
},

downloadBUAnalytics() {
  if (!this.buAnalyticsData) return;
  
  const { bu, apps } = this.buAnalyticsData;
  const completed = apps.filter(a => a.status === 'CLO').length;
  const wip = apps.filter(a => a.status === 'WIP').length;
  const tbs = apps.filter(a => a.status === 'TBS').length;
  const avgProgress = apps.length > 0
    ? Math.round(apps.reduce((sum, a) => sum + (a.progress || 0), 0) / apps.length * 10) / 10
    : 0;
  
  const exportData = {
    format: 'bu-analytics-v1',
    exportedAt: new Date().toISOString(),
    buData: {
      id: bu.id,
      key: bu.key,
      name: bu.name,
      domain: bu.domain,
      fullname: bu.fullname,
      color: bu.color || '#5b9dff',
      manager: bu.manager || ''
    },
    apps: apps.map(app => ({
      id: app.id,
      buId: app.buId,
      name: app.name,
      status: app.status,
      progress: app.progress || 0,
      weight: app.weight || 1,
      criticality: app.criticality || 'Medium',
      businessImpact: app.businessImpact || app.impact || 'Medium',
      priority: app.priority || 'Medium'
    })),
    statistics: {
      totalApps: apps.length,
      completedApps: completed,
      wipApps: wip,
      tbsApps: tbs,
      averageProgress: avgProgress,
      weightedProgress: Dashboard.ProgressCalculator.calculateBUProgress(bu.id)
    }
  };
  
  const json = JSON.stringify(exportData, null, 2);
  const blob = new Blob([json], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `bu-analytics_${bu.key}_${new Date().toISOString().split('T')[0]}.json`;
  a.click();
  URL.revokeObjectURL(url);
  
  document.getElementById('buAnalyticsExportModal').classList.remove('active');
  console.log('✅ BU Analytics exported:', bu.name);
},

handleBUAnalyticsFileImport(file) {
  if (!file.name.endsWith('.json')) {
    alert('❌ Please select a valid .json file');
    return;
  }
  
  const reader = new FileReader();
  reader.onload = (e) => {
    try {
      const data = JSON.parse(e.target.result);
      
      // Validate format
      if (data.format !== 'bu-analytics-v1') {
        throw new Error('Invalid file format. Expected bu-analytics-v1');
      }
      
      if (!data.buData || !Array.isArray(data.apps)) {
        throw new Error('Invalid file structure');
      }
      
      this.showBUAnalyticsImportPreview(data);
    } catch (err) {
      alert('❌ Error reading file:\n\n' + err.message);
      console.error('Import error:', err);
    }
  };
  reader.readAsText(file);
},

showBUAnalyticsImportPreview(data) {
  const { buData, apps, statistics } = data;
  
  document.getElementById('importBUName').textContent = buData.name;
  document.getElementById('importBUMeta').textContent = `${buData.domain} • ${buData.manager || 'No manager'}`;
  document.getElementById('importStatApps').textContent = apps.length;
  document.getElementById('importStatComplete').textContent = statistics.completedApps || 0;
  document.getElementById('importStatWIP').textContent = statistics.wipApps || 0;
  document.getElementById('importStatProgress').textContent = statistics.averageProgress.toFixed(1) + '%';
  
  const strategy = document.querySelector('input[name="buMergeStrategy"]:checked').value;
  const strategyText = {
    'replace': '🔄 Replace - This will overwrite the entire Business Unit with the imported data',
    'merge': '🔗 Merge - New apps will be added, existing apps will be updated',
    'append': '➕ Append - All apps will be added as new items'
  };
  
  document.getElementById('importMergeStrategyDisplay').textContent = strategyText[strategy];
  
  const appsList = document.getElementById('importAppsPreviewList');
  appsList.innerHTML = '';
  
  apps.forEach(app => {
    const item = document.createElement('div');
    item.className = 'app-preview-item';
    
    const statusBadges = {
      'TBS': 'app-status-tbs',
      'WIP': 'app-status-wip',
      'CLO': 'app-status-clo'
    };
    
    item.innerHTML = `
      <span class="app-name">${app.name}</span>
      <span class="app-status-badge ${statusBadges[app.status]}">${app.status}</span>
      <span class="app-progress">${app.progress}%</span>
    `;
    appsList.appendChild(item);
  });
  
  this.pendingImportData = data;
  document.getElementById('buAnalyticsImportModal').classList.add('active');
},

confirmBUAnalyticsImport() {
  if (!this.pendingImportData) return;
  
  const { buData, apps } = this.pendingImportData;
  const strategy = document.querySelector('input[name="buMergeStrategy"]:checked').value;
  
  try {
    if (strategy === 'replace') {
      this.mergeStrategyReplace(buData, apps);
    } else if (strategy === 'merge') {
      this.mergeStrategyMerge(buData, apps);
    } else if (strategy === 'append') {
      this.mergeStrategyAppend(buData, apps);
    }
    
    document.getElementById('buAnalyticsImportModal').classList.remove('active');
    alert(`✅ Successfully imported ${apps.length} applications from ${buData.name}`);
    this.renderAppsEditor();
    Dashboard.UIController.apply();
    console.log('✅ BU Analytics imported:', buData.name);
    
  } catch (err) {
    alert('❌ Import failed:\n\n' + err.message);
    console.error('Merge error:', err);
  }
},

mergeStrategyReplace(buData, apps) {
  // Find or create the BU
  let bu = Dashboard.StorageManager.getBUs().find(b => b.id === buData.id);
  
  if (!bu) {
    // Create new BU
    bu = Dashboard.StorageManager.addBU({
      key: buData.key,
      name: buData.name,
      domain: buData.domain,
      fullname: buData.fullname,
      color: buData.color,
      manager: buData.manager
    });
  }
  
  // Remove old apps for this BU
  const config = Dashboard.StorageManager.loadConfig();
  config.apps = config.apps.filter(a => a.buId !== bu.id);
  
  // Add new apps
  apps.forEach(app => {
    config.apps.push({
      id: Math.max(...config.apps.map(a => a.id || 0)) + 1,
      buId: bu.id,
      name: app.name,
      status: app.status,
      progress: app.progress,
      weight: app.weight,
      criticality: app.criticality,
      businessImpact: app.businessImpact,
      priority: app.priority
    });
  });
  
  Dashboard.StorageManager.saveConfig(config);
},

mergeStrategyMerge(buData, apps) {
  // Find or create the BU
  let bu = Dashboard.StorageManager.getBUs().find(b => b.id === buData.id);
  
  if (!bu) {
    bu = Dashboard.StorageManager.addBU({
      key: buData.key,
      name: buData.name,
      domain: buData.domain,
      fullname: buData.fullname,
      color: buData.color,
      manager: buData.manager
    });
  }
  
  const config = Dashboard.StorageManager.loadConfig();
  const existingApps = config.apps.filter(a => a.buId === bu.id);
  
  apps.forEach(importedApp => {
    const existing = existingApps.find(a => a.name === importedApp.name);
    
    if (existing) {
      // Update existing
      existing.status = importedApp.status;
      existing.progress = importedApp.progress;
      existing.criticality = importedApp.criticality;
      existing.businessImpact = importedApp.businessImpact;
      existing.priority = importedApp.priority;
    } else {
      // Add new
      config.apps.push({
        id: Math.max(...config.apps.map(a => a.id || 0)) + 1,
        buId: bu.id,
        name: importedApp.name,
        status: importedApp.status,
        progress: importedApp.progress,
        weight: importedApp.weight,
        criticality: importedApp.criticality,
        businessImpact: importedApp.businessImpact,
        priority: importedApp.priority
      });
    }
  });
  
  Dashboard.StorageManager.saveConfig(config);
},

mergeStrategyAppend(buData, apps) {
  // Find or create the BU
  let bu = Dashboard.StorageManager.getBUs().find(b => b.id === buData.id);
  
  if (!bu) {
    bu = Dashboard.StorageManager.addBU({
      key: buData.key,
      name: buData.name,
      domain: buData.domain,
      fullname: buData.fullname,
      color: buData.color,
      manager: buData.manager
    });
  }
  
  const config = Dashboard.StorageManager.loadConfig();
  
  // Add all apps as new (with new IDs)
  apps.forEach(app => {
    config.apps.push({
      id: Math.max(...config.apps.map(a => a.id || 0)) + 1,
      buId: bu.id,
      name: `${app.name} (imported)`,
      status: app.status,
      progress: app.progress,
      weight: app.weight,
      criticality: app.criticality,
      businessImpact: app.businessImpact,
      priority: app.priority
    });
  });
  
  Dashboard.StorageManager.saveConfig(config);
}

// ========== END BU ANALYTICS FUNCTIONS ==========
