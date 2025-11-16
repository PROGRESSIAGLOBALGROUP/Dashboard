"""
Test: Simulate exact browser execution - identify what's failing
"""

import re
import json

def extract_and_test_initialization():
    """Extract the initialization code and test it"""
    
    with open(r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    print("\n" + "="*80)
    print("BROWSER SIMULATION TEST: Find initialization failures")
    print("="*80)
    
    # Find the DOMContentLoaded handler
    pattern = r"document\.addEventListener\('DOMContentLoaded'[\s\S]*?\}\);"
    match = re.search(pattern, html)
    
    if not match:
        print("❌ DOMContentLoaded handler NOT FOUND")
        return False
    
    dom_handler = match.group(0)
    print("\n✅ DOMContentLoaded handler found:")
    print("\n" + dom_handler[:500] + "...")
    
    # Check if apply() is called ANYWHERE in the file (might be after the init)
    if 'Dashboard.UIController.apply()' not in html:
        print("\n❌ CRITICAL: apply() NOT found anywhere in the file")
        return False
    
    # Check if apply() is called specifically in a DOMContentLoaded handler
    # (could be any of the listeners, just need ONE)
    pattern = r"addEventListener\('DOMContentLoaded'[\s\S]{0,5000}?apply\(\)"
    if not re.search(pattern, html):
        print("\n⚠️ WARNING: apply() not found within 5000 chars of first DOMContentLoaded")
        print("But it exists in the file, so checking if it's in SOME listener...")
        if 'Dashboard.UIController.apply()' in html:
            print("✅ apply() IS called (found in file)")
        else:
            return False
    else:
        print("\n✅ apply() IS called in DOMContentLoaded")
    
    # Now check if UIController is defined
    if 'window.Dashboard.UIController = UIController' not in html:
        print("❌ UIController NOT exported to window.Dashboard")
        return False
    
    print("✅ UIController exported to window.Dashboard")
    
    # Check if apply() method exists in UIController
    pattern = r"const UIController = \{[\s\S]*?apply\(\)"
    if not re.search(pattern, html):
        print("❌ apply() method NOT defined in UIController")
        return False
    
    print("✅ apply() method defined in UIController")
    
    # Check if rebuildDATAFromStorage is defined
    if 'function rebuildDATAFromStorage' not in html:
        print("❌ rebuildDATAFromStorage() NOT defined")
        return False
    
    print("✅ rebuildDATAFromStorage() defined")
    
    # Check if StorageManager is exported
    if 'window.Dashboard.StorageManager = StorageManager' not in html:
        print("❌ StorageManager NOT exported to window.Dashboard")
        return False
    
    print("✅ StorageManager exported to window.Dashboard")
    
    # Check critical functions exist
    critical_checks = [
        ('Dashboard.StorageManager.init', 'StorageManager.init'),
        ('Dashboard.AdminController.init', 'AdminController.init'),
        ('Dashboard.UIController.init', 'UIController.init'),
        ('Dashboard.UIController.apply', 'UIController.apply'),
    ]
    
    print("\n" + "-"*80)
    print("Checking critical function calls in DOMContentLoaded:")
    print("-"*80)
    
    for func_full, func_name in critical_checks:
        if func_full in dom_handler:
            print(f"✅ {func_name} called")
        else:
            print(f"❌ {func_name} NOT called")
            return False
    
    print("\n" + "="*80)
    print("✅ ALL CHECKS PASSED - Initialization should work")
    print("="*80)
    
    print("\nIf dashboard still doesn't display, the issue is:")
    print("1. JavaScript error before DOMContentLoaded fires")
    print("2. Error INSIDE apply() method that we can't see without browser")
    print("3. Error in rebuildDATAFromStorage() or related functions")
    print("\nNEXT STEP: Open browser DevTools (F12) and check Console for errors")
    
    return True

if __name__ == '__main__':
    success = extract_and_test_initialization()
    exit(0 if success else 1)
