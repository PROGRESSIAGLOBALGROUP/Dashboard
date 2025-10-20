/* ========== APP REASSIGNMENT & AUDIT TRAIL ========== */

// Add to StorageManager
const StorageManager_reassignApp = {
  reassignApp(appId, newBuId) {
    console.log(`📋 [StorageManager] Reassigning app ${appId} to BU ${newBuId}`);
    
    const config = this.loadConfig();
    const app = config.apps.find(a => a.id === appId);
    
    if (!app) {
      console.error(`❌ App ${appId} not found`);
      return false;
    }
    
    const oldBuId = app.buId;
    const oldBU = config.buses.find(b => b.id === oldBuId);
    const newBU = config.buses.find(b => b.id === newBuId);
    
    if (!newBU) {
      console.error(`❌ Target BU ${newBuId} not found`);
      return false;
    }
    
    // Create audit entry
    const auditEntry = {
      timestamp: new Date().toISOString(),
      action: 'APP_REASSIGNED',
      appId: appId,
      appName: app.name,
      fromBuId: oldBuId,
      fromBuName: oldBU ? oldBU.name : 'Unknown',
      toBuId: newBuId,
      toBuName: newBU.name,
      status: app.status,
      progress: app.progress
    };
    
    // Update app
    app.buId = newBuId;
    
    // Initialize audit trail if doesn't exist
    if (!config.auditTrail) {
      config.auditTrail = [];
    }
    
    config.auditTrail.push(auditEntry);
    
    this.saveConfig(config);
    
    console.log(`✅ App reassigned: ${app.name} (${oldBU?.name} → ${newBU.name})`);
    console.log('📊 Audit entry:', auditEntry);
    
    return true;
  },
  
  getAuditTrail() {
    const config = this.loadConfig();
    return config.auditTrail || [];
  },
  
  clearAuditTrail() {
    const config = this.loadConfig();
    config.auditTrail = [];
    this.saveConfig(config);
    console.log('🗑️ Audit trail cleared');
  }
};

// Add to AdminController
const AdminController_reassignApp = {
  openReassignModal(appId) {
    console.log(`🔄 Opening reassign modal for app ${appId}`);
    
    const config = Dashboard.StorageManager.loadConfig();
    const app = config.apps.find(a => a.id === appId);
    
    if (!app) {
      console.error(`❌ App ${appId} not found`);
      return;
    }
    
    const currentBU = config.buses.find(b => b.id === app.buId);
    const otherBUs = config.buses.filter(b => b.id !== app.buId);
    
    // Create modal content
    let html = `
      <div class="reassign-modal">
        <h3>🔄 Reassign Application</h3>
        <div class="reassign-info">
          <p><strong>App:</strong> ${app.name}</p>
          <p><strong>Current BU:</strong> ${currentBU?.name || 'Unknown'}</p>
          <p><strong>Status:</strong> ${app.status} (${app.progress}%)</p>
        </div>
        <div class="reassign-selector">
          <label>Assign to Business Unit:</label>
          <div class="bu-options">
    `;
    
    otherBUs.forEach(bu => {
      const buApps = config.apps.filter(a => a.buId === bu.id).length;
      html += `
        <button class="bu-option" onclick="Dashboard.AdminController.confirmReassign(${appId}, ${bu.id})">
          <strong>${bu.name}</strong>
          <span class="app-count">${buApps} apps</span>
        </button>
      `;
    });
    
    html += `
          </div>
        </div>
        <div class="reassign-actions">
          <button class="btn btn-secondary" onclick="this.closest('.reassign-modal').remove()">Cancel</button>
        </div>
      </div>
    `;
    
    // Insert into a container or modal
    const container = document.createElement('div');
    container.className = 'reassign-container modal-overlay active';
    container.innerHTML = html;
    document.body.appendChild(container);
    
    // Close on backdrop click
    container.addEventListener('click', (e) => {
      if (e.target === container) {
        container.remove();
      }
    });
  },
  
  confirmReassign(appId, newBuId) {
    console.log(`✅ Confirming reassign: app ${appId} → BU ${newBuId}`);
    
    const success = Dashboard.StorageManager.reassignApp(appId, newBuId);
    
    if (success) {
      // Remove modal
      document.querySelector('.reassign-container')?.remove();
      
      // Refresh UI
      this.renderAppsEditor();
      Dashboard.UIController.apply();
      
      // Show notification
      const msg = `✅ App reassigned successfully`;
      console.log(msg);
      alert(msg);
    } else {
      alert('❌ Failed to reassign app');
    }
  },
  
  showAuditTrail() {
    console.log('📋 Opening audit trail');
    
    const trail = Dashboard.StorageManager.getAuditTrail();
    
    let html = `
      <div class="audit-modal">
        <h3>📋 Audit Trail</h3>
        <div class="audit-list">
    `;
    
    if (trail.length === 0) {
      html += '<p class="empty">No audit entries yet</p>';
    } else {
      trail.forEach(entry => {
        html += `
          <div class="audit-entry">
            <div class="entry-header">
              <strong>${entry.action}</strong>
              <span class="entry-time">${new Date(entry.timestamp).toLocaleString()}</span>
            </div>
            <div class="entry-details">
              <p>📱 App: <strong>${entry.appName}</strong> (Status: ${entry.status}, Progress: ${entry.progress}%)</p>
              <p>🔄 ${entry.fromBuName} → ${entry.toBuName}</p>
            </div>
          </div>
        `;
      });
    }
    
    html += `
        </div>
        <div class="audit-actions">
          <button class="btn btn-danger btn-sm" onclick="Dashboard.StorageManager.clearAuditTrail(); this.closest('.audit-modal').remove();">Clear Audit Trail</button>
          <button class="btn btn-secondary" onclick="this.closest('.audit-modal').remove()">Close</button>
        </div>
      </div>
    `;
    
    const container = document.createElement('div');
    container.className = 'audit-container modal-overlay active';
    container.innerHTML = html;
    document.body.appendChild(container);
    
    container.addEventListener('click', (e) => {
      if (e.target === container) {
        container.remove();
      }
    });
  }
};
