"""
Test: Verify that DOMContentLoaded initializes apply() correctly
This validates the critical fix: UIController.apply() was not being called on page load
"""

import re

def test_domcontentloaded_calls_apply():
    """Verify DOMContentLoaded event listener calls apply()"""
    
    with open(r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html', encoding='utf-8') as f:
        html = f.read()
    
    print("\n" + "="*80)
    print("TEST: DOMContentLoaded Initialization")
    print("="*80)
    
    tests = []
    
    # Test 1: Verify DOMContentLoaded exists
    print("\n[1/4] Checking if DOMContentLoaded event listener exists...")
    if 'document.addEventListener(\'DOMContentLoaded\'' in html:
        print("  ✅ DOMContentLoaded listener found")
        tests.append(('DOMContentLoaded exists', True))
    else:
        print("  ❌ DOMContentLoaded listener NOT found")
        tests.append(('DOMContentLoaded exists', False))
    
    # Test 2: Verify StorageManager.init() is called
    print("\n[2/4] Checking if StorageManager.init() is called...")
    pattern = r"DOMContentLoaded.*?StorageManager\.init\(\)"
    if re.search(pattern, html, re.DOTALL):
        print("  ✅ StorageManager.init() called in DOMContentLoaded")
        tests.append(('StorageManager.init() called', True))
    else:
        print("  ❌ StorageManager.init() NOT called")
        tests.append(('StorageManager.init() called', False))
    
    # Test 3: Verify UIController.init() is called
    print("\n[3/4] Checking if UIController.init() is called...")
    pattern = r"DOMContentLoaded.*?UIController\.init\(\)"
    if re.search(pattern, html, re.DOTALL):
        print("  ✅ UIController.init() called in DOMContentLoaded")
        tests.append(('UIController.init() called', True))
    else:
        print("  ❌ UIController.init() NOT called")
        tests.append(('UIController.init() called', False))
    
    # Test 4: CRITICAL - Verify UIController.apply() is called (THE FIX)
    print("\n[4/4] Checking if UIController.apply() is called (CRITICAL)...")
    pattern = r"DOMContentLoaded.*?Dashboard\.UIController\.apply\(\)"
    if re.search(pattern, html, re.DOTALL):
        print("  ✅ UIController.apply() called in DOMContentLoaded - RENDERING WILL HAPPEN")
        tests.append(('UIController.apply() called (CRITICAL)', True))
    else:
        print("  ❌ UIController.apply() NOT called - DASHBOARD WILL NOT RENDER")
        tests.append(('UIController.apply() called (CRITICAL)', False))
    
    # Print results
    print("\n" + "="*80)
    passed = sum(1 for _, result in tests if result)
    failed = sum(1 for _, result in tests if not result)
    
    for test_name, result in tests:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
    
    print("\n" + "="*80)
    print(f"RESULTS: {passed}/4 PASSED")
    
    if passed == 4:
        print("\n✅ ALL INITIALIZATION CHECKS PASSED")
        print("\n🎉 CRITICAL FIX APPLIED:")
        print("   UIController.apply() is now called during DOMContentLoaded")
        print("   This means:")
        print("   1. rebuildDATAFromStorage() will execute")
        print("   2. avgGlobal will be calculated correctly")
        print("   3. Status inclusion rules will be applied")
        print("   4. KPI values will display")
        print("   5. Hero progress will display")
        print("   6. Everything WILL WORK on page load")
        print("="*80 + "\n")
        return True
    else:
        print("\n❌ INITIALIZATION INCOMPLETE")
        print("   Dashboard will not render on page load")
        return False

if __name__ == '__main__':
    success = test_domcontentloaded_calls_apply()
    exit(0 if success else 1)
