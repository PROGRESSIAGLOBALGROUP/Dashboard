"""
Generate debug script for browser console
"""

script = """
// ========== BROWSER CONSOLE DEBUG SCRIPT ==========
// Paste this entire script in browser console (F12 → Console)
// It will tell us exactly what's happening

console.clear();
console.log('%c🔍 DASHBOARD DEBUG STARTED', 'color: #5b9dff; font-size: 16px; font-weight: bold');

// 1. Check if Dashboard object exists
console.log('%c1️⃣ Checking Dashboard object...', 'color: #ffd166; font-weight: bold');
if (window.Dashboard) {
  console.log('✅ Dashboard object exists');
  console.log('   - StorageManager:', !!window.Dashboard.StorageManager);
  console.log('   - UIController:', !!window.Dashboard.UIController);
  console.log('   - AdminController:', !!window.Dashboard.AdminController);
  console.log('   - DATA array:', Array.isArray(window.Dashboard.DATA), 'length:', window.Dashboard.DATA?.length);
} else {
  console.log('❌ Dashboard object MISSING - scripts didn\'t load properly');
}

// 2. Check if apply() was called
console.log('%c2️⃣ Checking if apply() was called...', 'color: #ffd166; font-weight: bold');
if (document.querySelector('#kpiAvg')?.textContent) {
  console.log('✅ KPI display has content:', document.querySelector('#kpiAvg').textContent);
} else {
  console.log('❌ KPI display is empty - apply() may not have been called');
}

// 3. Check localStorage
console.log('%c3️⃣ Checking localStorage...', 'color: #ffd166; font-weight: bold');
const config = JSON.parse(localStorage.getItem('dashboard_config_v1') || 'null');
if (config) {
  console.log('✅ Configuration loaded from localStorage');
  console.log('   - BUs:', config.buses?.length);
  console.log('   - Apps:', config.apps?.length);
  console.log('   - Formula:', config.formulaSettings?.globalMethod);
} else {
  console.log('⚠️ No configuration in localStorage - dashboard will show empty');
}

// 4. Check DATA array
console.log('%c4️⃣ Checking DATA array...', 'color: #ffd166; font-weight: bold');
if (window.Dashboard?.DATA?.length > 0) {
  console.log('✅ DATA array has items:');
  window.Dashboard.DATA.forEach(d => {
    console.log(`   - ${d.name}: ${d.progress}% (${d.appCount} apps)`);
  });
} else {
  console.log('❌ DATA array is empty or not initialized');
}

// 5. Check checkboxes
console.log('%c5️⃣ Checking status inclusion checkboxes...', 'color: #ffd166; font-weight: bold');
const checkboxes = {
  'include-tbs': document.getElementById('include-tbs'),
  'include-wip': document.getElementById('include-wip'),
  'include-clo': document.getElementById('include-clo')
};
Object.entries(checkboxes).forEach(([id, elem]) => {
  if (elem) {
    console.log(`✅ ${id}: ${elem.checked ? 'checked' : 'unchecked'}`);
  } else {
    console.log(`❌ ${id}: MISSING`);
  }
});

// 6. Call apply() manually to test
console.log('%c6️⃣ Attempting to call apply() manually...', 'color: #ff5f7a; font-weight: bold');
try {
  if (window.Dashboard?.UIController?.apply) {
    console.log('Calling apply()...');
    window.Dashboard.UIController.apply();
    console.log('✅ apply() executed successfully');
    
    // Check if display updated
    setTimeout(() => {
      const kpiValue = document.querySelector('#kpiAvg')?.textContent;
      if (kpiValue) {
        console.log('✅ Dashboard updated! KPI:', kpiValue);
      } else {
        console.log('⚠️ apply() ran but display may not have updated');
      }
    }, 100);
  } else {
    console.log('❌ apply() method not found');
  }
} catch (error) {
  console.log('❌ Error calling apply():', error.message);
  console.error(error);
}

console.log('%c✅ DEBUG COMPLETE', 'color: #32e685; font-size: 14px; font-weight: bold');
console.log('Check the output above to see what\'s working and what\'s not');
"""

print("\n" + "="*80)
print("BROWSER DEBUG SCRIPT")
print("="*80)
print("\n📋 Copy this entire script and paste it into browser console (F12):\n")
print(script)
print("\n" + "="*80)
print("This script will tell us exactly what's initialized and what's not")
print("="*80 + "\n")
