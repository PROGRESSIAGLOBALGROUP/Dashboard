"""
Live browser diagnostics - Debug why nothing is working
Captures console logs and analyzes the actual state
"""

import time
import json

def capture_browser_state():
    """
    This script will help us understand what's happening in the browser
    We'll check localStorage, the DATA array, and trigger various operations
    """
    
    script = """
// Step 1: Check if Dashboard object exists
console.log('=== DIAGNOSTIC START ===');
console.log('Dashboard object exists:', !!window.Dashboard);
console.log('StorageManager exists:', !!window.Dashboard?.StorageManager);
console.log('UIController exists:', !!window.Dashboard?.UIController);

// Step 2: Check localStorage structure
console.log('\\n=== LOCALSTORAGE STATE ===');
const allKeys = Object.keys(localStorage);
console.log('All localStorage keys:', allKeys);

// Step 3: Check configuration
const config = localStorage.getItem('dashboard_config_v1');
console.log('\\n=== CONFIG V1 ===');
if (config) {
  try {
    const parsed = JSON.parse(config);
    console.log('Config exists:', true);
    console.log('Formula settings:', parsed.formulaSettings);
  } catch (e) {
    console.log('ERROR parsing config:', e.message);
  }
} else {
  console.log('Config is NULL or empty');
}

// Step 4: Check DATA array
console.log('\\n=== DATA ARRAY ===');
console.log('Dashboard.DATA:', window.Dashboard?.DATA);
console.log('DATA length:', window.Dashboard?.DATA?.length || 0);

// Step 5: Check HTML checkboxes
console.log('\\n=== CHECKBOXES ===');
const checkboxes = {
  'include-tbs': document.getElementById('include-tbs'),
  'include-wip': document.getElementById('include-wip'),
  'include-clo': document.getElementById('include-clo'),
  'include-done': document.getElementById('include-done')
};

Object.entries(checkboxes).forEach(([id, elem]) => {
  if (elem) {
    console.log(`✅ ${id} exists, checked: ${elem.checked}`);
  } else {
    console.log(`❌ ${id} NOT FOUND`);
  }
});

// Step 6: Check KPI display
console.log('\\n=== KPI DISPLAY ===');
console.log('KPI Done:', document.querySelector('#kpiDone')?.textContent);
console.log('KPI WIP:', document.querySelector('#kpiWip')?.textContent);
console.log('KPI Todo:', document.querySelector('#kpiTodo')?.textContent);
console.log('KPI Avg:', document.querySelector('#kpiAvg')?.textContent);

// Step 7: Check Hero display
console.log('\\n=== HERO DISPLAY ===');
console.log('Hero %:', document.querySelector('#heroPct')?.textContent);
console.log('Hero Caption:', document.querySelector('#heroCaption')?.textContent);

console.log('\\n=== END DIAGNOSTIC ===');
    """
    
    return script

if __name__ == '__main__':
    script = capture_browser_state()
    print("Generated browser diagnostic script:")
    print("\nPaste this in browser console (F12):")
    print("=" * 80)
    print(script)
    print("=" * 80)
