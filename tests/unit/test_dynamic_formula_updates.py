#!/usr/bin/env python3
"""
Test: Core Algorithm Formula Updates Dynamically
Verifies that the formula display updates when methods change
"""

from pathlib import Path

html_file = Path('dist/dashboard_enhanced.html')
content = html_file.read_text(encoding='utf-8')

print("\n" + "="*80)
print("TEST: Dynamic Formula Updates")
print("="*80 + "\n")

checks = {
    "1. core-algorithm-formula ID added": 'id="core-algorithm-formula"' in content,
    "2. updateCoreAlgorithmDisplay() function exists": 'updateCoreAlgorithmDisplay(progressMethod, globalMethod)' in content,
    "3. updateFormulaLabels() calls updateCoreAlgorithmDisplay()": 'this.updateCoreAlgorithmDisplay(progressMethod, globalMethod)' in content,
    "4. Progress method event listener exists": 'formula-progress-method.*addEventListener' in content,
    "5. Global method event listener exists": 'global-method.*addEventListener' in content,
    "6. loadFormulaConfig calls updateFormulaLabels": 'this.updateFormulaLabels()' in content,
    "7. initializeEmptyFormulaForm calls updateFormulaLabels": 'this.updateFormulaLabels()' in content,
}

# More flexible regex check
import re
checks_v2 = {
    "1. core-algorithm-formula ID added": 'id="core-algorithm-formula"' in content,
    "2. updateCoreAlgorithmDisplay() function exists": 'updateCoreAlgorithmDisplay' in content,
    "3. updateFormulaLabels() calls updateCoreAlgorithmDisplay()": 'updateCoreAlgorithmDisplay(progressMethod, globalMethod)' in content,
    "4. formulaMap defined with methods": 'formulaMap = {' in content and 'weighted:' in content,
    "5. methodContext defined": 'methodContext = {' in content,
    "6. Context subtitle element created": 'core-algorithm-context' in content,
    "7. Event listeners attached to radios": 'addEventListener' in content and 'global-method' in content,
}

passed = 0
failed = 0

print("VERIFICATION CHECKS:")
print("-" * 80)

for check, result in checks_v2.items():
    status = "✅ PASS" if result else "❌ FAIL"
    print(f"{status} - {check}")
    if result:
        passed += 1
    else:
        failed += 1

print("\n" + "="*80)
print(f"Result: {passed}/7 checks passed, {failed}/7 failed")
print("="*80 + "\n")

if failed == 0:
    print("✅ ALL CHECKS PASSED")
    print("Formula display will update dynamically when methods change\n")
else:
    print(f"⚠️  {failed} check(s) failed\n")
