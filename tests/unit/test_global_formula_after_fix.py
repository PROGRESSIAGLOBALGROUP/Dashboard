#!/usr/bin/env python3
"""
Unit Tests for Global Progress Formula - POST-FIX
Verifies that the globalMethod bug is fixed
"""

import re
from pathlib import Path

class GlobalFormulaPostFixTester:
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_no_formula_global_method_refs(self):
        """Test that broken element references are gone"""
        if 'formula-global-method' in self.content:
            self.results.append({
                'test': 'No broken formula-global-method references',
                'status': 'FAIL',
                'message': 'Still contains references to non-existent element'
            })
            return False
        
        self.results.append({
            'test': 'No broken formula-global-method references',
            'status': 'PASS',
            'message': 'All broken element references removed'
        })
        return True
    
    def test_global_method_reads_from_radios(self):
        """Test that save function reads from radio buttons"""
        pattern = r"querySelector\(['\"]input\[name=['\"]global-method['\"].*?:checked"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'globalMethod reads from radio buttons',
                'status': 'PASS',
                'message': 'Correctly reads selected radio button value'
            })
            return True
        else:
            self.results.append({
                'test': 'globalMethod reads from radio buttons',
                'status': 'FAIL',
                'message': 'Not reading from radio buttons'
            })
            return False
    
    def test_global_method_sets_radio_buttons(self):
        """Test that form reset sets radio buttons correctly"""
        if "querySelector(`input[name=\"global-method\"][value=" in self.content and \
           ".checked = true" in self.content:
            self.results.append({
                'test': 'globalMethod sets radio buttons',
                'status': 'PASS',
                'message': 'Correctly sets radio button checked state'
            })
            return True
        
        self.results.append({
            'test': 'globalMethod sets radio buttons',
            'status': 'FAIL',
            'message': 'Radio button setting logic missing'
        })
        return False
    
    def test_event_listeners_on_radios(self):
        """Test that event listeners are attached to radio buttons"""
        pattern = r"querySelectorAll\(['\"]input\[name=['\"]global-method['\"]"
        
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Event listeners on global-method radios',
                'status': 'PASS',
                'message': 'Radio buttons have event listeners'
            })
            return True
        
        self.results.append({
            'test': 'Event listeners on global-method radios',
            'status': 'FAIL',
            'message': 'Event listeners missing'
        })
        return False
    
    def test_global_calculation_uses_method(self):
        """Test that global progress calculation uses selected method"""
        if "const globalMethod = config?.formulaSettings?.globalMethod" in self.content and \
           "if (globalMethod === 'simple')" in self.content:
            self.results.append({
                'test': 'Global calculation uses method setting',
                'status': 'PASS',
                'message': 'Calculation respects globalMethod setting'
            })
            return True
        
        self.results.append({
            'test': 'Global calculation uses method setting',
            'status': 'FAIL',
            'message': 'Calculation ignores globalMethod'
        })
        return False
    
    def run_all_tests(self):
        print("\n" + "="*70)
        print("GLOBAL PROGRESS FORMULA - UNIT TESTS (POST-FIX)")
        print("="*70 + "\n")
        
        tests = [
            self.test_no_formula_global_method_refs,
            self.test_global_method_reads_from_radios,
            self.test_global_method_sets_radio_buttons,
            self.test_event_listeners_on_radios,
            self.test_global_calculation_uses_method,
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
    tester = GlobalFormulaPostFixTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
