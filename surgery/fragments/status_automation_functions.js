// ========== STATUS AUTOMATION FUNCTIONS ==========
// These functions implement smart status transitions based on progress percentage

progressChangeHandler(appId, newProgress, oldProgress = null) {
  // Get current app to find old progress if not provided
  const app = Dashboard.StorageManager.getAllApps().find(a => a.id === appId);
  if (!app) return;
  
  oldProgress = oldProgress !== null ? oldProgress : (app.progress || 0);
  newProgress = parseInt(newProgress) || 0;
  
  // Clamp values
  if (newProgress < 0) newProgress = 0;
  if (newProgress > 100) newProgress = 100;
  
  // State machine logic
  if (oldProgress === 0 && newProgress === 0) {
    // No change, stay at TBS
    return;
  }
  
  if (newProgress === 0) {
    // Revert to TBS (always auto, no confirmation)
    this.handleStatusTransition(appId, 'TBS', 0);
    return;
  }
  
  if (oldProgress === 0 && newProgress > 0 && newProgress < 100) {
    // Transition from 0 to [1-99]: ask to start application
    this.showStatusConfirmation(appId, 'start', newProgress, app.name);
    return;
  }
  
  if (oldProgress > 0 && oldProgress < 100 && newProgress === 100) {
    // Transition to 100: ask to mark as complete
    this.showStatusConfirmation(appId, 'complete', newProgress, app.name);
    return;
  }
  
  if (newProgress >= 1 && newProgress < 100) {
    // Within [1-99] range: ensure status is WIP
    if (app.status !== 'WIP') {
      Dashboard.StorageManager.updateApp(appId, { progress: newProgress, status: 'WIP' });
      this.renderAppsEditor();
      Dashboard.UIController.apply();
    } else {
      Dashboard.StorageManager.updateApp(appId, { progress: newProgress });
      this.renderAppsEditor();
      Dashboard.UIController.apply();
    }
    return;
  }
  
  if (newProgress === 100) {
    // At 100%, keep CLO
    if (app.status !== 'CLO') {
      Dashboard.StorageManager.updateApp(appId, { progress: 100, status: 'CLO' });
    } else {
      Dashboard.StorageManager.updateApp(appId, { progress: 100 });
    }
    this.renderAppsEditor();
    Dashboard.UIController.apply();
    return;
  }
},

showStatusConfirmation(appId, type, newProgress, appName = '') {
  const modal = document.getElementById('statusConfirmationModal');
  const titleEl = document.getElementById('confirmTitle');
  const messageEl = document.getElementById('confirmMessage');
  const yesBtn = document.getElementById('confirmYes');
  const noBtn = document.getElementById('confirmNo');
  
  if (!modal || !titleEl || !messageEl || !yesBtn || !noBtn) {
    console.error('Status confirmation modal elements not found');
    return;
  }
  
  let title, message, newStatus;
  
  if (type === 'start') {
    title = '🚀 Start Application?';
    message = `Ready to start "${appName}"? This will change status from <strong>TBS</strong> to <strong>WIP</strong>.`;
    newStatus = 'WIP';
  } else if (type === 'complete') {
    title = '✅ Mark as Complete?';
    message = `Ready to mark "${appName}" as complete? This will change status from <strong>WIP</strong> to <strong>CLO</strong>.`;
    newStatus = 'CLO';
  } else {
    return;
  }
  
  titleEl.textContent = title;
  messageEl.innerHTML = message;
  
  // Clear previous event listeners by cloning
  const newYesBtn = yesBtn.cloneNode(true);
  const newNoBtn = noBtn.cloneNode(true);
  yesBtn.parentNode.replaceChild(newYesBtn, yesBtn);
  noBtn.parentNode.replaceChild(newNoBtn, noBtn);
  
  const updatedYesBtn = document.getElementById('confirmYes');
  const updatedNoBtn = document.getElementById('confirmNo');
  
  // YES handler
  updatedYesBtn.addEventListener('click', () => {
    this.handleStatusTransition(appId, newStatus, newProgress);
    modal.classList.remove('active');
  });
  
  // NO handler
  updatedNoBtn.addEventListener('click', () => {
    modal.classList.remove('active');
    // Revert the input value in the table
    const appRow = document.querySelector(`tr[data-app-id="${appId}"]`);
    if (appRow) {
      const progressInput = appRow.querySelector('input[type="number"]');
      if (progressInput) {
        const app = Dashboard.StorageManager.getAllApps().find(a => a.id === appId);
        progressInput.value = app.progress || 0;
      }
    }
  });
  
  // Show modal
  modal.classList.add('active');
},

handleStatusTransition(appId, newStatus, newProgress) {
  Dashboard.StorageManager.updateApp(appId, {
    status: newStatus,
    progress: newProgress
  });
  this.renderAppsEditor();
  Dashboard.UIController.apply();
},

// ========== END STATUS AUTOMATION FUNCTIONS ==========
