#!/usr/bin/env python3
"""Validate that Progress Calculation Method fixes are in place"""

import os
import sys

def validate_file():
    filepath = 'dist/dashboard_enhanced.html'
    
    if not os.path.exists(filepath):
        print(f"[FAIL] File not found: {filepath}")
        return False
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = [
        ('const progressMethod = config?.formulaSettings?.progressMethod', 'BU Progress Method selector'),
        ('const globalMethod = config?.formulaSettings?.globalMethod', 'Global Progress Method selector'),
        ("case 'simple':", 'Simple Average implementation'),
        ("case 'minimum':", 'Minimum Progress implementation'),
        ("case 'weighted':", 'Weighted Average implementation'),
    ]
    
    print("=== Progress Calculation Method - File Validation ===\n")
    
    all_passed = True
    for pattern, description in checks:
        if pattern in content:
            print(f"[OK] {description}")
        else:
            print(f"[FAIL] {description}")
            all_passed = False
    
    # Validate brackets
    open_braces = content.count('{')
    close_braces = content.count('}')
    if open_braces == close_braces:
        print(f"\n[OK] Brace balance: {open_braces} open/close pairs")
    else:
        print(f"\n[FAIL] Brace mismatch: {open_braces} open vs {close_braces} close")
        all_passed = False
    
    # Check file size
    file_size = len(content)
    print(f"[OK] File size: {file_size:,} bytes")
    
    print(f"\n=== Result: {'ALL CHECKS PASSED' if all_passed else 'SOME CHECKS FAILED'} ===")
    
    return all_passed

if __name__ == '__main__':
    success = validate_file()
    sys.exit(0 if success else 1)
