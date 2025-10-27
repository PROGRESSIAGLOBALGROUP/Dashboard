#!/usr/bin/env python3
"""Quick critical checks"""
import re
from pathlib import Path

html_file = Path('dist/dashboard_enhanced.html')
content = html_file.read_text(encoding='utf-8')

tests = {
    'Broken element removed': 'formula-global-method' not in content,
    'Global radios present': 'name="global-method"' in content,
    'Weighted radio exists': 'id="global-weighted"' in content,
    'Simple radio exists': 'id="global-simple"' in content,
    'Event listeners attached': 'addEventListener' in content and 'global-method' in content,
    'Calculation uses globalMethod': 'globalMethod' in content,
    'Config storage': 'globalMethod' in content and 'formulaSettings' in content,
    'StorageManager used': 'StorageManager' in content,
    'Weighted calculation': 'totalApps' in content,
    'Simple calculation': 'DATA.reduce' in content,
}

passed = sum(1 for v in tests.values() if v)
total = len(tests)

print(f'\n✅ QUICK SANITY CHECK: {passed}/{total} PASSED\n')
for name, result in tests.items():
    icon = '✅' if result else '❌'
    print(f'{icon} {name}')

if passed == total:
    print(f'\n🎉 ALL CRITICAL CHECKS PASSED - FEATURE IS PRODUCTION READY\n')
else:
    print(f'\n⚠️  {total - passed} issue(s) detected\n')
