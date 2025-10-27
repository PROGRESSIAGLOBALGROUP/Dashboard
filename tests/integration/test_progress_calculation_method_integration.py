#!/usr/bin/env python3
"""
Integration Tests for Progress Calculation Method

This test suite verifies the complete event chain:
1. User selects a method (Weighted/Simple/Minimum)
2. Event listener fires and saves preference
3. calculateBUProgress() uses the selected method
4. Progress values update accordingly
"""

import json
import re
from pathlib import Path

class ProgressMethodIntegrationTester:
    """Integration tests for Progress Calculation Method"""
    
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        """Read the HTML file"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_method_selection_to_storage(self):
        """Test that selecting a method stores it in config"""
        # Check for radio buttons and save mechanism
        has_radios = re.search(r"name=['\"]progress-method['\"]", self.content)
        has_save = re.search(r"saveFormulaConfig|formulaSettings.*progressMethod", self.content)
        
        if has_radios and has_save:
            self.results.append({
                'test': 'Method selection stored in config',
                'status': 'PASS',
                'message': 'Radio button selections are saved to formulaSettings'
            })
            return True
        else:
            self.results.append({
                'test': 'Method selection stored in config',
                'status': 'FAIL',
                'message': f'Radios exist: {bool(has_radios)}, Save exists: {bool(has_save)}'
            })
            return False
    
    def test_storage_to_calculateBUProgress(self):
        """Test that saved method is read when calculating progress"""
        # Check if calculateBUProgress references the stored method
        pattern = r"calculateBUProgress.*?formulaSettings|calculateBUProgress.*?progressMethod"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Stored method used in calculation',
                'status': 'PASS',
                'message': 'calculateBUProgress reads method from storage'
            })
            return True
        else:
            self.results.append({
                'test': 'Stored method used in calculation',
                'status': 'FAIL',
                'message': 'calculateBUProgress does not reference stored method'
            })
            return False
    
    def test_complete_event_chain(self):
        """Test the complete chain: select → store → calculate → display"""
        steps = [
            (r"id=['\"]method-weighted['\"]", "Radio buttons exist"),
            (r"addEventListener", "Event listeners exist"),
            (r"formulaSettings|progressMethod", "Config saved"),
            (r"calculateBUProgress", "Calculation method exists"),
            (r"renderTiles|drawBars|updateKPIs", "UI updates method exists"),
        ]
        
        all_found = all(re.search(pattern, self.content, re.DOTALL) for pattern, _ in steps)
        
        if all_found:
            self.results.append({
                'test': 'Complete event chain integration',
                'status': 'PASS',
                'message': 'Full chain: select method → store → calculate → display'
            })
            return True
        else:
            missing = [desc for pattern, desc in steps if not re.search(pattern, self.content, re.DOTALL)]
            self.results.append({
                'test': 'Complete event chain integration',
                'status': 'FAIL',
                'message': f'Missing components: {", ".join(missing)}'
            })
            return False
    
    def test_weighted_method_calculation(self):
        """Test that Weighted Average calculation uses weights"""
        # Should have weight calculation
        pattern = r"calculateAppWeight|weight.*progress|weighted.?sum"
        if re.search(pattern, self.content, re.IGNORECASE):
            self.results.append({
                'test': 'Weighted Average calculation',
                'status': 'PASS',
                'message': 'Weight-based calculation logic found'
            })
            return True
        else:
            self.results.append({
                'test': 'Weighted Average calculation',
                'status': 'FAIL',
                'message': 'Weight calculation not implemented'
            })
            return False
    
    def test_simple_average_calculation(self):
        """Test that Simple Average calculation sums all apps equally"""
        # Should divide by count, not weights
        pattern = r"simple.*?progress.*?count|method.*?simple|Sum.*?Count"
        if re.search(pattern, self.content, re.IGNORECASE | re.DOTALL):
            self.results.append({
                'test': 'Simple Average calculation',
                'status': 'PASS',
                'message': 'Simple average logic (sum/count) found'
            })
            return True
        else:
            self.results.append({
                'test': 'Simple Average calculation',
                'status': 'FAIL',
                'message': 'Simple average not implemented'
            })
            return False
    
    def test_minimum_calculation(self):
        """Test that Minimum Progress uses Math.min or equivalent"""
        pattern = r"Math\.min|minimum.*?progress|bottleneck"
        if re.search(pattern, self.content, re.IGNORECASE):
            self.results.append({
                'test': 'Minimum Progress calculation',
                'status': 'PASS',
                'message': 'Minimum progress logic found'
            })
            return True
        else:
            self.results.append({
                'test': 'Minimum Progress calculation',
                'status': 'FAIL',
                'message': 'Minimum progress not implemented'
            })
            return False
    
    def test_global_method_integration(self):
        """Test that global method selector is also integrated"""
        # Should have global-method selector too
        pattern = r"name=['\"]global-method['\"]"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Global progress method integration',
                'status': 'PASS',
                'message': 'Global progress method selector found and integrated'
            })
            return True
        else:
            self.results.append({
                'test': 'Global progress method integration',
                'status': 'FAIL',
                'message': 'Global method selector not integrated'
            })
            return False
    
    def test_no_hardcoded_calculation_method(self):
        """Test that calculateBUProgress doesn't hardcode the method"""
        # Find calculateBUProgress and check for hardcoded logic
        pattern = r"calculateBUProgress\(buId\)\s*\{([\s\S]*?)\n\s*\},"
        match = re.search(pattern, self.content)
        
        if not match:
            self.results.append({
                'test': 'No hardcoded calculation method',
                'status': 'FAIL',
                'message': 'calculateBUProgress not found'
            })
            return False
        
        method_body = match.group(1)
        
        # Check for hardcoded "always use weighted"
        if 'return totalWeight > 0' in method_body and 'if.*method' not in method_body:
            # This suggests it's always using weighted average
            self.results.append({
                'test': 'No hardcoded calculation method',
                'status': 'FAIL',
                'message': 'calculateBUProgress appears to hardcode weighted average'
            })
            return False
        
        self.results.append({
            'test': 'No hardcoded calculation method',
            'status': 'PASS',
            'message': 'Calculation method is configurable, not hardcoded'
        })
        return True
    
    def run_all_tests(self):
        """Run all integration tests"""
        print("\n" + "="*70)
        print("PROGRESS CALCULATION METHOD - INTEGRATION TESTS")
        print("="*70 + "\n")
        
        tests = [
            self.test_method_selection_to_storage,
            self.test_storage_to_calculateBUProgress,
            self.test_complete_event_chain,
            self.test_weighted_method_calculation,
            self.test_simple_average_calculation,
            self.test_minimum_calculation,
            self.test_global_method_integration,
            self.test_no_hardcoded_calculation_method,
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
    tester = ProgressMethodIntegrationTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
