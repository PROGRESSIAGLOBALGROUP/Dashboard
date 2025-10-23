/* ===== APPLICATIONS OVERVIEW - WORLD CLASS LOGIC ===== */

// Namespace
const AppsOverviewWorldClass = {
  
  currentFilter: { wave: null, status: null, search: '' },
  allAppsData: [],
  
  /**
   * Initialize world-class applications overview
   */
  init() {
    console.log('[AppsOverviewWorldClass] Initializing...');
    
    // Bind event listeners
    this.bindEvents();
    
    // Load initial data
    this.refresh();
    
    console.log('[AppsOverviewWorldClass] Ready');
  },
  
  /**
   * Bind all event listeners
   */
  bindEvents() {
    // Search input
    const searchInput = document.getElementById('appsOverviewSearch');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.currentFilter.search = e.target.value.toLowerCase();
        this.render();
      });
    }
    
    // Status filter pills
    document.querySelectorAll('.status-pill-filter').forEach(btn => {
      btn.addEventListener('click', (e) => {
        document.querySelectorAll('.status-pill-filter').forEach(b => b.classList.remove('active'));
        e.target.closest('button').classList.add('active');
        this.currentFilter.status = e.target.closest('button').dataset.status === 'all' ? null : e.target.closest('button').dataset.status;
        this.render();
      });
    });
    
    // Set initial status filter
    document.querySelector('.status-pill-filter[data-status="all"]').classList.add('active');
  },
  
  /**
   * Refresh data from Dashboard
   */
  refresh() {
    try {
      const config = Dashboard.StorageManager.loadConfig();
      
      // Build comprehensive apps data
      this.allAppsData = (config.apps || []).map(app => {
        const bu = (config.buses || []).find(b => b.id === app.buId);
        return {
          ...app,
          buName: bu?.name || 'N/A',
          buKey: bu?.key || 'N/A'
        };
      });
      
      this.render();
    } catch (error) {
      console.error('[AppsOverviewWorldClass] Error refreshing:', error);
    }
  },
  
  /**
   * Render overview
   */
  render() {
    // Filter data
    const filteredData = this.filterData();
    
    // Update metrics
    this.updateMetrics(filteredData);
    
    // Update charts
    this.updateCharts(filteredData);
    
    // Update table
    this.renderTable(filteredData);
  },
  
  /**
   * Filter data based on current filters
   */
  filterData() {
    return this.allAppsData.filter(app => {
      // Search filter
      if (this.currentFilter.search) {
        const search = this.currentFilter.search;
        const match = (
          app.name?.toLowerCase().includes(search) ||
          app.buName?.toLowerCase().includes(search) ||
          app.buKey?.toLowerCase().includes(search) ||
          app.id?.toLowerCase().includes(search)
        );
        if (!match) return false;
      }
      
      // Status filter
      if (this.currentFilter.status) {
        if (app.status !== this.currentFilter.status) return false;
      }
      
      // Wave filter
      if (this.currentFilter.wave) {
        if (app.wave !== this.currentFilter.wave) return false;
      }
      
      return true;
    });
  },
  
  /**
   * Update KPI metrics
   */
  updateMetrics(filtered) {
    const total = this.allAppsData.length;
    const count = filtered.length;
    const completion = count > 0 ? Math.round(filtered.reduce((sum, a) => sum + (a.progress || 0), 0) / count) : 0;
    
    // Total apps
    document.getElementById('statsTotalApps').textContent = total;
    
    // Completion
    document.getElementById('statsCompletionPct').textContent = completion;
    
    // At risk (< 50% progress)
    const atRisk = filtered.filter(a => (a.progress || 0) < 50).length;
    document.getElementById('statsAtRisk').textContent = atRisk;
    
    // Wave counts
    const wave1 = filtered.filter(a => a.wave === 'Wave 1').length;
    const wave2 = filtered.filter(a => a.wave === 'Wave 2').length;
    const wave3 = filtered.filter(a => a.wave === 'Wave 3').length;
    
    document.getElementById('waveCount1').textContent = wave1;
    document.getElementById('waveCount2').textContent = wave2;
    document.getElementById('waveCount3').textContent = wave3;
    
    // Completion min/max
    if (filtered.length > 0) {
      const progressValues = filtered.map(a => a.progress || 0);
      document.getElementById('completionMin').textContent = Math.min(...progressValues);
      document.getElementById('completionMax').textContent = Math.max(...progressValues);
    }
    
    // Table info
    document.getElementById('appsCountDisplay').textContent = count;
    document.getElementById('appsTotalDisplay').textContent = total;
  },
  
  /**
   * Update mini charts
   */
  updateCharts(filtered) {
    // Wave distribution
    if (filtered.length > 0) {
      const w1 = filtered.filter(a => a.wave === 'Wave 1').length;
      const w2 = filtered.filter(a => a.wave === 'Wave 2').length;
      const w3 = filtered.filter(a => a.wave === 'Wave 3').length;
      const max = Math.max(w1, w2, w3, 1);
      
      const waveChart = document.getElementById('waveDistChart');
      if (waveChart) {
        waveChart.innerHTML = `
          <div style="flex: 1; background: rgba(50,230,133,0.3); height: ${Math.round(w1/max*100)}%; border-radius: 2px; min-height: 4px;" title="Wave 1: ${w1}"></div>
          <div style="flex: 1; background: rgba(255,209,102,0.3); height: ${Math.round(w2/max*100)}%; border-radius: 2px; min-height: 4px;" title="Wave 2: ${w2}"></div>
          <div style="flex: 1; background: rgba(91,157,255,0.3); height: ${Math.round(w3/max*100)}%; border-radius: 2px; min-height: 4px;" title="Wave 3: ${w3}"></div>
        `;
      }
    }
    
    // Status breakdown
    if (filtered.length > 0) {
      const clo = filtered.filter(a => a.status === 'CLO').length;
      const wip = filtered.filter(a => a.status === 'WIP').length;
      const tbs = filtered.filter(a => a.status === 'TBS').length;
      const max = Math.max(clo, wip, tbs, 1);
      
      const statusChart = document.getElementById('statusBreakChart');
      if (statusChart) {
        statusChart.innerHTML = `
          <div style="flex: 1; background: rgba(50,230,133,0.4); border-radius: 2px; position: relative;" title="Complete: ${clo}"><span style="position: absolute; bottom: -18px; font-size: 10px; color: #32e685; left: 0; right: 0; text-align: center;">${clo}</span></div>
          <div style="flex: 1; background: rgba(255,209,102,0.4); border-radius: 2px; position: relative;" title="In Progress: ${wip}"><span style="position: absolute; bottom: -18px; font-size: 10px; color: #ffd166; left: 0; right: 0; text-align: center;">${wip}</span></div>
          <div style="flex: 1; background: rgba(255,95,122,0.4); border-radius: 2px; position: relative;" title="To Start: ${tbs}"><span style="position: absolute; bottom: -18px; font-size: 10px; color: #ff5f7a; left: 0; right: 0; text-align: center;">${tbs}</span></div>
        `;
      }
    }
  },
  
  /**
   * Render table
   */
  renderTable(filtered) {
    const tbody = document.getElementById('appsOverviewTableBody');
    const emptyState = document.getElementById('emptyState');
    
    if (!tbody) return;
    
    if (filtered.length === 0) {
      tbody.innerHTML = '';
      emptyState.style.display = 'block';
      return;
    }
    
    emptyState.style.display = 'none';
    
    tbody.innerHTML = filtered.map(app => {
      const isAtRisk = (app.progress || 0) < 50 && app.status !== 'CLO';
      const isCritical = (app.progress || 0) < 30 && app.status === 'WIP';
      const isComplete = app.status === 'CLO';
      
      let rowClass = 'complete-row';
      if (isCritical) rowClass = 'critical-row';
      else if (isAtRisk) rowClass = 'at-risk-row';
      
      const statusEmoji = app.status === 'CLO' ? '✓' : app.status === 'WIP' ? '🔄' : '⏳';
      const statusClass = app.status?.toLowerCase() || 'tbs';
      
      const waveClass = `wave-${app.wave?.split(' ')[1] || '1'}`;
      
      const factors = [
        app.criticality && { label: app.criticality, class: 'critical' },
        app.impact && { label: app.impact, class: 'impact' },
        app.priority && { label: app.priority, class: 'priority' }
      ].filter(Boolean);
      
      return `
        <tr class="${rowClass}">
          <td>${app.order || '-'}</td>
          <td>
            <div style="font-weight: 600; color: var(--text);">${app.name}</div>
            <div style="font-size: 11px; color: #aaa;">ID: ${app.id || '-'}</div>
          </td>
          <td><strong>${app.buKey}</strong></td>
          <td style="text-align: center;">
            <span class="wave-badge ${waveClass}">${app.wave || 'Wave 1'}</span>
          </td>
          <td style="text-align: center;">
            <strong style="color: #5b9dff;">${(app.weight || 0).toFixed(2)}</strong>
          </td>
          <td>
            <div class="factors-cell">
              ${factors.map(f => `<span class="factor-badge ${f.class?.toLowerCase()}">${f.label}</span>`).join('')}
            </div>
          </td>
          <td>
            <div class="progress-sparkline">
              <div class="progress-bar-container">
                <div class="progress-bar-fill" style="width: ${app.progress || 0}%"></div>
              </div>
              <span class="progress-value">${app.progress || 0}%</span>
            </div>
          </td>
          <td style="text-align: center;">
            <span class="status-badge-inline ${statusClass}">
              ${statusEmoji} ${app.status || 'TBS'}
            </span>
          </td>
        </tr>
      `;
    }).join('');
  }
};

// Auto-initialize when modal is opened
document.addEventListener('DOMContentLoaded', () => {
  // Hook into admin modal open
  const originalOpenModal = (window.Dashboard?.AdminController?.openModal || function(){});
  window.Dashboard = window.Dashboard || {};
  window.Dashboard.AdminController = window.Dashboard.AdminController || {};
  
  const wrappedOpenModal = function() {
    originalOpenModal.apply(this, arguments);
    setTimeout(() => {
      if (document.getElementById('tab-app-overview').style.display === 'block' || 
          document.getElementById('tab-app-overview').classList.contains('active')) {
        AppsOverviewWorldClass.init();
      }
    }, 100);
  };
  
  // Also initialize on tab click
  const tabButtons = document.querySelectorAll('[data-tab="app-overview"]');
  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      setTimeout(() => AppsOverviewWorldClass.init(), 50);
    });
  });
});

// Export to global
window.AppsOverviewWorldClass = AppsOverviewWorldClass;
