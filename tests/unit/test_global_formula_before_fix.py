#!/usr/bin/env python3
"""
Unit Tests for Global Progress Formula Fix
Tests BEFORE applying the fix to verify the bug exists
"""

import re
from pathlib import Path

class GlobalFormulaTester:
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_global_method_radios_exist(self):
        """Test that radio buttons for global method exist"""
        if 'id="global-weighted"' in self.content and 'id="global-simple"' in self.content:
            if 'name="global-method"' in self.content:
                self.results.append({
                    'test': 'Global method radio buttons exist',
                    'status': 'PASS',
                    'message': 'Both Weighted and Simple radio buttons present'
                })
                return True
        
        self.results.append({
            'test': 'Global method radio buttons exist',
            'status': 'FAIL',
            'message': 'Radio buttons missing or wrong'
        })
        return False
    
    def test_global_method_saved_in_config(self):
        """Test that globalMethod is saved to config"""
        if 'globalMethod:' in self.content and 'formulaConfig' in self.content:
            self.results.append({
                'test': 'globalMethod saved in config',
                'status': 'PASS',
                'message': 'globalMethod is part of save config'
            })
            return True
        
        self.results.append({
            'test': 'globalMethod saved in config',
            'status': 'FAIL',
            'message': 'globalMethod not in config save'
        })
        return False
    
    def test_global_method_reads_correct_element(self):
        """Test that save reads from correct element"""
        # This is the BUG TEST - should fail if bug exists
        pattern = r"globalMethod:\s*document\.querySelector\(['\"]input\[name=['\"]global-method['\"]['\"].*?:checked"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'globalMethod reads correct element',
                'status': 'PASS',
                'message': 'Correctly reads from global-method radio buttons'
            })
            return True
        else:
            # This is expected to FAIL (bug exists)
            self.results.append({
                'test': 'globalMethod reads correct element',
                'status': 'FAIL',
                'message': 'Reading from wrong element or missing selector'
            })
            return False
    
    def test_global_method_persists_on_reload(self):
        """Test that globalMethod is reloaded on page load"""
        if "globalMethod: fc.globalMethod || 'weighted'" in self.content or \
           "globalMethod: savedGlobal || 'weighted'" in self.content:
            self.results.append({
                'test': 'globalMethod persists on reload',
                'status': 'PASS',
                'message': 'globalMethod loaded from config on init'
            })
            return True
        
        self.results.append({
            'test': 'globalMethod persists on reload',
            'status': 'FAIL',
            'message': 'Reload logic missing'
        })
        return False
    
    def test_global_method_affects_calculation(self):
        """Test that globalMethod affects actual calculation"""
        if "globalMethod === 'simple'" in self.content and \
           "if (globalMethod === 'simple')" in self.content:
            self.results.append({
                'test': 'globalMethod affects calculation',
                'status': 'PASS',
                'message': 'Calculation uses globalMethod setting'
            })
            return True
        
        self.results.append({
            'test': 'globalMethod affects calculation',
            'status': 'FAIL',
            'message': 'Calculation ignores globalMethod'
        })
        return False
    
    def run_all_tests(self):
        print("\n" + "="*70)
        print("GLOBAL PROGRESS FORMULA - UNIT TESTS (PRE-FIX)")
        print("="*70 + "\n")
        
        tests = [
            self.test_global_method_radios_exist,
            self.test_global_method_saved_in_config,
            self.test_global_method_reads_correct_element,  # THIS SHOULD FAIL (bug test)
            self.test_global_method_persists_on_reload,
            self.test_global_method_affects_calculation,
        ]
        
        for test in tests:
            test()
        
        passed = sum(1 for r in self.results if r['status'] == 'PASS')
        failed = sum(1 for r in self.results if r['status'] == 'FAIL')
        
        for result in self.results:
            icon = "✅" if result['status'] == 'PASS' else "❌"
            print(f"{icon} {result['test']}")
            print(f"   └─ {result['message']}\n")
        
        print("="*70)
        print(f"Results: {passed} passed, {failed} failed out of {len(self.results)} tests")
        print("="*70 + "\n")
        
        return failed == 0

if __name__ == '__main__':
    import sys
    tester = GlobalFormulaTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
