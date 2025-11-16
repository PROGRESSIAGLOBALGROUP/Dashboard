/**
 * BROWSER VERIFICATION SCRIPT - Clear All Data Fix
 * 
 * Usage: Copy-paste this into Browser DevTools Console AFTER the page loads
 * 
 * Scenarios:
 * 1. Fresh load: Should show data loaded from EMBEDDED_DATA
 * 2. After clicking Clear All Data: localStorage should be empty except flag
 * 3. After reload: Should stay empty if flag persists
 */

console.clear();
console.log("=" * 60);
console.log("CLEAR ALL DATA FIX - BROWSER VERIFICATION");
console.log("=" * 60);

const STORAGE_KEY = 'dashboard_config_v1';
const MANUAL_CLEAR_FLAG = 'dashboard_user_manually_cleared_v1';

// ==================================================
// UTILITY FUNCTIONS
// ==================================================

function getStorageStatus() {
  const config = localStorage.getItem(STORAGE_KEY);
  const flag = localStorage.getItem(MANUAL_CLEAR_FLAG);
  const allKeys = Object.keys(localStorage);
  
  return {
    configExists: config !== null,
    flagExists: flag !== null,
    configSize: config ? JSON.parse(config).buses.length : 0,
    allStorageKeys: allKeys,
    totalStorageItems: allKeys.length
  };
}

function getDashboardState() {
  return {
    DATA_array: window.Dashboard?.DATA || [],
    StorageManager: window.Dashboard?.StorageManager !== undefined,
    DataLoader: window.Dashboard?.DataLoader !== undefined,
    BUs: window.Dashboard?.StorageManager?.getBUs?.() || []
  };
}

// ==================================================
// VERIFICATION CHECKS
// ==================================================

console.log("\n📊 CURRENT STATE:");
console.log("─" * 50);

const storage = getStorageStatus();
const dashboard = getDashboardState();

console.log("\n🔍 localStorage Status:");
console.log(`  • Config exists: ${storage.configExists}`);
console.log(`  • Manual clear flag exists: ${storage.flagExists}`);
console.log(`  • Business Units in config: ${storage.configSize}`);
console.log(`  • Total localStorage items: ${storage.totalStorageItems}`);
console.log(`  • Storage keys:`, storage.allStorageKeys);

console.log("\n🔍 Dashboard State:");
console.log(`  • DATA array length: ${dashboard.DATA_array.length}`);
console.log(`  • StorageManager available: ${dashboard.StorageManager}`);
console.log(`  • DataLoader available: ${dashboard.DataLoader}`);
console.log(`  • Business Units from storage: ${dashboard.BUs.length}`);

// ==================================================
// CRITICAL CHECKS
// ==================================================

console.log("\n🚨 CRITICAL CHECKS:");
console.log("─" * 50);

if (storage.flagExists) {
  const flagData = JSON.parse(localStorage.getItem(MANUAL_CLEAR_FLAG));
  console.log("✅ Manual clear flag IS SET");
  console.log(`   Timestamp: ${flagData.timestamp}`);
  console.log(`   Reason: ${flagData.reason}`);
  
  if (!storage.configExists) {
    console.log("✅ Config data IS EMPTY (as expected after Clear All Data)");
  } else {
    console.log("❌ ERROR: Config data still exists despite clear flag!");
  }
} else {
  console.log("ℹ️  No manual clear flag (normal for fresh load)");
  
  if (storage.configExists) {
    console.log("✅ Config data exists (normal for fresh load)");
    console.log(`   Business Units loaded: ${storage.configSize}`);
  } else {
    console.log("⚠️  No config data and no clear flag - dashboard is empty");
  }
}

// ==================================================
// ACTION MENU
// ==================================================

console.log("\n📋 AVAILABLE ACTIONS:");
console.log("─" * 50);
console.log(`
1. SIMULATE CLEAR ALL DATA:
   → In browser, click "Clear All Data" button in Settings tab
   → This should set the manual clear flag and empty localStorage
   → Then check: checkStorageAfterClear()

2. VERIFY AFTER CLEAR:
   → After clicking Clear, run: checkStorageAfterClear()
   → Should show: flag exists, config empty, no BUs

3. VERIFY AFTER RELOAD:
   → After page reload, run: checkStorageAfterReload()
   → Should show: flag still exists, config still empty, no BUs

4. FULL FLOW TEST:
   → Run: testFullClearFlow()
   → Shows complete before/after comparison
`);

// ==================================================
// TEST FUNCTIONS (runnable from console)
// ==================================================

window.checkStorageAfterClear = function() {
  console.log("\n🔍 POST-CLEAR CHECK:");
  const status = getStorageStatus();
  
  if (status.flagExists && !status.configExists) {
    console.log("✅ SUCCESS: Clear All Data worked correctly!");
    console.log(`   • Manual clear flag: SET`);
    console.log(`   • Config data: EMPTY`);
    console.log(`   • Ready for reload test...`);
  } else {
    console.log("❌ FAILURE: Clear All Data did NOT work!");
    console.log(`   • Flag exists: ${status.flagExists} (should be true)`);
    console.log(`   • Config exists: ${status.configExists} (should be false)`);
  }
};

window.checkStorageAfterReload = function() {
  console.log("\n🔍 POST-RELOAD CHECK:");
  const status = getStorageStatus();
  const dashboard = getDashboardState();
  
  if (status.flagExists && !status.configExists && dashboard.BUs.length === 0) {
    console.log("✅ PERFECT: Dashboard stayed empty after reload!");
    console.log(`   • Manual clear flag: ${status.flagExists ? 'STILL SET' : 'MISSING'}`);
    console.log(`   • Config data: STILL EMPTY`);
    console.log(`   • Business Units: 0 (correct)`);
    console.log(`   • Fix is WORKING! ✨`);
  } else {
    console.log("❌ PROBLEM: Dashboard data was restored!");
    console.log(`   • Manual clear flag: ${status.flagExists}`);
    console.log(`   • Config exists: ${status.configExists} (should be false)`);
    console.log(`   • Business Units: ${dashboard.BUs.length} (should be 0)`);
  }
};

window.testFullClearFlow = function() {
  console.log("\n" + "=" * 60);
  console.log("FULL CLEAR FLOW TEST");
  console.log("=" * 60);
  
  const before = getStorageStatus();
  console.log("\n📌 BEFORE CLEAR:");
  console.log(`   • Config data: ${before.configExists ? `EXISTS (${before.configSize} BUs)` : 'EMPTY'}`);
  console.log(`   • Clear flag: ${before.flagExists ? 'SET' : 'NOT SET'}`);
  
  console.log("\n⏳ [User clicks 'Clear All Data' button]");
  console.log("   Waiting for action...");
  console.log("\n   Then run: checkStorageAfterClear()");
};

console.log("\n✅ Script loaded. Use functions above to test!");
console.log("   • checkStorageAfterClear()");
console.log("   • checkStorageAfterReload()");
console.log("   • testFullClearFlow()");
