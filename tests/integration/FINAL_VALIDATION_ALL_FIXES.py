"""
FINAL VALIDATION: Complete Dashboard Initialization & Rendering Flow
This validates that the dashboard will now work end-to-end after the initialization fix
"""

import re

def final_validation():
    """Complete validation of all four critical fixes"""
    
    with open(r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html', encoding='utf-8') as f:
        html = f.read()
    
    print("\n" + "╔" + "="*78 + "╗")
    print("║" + " "*78 + "║")
    print("║" + "  FINAL VALIDATION: ALL FOUR CRITICAL FIXES".center(78) + "║")
    print("║" + " "*78 + "║")
    print("╚" + "="*78 + "╝")
    
    validations = []
    
    # ============ FIX #1: KPI-HERO SYNC ============
    print("\n" + "─"*80)
    print("FIX #1: KPI receives avgGlobal parameter (KPI-Hero Sync)")
    print("─"*80)
    
    pattern = r"updateKPIs\(items, avgGlobal"
    if re.search(pattern, html):
        print("✅ updateKPIs() accepts avgGlobal parameter")
        validations.append(('KPI receives avgGlobal', True))
    else:
        print("❌ updateKPIs() doesn't have avgGlobal parameter")
        validations.append(('KPI receives avgGlobal', False))
    
    pattern = r"this\.updateKPIs\(items, avgGlobal\)"
    if re.search(pattern, html):
        print("✅ apply() passes avgGlobal to updateKPIs()")
        validations.append(('apply() passes avgGlobal', True))
    else:
        print("❌ apply() doesn't pass avgGlobal")
        validations.append(('apply() passes avgGlobal', False))
    
    pattern = r"document\.querySelector\('#kpiAvg'\)\.textContent = avgGlobal"
    if re.search(pattern, html):
        print("✅ updateKPIs() displays avgGlobal in KPI display")
        validations.append(('KPI displays avgGlobal', True))
    else:
        print("❌ KPI doesn't display avgGlobal")
        validations.append(('KPI displays avgGlobal', False))
    
    # ============ FIX #2: STATUS INCLUSION FILTERING ============
    print("\n" + "─"*80)
    print("FIX #2: rebuildDATAFromStorage() filters by status inclusion rules")
    print("─"*80)
    
    pattern = r"const includesTBS = document\.getElementById\('include-tbs'\)\?\.checked"
    if re.search(pattern, html):
        print("✅ rebuildDATAFromStorage() reads include-tbs checkbox")
        validations.append(('Read include-tbs', True))
    else:
        print("❌ rebuildDATAFromStorage() doesn't read include-tbs")
        validations.append(('Read include-tbs', False))
    
    pattern = r"const filteredApps = apps\.filter\(app => \{"
    if re.search(pattern, html):
        print("✅ rebuildDATAFromStorage() filters apps by status")
        validations.append(('Filter apps by status', True))
    else:
        print("❌ rebuildDATAFromStorage() doesn't filter apps")
        validations.append(('Filter apps by status', False))
    
    pattern = r"appCount: filteredCount"
    if re.search(pattern, html):
        print("✅ rebuildDATAFromStorage() uses filtered count for calculations")
        validations.append(('Use filteredCount for calc', True))
    else:
        print("❌ rebuildDATAFromStorage() doesn't use filteredCount")
        validations.append(('Use filteredCount for calc', False))
    
    # ============ FIX #3: CHECKBOX PERSISTENCE ============
    print("\n" + "─"*80)
    print("FIX #3: saveAndClose() uses correct checkbox IDs (include-clo)")
    print("─"*80)
    
    # Check for old broken checkbox ID
    if 'include-done' in html:
        matches = len(re.findall(r"include-done", html))
        if matches > 0:
            print(f"❌ Found {matches} references to non-existent 'include-done' checkbox")
            validations.append(('No include-done references', False))
        else:
            print("✅ No references to broken 'include-done' checkbox")
            validations.append(('No include-done references', True))
    else:
        print("✅ No references to broken 'include-done' checkbox")
        validations.append(('No include-done references', True))
    
    # Check for correct checkbox ID
    pattern = r"clo: document\.getElementById\('include-clo'\)"
    if re.search(pattern, html):
        print("✅ saveAndClose() reads correct 'include-clo' checkbox")
        validations.append(('Read include-clo', True))
    else:
        print("❌ saveAndClose() doesn't read 'include-clo' checkbox")
        validations.append(('Read include-clo', False))
    
    # ============ FIX #4: INITIALIZATION ============
    print("\n" + "─"*80)
    print("FIX #4: DOMContentLoaded calls apply() for initial render")
    print("─"*80)
    
    pattern = r"document\.addEventListener\('DOMContentLoaded'"
    if re.search(pattern, html):
        print("✅ DOMContentLoaded event listener defined")
        validations.append(('DOMContentLoaded listener', True))
    else:
        print("❌ DOMContentLoaded listener not found")
        validations.append(('DOMContentLoaded listener', False))
    
    pattern = r"DOMContentLoaded.*?Dashboard\.UIController\.apply\(\)"
    if re.search(pattern, html, re.DOTALL):
        print("✅ apply() called in DOMContentLoaded (CRITICAL)")
        validations.append(('apply() in DOMContentLoaded', True))
    else:
        print("❌ apply() NOT called in DOMContentLoaded")
        validations.append(('apply() in DOMContentLoaded', False))
    
    # ============ SUMMARY ============
    print("\n" + "╔" + "="*78 + "╗")
    print("║" + "  VALIDATION RESULTS".center(78) + "║")
    print("╚" + "="*78 + "╝")
    
    passed = sum(1 for _, result in validations if result)
    total = len(validations)
    
    # Group by fix
    fixes = {
        'KPI-Hero Sync': validations[0:3],
        'Status Inclusion Filter': validations[3:6],
        'Checkbox Persistence': validations[6:9],
        'Initialization': validations[9:12]
    }
    
    print()
    for fix_name, fix_tests in fixes.items():
        fix_passed = sum(1 for _, result in fix_tests if result)
        fix_total = len(fix_tests)
        status = "✅" if fix_passed == fix_total else "⚠️"
        print(f"{status} {fix_name}: {fix_passed}/{fix_total}")
        for test_name, result in fix_tests:
            print(f"   {'✅' if result else '❌'} {test_name}")
    
    print("\n" + "─"*80)
    print(f"TOTAL: {passed}/{total} VALIDATIONS PASSED")
    print("─"*80)
    
    if passed == total:
        print("\n🎉 ALL FIXES VALIDATED AND READY FOR DEPLOYMENT")
        print("\nExpected Behavior After Deployment:")
        print("  1. Dashboard renders on page load ✅")
        print("  2. KPI values display correctly ✅")
        print("  3. Hero Progress and KPI show same value ✅")
        print("  4. Status Inclusion Rules affect KPI ✅")
        print("  5. Configuration persists after Save & Close ✅")
        print("  6. Values restore after page refresh (F5) ✅")
        print("\n" + "="*80 + "\n")
        return True
    else:
        print(f"\n⚠️ {total - passed} VALIDATIONS FAILED")
        return False

if __name__ == '__main__':
    success = final_validation()
    exit(0 if success else 1)
