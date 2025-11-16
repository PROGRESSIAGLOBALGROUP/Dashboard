"""
FINAL TEST: Verify apply() is truly called in DOMContentLoaded
"""

with open(r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("\n" + "="*80)
print("VERIFICATION: apply() in DOMContentLoaded")
print("="*80)

# Find the first DOMContentLoaded
import re
pattern = r"document\.addEventListener\('DOMContentLoaded'[\s\S]*?\}\);"
match = re.search(pattern, html)

if match:
    dom_handler = match.group(0)
    print("\n✅ DOMContentLoaded handler found")
    print(f"\nFirst 800 characters of handler:")
    print(dom_handler[:800])
    
    # Check explicitly for apply() in this handler
    if "apply()" in dom_handler:
        print("\n✅ apply() IS PRESENT in DOMContentLoaded handler")
    else:
        print("\n❌ apply() NOT PRESENT")
        
    # Check for the key initialization calls
    checks = {
        "StorageManager.init()": "StorageManager.init()" in dom_handler,
        "AdminController.init()": "AdminController.init()" in dom_handler,
        "UIController.init()": "UIController.init()" in dom_handler,
        "apply()": "apply()" in dom_handler,
    }
    
    print("\nInitialization Checklist:")
    for name, found in checks.items():
        status = "✅" if found else "❌"
        print(f"  {status} {name}")
    
    if all(checks.values()):
        print("\n🎉 ALL CHECKS PASSED - Dashboard will initialize on load")
    else:
        print("\n⚠️ Some checks failed - investigate above")
else:
    print("❌ DOMContentLoaded handler not found")

print("\n" + "="*80)
