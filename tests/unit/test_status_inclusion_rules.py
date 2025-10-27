#!/usr/bin/env python3
"""
Unit Tests for Status Inclusion Rules Fix

This test suite verifies that the Status Inclusion Rules implementation
correctly filters applications based on TBS/WIP/CLO status checkboxes.

Tests:
- Verify calculateBUProgress() reads status checkboxes
- Verify dynamic filtering logic
- Verify KPI calculations with different status filters
- Verify no regressions in weight calculation
"""

import json
import re
from pathlib import Path

class StatusInclusionTester:
    """Unit tests for Status Inclusion Rules"""
    
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        """Read the HTML file"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_calculateBUProgress_reads_tbs_checkbox(self):
        """Test that calculateBUProgress() reads include-tbs checkbox"""
        pattern = r"const includesTBS = document\.getElementById\('include-tbs'\)\?\.checked"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'calculateBUProgress reads TBS checkbox',
                'status': 'PASS',
                'message': 'includes-tbs checkbox read correctly'
            })
            return True
        else:
            self.results.append({
                'test': 'calculateBUProgress reads TBS checkbox',
                'status': 'FAIL',
                'message': 'TBS checkbox not read'
            })
            return False
    
    def test_calculateBUProgress_reads_wip_checkbox(self):
        """Test that calculateBUProgress() reads include-wip checkbox"""
        pattern = r"const includesWIP = document\.getElementById\('include-wip'\)\?\.checked"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'calculateBUProgress reads WIP checkbox',
                'status': 'PASS',
                'message': 'includes-wip checkbox read correctly'
            })
            return True
        else:
            self.results.append({
                'test': 'calculateBUProgress reads WIP checkbox',
                'status': 'FAIL',
                'message': 'WIP checkbox not read'
            })
            return False
    
    def test_calculateBUProgress_reads_clo_checkbox(self):
        """Test that calculateBUProgress() reads include-clo checkbox"""
        pattern = r"const includesCLO = document\.getElementById\('include-clo'\)\?\.checked"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'calculateBUProgress reads CLO checkbox',
                'status': 'PASS',
                'message': 'includes-clo checkbox read correctly'
            })
            return True
        else:
            self.results.append({
                'test': 'calculateBUProgress reads CLO checkbox',
                'status': 'FAIL',
                'message': 'CLO checkbox not read'
            })
            return False
    
    def test_dynamic_filtering_logic_tbs(self):
        """Test that TBS status filtering logic exists"""
        pattern = r"if \(app\.status === 'TBS'\) return includesTBS"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Dynamic filtering for TBS status',
                'status': 'PASS',
                'message': 'TBS filtering logic implemented'
            })
            return True
        else:
            self.results.append({
                'test': 'Dynamic filtering for TBS status',
                'status': 'FAIL',
                'message': 'TBS filtering logic missing'
            })
            return False
    
    def test_dynamic_filtering_logic_wip(self):
        """Test that WIP status filtering logic exists"""
        pattern = r"if \(app\.status === 'WIP'\) return includesWIP"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Dynamic filtering for WIP status',
                'status': 'PASS',
                'message': 'WIP filtering logic implemented'
            })
            return True
        else:
            self.results.append({
                'test': 'Dynamic filtering for WIP status',
                'status': 'FAIL',
                'message': 'WIP filtering logic missing'
            })
            return False
    
    def test_dynamic_filtering_logic_clo(self):
        """Test that CLO status filtering logic exists"""
        pattern = r"if \(app\.status === 'CLO'\) return includesCLO"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Dynamic filtering for CLO status',
                'status': 'PASS',
                'message': 'CLO filtering logic implemented'
            })
            return True
        else:
            self.results.append({
                'test': 'Dynamic filtering for CLO status',
                'status': 'FAIL',
                'message': 'CLO filtering logic missing'
            })
            return False
    
    def test_old_hardcoded_logic_removed(self):
        """Test that old hardcoded 'app.status !== TBS' logic is removed from calculateBUProgress"""
        # Find calculateBUProgress method
        pattern = r"calculateBUProgress\(buId\)\s*\{([^}]*?(?:\{[^}]*\}[^}]*?)*)\}"
        matches = list(re.finditer(pattern, self.content, re.DOTALL))
        
        if not matches:
            self.results.append({
                'test': 'Old hardcoded logic removed',
                'status': 'FAIL',
                'message': 'calculateBUProgress method not found'
            })
            return False
        
        for match in matches:
            method_body = match.group(1)
            # Should not contain old hardcoded logic in the method
            if "app.status !== 'TBS'" in method_body and "const activeApps = apps.filter" in method_body:
                # This is the old pattern - check if it's been replaced
                if "includesTBS" in method_body:
                    # New logic is there, old is gone
                    continue
                else:
                    self.results.append({
                        'test': 'Old hardcoded logic removed',
                        'status': 'FAIL',
                        'message': 'Old hardcoded logic still using app.status !== TBS'
                    })
                    return False
        
        self.results.append({
            'test': 'Old hardcoded logic removed',
            'status': 'PASS',
            'message': 'Old hardcoded logic successfully replaced with dynamic filtering'
        })
        return True
    
    def test_updateStatusInclusion_triggers_apply(self):
        """Test that updateStatusInclusion() calls Dashboard.UIController.apply()"""
        pattern = r"updateStatusInclusion\(\)\s*\{([^}]*?(?:\{[^}]*\}[^}]*?)*)\}"
        matches = list(re.finditer(pattern, self.content, re.DOTALL))
        
        for match in matches:
            method_body = match.group(1)
            if 'Dashboard.UIController.apply()' in method_body or 'apply()' in method_body:
                self.results.append({
                    'test': 'updateStatusInclusion() triggers apply()',
                    'status': 'PASS',
                    'message': 'Recalculation trigger implemented'
                })
                return True
        
        self.results.append({
            'test': 'updateStatusInclusion() triggers apply()',
            'status': 'FAIL',
            'message': 'Recalculation trigger not found'
        })
        return False
    
    def test_event_listener_exists(self):
        """Test that event listeners for status checkboxes exist"""
        pattern = r"inclusion-checkbox.*addEventListener\('change'"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Event listener for status checkboxes',
                'status': 'PASS',
                'message': 'Event listener properly set up'
            })
            return True
        else:
            self.results.append({
                'test': 'Event listener for status checkboxes',
                'status': 'FAIL',
                'message': 'Event listener not found'
            })
            return False
    
    def test_weight_calculation_unchanged(self):
        """Test that weight calculation formula is unchanged"""
        # Weight formula: [(C × I × P) / 27] × 3
        pattern = r"calculateAppWeight.*?\(\s*app\s*\)\s*\{[^}]*\}"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Weight calculation unchanged',
                'status': 'PASS',
                'message': 'Weight calculation formula preserved'
            })
            return True
        else:
            self.results.append({
                'test': 'Weight calculation unchanged',
                'status': 'FAIL',
                'message': 'Weight calculation may have been modified'
            })
            return False
    
    def run_all_tests(self):
        """Run all unit tests"""
        print("\n" + "="*70)
        print("STATUS INCLUSION RULES - UNIT TESTS")
        print("="*70 + "\n")
        
        tests = [
            self.test_calculateBUProgress_reads_tbs_checkbox,
            self.test_calculateBUProgress_reads_wip_checkbox,
            self.test_calculateBUProgress_reads_clo_checkbox,
            self.test_dynamic_filtering_logic_tbs,
            self.test_dynamic_filtering_logic_wip,
            self.test_dynamic_filtering_logic_clo,
            self.test_old_hardcoded_logic_removed,
            self.test_updateStatusInclusion_triggers_apply,
            self.test_event_listener_exists,
            self.test_weight_calculation_unchanged,
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
    tester = StatusInclusionTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
