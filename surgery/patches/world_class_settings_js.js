// Settings Tab Enhanced Functionality

/* World-Class Settings Manager */
const AdvancedSettingsManager = {
  SETTINGS_KEY: 'dashboard_advanced_settings_v1',
  BACKUP_KEY: 'dashboard_backup_v1',
  AUDIT_KEY: 'dashboard_audit_log_v1',
  
  defaultSettings: {
    performance: {
      animationSpeed: 1.0,
      refreshInterval: 30000,
      enableTransitions: true
    },
    display: {
      theme: 'auto',
      density: 'comfortable',
      showTooltips: true
    },
    notifications: {
      enableNotifications: true,
      notifyOnProgress: false,
      notifyOnCompletion: true
    },
    security: {
      enableEncryption: true,
      enableAuditLog: true
    },
    privacy: {
      shareUsageData: false,
      enableCrashReports: false,
      dataRetention: 90
    },
    export: {
      includeCalculatedMetrics: true,
      includeAuditTrail: true,
      includeSystemInfo: false
    }
  },
  
  init() {
    this.loadSettings();
    this.setupSettingsEventListeners();
    this.updateSettingsUI();
    this.initializeDragAndDrop();
    this.updateSystemInfo();
    this.loadAuditTrail();
  },
  
  loadSettings() {
    const stored = localStorage.getItem(this.SETTINGS_KEY);
    this.settings = stored ? { ...this.defaultSettings, ...JSON.parse(stored) } : { ...this.defaultSettings };
    return this.settings;
  },
  
  saveSettings() {
    localStorage.setItem(this.SETTINGS_KEY, JSON.stringify(this.settings));
    this.logAuditEvent('settings_changed', 'Settings configuration updated');
    this.showNotification('⚙️ Settings saved successfully', 'success');
    this.updateSystemInfo();
  },
  
  setupSettingsEventListeners() {
    // Performance Settings
    const animationSpeed = document.getElementById('animationSpeed');
    const animationSpeedValue = document.getElementById('animationSpeedValue');
    const refreshInterval = document.getElementById('refreshInterval');
    const enableTransitions = document.getElementById('enableTransitions');
    
    if (animationSpeed) {
      animationSpeed.addEventListener('input', (e) => {
        const value = parseFloat(e.target.value);
        this.settings.performance.animationSpeed = value;
        animationSpeedValue.textContent = value.toFixed(1) + 's';
        this.applyAnimationSpeed(value);
      });
    }
    
    if (refreshInterval) {
      refreshInterval.addEventListener('change', (e) => {
        this.settings.performance.refreshInterval = parseInt(e.target.value);
        this.setupAutoRefresh();
      });
    }
    
    if (enableTransitions) {
      enableTransitions.addEventListener('change', (e) => {
        this.settings.performance.enableTransitions = e.target.checked;
        this.applyTransitionSettings(e.target.checked);
      });
    }
    
    // Display Settings
    const themeInputs = document.querySelectorAll('input[name="theme"]');
    const displayDensity = document.getElementById('displayDensity');
    const showTooltips = document.getElementById('showTooltips');
    
    themeInputs.forEach(input => {
      input.addEventListener('change', (e) => {
        if (e.target.checked) {
          this.settings.display.theme = e.target.value;
          this.applyTheme(e.target.value);
        }
      });
    });
    
    if (displayDensity) {
      displayDensity.addEventListener('change', (e) => {
        this.settings.display.density = e.target.value;
        this.applyDensity(e.target.value);
      });
    }
    
    if (showTooltips) {
      showTooltips.addEventListener('change', (e) => {
        this.settings.display.showTooltips = e.target.checked;
        this.toggleTooltips(e.target.checked);
      });
    }
    
    // Notification Settings
    const enableNotifications = document.getElementById('enableNotifications');
    const notifyOnProgress = document.getElementById('notifyOnProgress');
    const notifyOnCompletion = document.getElementById('notifyOnCompletion');
    
    if (enableNotifications) {
      enableNotifications.addEventListener('change', (e) => {
        this.settings.notifications.enableNotifications = e.target.checked;
        if (e.target.checked) {
          this.requestNotificationPermission();
        }
      });
    }
    
    if (notifyOnProgress) {
      notifyOnProgress.addEventListener('change', (e) => {
        this.settings.notifications.notifyOnProgress = e.target.checked;
      });
    }
    
    if (notifyOnCompletion) {
      notifyOnCompletion.addEventListener('change', (e) => {
        this.settings.notifications.notifyOnCompletion = e.target.checked;
      });
    }
    
    // Security & Privacy Settings
    const enableEncryption = document.getElementById('enableEncryption');
    const enableAuditLog = document.getElementById('enableAuditLog');
    const shareUsageData = document.getElementById('shareUsageData');
    const enableCrashReports = document.getElementById('enableCrashReports');
    const dataRetention = document.getElementById('dataRetention');
    
    if (enableEncryption) {
      enableEncryption.addEventListener('change', (e) => {
        this.settings.security.enableEncryption = e.target.checked;
        this.toggleEncryption(e.target.checked);
      });
    }
    
    if (enableAuditLog) {
      enableAuditLog.addEventListener('change', (e) => {
        this.settings.security.enableAuditLog = e.target.checked;
      });
    }
    
    if (shareUsageData) {
      shareUsageData.addEventListener('change', (e) => {
        this.settings.privacy.shareUsageData = e.target.checked;
      });
    }
    
    if (enableCrashReports) {
      enableCrashReports.addEventListener('change', (e) => {
        this.settings.privacy.enableCrashReports = e.target.checked;
      });
    }
    
    if (dataRetention) {
      dataRetention.addEventListener('change', (e) => {
        this.settings.privacy.dataRetention = parseInt(e.target.value);
        this.cleanupOldData();
      });
    }
    
    // Export Options
    const includeCalculatedMetrics = document.getElementById('includeCalculatedMetrics');
    const includeAuditTrail = document.getElementById('includeAuditTrail');
    const includeSystemInfo = document.getElementById('includeSystemInfo');
    
    if (includeCalculatedMetrics) {
      includeCalculatedMetrics.addEventListener('change', (e) => {
        this.settings.export.includeCalculatedMetrics = e.target.checked;
      });
    }
    
    if (includeAuditTrail) {
      includeAuditTrail.addEventListener('change', (e) => {
        this.settings.export.includeAuditTrail = e.target.checked;
      });
    }
    
    if (includeSystemInfo) {
      includeSystemInfo.addEventListener('change', (e) => {
        this.settings.export.includeSystemInfo = e.target.checked;
      });
    }
    
    // Action Buttons
    const createBackupBtn = document.getElementById('createBackupBtn');
    const restoreBackupBtn = document.getElementById('restoreBackupBtn');
    const showAuditTrailBtn = document.getElementById('showAuditTrailBtn');
    const exportAuditBtn = document.getElementById('exportAuditBtn');
    const resetConfigBtn = document.getElementById('resetConfigBtn');
    const saveSettingsBtn = document.getElementById('saveSettingsBtn');
    const resetAllSettingsBtn = document.getElementById('resetAllSettingsBtn');
    
    if (createBackupBtn) {
      createBackupBtn.addEventListener('click', () => this.createBackup());
    }
    
    if (restoreBackupBtn) {
      restoreBackupBtn.addEventListener('click', () => this.restoreBackup());
    }
    
    if (showAuditTrailBtn) {
      showAuditTrailBtn.addEventListener('click', () => this.showAuditTrail());
    }
    
    if (exportAuditBtn) {
      exportAuditBtn.addEventListener('click', () => this.exportAuditLog());
    }
    
    if (resetConfigBtn) {
      resetConfigBtn.addEventListener('click', () => this.resetConfiguration());
    }
    
    if (saveSettingsBtn) {
      saveSettingsBtn.addEventListener('click', () => this.saveSettings());
    }
    
    if (resetAllSettingsBtn) {
      resetAllSettingsBtn.addEventListener('click', () => this.resetAllSettings());
    }
    
    // Clear All Data Enhanced
    const confirmationCheckboxes = document.querySelectorAll('#confirmDeletion1, #confirmDeletion2, #confirmDeletion3');
    const clearAllDataBtn = document.getElementById('clearAllDataBtn');
    
    confirmationCheckboxes.forEach(checkbox => {
      checkbox.addEventListener('change', () => {
        const allChecked = Array.from(confirmationCheckboxes).every(cb => cb.checked);
        if (clearAllDataBtn) {
          clearAllDataBtn.disabled = !allChecked;
        }
      });
    });
  },
  
  updateSettingsUI() {
    // Update Performance UI
    const animationSpeed = document.getElementById('animationSpeed');
    const animationSpeedValue = document.getElementById('animationSpeedValue');
    const refreshInterval = document.getElementById('refreshInterval');
    const enableTransitions = document.getElementById('enableTransitions');
    
    if (animationSpeed) {
      animationSpeed.value = this.settings.performance.animationSpeed;
      animationSpeedValue.textContent = this.settings.performance.animationSpeed.toFixed(1) + 's';
    }
    
    if (refreshInterval) {
      refreshInterval.value = this.settings.performance.refreshInterval;
    }
    
    if (enableTransitions) {
      enableTransitions.checked = this.settings.performance.enableTransitions;
    }
    
    // Update Display UI
    const themeInput = document.querySelector(`input[name="theme"][value="${this.settings.display.theme}"]`);
    const displayDensity = document.getElementById('displayDensity');
    const showTooltips = document.getElementById('showTooltips');
    
    if (themeInput) {
      themeInput.checked = true;
    }
    
    if (displayDensity) {
      displayDensity.value = this.settings.display.density;
    }
    
    if (showTooltips) {
      showTooltips.checked = this.settings.display.showTooltips;
    }
    
    // Update Notification UI
    const enableNotifications = document.getElementById('enableNotifications');
    const notifyOnProgress = document.getElementById('notifyOnProgress');
    const notifyOnCompletion = document.getElementById('notifyOnCompletion');
    
    if (enableNotifications) {
      enableNotifications.checked = this.settings.notifications.enableNotifications;
    }
    
    if (notifyOnProgress) {
      notifyOnProgress.checked = this.settings.notifications.notifyOnProgress;
    }
    
    if (notifyOnCompletion) {
      notifyOnCompletion.checked = this.settings.notifications.notifyOnCompletion;
    }
    
    // Update Security & Privacy UI
    const enableEncryption = document.getElementById('enableEncryption');
    const enableAuditLog = document.getElementById('enableAuditLog');
    const shareUsageData = document.getElementById('shareUsageData');
    const enableCrashReports = document.getElementById('enableCrashReports');
    const dataRetention = document.getElementById('dataRetention');
    
    if (enableEncryption) {
      enableEncryption.checked = this.settings.security.enableEncryption;
    }
    
    if (enableAuditLog) {
      enableAuditLog.checked = this.settings.security.enableAuditLog;
    }
    
    if (shareUsageData) {
      shareUsageData.checked = this.settings.privacy.shareUsageData;
    }
    
    if (enableCrashReports) {
      enableCrashReports.checked = this.settings.privacy.enableCrashReports;
    }
    
    if (dataRetention) {
      dataRetention.value = this.settings.privacy.dataRetention;
    }
    
    // Update Export Options UI
    const includeCalculatedMetrics = document.getElementById('includeCalculatedMetrics');
    const includeAuditTrail = document.getElementById('includeAuditTrail');
    const includeSystemInfo = document.getElementById('includeSystemInfo');
    
    if (includeCalculatedMetrics) {
      includeCalculatedMetrics.checked = this.settings.export.includeCalculatedMetrics;
    }
    
    if (includeAuditTrail) {
      includeAuditTrail.checked = this.settings.export.includeAuditTrail;
    }
    
    if (includeSystemInfo) {
      includeSystemInfo.checked = this.settings.export.includeSystemInfo;
    }
  },
  
  initializeDragAndDrop() {
    const importZone = document.getElementById('importZone');
    const importFileInput = document.getElementById('importAdminJSON');
    
    if (importZone && importFileInput) {
      ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        importZone.addEventListener(eventName, this.preventDefaults, false);
      });
      
      ['dragenter', 'dragover'].forEach(eventName => {
        importZone.addEventListener(eventName, () => importZone.classList.add('dragover'), false);
      });
      
      ['dragleave', 'drop'].forEach(eventName => {
        importZone.addEventListener(eventName, () => importZone.classList.remove('dragover'), false);
      });
      
      importZone.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length > 0) {
          this.handleFileImport(files[0]);
        }
      });
      
      importZone.addEventListener('click', () => importFileInput.click());
      
      importFileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
          this.handleFileImport(e.target.files[0]);
        }
      });
    }
  },
  
  preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
  },
  
  handleFileImport(file) {
    if (!file.type.includes('json')) {
      this.showNotification('❌ Please select a valid JSON file', 'error');
      return;
    }
    
    if (file.size > 10 * 1024 * 1024) { // 10MB limit
      this.showNotification('❌ File size too large. Maximum 10MB allowed.', 'error');
      return;
    }
    
    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const config = JSON.parse(e.target.result);
        this.validateAndImportConfig(config);
      } catch (error) {
        this.showNotification('❌ Invalid JSON file format', 'error');
        console.error('Import error:', error);
      }
    };
    reader.readAsText(file);
  },
  
  validateAndImportConfig(config) {
    // Enhanced validation
    const validationResult = this.validateConfigStructure(config);
    const validationResultEl = document.getElementById('validationResult');
    
    if (validationResult.isValid) {
      validationResultEl.style.display = 'block';
      validationResultEl.querySelector('.status-text').textContent = 'Configuration validated successfully';
      validationResultEl.querySelector('.validation-details').innerHTML = `
        <div>• Business Units: ${config.buses?.length || 0}</div>
        <div>• Applications: ${config.apps?.length || 0}</div>
        <div>• Waves: ${config.waves?.length || 0}</div>
      `;
      
      // Show import confirmation dialog
      this.showImportConfirmationDialog(config);
      this.logAuditEvent('config_validated', 'Configuration file validated for import');
    } else {
      validationResultEl.style.display = 'block';
      validationResultEl.classList.add('error');
      validationResultEl.querySelector('.status-icon').textContent = '❌';
      validationResultEl.querySelector('.status-text').textContent = 'Validation failed';
      validationResultEl.querySelector('.validation-details').innerHTML = validationResult.errors.map(error => `<div>• ${error}</div>`).join('');
      this.logAuditEvent('config_validation_failed', `Validation errors: ${validationResult.errors.join(', ')}`);
    }
  },
  
  validateConfigStructure(config) {
    const errors = [];
    
    if (!config.buses || !Array.isArray(config.buses)) {
      errors.push('Missing or invalid "buses" array');
    }
    
    if (!config.apps || !Array.isArray(config.apps)) {
      errors.push('Missing or invalid "apps" array');
    }
    
    if (!config.waves || !Array.isArray(config.waves)) {
      errors.push('Missing or invalid "waves" array');
    }
    
    // Validate referential integrity
    if (config.buses && config.apps) {
      const buIds = new Set(config.buses.map(bu => bu.id));
      config.apps.forEach((app, index) => {
        if (!buIds.has(app.buId)) {
          errors.push(`App at index ${index} references non-existent Business Unit ID ${app.buId}`);
        }
      });
    }
    
    return {
      isValid: errors.length === 0,
      errors
    };
  },
  
  showImportConfirmationDialog(config) {
    const confirmation = confirm(`Import this configuration?\n\nThis will replace all current data:\n• ${config.buses.length} Business Units\n• ${config.apps.length} Applications\n• ${config.waves.length} Waves\n\nClick OK to proceed or Cancel to abort.`);
    
    if (confirmation) {
      // Import the configuration using existing AdminController method
      Dashboard.StorageManager.saveConfig(config);
      this.showNotification('✅ Configuration imported successfully', 'success');
      this.logAuditEvent('config_imported', `Imported ${config.buses.length} BUs, ${config.apps.length} apps, ${config.waves.length} waves`);
      
      // Refresh the dashboard
      setTimeout(() => {
        location.reload();
      }, 1500);
    }
  },
  
  createBackup() {
    const config = Dashboard.StorageManager.loadConfig();
    const backup = {
      timestamp: new Date().toISOString(),
      version: '2.0.0',
      data: config,
      settings: this.settings
    };
    
    localStorage.setItem(this.BACKUP_KEY, JSON.stringify(backup));
    this.showNotification('💾 Backup created successfully', 'success');
    this.logAuditEvent('backup_created', 'Manual backup created');
    this.updateBackupInfo();
  },
  
  restoreBackup() {
    const backup = localStorage.getItem(this.BACKUP_KEY);
    if (!backup) {
      this.showNotification('❌ No backup found', 'error');
      return;
    }
    
    const confirmation = confirm('Restore from backup?\n\nThis will replace all current data with the backup version.\n\nClick OK to proceed or Cancel to abort.');
    
    if (confirmation) {
      try {
        const backupData = JSON.parse(backup);
        Dashboard.StorageManager.saveConfig(backupData.data);
        this.settings = backupData.settings || this.defaultSettings;
        localStorage.setItem(this.SETTINGS_KEY, JSON.stringify(this.settings));
        
        this.showNotification('✅ Backup restored successfully', 'success');
        this.logAuditEvent('backup_restored', `Restored backup from ${backupData.timestamp}`);
        
        setTimeout(() => {
          location.reload();
        }, 1500);
      } catch (error) {
        this.showNotification('❌ Failed to restore backup', 'error');
        console.error('Restore error:', error);
      }
    }
  },
  
  updateBackupInfo() {
    const backup = localStorage.getItem(this.BACKUP_KEY);
    const lastBackupTime = document.getElementById('lastBackupTime');
    
    if (backup && lastBackupTime) {
      try {
        const backupData = JSON.parse(backup);
        const date = new Date(backupData.timestamp);
        lastBackupTime.textContent = date.toLocaleString();
      } catch (error) {
        lastBackupTime.textContent = 'Invalid backup';
      }
    }
  },
  
  updateSystemInfo() {
    const configVersion = document.getElementById('configVersion');
    const lastModified = document.getElementById('lastModified');
    const storageInfo = document.getElementById('storageInfo');
    const storageUsed = document.getElementById('storageUsed');
    
    if (configVersion) {
      configVersion.textContent = '2.0.0';
    }
    
    if (lastModified) {
      const config = Dashboard.StorageManager.loadConfig();
      lastModified.textContent = config.lastModified ? new Date(config.lastModified).toLocaleString() : 'Never';
    }
    
    // Calculate storage usage
    let totalSize = 0;
    for (let key in localStorage) {
      if (localStorage.hasOwnProperty(key)) {
        totalSize += localStorage[key].length;
      }
    }
    
    const sizeKB = (totalSize / 1024).toFixed(1);
    
    if (storageInfo) {
      storageInfo.textContent = `${sizeKB} KB`;
    }
    
    if (storageUsed) {
      storageUsed.textContent = `${sizeKB} KB`;
    }
  },
  
  logAuditEvent(action, description) {
    if (!this.settings.security.enableAuditLog) return;
    
    const auditLog = JSON.parse(localStorage.getItem(this.AUDIT_KEY) || '[]');
    const event = {
      timestamp: new Date().toISOString(),
      action,
      description,
      userAgent: navigator.userAgent,
      url: window.location.href
    };
    
    auditLog.push(event);
    
    // Keep only recent entries based on retention policy
    const retentionDays = this.settings.privacy.dataRetention;
    if (retentionDays > 0) {
      const cutoffDate = new Date();
      cutoffDate.setDate(cutoffDate.getDate() - retentionDays);
      const filteredLog = auditLog.filter(entry => new Date(entry.timestamp) > cutoffDate);
      localStorage.setItem(this.AUDIT_KEY, JSON.stringify(filteredLog));
    } else {
      localStorage.setItem(this.AUDIT_KEY, JSON.stringify(auditLog));
    }
    
    this.updateAuditStats();
  },
  
  loadAuditTrail() {
    this.updateAuditStats();
  },
  
  updateAuditStats() {
    const auditLog = JSON.parse(localStorage.getItem(this.AUDIT_KEY) || '[]');
    const auditEntries = document.getElementById('auditEntries');
    const auditToday = document.getElementById('auditToday');
    
    if (auditEntries) {
      auditEntries.textContent = auditLog.length;
    }
    
    if (auditToday) {
      const today = new Date().toDateString();
      const todayEntries = auditLog.filter(entry => new Date(entry.timestamp).toDateString() === today);
      auditToday.textContent = todayEntries.length;
    }
  },
  
  showAuditTrail() {
    const auditLog = JSON.parse(localStorage.getItem(this.AUDIT_KEY) || '[]');
    
    if (auditLog.length === 0) {
      this.showNotification('📋 No audit entries found', 'info');
      return;
    }
    
    // Create and show audit trail modal
    const auditHTML = auditLog.slice(-50).reverse().map(entry => `
      <div class="audit-entry">
        <div class="audit-timestamp">${new Date(entry.timestamp).toLocaleString()}</div>
        <div class="audit-action">${entry.action}</div>
        <div class="audit-description">${entry.description}</div>
      </div>
    `).join('');
    
    const auditModal = document.createElement('div');
    auditModal.className = 'audit-modal-overlay';
    auditModal.innerHTML = `
      <div class="audit-modal-content">
        <div class="audit-modal-header">
          <h3>📋 Audit Trail (Last 50 entries)</h3>
          <button class="audit-modal-close">✕</button>
        </div>
        <div class="audit-modal-body">
          ${auditHTML}
        </div>
      </div>
    `;
    
    document.body.appendChild(auditModal);
    
    // Add close functionality
    auditModal.querySelector('.audit-modal-close').addEventListener('click', () => {
      document.body.removeChild(auditModal);
    });
    
    auditModal.addEventListener('click', (e) => {
      if (e.target === auditModal) {
        document.body.removeChild(auditModal);
      }
    });
    
    this.logAuditEvent('audit_trail_viewed', 'User viewed audit trail');
  },
  
  exportAuditLog() {
    const auditLog = JSON.parse(localStorage.getItem(this.AUDIT_KEY) || '[]');
    
    if (auditLog.length === 0) {
      this.showNotification('📋 No audit entries to export', 'info');
      return;
    }
    
    const exportData = {
      exportedAt: new Date().toISOString(),
      version: '2.0.0',
      totalEntries: auditLog.length,
      entries: auditLog
    };
    
    const json = JSON.stringify(exportData, null, 2);
    const blob = new Blob([json], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `dashboard_audit_log_${new Date().toISOString().slice(0, 10)}.json`;
    a.click();
    URL.revokeObjectURL(url);
    
    this.showNotification('📄 Audit log exported successfully', 'success');
    this.logAuditEvent('audit_log_exported', `Exported ${auditLog.length} audit entries`);
  },
  
  resetConfiguration() {
    const confirmation = confirm('Reset all settings to default?\n\nThis will not affect your data (Business Units, Applications) but will reset all preferences and configurations.\n\nClick OK to proceed or Cancel to abort.');
    
    if (confirmation) {
      this.settings = { ...this.defaultSettings };
      this.saveSettings();
      this.updateSettingsUI();
      this.showNotification('🔄 Settings reset to defaults', 'success');
      this.logAuditEvent('settings_reset', 'All settings reset to default values');
    }
  },
  
  resetAllSettings() {
    this.resetConfiguration();
  },
  
  applyAnimationSpeed(speed) {
    document.documentElement.style.setProperty('--animation-duration', `${speed}s`);
  },
  
  applyTransitionSettings(enabled) {
    document.documentElement.style.setProperty('--transitions-enabled', enabled ? 'all 0.3s ease' : 'none');
  },
  
  applyTheme(theme) {
    if (theme === 'auto') {
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
    } else {
      document.documentElement.setAttribute('data-theme', theme);
    }
    this.logAuditEvent('theme_changed', `Theme changed to ${theme}`);
  },
  
  applyDensity(density) {
    document.documentElement.setAttribute('data-density', density);
    this.logAuditEvent('density_changed', `Display density changed to ${density}`);
  },
  
  toggleTooltips(enabled) {
    document.documentElement.style.setProperty('--tooltips-enabled', enabled ? 'block' : 'none');
  },
  
  toggleEncryption(enabled) {
    // Note: This is a placeholder for encryption functionality
    // In a real implementation, you would encrypt/decrypt localStorage data
    this.logAuditEvent('encryption_toggled', `Data encryption ${enabled ? 'enabled' : 'disabled'}`);
  },
  
  setupAutoRefresh() {
    if (this.refreshTimer) {
      clearInterval(this.refreshTimer);
    }
    
    if (this.settings.performance.refreshInterval > 0) {
      this.refreshTimer = setInterval(() => {
        if (Dashboard && Dashboard.UIController && Dashboard.UIController.apply) {
          Dashboard.UIController.apply();
        }
      }, this.settings.performance.refreshInterval);
    }
  },
  
  requestNotificationPermission() {
    if ('Notification' in window) {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          this.showNotification('🔔 Notifications enabled', 'success');
        } else {
          this.showNotification('🔕 Notification permission denied', 'warning');
        }
      });
    }
  },
  
  showNotification(message, type = 'info') {
    // Create and show a toast notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Style the notification
    Object.assign(notification.style, {
      position: 'fixed',
      top: '20px',
      right: '20px',
      padding: '16px 24px',
      borderRadius: '8px',
      color: 'white',
      fontWeight: '500',
      zIndex: '10000',
      animation: 'slideInRight 0.3s ease',
      maxWidth: '400px',
      boxShadow: '0 8px 24px rgba(0,0,0,0.3)'
    });
    
    // Set background color based on type
    const colors = {
      success: '#32e685',
      error: '#ff5f7a',
      warning: '#ffd166',
      info: '#5b9dff'
    };
    
    notification.style.background = colors[type] || colors.info;
    
    document.body.appendChild(notification);
    
    // Remove after 4 seconds
    setTimeout(() => {
      notification.style.animation = 'slideOutRight 0.3s ease';
      setTimeout(() => {
        if (notification.parentNode) {
          document.body.removeChild(notification);
        }
      }, 300);
    }, 4000);
  },
  
  cleanupOldData() {
    const retentionDays = this.settings.privacy.dataRetention;
    if (retentionDays === 0) return; // Indefinite retention
    
    // Cleanup audit log
    const auditLog = JSON.parse(localStorage.getItem(this.AUDIT_KEY) || '[]');
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - retentionDays);
    
    const filteredLog = auditLog.filter(entry => new Date(entry.timestamp) > cutoffDate);
    localStorage.setItem(this.AUDIT_KEY, JSON.stringify(filteredLog));
    
    this.updateAuditStats();
    this.logAuditEvent('data_cleanup', `Cleaned up data older than ${retentionDays} days`);
  }
};

// Initialize Advanced Settings when the admin modal is opened
document.addEventListener('DOMContentLoaded', () => {
  // Wait for Dashboard to be initialized
  const initAdvancedSettings = () => {
    if (window.Dashboard && window.Dashboard.AdminController) {
      // Override the original switchTab to initialize advanced settings
      const originalSwitchTab = Dashboard.AdminController.switchTab;
      Dashboard.AdminController.switchTab = function(tabName) {
        originalSwitchTab.call(this, tabName);
        
        if (tabName === 'settings') {
          // Initialize advanced settings when Settings tab is activated
          setTimeout(() => {
            AdvancedSettingsManager.init();
          }, 100);
        }
      };
      
      // Also override the enhanced export functionality
      const originalExportConfig = Dashboard.AdminController.exportConfig;
      Dashboard.AdminController.exportConfig = function() {
        const config = Dashboard.StorageManager.loadConfig();
        const settings = AdvancedSettingsManager.loadSettings();
        
        // Create enhanced export based on user preferences
        const enrichedConfig = {
          ...config,
          exportMetadata: {
            exportedAt: new Date().toISOString(),
            version: '2.0.0',
            schema: 'dashboard_config_v2_enhanced',
            totalBUs: config.buses.length,
            totalApps: config.apps.length,
            totalWaves: config.waves.length
          }
        };
        
        // Add calculated metrics if enabled
        if (settings.export.includeCalculatedMetrics) {
          enrichedConfig.buses = config.buses.map(bu => ({
            ...bu,
            calculatedProgress: Dashboard.ProgressCalculator.calculateBUProgress(bu.id),
            appCount: config.apps.filter(app => app.buId === bu.id).length
          }));
          
          enrichedConfig.apps = config.apps.map(app => ({
            ...app,
            buName: config.buses.find(b => b.id === app.buId)?.name || 'Unknown',
            calculatedWeight: Dashboard.ProgressCalculator.calculateAppWeight(app)
          }));
        }
        
        // Add audit trail if enabled
        if (settings.export.includeAuditTrail) {
          const auditLog = JSON.parse(localStorage.getItem(AdvancedSettingsManager.AUDIT_KEY) || '[]');
          enrichedConfig.auditTrail = auditLog.slice(-100); // Last 100 entries
        }
        
        // Add system info if enabled
        if (settings.export.includeSystemInfo) {
          enrichedConfig.systemInfo = {
            userAgent: navigator.userAgent,
            timestamp: new Date().toISOString(),
            timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
            language: navigator.language,
            settings: settings
          };
        }
        
        const json = JSON.stringify(enrichedConfig, null, 2);
        const blob = new Blob([json], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `dashboard_enhanced_config_${new Date().toISOString().slice(0, 10)}.json`;
        a.click();
        URL.revokeObjectURL(url);
        
        AdvancedSettingsManager.logAuditEvent('config_exported', 'Enhanced configuration exported');
        AdvancedSettingsManager.showNotification('📥 Enhanced configuration exported successfully', 'success');
      };
    } else {
      // Retry after a short delay
      setTimeout(initAdvancedSettings, 100);
    }
  };
  
  initAdvancedSettings();
});

// Add notification animations CSS
const notificationStyles = document.createElement('style');
notificationStyles.textContent = `
  @keyframes slideInRight {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
  
  @keyframes slideOutRight {
    from {
      transform: translateX(0);
      opacity: 1;
    }
    to {
      transform: translateX(100%);
      opacity: 0;
    }
  }
  
  .audit-modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.9);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    backdrop-filter: blur(10px);
  }
  
  .audit-modal-content {
    background: var(--panel);
    border: 1px solid var(--ring);
    border-radius: 16px;
    width: 90%;
    max-width: 800px;
    max-height: 80vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }
  
  .audit-modal-header {
    padding: 24px;
    border-bottom: 1px solid var(--ring);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .audit-modal-header h3 {
    margin: 0;
    color: var(--text);
    font-size: 20px;
  }
  
  .audit-modal-close {
    background: none;
    border: none;
    color: var(--text);
    font-size: 24px;
    cursor: pointer;
    padding: 4px;
    border-radius: 4px;
    transition: background 0.2s ease;
  }
  
  .audit-modal-close:hover {
    background: var(--ring);
  }
  
  .audit-modal-body {
    padding: 24px;
    overflow-y: auto;
    flex: 1;
  }
  
  .audit-entry {
    padding: 16px;
    border: 1px solid var(--ring);
    border-radius: 8px;
    margin-bottom: 12px;
    background: rgba(91,157,255,0.02);
    transition: background 0.2s ease;
  }
  
  .audit-entry:hover {
    background: rgba(91,157,255,0.05);
  }
  
  .audit-timestamp {
    font-size: 12px;
    color: var(--text-muted, rgba(233, 238, 247, 0.7));
    margin-bottom: 4px;
  }
  
  .audit-action {
    font-weight: 600;
    color: var(--primary);
    margin-bottom: 4px;
  }
  
  .audit-description {
    font-size: 14px;
    color: var(--text);
  }
`;

document.head.appendChild(notificationStyles);

// End Settings Tab Functionality