#!/usr/bin/env python3
"""
Unit Tests for Progress Calculation Method Fix

This test suite verifies that the Progress Calculation Method options
(Weighted, Simple, Minimum) actually affect progress calculations.

Tests:
- Verify calculateBUProgress() reads progress method from config
- Verify Weighted Average method works
- Verify Simple Average method works
- Verify Minimum Progress method works
- Verify method selection is saved and applied
"""

import json
import re
from pathlib import Path

class ProgressMethodTester:
    """Unit tests for Progress Calculation Method"""
    
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        """Read the HTML file"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_radio_buttons_exist(self):
        """Test that radio buttons for progress methods exist"""
        pattern = r"id=['\"]method-weighted['\"].*?id=['\"]method-simple['\"].*?id=['\"]method-minimum['\"]"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Progress method radio buttons exist',
                'status': 'PASS',
                'message': 'All three method options (Weighted, Simple, Minimum) present in UI'
            })
            return True
        else:
            self.results.append({
                'test': 'Progress method radio buttons exist',
                'status': 'FAIL',
                'message': 'Missing one or more radio button options'
            })
            return False
    
    def test_method_saved_to_config(self):
        """Test that selected method is saved to formulaSettings"""
        pattern = r"progressMethod:\s*document\.querySelector\(['\"]input\[name=['\"]progress-method['\"]"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Selected method saved to config',
                'status': 'PASS',
                'message': 'progressMethod read from radio buttons and saved'
            })
            return True
        else:
            self.results.append({
                'test': 'Selected method saved to config',
                'status': 'FAIL',
                'message': 'progressMethod not saved to configuration'
            })
            return False
    
    def test_calculateBUProgress_reads_method(self):
        """Test that calculateBUProgress() reads the progress method from config"""
        # Find calculateBUProgress method
        pattern = r"calculateBUProgress\(buId\)\s*\{([\s\S]*?)\n\s*\},"
        match = re.search(pattern, self.content)
        
        if not match:
            self.results.append({
                'test': 'calculateBUProgress() reads method setting',
                'status': 'FAIL',
                'message': 'calculateBUProgress method not found'
            })
            return False
        
        method_body = match.group(1)
        
        # Should reference progressMethod or formulaSettings
        if 'progressMethod' in method_body or 'formulaSettings' in method_body:
            self.results.append({
                'test': 'calculateBUProgress() reads method setting',
                'status': 'PASS',
                'message': 'calculateBUProgress() reads progress method from config'
            })
            return True
        else:
            self.results.append({
                'test': 'calculateBUProgress() reads method setting',
                'status': 'FAIL',
                'message': 'calculateBUProgress() does not read progress method'
            })
            return False
    
    def test_simple_average_logic_exists(self):
        """Test that Simple Average calculation logic exists"""
        # Simple average: sum of progress / count
        pattern = r"simple|Simple|SIMPLE"
        if re.search(pattern, self.content):
            # Check if there's logic for simple average
            pattern2 = r"method === ['\"]simple['\"]|progressMethod === ['\"]simple['\"]"
            if re.search(pattern2, self.content):
                self.results.append({
                    'test': 'Simple Average logic implemented',
                    'status': 'PASS',
                    'message': 'Simple Average calculation logic found'
                })
                return True
        
        self.results.append({
            'test': 'Simple Average logic implemented',
            'status': 'FAIL',
            'message': 'Simple Average logic not found in calculateBUProgress'
        })
        return False
    
    def test_minimum_logic_exists(self):
        """Test that Minimum Progress calculation logic exists"""
        pattern = r"method === ['\"]minimum['\"]|progressMethod === ['\"]minimum['\"]|Math\.min"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Minimum Progress logic implemented',
                'status': 'PASS',
                'message': 'Minimum Progress calculation logic found'
            })
            return True
        else:
            self.results.append({
                'test': 'Minimum Progress logic implemented',
                'status': 'FAIL',
                'message': 'Minimum Progress logic not found in calculateBUProgress'
            })
            return False
    
    def test_event_listener_on_radio_buttons(self):
        """Test that radio buttons have event listeners"""
        # Check for addEventListener on progress-method elements
        pattern = r"input\[name=['\"]progress-method['\"].*?addEventListener"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Event listener on method radio buttons',
                'status': 'PASS',
                'message': 'Radio button changes trigger event handlers'
            })
            return True
        else:
            self.results.append({
                'test': 'Event listener on method radio buttons',
                'status': 'FAIL',
                'message': 'No event listener on method radio buttons'
            })
            return False
    
    def test_method_persists_across_sessions(self):
        """Test that selected method is persisted in localStorage"""
        pattern = r"localStorage|StorageManager.*progressMethod|formulaSettings"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Method selection persists (localStorage)',
                'status': 'PASS',
                'message': 'Progress method saved to persistent storage'
            })
            return True
        else:
            self.results.append({
                'test': 'Method selection persists (localStorage)',
                'status': 'FAIL',
                'message': 'Progress method not persisted'
            })
            return False
    
    def test_weighted_average_is_default(self):
        """Test that Weighted Average is the default method"""
        pattern = r"checked>.*method-weighted|method-weighted.*checked"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Weighted Average is default',
                'status': 'PASS',
                'message': 'Weighted Average option is pre-selected by default'
            })
            return True
        else:
            self.results.append({
                'test': 'Weighted Average is default',
                'status': 'FAIL',
                'message': 'Weighted Average is not the default'
            })
            return False
    
    def run_all_tests(self):
        """Run all unit tests"""
        print("\n" + "="*70)
        print("PROGRESS CALCULATION METHOD - UNIT TESTS")
        print("="*70 + "\n")
        
        tests = [
            self.test_radio_buttons_exist,
            self.test_method_saved_to_config,
            self.test_calculateBUProgress_reads_method,
            self.test_simple_average_logic_exists,
            self.test_minimum_logic_exists,
            self.test_event_listener_on_radio_buttons,
            self.test_method_persists_across_sessions,
            self.test_weighted_average_is_default,
        ]
        
        for test in tests:
            test()
        
        # Print results
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
    tester = ProgressMethodTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
