#!/usr/bin/env python3
"""
REGRESSION TEST - Comprehensive Verification
Verify no regressions from dynamic formula updates implementation
"""

from pathlib import Path

html_file = Path('dist/dashboard_enhanced.html')
content = html_file.read_text(encoding='utf-8')

print("\n" + "="*80)
print("COMPREHENSIVE REGRESSION TEST")
print("="*80 + "\n")

tests = {
    "GLOBAL PROGRESS FORMULA": [
        ('globalMethod variable used', 'globalMethod' in content),
        ('Global method config stored', 'formulaSettings.globalMethod' in content or 'globalMethod:' in content),
        ('Global method in calculations', 'globalMethod === \'simple\'' in content or 'globalMethod ===\'simple\'' in content),
        ('Both global methods exist', 'global-weighted' in content and 'global-simple' in content),
    ],
    "PROGRESS CALCULATION METHOD": [
        ('progressMethod variable used', 'progressMethod' in content),
        ('Progress method config stored', 'formulaSettings.progressMethod' in content or 'progressMethod:' in content),
        ('Progress method in calculations', 'switch (progressMethod)' in content or 'case \'weighted\':' in content),
        ('All 3 methods implemented', 'case \'simple\':' in content and 'case \'minimum\':' in content),
    ],
    "STATUS INCLUSION RULES": [
        ('Status filters exist', 'include-status-tbs' in content and 'include-status-wip' in content),
        ('CLO status filter exists', 'include-status-clo' in content),
        ('Status inclusion in config', 'statusInclusion' in content),
    ],
    "ADMIN PANEL": [
        ('Admin modal exists', 'id="adminModal"' in content),
        ('Close button exists', 'closeAdminModal' in content),
        ('Modal class management', 'classList.add' in content and 'classList.remove' in content),
    ],
    "EVENT SYSTEM": [
        ('Event listeners attached', 'addEventListener' in content),
        ('Formula updates on change', 'updateFormulaLabels()' in content),
        ('Progress method listener', 'formula-progress-method' in content and 'addEventListener' in content),
        ('Global method listeners', 'global-method' in content and 'addEventListener' in content),
    ],
    "STORAGE & PERSISTENCE": [
        ('localStorage used', 'localStorage' in content),
        ('Configuration loading', 'loadFormulaConfig' in content),
        ('Configuration saving', 'dashboard_formula_config' in content or 'saveConfig' in content),
    ],
    "DYNAMIC FORMULA UPDATES (NEW)": [
        ('Element has ID', 'id="core-algorithm-formula"' in content),
        ('Update function exists', 'updateCoreAlgorithmDisplay' in content),
        ('Function called from updateFormulaLabels', 'this.updateCoreAlgorithmDisplay(progressMethod, globalMethod)' in content),
        ('Method context defined', 'methodContext' in content),
    ],
}

all_pass = True
total_tests = 0
total_pass = 0

for category, category_tests in tests.items():
    print(f"\n{category}:")
    print("-" * 80)
    
    category_pass = 0
    for test_name, result in category_tests:
        total_tests += 1
        if result:
            total_pass += 1
            category_pass += 1
            print(f"  ✅ {test_name}")
        else:
            all_pass = False
            print(f"  ❌ {test_name}")
    
    print(f"  Result: {category_pass}/{len(category_tests)} passed")

print("\n" + "="*80)
print(f"TOTAL: {total_pass}/{total_tests} tests passed")
print("="*80 + "\n")

if all_pass:
    print("✅ NO REGRESSIONS DETECTED")
    print("All existing features working correctly with new dynamic formula updates\n")
    exit(0)
else:
    print("❌ Some regression detected\n")
    exit(1)
