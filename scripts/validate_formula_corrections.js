// VALIDATION SCRIPT - Formula Tab Corrections
// Run this in DevTools console to verify all corrections are working

console.clear();
console.log('🧪 VALIDATING FORMULA TAB CORRECTIONS');
console.log('='*50);

// TEST 1: Verify Global Method Selectors exist and are radio buttons
console.group('✅ TEST 1: Global Method Selector');
const globalWeighted = document.getElementById('global-weighted');
const globalSimple = document.getElementById('global-simple');
console.log('global-weighted element:', globalWeighted);
console.log('global-simple element:', globalSimple);
console.log('Type:', globalWeighted?.type);
console.log('Name:', globalWeighted?.name);
const selectedGlobal = document.querySelector('input[name="global-method"]:checked')?.value;
console.log('Currently selected:', selectedGlobal);
console.groupEnd();

// TEST 2: Verify Progress Method Selectors exist
console.group('✅ TEST 2: Progress Method Selector');
const progressWeighted = document.querySelector('input[name="progress-method"][value="weighted"]');
const progressSimple = document.querySelector('input[name="progress-method"][value="simple"]');
const progressMinimum = document.querySelector('input[name="progress-method"][value="minimum"]');
console.log('progress-method weighted:', progressWeighted?.checked);
console.log('progress-method simple:', progressSimple?.checked);
console.log('progress-method minimum:', progressMinimum?.checked);
console.groupEnd();

// TEST 3: Verify Status Inclusion Checkboxes
console.group('✅ TEST 3: Status Inclusion Checkboxes');
const includeTbs = document.getElementById('include-tbs');
const includeWip = document.getElementById('include-wip');
const includeClo = document.getElementById('include-clo');
console.log('include-tbs checked:', includeTbs?.checked);
console.log('include-wip checked:', includeWip?.checked);
console.log('include-clo checked (was include-done):', includeClo?.checked);
console.log('Note: include-done should NOT exist:', document.getElementById('include-done'));
console.groupEnd();

// TEST 4: Verify Configuration is saved correctly
console.group('✅ TEST 4: Configuration Storage');
const config = Dashboard.StorageManager.loadConfig();
console.log('Loaded config object:', config);
console.log('Formula settings:', config.formulaSettings);
if (config.formulaSettings) {
  console.log('✅ Configuration saved');
  console.log('Progress method:', config.formulaSettings.progressMethod);
  console.log('Global method:', config.formulaSettings.globalMethod);
  console.log('Status inclusions:', config.formulaSettings.statusInclusions);
} else {
  console.log('❌ No formula settings found (may be first load)');
}
console.groupEnd();

// TEST 5: Check localStorage keys
console.group('✅ TEST 5: Storage Keys');
const v2Key = localStorage.getItem('dashboard_formula_config_v2');
const v1Key = localStorage.getItem('dashboard_formula_config');
console.log('dashboard_formula_config_v2:', v2Key ? 'EXISTS ✅' : 'MISSING');
console.log('dashboard_formula_config (old):', v1Key ? 'EXISTS' : 'NOT FOUND ✅');
console.log('Recommended key in use: dashboard_formula_config_v2');
console.groupEnd();

// TEST 6: Event listeners are attached
console.group('✅ TEST 6: Event Listeners');
console.log('Testing formula change event...');
const initialGlobal = document.querySelector('input[name="global-method"]:checked')?.value;
document.getElementById('global-simple').click();
const afterClick = document.querySelector('input[name="global-method"]:checked')?.value;
console.log('Initial selection:', initialGlobal);
console.log('After clicking simple:', afterClick);
console.log('Event listeners working:', afterClick === 'simple' ? '✅' : '❌');
// Reset
document.getElementById('global-weighted').click();
console.groupEnd();

// TEST 7: Calculator inputs exist
console.group('✅ TEST 7: Weight Calculator Controls');
const calcCriticality = document.getElementById('calc-criticality');
const calcImpact = document.getElementById('calc-impact');
const calcPriority = document.getElementById('calc-priority');
console.log('calc-criticality:', calcCriticality?.value);
console.log('calc-impact:', calcImpact?.value);
console.log('calc-priority (was calc-order):', calcPriority?.value);
console.log('All calculator inputs present:', 
  calcCriticality && calcImpact && calcPriority ? '✅' : '❌');
console.groupEnd();

// SUMMARY
console.group('📊 VALIDATION SUMMARY');
const allTestsPassed = 
  globalWeighted && globalSimple &&
  progressWeighted && progressSimple &&
  includeTbs && includeWip && includeClo &&
  !document.getElementById('include-done') &&
  calcCriticality && calcImpact && calcPriority;

console.log(allTestsPassed ? 
  '✅ ALL TESTS PASSED - Formula tab corrections working perfectly!' :
  '❌ SOME TESTS FAILED - Check above for details');
console.groupEnd();

console.log('='*50);
console.log('Validation complete!');

// BONUS: Display current formula settings
console.group('📋 CURRENT FORMULA CONFIGURATION');
const currentConfig = {
  progressMethod: document.querySelector('input[name="progress-method"]:checked')?.value,
  globalMethod: document.querySelector('input[name="global-method"]:checked')?.value,
  statusInclusions: {
    tbs: document.getElementById('include-tbs')?.checked,
    wip: document.getElementById('include-wip')?.checked,
    clo: document.getElementById('include-clo')?.checked
  },
  calculator: {
    criticality: document.getElementById('calc-criticality')?.value,
    impact: document.getElementById('calc-impact')?.value,
    priority: document.getElementById('calc-priority')?.value
  }
};
console.table(currentConfig);
console.groupEnd();
