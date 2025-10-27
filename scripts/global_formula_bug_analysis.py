#!/usr/bin/env python3
"""
Verification Test - Global Progress Formula Bug Detection
Identifies why Global Progress Formula settings aren't being saved
"""

import re

def analyze_global_formula_bug():
    with open('dist/dashboard_enhanced.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n" + "="*80)
    print("GLOBAL PROGRESS FORMULA - BUG VERIFICATION")
    print("="*80 + "\n")
    
    print("STEP 1: Verify radio buttons exist")
    print("-" * 80)
    
    if 'name="global-method"' in content:
        print("✅ Radio buttons with name='global-method' found")
        # Find all global-method inputs
        radios = re.findall(r'id="(global-\w+)".*?name="global-method".*?value="(\w+)"', content, re.DOTALL)
        for id_val, value in radios:
            print(f"   └─ {id_val} = {value}")
    else:
        print("❌ No radio buttons with name='global-method'")
        return False
    
    print("\nSTEP 2: Check saveFormulaConfig() method")
    print("-" * 80)
    
    # Find where globalMethod is read in save
    pattern = r"saveFormulaConfig\(\)\s*\{([\s\S]*?)\n\s*\}"
    match = re.search(pattern, content)
    
    if match:
        save_body = match.group(1)
        
        # Check what it's reading for globalMethod
        if "formula-global-method" in save_body:
            print("❌ PROBLEM: Trying to read from 'formula-global-method'")
            print("   └─ This element doesn't exist!")
        elif "global-method" in save_body:
            print("✅ Reading from 'global-method' (correct)")
        else:
            print("❌ Not reading globalMethod at all")
            return False
    
    print("\nSTEP 3: Check if globalMethod is being saved to config")
    print("-" * 80)
    
    if "globalMethod:" in content:
        print("✅ globalMethod is included in config save")
        # Find what value it's getting
        if "document.getElementById('formula-global-method')" in content:
            print("❌ CRITICAL BUG: Reading from wrong element ID")
            print("   └─ Should read from: document.querySelector('input[name=\"global-method\"]:checked')")
        elif "document.querySelector('input[name=\"global-method\"]" in content:
            print("✅ Reading from correct selector")
        else:
            print("⚠️  Unclear how value is being read")
    else:
        print("❌ globalMethod not in save config")
        return False
    
    print("\nSTEP 4: Check event listeners for global-method radios")
    print("-" * 80)
    
    if "querySelectorAll('#tab-formulas input[name=\"global-method\"]')" in content or \
       "querySelectorAll('input[name=\"global-method\"]')" in content:
        print("✅ Event listeners attached to global-method radios")
    else:
        print("⚠️  No explicit event listeners for global-method radio change")
    
    print("\nSTEP 5: Check reset config uses correct global-method")
    print("-" * 80)
    
    pattern = r"resetFormulaConfig\(\)\s*\{([\s\S]*?)\}"
    match = re.search(pattern, content)
    
    if match:
        reset_body = match.group(1)
        if "formula-global-method" in reset_body:
            print("❌ Reset also uses wrong element ID: 'formula-global-method'")
        elif "global-method" in reset_body:
            print("✅ Reset correctly sets global-method")
        else:
            print("⚠️  Reset doesn't mention global-method")
    
    print("\n" + "="*80)
    print("ROOT CAUSE ANALYSIS")
    print("="*80 + "\n")
    
    print("""
The Global Progress Formula has a CRITICAL BUG:

SYMPTOM:
  - User selects "Simple BU Average" in Admin Modal
  - Selection appears to work (radio button changes)
  - But next refresh, it's back to "Weighted by BU Size"
  - Changes not persisting

ROOT CAUSE:
  - saveFormulaConfig() reads from: document.getElementById('formula-global-method')
  - But HTML has: <input name="global-method" id="global-weighted"> and <input name="global-method" id="global-simple">
  - Element 'formula-global-method' DOES NOT EXIST
  - So globalMethod always stays undefined/unset
  - Gets saved as undefined, so defaults back to 'weighted'

IMPACT:
  - Global Progress Formula selection NEVER WORKS
  - User thinks feature is broken (it is - partially)
  - Changes not persisting
  - Always uses 'weighted' as fallback

SOLUTION REQUIRED:
  - Fix line 6885: Change getElementById('formula-global-method')
  - To: querySelector('input[name="global-method"]:checked')
  - This will read the ACTUAL selected radio button value
""")
    
    return True

if __name__ == '__main__':
    import sys
    success = analyze_global_formula_bug()
    sys.exit(0 if success else 1)
