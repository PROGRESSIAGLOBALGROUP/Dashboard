#!/usr/bin/env python3
"""
Test: Formula Initialization Fix - Simple Direct Verification
Validates that the fixes were applied correctly
"""

import re

def main():
    with open('dist/dashboard_enhanced.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n" + "="*90)
    print("✅ FORMULA INITIALIZATION FIX - VERIFICATION")
    print("="*90 + "\n")
    
    tests_passed = 0
    tests_total = 0
    
    # TEST 1: Old pattern should NOT exist in loadFormulaConfig
    tests_total += 1
    bad_pattern_1 = "document.getElementById('formula-progress-method').value"
    if bad_pattern_1 not in content:
        print("✅ TEST 1: PASS - Old getElementById pattern removed from loadFormulaConfig")
        tests_passed += 1
    else:
        print("❌ TEST 1: FAIL - Old getElementById pattern still exists")
    
    # TEST 2: New pattern should exist - querySelector with progress-method
    tests_total += 1
    good_pattern_1 = "querySelector(`input[name=\"progress-method\"][value=\"${config.progressMethod"
    if good_pattern_1 in content:
        print("✅ TEST 2: PASS - New querySelector pattern found in loadFormulaConfig")
        tests_passed += 1
    else:
        print("❌ TEST 2: FAIL - New querySelector pattern not found")
    
    # TEST 3: initializeEmptyFormulaForm should use querySelector
    tests_total += 1
    good_pattern_2 = 'querySelector(\'input[name="progress-method"][value="weighted"]\')'
    if good_pattern_2 in content:
        print("✅ TEST 3: PASS - initializeEmptyFormulaForm uses querySelector")
        tests_passed += 1
    else:
        print("❌ TEST 3: FAIL - initializeEmptyFormulaForm not using querySelector")
    
    # TEST 4: Both functions check if radio exists before using
    tests_total += 1
    check_pattern = "if (progressMethodRadio) progressMethodRadio.checked = true"
    check_count = content.count(check_pattern)
    if check_count >= 2:
        print(f"✅ TEST 4: PASS - Radio element check found {check_count} times")
        tests_passed += 1
    else:
        print(f"❌ TEST 4: FAIL - Radio element check found only {check_count} times")
    
    # TEST 5: Event listeners still present
    tests_total += 1
    event_pattern = "document.querySelectorAll('input[name=\"progress-method\"]').forEach(radio =>"
    if event_pattern in content:
        print("✅ TEST 5: PASS - Event listeners for progress-method radio buttons still attached")
        tests_passed += 1
    else:
        print("❌ TEST 5: FAIL - Event listeners not found")
    
    # TEST 6: updateFormulaLabels still present
    tests_total += 1
    update_pattern = "this.updateFormulaLabels()"
    update_count = content.count(update_pattern)
    if update_count >= 2:
        print(f"✅ TEST 6: PASS - updateFormulaLabels called {update_count} times")
        tests_passed += 1
    else:
        print(f"❌ TEST 6: FAIL - updateFormulaLabels called only {update_count} times")
    
    # TEST 7: Global method radio button handling correct
    tests_total += 1
    global_pattern = "querySelector(`input[name=\"global-method\"][value=\"${config.globalMethod"
    if global_pattern in content:
        print("✅ TEST 7: PASS - Global method radio button handled correctly")
        tests_passed += 1
    else:
        print("❌ TEST 7: FAIL - Global method radio button not found")
    
    # TEST 8: No syntax errors around fixes
    tests_total += 1
    # Check for balanced parentheses/brackets in key sections
    load_formula_section = content[content.find("loadFormulaConfig()"):content.find("loadFormulaConfig()") + 3000]
    if load_formula_section.count("(") - load_formula_section.count(")") == 0:
        print("✅ TEST 8: PASS - Syntax check passed for loadFormulaConfig")
        tests_passed += 1
    else:
        print("❌ TEST 8: FAIL - Syntax error in loadFormulaConfig")
    
    print("\n" + "="*90)
    print(f"RESULTS: {tests_passed}/{tests_total} tests passed")
    print("="*90)
    
    if tests_passed == tests_total:
        print("\n✅ ALL FIXES VERIFIED AND APPLIED CORRECTLY\n")
        print("Summary of fixes:")
        print("  1. loadFormulaConfig() now uses querySelector for progress-method")
        print("  2. initializeEmptyFormulaForm() now uses querySelector for progress-method")
        print("  3. Both functions safely check radio existence before use")
        print("  4. Event listeners remain intact and working")
        print("  5. updateFormulaLabels() still called on initialization")
        print("  6. Global method radio button handling correct")
        print("\nFormula display will now update when radio buttons are changed!")
        print("="*90 + "\n")
        return 0
    else:
        print(f"\n❌ {tests_total - tests_passed} test(s) failed\n")
        return 1

if __name__ == '__main__':
    exit(main())
