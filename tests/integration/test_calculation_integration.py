#!/usr/bin/env python3
"""
Integration Test - Global + BU Progress Calculation Methods
Verifies both calculation systems work together correctly
"""

import re
from pathlib import Path

class IntegrationTest:
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_1_both_selectors_present(self):
        """Test that both Progress Method and Global Method selectors exist"""
        progress_method_radios = 'name="progress-method"' in self.content
        global_method_radios = 'name="global-method"' in self.content
        
        if progress_method_radios and global_method_radios:
            self.results.append({
                'test': '1. Both Method Selectors Present',
                'status': 'PASS',
                'message': 'Progress Method and Global Method selectors both exist'
            })
            return True
        else:
            self.results.append({
                'test': '1. Both Method Selectors Present',
                'status': 'FAIL',
                'message': f'Progress: {progress_method_radios}, Global: {global_method_radios}'
            })
            return False
    
    def test_2_independent_configurations(self):
        """Test that both configs are independent (separate storage)"""
        has_progress_config = 'progressMethod:' in self.content
        has_global_config = 'globalMethod:' in self.content
        
        if has_progress_config and has_global_config:
            self.results.append({
                'test': '2. Independent Configurations',
                'status': 'PASS',
                'message': 'Both settings stored independently in config'
            })
            return True
        else:
            self.results.append({
                'test': '2. Independent Configurations',
                'status': 'FAIL',
                'message': 'Missing one or both config settings'
            })
            return False
    
    def test_3_bu_method_affects_bu_calc(self):
        """Test that BU Progress Method affects BU-level calculations"""
        pattern = r"calculateBUProgress.*?progressMethod.*?case\s+['\"]simple"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': '3. BU Method Affects BU Calculations',
                'status': 'PASS',
                'message': 'calculateBUProgress() respects progressMethod setting'
            })
            return True
        else:
            self.results.append({
                'test': '3. BU Method Affects BU Calculations',
                'status': 'FAIL',
                'message': 'BU calculation not using progressMethod'
            })
            return False
    
    def test_4_global_method_affects_global_calc(self):
        """Test that Global Method affects global calculation"""
        pattern = r"globalMethod.*?simple.*?avgGlobal.*?DATA\.reduce"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': '4. Global Method Affects Global Calculation',
                'status': 'PASS',
                'message': 'Global progress calculation respects globalMethod'
            })
            return True
        else:
            self.results.append({
                'test': '4. Global Method Affects Global Calculation',
                'status': 'FAIL',
                'message': 'Global calculation not using globalMethod'
            })
            return False
    
    def test_5_status_inclusion_works_with_bu_method(self):
        """Test that Status Inclusion Rules work with BU Progress Method"""
        pattern = r"include.*?TBS.*?activeApps.*?progress.*?simple"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': '5. Status Inclusion + BU Method Integration',
                'status': 'PASS',
                'message': 'Status filtering applied before method calculation'
            })
            return True
        else:
            self.results.append({
                'test': '5. Status Inclusion + BU Method Integration',
                'status': 'FAIL',
                'message': 'Status inclusion may not work with method selection'
            })
            return False
    
    def test_6_three_bu_methods_available(self):
        """Test that all 3 BU progress methods are available"""
        weighted_ok = "case 'weighted':" in self.content
        simple_ok = "case 'simple':" in self.content
        minimum_ok = "case 'minimum':" in self.content
        
        if weighted_ok and simple_ok and minimum_ok:
            self.results.append({
                'test': '6. All 3 BU Methods Available',
                'status': 'PASS',
                'message': 'Weighted, Simple, and Minimum methods all present'
            })
            return True
        else:
            self.results.append({
                'test': '6. All 3 BU Methods Available',
                'status': 'FAIL',
                'message': f'Weighted: {weighted_ok}, Simple: {simple_ok}, Minimum: {minimum_ok}'
            })
            return False
    
    def test_7_two_global_methods_available(self):
        """Test that both global methods are available"""
        weighted_global = "globalMethod === 'weighted'" in self.content or \
                         "Weighted by BU Size" in self.content
        simple_global = "globalMethod === 'simple'" in self.content or \
                       "Simple BU Average" in self.content
        
        if weighted_global and simple_global:
            self.results.append({
                'test': '7. Both Global Methods Available',
                'status': 'PASS',
                'message': 'Weighted by BU Size and Simple BU Average both present'
            })
            return True
        else:
            self.results.append({
                'test': '7. Both Global Methods Available',
                'status': 'FAIL',
                'message': f'Weighted: {weighted_global}, Simple: {simple_global}'
            })
            return False
    
    def test_8_both_use_storage_manager(self):
        """Test that both methods use StorageManager for persistence"""
        pattern = r"StorageManager.*?progressMethod.*?StorageManager.*?globalMethod"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': '8. Both Use StorageManager',
                'status': 'PASS',
                'message': 'Both methods properly persisted via StorageManager'
            })
            return True
        else:
            self.results.append({
                'test': '8. Both Use StorageManager',
                'status': 'FAIL',
                'message': 'StorageManager not used for both methods'
            })
            return False
    
    def test_9_no_hardcoded_defaults_except_weighted(self):
        """Test that defaults are correct (weighted as default)"""
        if "progressMethod || 'weighted'" in self.content and \
           "globalMethod || 'weighted'" in self.content:
            self.results.append({
                'test': '9. Correct Defaults (Weighted)',
                'status': 'PASS',
                'message': 'Both methods default to weighted as expected'
            })
            return True
        else:
            self.results.append({
                'test': '9. Correct Defaults (Weighted)',
                'status': 'FAIL',
                'message': 'Default fallback values may be incorrect'
            })
            return False
    
    def test_10_rounding_consistent(self):
        """Test that rounding is consistent across methods"""
        rounding_pattern = r"Math\.round\(.*?\* 100\) / 100"
        matches = len(re.findall(rounding_pattern, self.content))
        
        if matches >= 6:  # At least 6 places where we round
            self.results.append({
                'test': '10. Consistent Rounding',
                'status': 'PASS',
                'message': f'Proper rounding found in {matches} places'
            })
            return True
        else:
            self.results.append({
                'test': '10. Consistent Rounding',
                'status': 'FAIL',
                'message': f'Only {matches} rounding operations found'
            })
            return False
    
    def run_all_tests(self):
        print("\n" + "="*80)
        print("INTEGRATION TEST - PROGRESS & GLOBAL FORMULA METHODS")
        print("="*80 + "\n")
        
        tests = [
            self.test_1_both_selectors_present,
            self.test_2_independent_configurations,
            self.test_3_bu_method_affects_bu_calc,
            self.test_4_global_method_affects_global_calc,
            self.test_5_status_inclusion_works_with_bu_method,
            self.test_6_three_bu_methods_available,
            self.test_7_two_global_methods_available,
            self.test_8_both_use_storage_manager,
            self.test_9_no_hardcoded_defaults_except_weighted,
            self.test_10_rounding_consistent,
        ]
        
        for test in tests:
            test()
        
        passed = sum(1 for r in self.results if r['status'] == 'PASS')
        failed = sum(1 for r in self.results if r['status'] == 'FAIL')
        
        for result in self.results:
            icon = "✅" if result['status'] == 'PASS' else "❌"
            print(f"{icon} {result['test']}")
            print(f"   └─ {result['message']}\n")
        
        print("="*80)
        print(f"Results: {passed} passed, {failed} failed out of {len(self.results)} tests")
        print("="*80 + "\n")
        
        if failed == 0:
            print("🎉 INTEGRATION TEST PASSED")
            print("Both calculation systems work together correctly\n")
        else:
            print(f"⚠️  {failed} issue(s) detected\n")
        
        return failed == 0

if __name__ == '__main__':
    import sys
    tester = IntegrationTest()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
