#!/usr/bin/env python3
"""
Analysis: All references to formula-global-method
Identify all locations where code tries to access non-existent element
"""

import re

def analyze_all_references():
    with open('dist/dashboard_enhanced.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    print("\n" + "="*80)
    print("GLOBAL FORMULA METHOD - ALL REFERENCES TO 'formula-global-method'")
    print("="*80 + "\n")
    
    # Find all references
    references = []
    for i, line in enumerate(lines, 1):
        if 'formula-global-method' in line:
            references.append((i, line.strip()))
    
    print(f"Found {len(references)} references:\n")
    
    for line_num, line_content in references:
        # Determine what operation is being done
        if '.addEventListener' in line_content:
            operation = "EVENT LISTENER"
            fix = "Change to: querySelectorAll('input[name=\"global-method\"]')"
        elif '.value =' in line_content:
            operation = "SETTING VALUE"
            fix = "Use: querySelectorAll('input[name=\"global-method\"]').forEach(r => r.checked = ...)"
        elif '.value' in line_content and '=' not in line_content:
            operation = "READING VALUE"
            fix = "Change to: querySelector('input[name=\"global-method\"]:checked')"
        elif '.checked' in line_content:
            operation = "CHECK/UNCHECK"
            fix = "Reference radio button by correct ID"
        else:
            operation = "UNKNOWN"
            fix = "Manual review required"
        
        print(f"Line {line_num}: {operation}")
        print(f"  Current:  {line_content[:80]}")
        print(f"  Fix:      {fix}")
        print()
    
    print("="*80)
    print(f"TOTAL FIXES NEEDED: {len(references)}")
    print("="*80 + "\n")
    
    return len(references)

if __name__ == '__main__':
    analyze_all_references()
