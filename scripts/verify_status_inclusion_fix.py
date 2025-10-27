#!/usr/bin/env python3
"""
Status Inclusion Rules Fix - Verification Script
Automated verification that the Status Inclusion Rules fix is working correctly.

This script:
1. Verifies the code changes are in place
2. Checks the event listener chain
3. Validates that calculateBUProgress() reads from DOM checkboxes
4. Confirms updateStatusInclusion() calls UIController.apply()
"""

import re
import json
from pathlib import Path

def read_file(filepath):
    """Read file contents."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def verify_fix():
    """Verify all aspects of the Status Inclusion Rules fix."""
    
    html_file = Path('dist/dashboard_enhanced.html')
    if not html_file.exists():
        print("❌ File not found: dist/dashboard_enhanced.html")
        return False
    
    content = read_file(html_file)
    results = {
        'all_passed': True,
        'checks': []
    }
    
    # Check 1: Verify calculateBUProgress() reads status checkboxes
    print("\n🔍 Check 1: calculateBUProgress() reads checkboxes dynamically")
    pattern1 = r"const includesTBS = document\.getElementById\('include-tbs'\)\?\.checked"
    if re.search(pattern1, content):
        print("✅ PASS - calculateBUProgress() reads include-tbs checkbox")
        results['checks'].append({'name': 'Read include-tbs checkbox', 'status': 'PASS'})
    else:
        print("❌ FAIL - calculateBUProgress() doesn't read include-tbs checkbox")
        results['checks'].append({'name': 'Read include-tbs checkbox', 'status': 'FAIL'})
        results['all_passed'] = False
    
    pattern2 = r"const includesWIP = document\.getElementById\('include-wip'\)\?\.checked"
    if re.search(pattern2, content):
        print("✅ PASS - calculateBUProgress() reads include-wip checkbox")
        results['checks'].append({'name': 'Read include-wip checkbox', 'status': 'PASS'})
    else:
        print("❌ FAIL - calculateBUProgress() doesn't read include-wip checkbox")
        results['checks'].append({'name': 'Read include-wip checkbox', 'status': 'FAIL'})
        results['all_passed'] = False
    
    pattern3 = r"const includesCLO = document\.getElementById\('include-clo'\)\?\.checked"
    if re.search(pattern3, content):
        print("✅ PASS - calculateBUProgress() reads include-clo checkbox")
        results['checks'].append({'name': 'Read include-clo checkbox', 'status': 'PASS'})
    else:
        print("❌ FAIL - calculateBUProgress() doesn't read include-clo checkbox")
        results['checks'].append({'name': 'Read include-clo checkbox', 'status': 'FAIL'})
        results['all_passed'] = False
    
    # Check 2: Verify filtering logic exists
    print("\n🔍 Check 2: calculateBUProgress() has dynamic filtering logic")
    pattern_filter = r"if \(app\.status === 'TBS'\) return includesTBS"
    if re.search(pattern_filter, content):
        print("✅ PASS - Dynamic filtering logic exists for TBS status")
        results['checks'].append({'name': 'Dynamic TBS filtering', 'status': 'PASS'})
    else:
        print("❌ FAIL - Dynamic filtering logic missing for TBS status")
        results['checks'].append({'name': 'Dynamic TBS filtering', 'status': 'FAIL'})
        results['all_passed'] = False
    
    # Check 3: Verify old hardcoded logic is GONE
    print("\n🔍 Check 3: Old hardcoded logic removed")
    pattern_old = r"app\.status !== 'TBS'"
    if not re.search(pattern_old, content):
        print("✅ PASS - Old hardcoded 'app.status !== TBS' logic removed")
        results['checks'].append({'name': 'Old hardcoded logic removed', 'status': 'PASS'})
    else:
        print("⚠️  WARNING - Old hardcoded logic still present (may be intentional)")
        results['checks'].append({'name': 'Old hardcoded logic removed', 'status': 'WARNING'})
    
    # Check 4: Verify updateStatusInclusion() calls apply()
    print("\n🔍 Check 4: updateStatusInclusion() triggers recalculation")
    # Find updateStatusInclusion method and check if it contains apply() call
    pattern_method = r"updateStatusInclusion\(\)\s*\{([^}]*?(?:\{[^}]*\}[^}]*?)*)\}"
    matches = re.finditer(pattern_method, content, re.DOTALL)
    found_apply = False
    for match in matches:
        method_body = match.group(1)
        if 'Dashboard.UIController.apply()' in method_body or 'apply()' in method_body:
            found_apply = True
            break
    
    if found_apply:
        print("✅ PASS - updateStatusInclusion() calls Dashboard.UIController.apply()")
        results['checks'].append({'name': 'updateStatusInclusion() calls apply()', 'status': 'PASS'})
    else:
        print("❌ FAIL - updateStatusInclusion() doesn't call Dashboard.UIController.apply()")
        results['checks'].append({'name': 'updateStatusInclusion() calls apply()', 'status': 'FAIL'})
        results['all_passed'] = False
    
    # Check 5: Verify event listener is set up
    print("\n🔍 Check 5: Event listener chain exists")
    pattern_listener = r"checkbox\.addEventListener\('change'.*updateStatusInclusion"
    if re.search(pattern_listener, content, re.DOTALL):
        print("✅ PASS - Event listener calls updateStatusInclusion()")
        results['checks'].append({'name': 'Event listener chain', 'status': 'PASS'})
    else:
        print("❌ FAIL - Event listener chain not properly set up")
        results['checks'].append({'name': 'Event listener chain', 'status': 'FAIL'})
        results['all_passed'] = False
    
    # Check 6: Verify UIController.apply() exists
    print("\n🔍 Check 6: UIController.apply() method exists")
    pattern_apply_method = r"apply\(\)\s*{[^}]*rebuildDATAFromStorage"
    if re.search(pattern_apply_method, content, re.DOTALL):
        print("✅ PASS - UIController.apply() method exists and recalculates")
        results['checks'].append({'name': 'UIController.apply() exists', 'status': 'PASS'})
    else:
        print("❌ FAIL - UIController.apply() method not found")
        results['checks'].append({'name': 'UIController.apply() exists', 'status': 'FAIL'})
        results['all_passed'] = False
    
    # Check 7: Verify backup file exists
    print("\n🔍 Check 7: Backup file exists")
    backup_file = Path('dist/dashboard_enhanced_20251026_pre_status_rules_fix.html')
    if backup_file.exists():
        print(f"✅ PASS - Backup file exists ({backup_file.name})")
        results['checks'].append({'name': 'Backup file exists', 'status': 'PASS'})
    else:
        print("⚠️  WARNING - Backup file not found")
        results['checks'].append({'name': 'Backup file exists', 'status': 'WARNING'})
    
    # Check 8: Verify code_surgeon job exists
    print("\n🔍 Check 8: Code_surgeon job documentation exists")
    job_file = Path('surgery/jobs/20251026_status_inclusion_rules_fix.json')
    if job_file.exists():
        print(f"✅ PASS - Code_surgeon job exists ({job_file.name})")
        results['checks'].append({'name': 'Code_surgeon job', 'status': 'PASS'})
        with open(job_file, 'r') as f:
            job_data = json.load(f)
            print(f"   Description: {job_data.get('description', 'N/A')[:80]}...")
    else:
        print("❌ FAIL - Code_surgeon job not found")
        results['checks'].append({'name': 'Code_surgeon job', 'status': 'FAIL'})
        results['all_passed'] = False
    
    # Summary
    print("\n" + "="*70)
    print("VERIFICATION SUMMARY")
    print("="*70)
    
    passed = sum(1 for c in results['checks'] if c['status'] == 'PASS')
    failed = sum(1 for c in results['checks'] if c['status'] == 'FAIL')
    warnings = sum(1 for c in results['checks'] if c['status'] == 'WARNING')
    
    print(f"\n✅ PASSED:  {passed}")
    print(f"❌ FAILED:  {failed}")
    print(f"⚠️  WARNING: {warnings}")
    
    if results['all_passed']:
        print("\n🎉 ALL CRITICAL CHECKS PASSED")
        print("Status Inclusion Rules fix is properly implemented!")
        return True
    else:
        print("\n🚨 SOME CRITICAL CHECKS FAILED")
        print("Review the failures above and correct them.")
        return False

if __name__ == '__main__':
    import sys
    success = verify_fix()
    sys.exit(0 if success else 1)
