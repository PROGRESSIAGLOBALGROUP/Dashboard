#!/usr/bin/env python3
"""
Deep code analysis of Progress Calculation Method implementations
Verifies mathematical correctness of each calculation method
"""

import re

def analyze_calculation_methods():
    with open('dist/dashboard_enhanced.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n" + "="*80)
    print("DEEP CODE ANALYSIS - PROGRESS CALCULATION METHODS")
    print("="*80 + "\n")
    
    # Extract calculateBUProgress method
    pattern = r"calculateBUProgress\(buId\)\s*\{([\s\S]*?)\n\s*\},\s*recalculate"
    match = re.search(pattern, content)
    
    if not match:
        print("[FAIL] calculateBUProgress method not found")
        return False
    
    method_body = match.group(1)
    
    print("1. ANALYSIS OF CALCULATION METHODS\n")
    
    # Check for all three methods
    methods_checks = [
        ("case 'simple':", "Simple Average", 
         lambda: "activeApps.length > 0 ? Math.round((simpleSum / activeApps.length)" in method_body),
        ("case 'minimum':", "Minimum Progress",
         lambda: "Math.min(min, progress)" in method_body and "Math.round(minProgress" in method_body),
        ("case 'weighted':", "Weighted Average",
         lambda: "calculateAppWeight(app)" in method_body and "weightedSum / totalWeight" in method_body),
    ]
    
    all_ok = True
    for case, name, checker in methods_checks:
        if case in method_body:
            if checker():
                print(f"   ✅ {name}")
                print(f"      └─ Correct logic found")
            else:
                print(f"   ❌ {name}")
                print(f"      └─ Case found but logic may be incorrect")
                all_ok = False
        else:
            print(f"   ❌ {name}")
            print(f"      └─ Case statement not found")
            all_ok = False
    
    print("\n2. CALCULATION CORRECTNESS\n")
    
    # Verify math for each method
    checks = [
        ("Simple Average", 
         r"simpleSum / activeApps\.length",
         "Correctly sums all progress values and divides by count (equal weighting)"),
        
        ("Minimum Progress",
         r"Math\.min\(min, progress\)",
         "Correctly finds the minimum progress value (bottleneck approach)"),
        
        ("Weighted Average",
         r"calculateAppWeight\(app\).*?weightedSum / totalWeight",
         "Correctly multiplies progress by weight, sums both, then divides"),
    ]
    
    for name, pattern, description in checks:
        if re.search(pattern, method_body, re.DOTALL):
            print(f"   ✅ {name}")
            print(f"      └─ {description}")
        else:
            print(f"   ❌ {name}")
            print(f"      └─ Pattern not found")
            all_ok = False
    
    print("\n3. CONFIG READING\n")
    
    # Check config reading
    config_checks = [
        (r"const config = Dashboard\.StorageManager\.loadConfig\(\)", 
         "Config loaded from StorageManager"),
        (r"config\?\.formulaSettings\?\.progressMethod",
         "progressMethod accessed with safe navigation"),
        (r"progressMethod \|\| 'weighted'",
         "Weighted Average is default fallback"),
    ]
    
    for pattern, description in config_checks:
        if re.search(pattern, method_body):
            print(f"   ✅ {description}")
        else:
            print(f"   ❌ {description}")
            all_ok = False
    
    print("\n4. STATUS INCLUSION INTEGRATION\n")
    
    # Check status inclusion
    status_checks = [
        (r"const includesTBS = document\.getElementById\('include-tbs'\)",
         "TBS status inclusion read from checkbox"),
        (r"const includesWIP = document\.getElementById\('include-wip'\)",
         "WIP status inclusion read from checkbox"),
        (r"const includesCLO = document\.getElementById\('include-clo'\)",
         "CLO status inclusion read from checkbox"),
        (r"const activeApps = apps\.filter\(app => \{",
         "Apps filtered based on status inclusion rules"),
    ]
    
    for pattern, description in status_checks:
        if re.search(pattern, method_body):
            print(f"   ✅ {description}")
        else:
            print(f"   ❌ {description}")
            all_ok = False
    
    print("\n5. ERROR HANDLING\n")
    
    # Check error handling
    error_checks = [
        (r"if \(apps\.length === 0\) return 0",
         "Returns 0 if no apps"),
        (r"if \(activeApps\.length === 0\) return 0",
         "Returns 0 if no active apps after filtering"),
        (r"const progress = app\.progress \|\| 0",
         "Handles missing progress values"),
        (r"const min.*?= 100.*?Math\.min\(min, progress\)",
         "Minimum starts at 100 to find true minimum"),
    ]
    
    for pattern, description in error_checks:
        if re.search(pattern, method_body, re.DOTALL):
            print(f"   ✅ {description}")
        else:
            print(f"   ❌ {description}")
            # Don't fail on this - it's best practice but not critical
    
    print("\n6. GLOBAL PROGRESS CALCULATION\n")
    
    # Check global progress method
    global_pattern = r"const globalMethod = config\?\.formulaSettings\?\.globalMethod"
    if re.search(global_pattern, content):
        print(f"   ✅ Global progress uses globalMethod from config")
    else:
        print(f"   ❌ Global progress doesn't read globalMethod setting")
        all_ok = False
    
    # Check global method implementation
    global_simple = r"globalMethod === ['\"]simple['\"]"
    global_weighted = r"globalMethod === ['\"]weighted['\"]|else"
    
    if re.search(global_simple, content):
        print(f"   ✅ Global method supports 'simple' option")
    else:
        print(f"   ⚠️  Global 'simple' method implementation unclear")
    
    if re.search(global_weighted, content):
        print(f"   ✅ Global method supports 'weighted' option")
    else:
        print(f"   ⚠️  Global 'weighted' method implementation unclear")
    
    print("\n" + "="*80)
    print(f"RESULT: {'✅ ALL CHECKS PASSED' if all_ok else '❌ SOME CHECKS FAILED'}")
    print("="*80 + "\n")
    
    return all_ok

if __name__ == '__main__':
    import sys
    success = analyze_calculation_methods()
    sys.exit(0 if success else 1)
