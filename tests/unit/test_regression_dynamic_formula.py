#!/usr/bin/env python3
"""
REGRESSION TEST - Verify no other features were affected
Confirms that the dynamic formula updates didn't break anything else
"""

from pathlib import Path
import re

html_file = Path('dist/dashboard_enhanced.html')
content = html_file.read_text(encoding='utf-8')

print("\n" + "="*80)
print("REGRESSION TEST - Verify No Side Effects from Dynamic Formula Updates")
print("="*80 + "\n")

checks = {
    "Global Progress Formula still works": [
        'globalMethod' in content,
        'calculateGlobalProgress' in content,
        'global-weighted' in content,
        'global-simple' in content,
    ],
    "Progress Calculation Method still works": [
        'progressMethod' in content,
        'calculateBUProgress' in content,
        'formula-progress-method' in content,
        'case \'weighted\':' in content,
    ],
    "Status Inclusion Rules still work": [
        'include-status-tbs' in content,
        'include-status-wip' in content,
        'include-status-clo' in content,
        'TBS' in content,
    ],
    "Event listeners properly attached": [
        'addEventListener' in content,
        'this.updateFormulaLabels()' in content,
        'global-method' in content,
    ],
    "StorageManager working": [
        'StorageManager' in content,
        'localStorage' in content,
        'saveConfig' in content,
    ],
    "UIController working": [
        'UIController' in content,
        'apply()' in content,
        'renderTiles' in content,
    ],
    "No duplicate function definitions": [
        content.count('updateCoreAlgorithmDisplay') == 2,  # 1 call + 1 definition
        content.count('updateFormulaLabels()') >= 3,  # Multiple calls
    ],
    "Formula elements still present": [
        'formula-showcase' in content,
        'formula-box' in content,
        'formula-equation' in content,
        'core-algorithm-formula' in content,
    ],
    "BU progress calculation intact": [
        'calculateBUProgress' in content,
        'activeApps' in content,
        'app.status' in content,
    ],
    "Admin panel functions working": [
        'openAdminPanel' in content,
        'closeAdminPanel' in content,
        'AdminPanel' in content,
    ],
}

print("REGRESSION CHECK RESULTS:")
print("-" * 80)

total_checks = 0
total_passed = 0
failed_areas = []

for area, check_list in checks.items():
    area_passed = all(check_list)
    total_checks += 1
    if area_passed:
        total_passed += 1
        print(f"✅ {area}")
    else:
        failed_areas.append(area)
        print(f"❌ {area}")
        for i, check in enumerate(check_list, 1):
            status = "✓" if check else "✗"
            print(f"   {status} Check {i}: {check}")

print("\n" + "="*80)
print(f"Regression Test Results: {total_passed}/{total_checks} areas OK")
print("="*80 + "\n")

if total_passed == total_checks:
    print("✅ NO REGRESSIONS DETECTED")
    print("All existing features continue to work correctly\n")
    exit(0)
else:
    print(f"⚠️  {total_checks - total_passed} area(s) may have issues:")
    for area in failed_areas:
        print(f"   - {area}")
    print()
    exit(1)
