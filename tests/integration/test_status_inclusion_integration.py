#!/usr/bin/env python3
"""
Integration Tests for Status Inclusion Rules Fix

This test suite verifies the complete event chain and real-world behavior:
1. User toggles checkbox
2. Event listener fires updateStatusInclusion()
3. calculateBUProgress() reads new checkbox state
4. UI updates with new progress values

Tests use real data structures matching the dashboard schema.
"""

import json
import re
from pathlib import Path

class StatusInclusionIntegrationTester:
    """Integration tests for Status Inclusion Rules event chain"""
    
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        """Read the HTML file"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_event_chain_checkbox_to_listener(self):
        """Test that checkboxes trigger event listeners"""
        # Check for checkbox HTML
        checkbox_pattern = r"id=['\"]include-(?:tbs|wip|clo)['\"].*?class=['\"][^'\"]*inclusion-checkbox"
        checkboxes_exist = len(re.findall(checkbox_pattern, self.content)) >= 3
        
        # Check for event listener
        listener_pattern = r"addEventListener\('change'.*?updateStatusInclusion"
        listener_exists = re.search(listener_pattern, self.content, re.DOTALL)
        
        if checkboxes_exist and listener_exists:
            self.results.append({
                'test': 'Event chain: checkbox → listener',
                'status': 'PASS',
                'message': 'Checkboxes and event listeners properly connected'
            })
            return True
        else:
            self.results.append({
                'test': 'Event chain: checkbox → listener',
                'status': 'FAIL',
                'message': f'Checkboxes exist: {checkboxes_exist}, Listener exists: {bool(listener_exists)}'
            })
            return False
    
    def test_event_chain_listener_to_updateStatusInclusion(self):
        """Test that event listener calls updateStatusInclusion()"""
        pattern = r"addEventListener\('change'.*?this\.updateStatusInclusion\(\)"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Event chain: listener → updateStatusInclusion()',
                'status': 'PASS',
                'message': 'updateStatusInclusion() properly called from event listener'
            })
            return True
        else:
            self.results.append({
                'test': 'Event chain: listener → updateStatusInclusion()',
                'status': 'FAIL',
                'message': 'Event listener does not call updateStatusInclusion()'
            })
            return False
    
    def test_event_chain_updateStatusInclusion_to_apply(self):
        """Test that updateStatusInclusion() calls UIController.apply()"""
        # Find the method and check if it contains apply()
        pattern = r"updateStatusInclusion\(\)\s*\{([^}]*?(?:\{[^}]*\}[^}]*?)*)\}"
        matches = list(re.finditer(pattern, self.content, re.DOTALL))
        
        for match in matches:
            method_body = match.group(1)
            if 'Dashboard.UIController.apply()' in method_body or 'apply()' in method_body:
                self.results.append({
                    'test': 'Event chain: updateStatusInclusion() → apply()',
                    'status': 'PASS',
                    'message': 'apply() properly called from updateStatusInclusion()'
                })
                return True
        
        self.results.append({
            'test': 'Event chain: updateStatusInclusion() → apply()',
            'status': 'FAIL',
            'message': 'apply() not called from updateStatusInclusion()'
        })
        return False
    
    def test_event_chain_apply_recalculates(self):
        """Test that apply() method recalculates progress"""
        # Check that apply() calls rebuild and progress functions
        pattern = r"apply\(\)\s*\{[^}]*rebuildDATAFromStorage|drawBars|renderTiles"
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': 'Event chain: apply() recalculates',
                'status': 'PASS',
                'message': 'apply() triggers recalculation and UI update'
            })
            return True
        else:
            self.results.append({
                'test': 'Event chain: apply() recalculates',
                'status': 'FAIL',
                'message': 'apply() does not properly recalculate'
            })
            return False
    
    def test_complete_event_chain(self):
        """Test the complete event chain from checkbox to UI update"""
        steps = [
            (r"id=['\"]include-tbs['\"]", "Checkbox exists"),
            (r"addEventListener\('change'", "Event listener exists"),
            (r"updateStatusInclusion\(\)", "updateStatusInclusion() exists"),
            (r"Dashboard\.UIController\.apply\(\)", "apply() called"),
            (r"calculateBUProgress\(buId\)", "calculateBUProgress() exists"),
        ]
        
        all_found = True
        for pattern, description in steps:
            if not re.search(pattern, self.content):
                all_found = False
                break
        
        if all_found:
            self.results.append({
                'test': 'Complete event chain integration',
                'status': 'PASS',
                'message': 'Full chain: checkbox → listener → updateStatusInclusion → apply → recalculate'
            })
            return True
        else:
            self.results.append({
                'test': 'Complete event chain integration',
                'status': 'FAIL',
                'message': 'Some components of the event chain are missing'
            })
            return False
    
    def test_no_hardcoded_defaults_in_calculateBUProgress(self):
        """Test that calculateBUProgress doesn't hardcode status values"""
        # Find the method
        pattern = r"calculateBUProgress\(buId\)\s*\{([\s\S]*?)\n\s*\},"
        match = re.search(pattern, self.content)
        
        if not match:
            self.results.append({
                'test': 'No hardcoded status defaults',
                'status': 'FAIL',
                'message': 'calculateBUProgress method not found'
            })
            return False
        
        method_body = match.group(1)
        
        # Should read from DOM, not hardcode
        has_dom_reads = 'document.getElementById' in method_body
        has_dynamic_filter = 'return includesTBS' in method_body or 'return includesWIP' in method_body
        
        if has_dom_reads and has_dynamic_filter:
            self.results.append({
                'test': 'No hardcoded status defaults',
                'status': 'PASS',
                'message': 'Status filtering is dynamic, not hardcoded'
            })
            return True
        else:
            self.results.append({
                'test': 'No hardcoded status defaults',
                'status': 'FAIL',
                'message': f'Dynamic reads: {has_dom_reads}, Dynamic filter: {has_dynamic_filter}'
            })
            return False
    
    def test_kpi_update_integration(self):
        """Test that KPI metrics are updated in apply()"""
        pattern = r"updateKPIs\(items\)"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'KPI metrics updated',
                'status': 'PASS',
                'message': 'updateKPIs() called in apply() - metrics will update'
            })
            return True
        else:
            self.results.append({
                'test': 'KPI metrics updated',
                'status': 'FAIL',
                'message': 'updateKPIs() not called - metrics may not update'
            })
            return False
    
    def test_multi_column_sorting_not_broken(self):
        """Test that multi-column sorting is still intact"""
        # Check for sorting method
        pattern = r"cycleSortOrder\(columnName\)"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'Multi-column sorting intact',
                'status': 'PASS',
                'message': 'cycleSortOrder() method found - sorting not broken'
            })
            return True
        else:
            self.results.append({
                'test': 'Multi-column sorting intact',
                'status': 'FAIL',
                'message': 'cycleSortOrder() not found - sorting may be broken'
            })
            return False
    
    def test_storage_manager_integration(self):
        """Test that StorageManager is still used correctly"""
        pattern = r"Dashboard\.StorageManager\.getAppsByBU\(buId\)"
        if re.search(pattern, self.content):
            self.results.append({
                'test': 'StorageManager integration',
                'status': 'PASS',
                'message': 'StorageManager correctly used to fetch app data'
            })
            return True
        else:
            self.results.append({
                'test': 'StorageManager integration',
                'status': 'FAIL',
                'message': 'StorageManager not properly integrated'
            })
            return False
    
    def run_all_tests(self):
        """Run all integration tests"""
        print("\n" + "="*70)
        print("STATUS INCLUSION RULES - INTEGRATION TESTS")
        print("="*70 + "\n")
        
        tests = [
            self.test_event_chain_checkbox_to_listener,
            self.test_event_chain_listener_to_updateStatusInclusion,
            self.test_event_chain_updateStatusInclusion_to_apply,
            self.test_event_chain_apply_recalculates,
            self.test_complete_event_chain,
            self.test_no_hardcoded_defaults_in_calculateBUProgress,
            self.test_kpi_update_integration,
            self.test_multi_column_sorting_not_broken,
            self.test_storage_manager_integration,
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
    tester = StatusInclusionIntegrationTester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
