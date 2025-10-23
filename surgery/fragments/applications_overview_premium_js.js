  // =========================
  // Applications Overview Tab - Premium Features
  // =========================
  
  renderAppsOverview() {
    this.initAppOverviewFilters();
    this.setupAppsOverviewSearch();
    this.renderAppsOverviewTable();
    this.updateAppsOverviewStats();
  },

  setupAppsOverviewSearch() {
    const searchInput = document.querySelector('#appsOverviewSearch');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.currentOverviewSearch = e.target.value.toLowerCase();
        this.renderAppsOverviewTable();
        this.updateAppsOverviewStats();
      });
    }
  },

  updateAppsOverviewStats() {
    const totalStats = document.querySelector('#statsTotal');
    const filteredStats = document.querySelector('#statsFiltered');
    const completionStats = document.querySelector('#statsCompletion');
    const countDisplay = document.querySelector('#appsCountDisplay');
    
    if (!totalStats) return;
    
    let apps = Dashboard.StorageManager.getAllApps();
    const totalCount = apps.length;
    
    // Apply filters
    let filteredApps = this.getFilteredApps();
    
    // Calculate average completion
    const avgCompletion = filteredApps.length > 0
      ? Math.round(filteredApps.reduce((sum, app) => sum + (app.progress || 0), 0) / filteredApps.length)
      : 0;
    
    totalStats.textContent = totalCount;
    filteredStats.textContent = filteredApps.length;
    completionStats.textContent = avgCompletion + '%';
    countDisplay.textContent = filteredApps.length;
  },

  getFilteredApps() {
    let apps = Dashboard.StorageManager.getAllApps();
    
    // Apply field/value filters
    if (this.currentOverviewFilters.field !== 'all' && this.currentOverviewFilters.value !== 'all') {
      const fieldToProperty = {
        'status': 'status',
        'criticality': 'criticality',
        'wave': 'wave',
        'buId': 'buId'
      };
      const field = fieldToProperty[this.currentOverviewFilters.field];
      const value = this.currentOverviewFilters.value;
      apps = apps.filter(app => String(app[field]) === String(value));
    }
    
    // Apply search filter
    if (this.currentOverviewSearch) {
      apps = apps.filter(app => 
        app.name.toLowerCase().includes(this.currentOverviewSearch) ||
        (app.wave && app.wave.toLowerCase().includes(this.currentOverviewSearch)) ||
        app.id.toString().includes(this.currentOverviewSearch)
      );
    }
    
    return apps;
  },

  renderAppsOverviewTable() {
    const tableBody = document.querySelector('#appsOverviewTableBody');
    const emptyState = document.querySelector('#emptyState');
    if (!tableBody) return;
    
    let apps = this.getFilteredApps();
    
    // Apply sorting
    if (this.currentSort.column) {
      const { column, direction } = this.currentSort;
      const columnToProperty = {
        'ID': 'id',
        'BU': 'buId',
        'Wave': 'wave',
        'App Name': 'name',
        'Priority': 'priority',
        'Criticality': 'criticality',
        'Business Impact': 'impact',
        'Completion': 'progress',
        'Status': 'status'
      };
      
      const propertyName = columnToProperty[column];
      apps.sort((a, b) => {
        const aValue = a[propertyName] || '';
        const bValue = b[propertyName] || '';
        
        if (propertyName === 'progress' || propertyName === 'id' || propertyName === 'buId') {
          const aNum = parseInt(aValue) || 0;
          const bNum = parseInt(bValue) || 0;
          return direction === 'asc' ? (aNum - bNum) : (bNum - aNum);
        } else {
          return direction === 'asc' 
            ? aValue.toString().localeCompare(bValue.toString())
            : bValue.toString().localeCompare(aValue.toString());
        }
      });
    }
    
    let html = '';
    if (apps.length === 0) {
      html = '<tr style="background: var(--bg-2);"><td colspan="9" style="text-align:center;padding:40px;"><div class="empty-state-icon">🔍</div><div class="empty-state-title">No applications found</div><div class="empty-state-description">Try adjusting your filters or search criteria</div></td></tr>';
    } else {
      const validApps = apps.filter(app => app.id && app.name && app.buId !== undefined);
      validApps.forEach(app => {
        const bu = Dashboard.StorageManager.getBUById(app.buId);
        const buName = bu ? bu.name : app.buId;
        
        const criticality = app.criticality || 'Medium';
        const priority = app.priority || 'Medium';
        const status = app.status || 'TBS';
        
        const rowClass = criticality === 'High' ? 'high' : (criticality === 'Critical' ? 'critical' : 'medium');
        
        const priorityBadge = `<span class="priority-badge-premium ${priority.toLowerCase()}">${this.getPriorityEmoji(priority)} ${priority}</span>`;
        const criticalityBadge = `<span class="criticality-badge-premium ${criticality.toLowerCase()}">${this.getCriticalityEmoji(criticality)} ${criticality}</span>`;
        const statusBadge = `<span class="status-badge-premium ${status.toLowerCase()}">${this.getStatusEmoji(status)} ${status}</span>`;
        
        const progressBar = `<div class="progress-container"><div class="progress-label"><span class="progress-percentage">${app.progress || 0}%</span></div><div class="progress-bar-premium shimmer"><div class="progress-value-premium" style="width: ${app.progress || 0}%"></div></div></div>`;
        
        html += `<tr class="${rowClass}"><td>${app.id}</td><td title="${buName}">${buName}</td><td>${app.wave || '-'}</td><td>${app.name}</td><td>${priorityBadge}</td><td>${criticalityBadge}</td><td>${app.impact || 'Medium'}</td><td class="progress-cell-premium">${progressBar}</td><td>${statusBadge}</td></tr>`;
      });
    }
    
    tableBody.innerHTML = html;
    
    // Update empty state visibility
    if (apps.length === 0) {
      if (emptyState) emptyState.style.display = 'flex';
    } else {
      if (emptyState) emptyState.style.display = 'none';
    }
    
    this.updateFilterBadges();
  },

  sortAppsOverview(columnName, columnIndex) {
    const headers = document.querySelectorAll('#appsOverviewTable th');
    
    headers.forEach(header => {
      header.classList.remove('sort-asc', 'sort-desc');
    });
    
    if (this.currentSort.column === columnName) {
      this.currentSort.direction = this.currentSort.direction === 'asc' ? 'desc' : 'asc';
    } else {
      this.currentSort.column = columnName;
      this.currentSort.direction = 'asc';
    }
    
    headers[columnIndex].classList.add(
      this.currentSort.direction === 'asc' ? 'sort-asc' : 'sort-desc'
    );
    
    this.renderAppsOverviewTable();
  },

  getPriorityEmoji(priority) {
    return priority === 'High' ? '🔴' : (priority === 'Low' ? '🟢' : '🟡');
  },

  getCriticalityEmoji(criticality) {
    return criticality === 'Critical' ? '🔴' : (criticality === 'High' ? '⚠️' : '✅');
  },

  getStatusEmoji(status) {
    return status === 'CLO' ? '✅' : (status === 'WIP' ? '⏱️' : '📋');
  },

  updateFilterBadges() {
    const container = document.querySelector('#activeFiltersBadges');
    const list = document.querySelector('#activeFiltersList');
    
    if (!container || !list) return;
    
    const hasFilters = (this.currentOverviewFilters.field !== 'all' && this.currentOverviewFilters.value !== 'all') || this.currentOverviewSearch;
    
    if (hasFilters) {
      container.style.display = 'flex';
      let badges = '';
      
      if (this.currentOverviewSearch) {
        badges += `<span class="active-filter-badge">🔎 "<strong>${this.currentOverviewSearch}</strong>" <span class="remove-filter" onclick="Dashboard.AdminController.clearSearch()">✕</span></span>`;
      }
      
      if (this.currentOverviewFilters.field !== 'all' && this.currentOverviewFilters.value !== 'all') {
        const fieldLabel = this.currentOverviewFilters.field;
        badges += `<span class="active-filter-badge">${fieldLabel}: <strong>${this.currentOverviewFilters.value}</strong> <span class="remove-filter" onclick="Dashboard.AdminController.clearFieldFilter()">✕</span></span>`;
      }
      
      list.innerHTML = badges;
    } else {
      container.style.display = 'none';
    }
  },

  clearSearch() {
    const searchInput = document.querySelector('#appsOverviewSearch');
    if (searchInput) searchInput.value = '';
    this.currentOverviewSearch = '';
    this.renderAppsOverviewTable();
    this.updateAppsOverviewStats();
  },

  clearFieldFilter() {
    this.currentOverviewFilters = { field: 'all', value: 'all' };
    const filterField = document.querySelector('#overviewFilterField');
    const filterValue = document.querySelector('#overviewFilterValue');
    if (filterField) filterField.value = 'all';
    if (filterValue) filterValue.value = 'all';
    this.renderAppsOverviewTable();
    this.updateAppsOverviewStats();
  }
