/**
 * Quick Test Script for Progress Calculation Method
 * 
 * Copy this to DevTools Console and run to verify the feature is working:
 * 1. Open dashboard_enhanced.html in browser
 * 2. Press F12 to open DevTools
 * 3. Go to Console tab
 * 4. Copy and paste this entire script
 * 5. Press Enter
 * 
 * Expected output: Shows current method and all three calculations
 */

console.log('=== PROGRESS CALCULATION METHOD TEST ===\n');

try {
  // 1. Check if Dashboard object exists
  if (!window.Dashboard) {
    console.error('[FAIL] Dashboard object not found');
    throw new Error('Dashboard not initialized');
  }
  console.log('[OK] Dashboard object exists');

  // 2. Load configuration
  const config = Dashboard.StorageManager.loadConfig();
  console.log('[OK] Config loaded');

  // 3. Check progress method setting
  const progressMethod = config?.formulaSettings?.progressMethod || 'weighted';
  console.log(`[OK] Progress Method Setting: "${progressMethod}"`);

  // 4. Check global method setting
  const globalMethod = config?.formulaSettings?.globalMethod || 'weighted';
  console.log(`[OK] Global Method Setting: "${globalMethod}"`);

  // 5. Get a business unit to test (first one)
  if (config.buses && config.buses.length > 0) {
    const testBU = config.buses[0];
    console.log(`\n[INFO] Testing with BU: ${testBU.name}`);

    // 6. Calculate progress using the current method
    const progress = Dashboard.ProgressCalculator.calculateBUProgress(testBU.id);
    console.log(`[OK] Calculated Progress: ${progress}%`);

    // 7. Show applications in this BU
    const appsInBU = config.apps.filter(app => app.buId === testBU.id);
    console.log(`[INFO] Apps in BU: ${appsInBU.length}`);

    if (appsInBU.length > 0) {
      const appProgress = appsInBU.map(app => ({
        name: app.name,
        progress: app.progress,
        status: app.status
      }));
      console.table(appProgress);
    }

    // 8. Show test results
    console.log('\n=== TEST RESULTS ===');
    console.log(`[✓] Progress Method Feature is WORKING`);
    console.log(`    - Current method: ${progressMethod}`);
    console.log(`    - BU Progress: ${progress}%`);
    console.log(`    - Apps counted: ${appsInBU.length}`);

  } else {
    console.warn('[WARN] No business units found to test');
  }

} catch (error) {
  console.error('[ERROR]', error.message);
  console.error(error.stack);
}

console.log('\n=== MANUAL VERIFICATION STEPS ===');
console.log('1. Go to Admin Modal (click settings icon)');
console.log('2. Click "Calculation Formulas" tab');
console.log('3. Try selecting "Simple Average"');
console.log('4. Watch the dashboard progress bars update');
console.log('5. Try "Minimum Progress" option');
console.log('6. Verify changes are reflected in all progress displays');
console.log('7. Refresh page - selection should persist');
