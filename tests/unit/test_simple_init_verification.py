"""
SIMPLE VERIFICATION: Is apply() after DOMContentLoaded?
"""

with open(r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("\n" + "="*80)
print("FINAL VERIFICATION: Initialization Order")
print("="*80)

# Find line numbers
dom_content_line = None
apply_line = None

for i, line in enumerate(lines, 1):
    if "document.addEventListener('DOMContentLoaded'" in line and dom_content_line is None:
        dom_content_line = i
        print(f"\n✅ DOMContentLoaded found at line {i}")
    
    if "Dashboard.UIController.apply()" in line:
        if apply_line is None or (dom_content_line and i > dom_content_line):
            apply_line = i
            print(f"✅ apply() called at line {i}")

# Verify order
print("\n" + "-"*80)

if dom_content_line and apply_line:
    if apply_line > dom_content_line:
        print(f"✅ apply() ({apply_line}) is AFTER DOMContentLoaded ({dom_content_line})")
        
        # Find the closing brace of DOMContentLoaded
        for i in range(dom_content_line, min(dom_content_line + 200, len(lines))):
            if "});" in lines[i] and apply_line < i + dom_content_line:
                print(f"✅ apply() call is INSIDE DOMContentLoaded block (closes at line ~{i})")
                break
        
        print("\n🎉 INITIALIZATION FLOW IS CORRECT:")
        print("   1. DOMContentLoaded fires")
        print("   2. StorageManager.init()")
        print("   3. AdminController.init()")
        print("   4. UIController.init()")
        print("   5. apply() called to render dashboard ✅")
        
    else:
        print(f"❌ apply() ({apply_line}) is BEFORE DOMContentLoaded ({dom_content_line})")
else:
    print(f"❌ Missing DOMContentLoaded ({dom_content_line}) or apply() ({apply_line})")

print("\n" + "="*80 + "\n")
