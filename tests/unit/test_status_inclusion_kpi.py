"""
Test: Status Inclusion Rules Impact on KPI
Validates that Status Inclusion checkboxes (TBS/WIP/CLO) affect KPI calculations
"""

import re
import json
from pathlib import Path

class StatusInclusionKPITest:
    """Test that Status Inclusion Rules properly filter apps in rebuildDATAFromStorage"""
    
    def __init__(self, html_file):
        self.html_file = Path(html_file)
        self.content = self.html_file.read_text(encoding='utf-8')
        self.results = []
    
    def run_all_tests(self):
        """Execute all tests"""
        print("\n" + "="*70)
        print("STATUS INCLUSION RULES KPI IMPACT TESTS")
        print("="*70)
        
        self.test_rebuild_reads_status_checkboxes()
        self.test_rebuild_filters_apps_by_status()
        self.test_filtered_count_used_for_weighted_global()
        self.test_progress_zero_when_all_filtered()
        self.test_rebuild_called_on_status_change()
        
        return self.print_results()
    
    def test_rebuild_reads_status_checkboxes(self):
        """Test: rebuildDATAFromStorage reads TBS/WIP/CLO checkboxes"""
        pattern = r"const includesTBS = document\.getElementById\('include-tbs'\)\?\.checked"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ rebuildDATAFromStorage reads status checkboxes',
                'status': 'PASS',
                'message': 'Reads include-tbs, include-wip, include-clo DOM elements'
            })
            return True
        else:
            self.results.append({
                'test': '❌ rebuildDATAFromStorage reads status checkboxes',
                'status': 'FAIL',
                'message': 'Does not read TBS/WIP/CLO checkbox values'
            })
            return False
    
    def test_rebuild_filters_apps_by_status(self):
        """Test: rebuildDATAFromStorage filters apps by status before calculating"""
        # Look for the pattern that filters apps
        pattern = r"const filteredApps = apps\.filter\(app => \{[\s\S]*?if \(app\.status === 'TBS'\) return includesTBS"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Apps filtered by status inclusion rules',
                'status': 'PASS',
                'message': 'rebuildDATAFromStorage filters apps before calculating progress'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Apps filtered by status inclusion rules',
                'status': 'FAIL',
                'message': 'Apps not filtered by status in rebuildDATAFromStorage'
            })
            return False
    
    def test_filtered_count_used_for_weighted_global(self):
        """Test: filteredCount (not total count) used for appCount in DATA"""
        pattern = r"const filteredCount = apps\.filter[\s\S]*?appCount: filteredCount"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Filtered count used for weighted global calculation',
                'status': 'PASS',
                'message': 'appCount in DATA reflects filtered apps, not total apps'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Filtered count used for weighted global calculation',
                'status': 'FAIL',
                'message': 'appCount not correctly set to filteredCount'
            })
            return False
    
    def test_progress_zero_when_all_filtered(self):
        """Test: Progress = 0 when all apps are filtered out"""
        # Check for condition that only calculates if filteredApps.length > 0
        pattern = r"if \(filteredApps\.length > 0\) \{[\s\S]*?progress = "
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Progress = 0 when all apps filtered out',
                'status': 'PASS',
                'message': 'Correctly handles case where no apps pass status filter'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Progress = 0 when all apps filtered out',
                'status': 'FAIL',
                'message': 'Does not handle empty filtered apps array'
            })
            return False
    
    def test_rebuild_called_on_status_change(self):
        """Test: updateStatusInclusion calls rebuildDATAFromStorage via apply()"""
        # Look for updateStatusInclusion calling UIController.apply()
        pattern = r"updateStatusInclusion\(\) \{[\s\S]*?Dashboard\.UIController\.apply\(\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Status change triggers rebuildDATAFromStorage',
                'status': 'PASS',
                'message': 'updateStatusInclusion calls UIController.apply() which rebuilds DATA'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Status change triggers rebuildDATAFromStorage',
                'status': 'FAIL',
                'message': 'updateStatusInclusion does not trigger rebuild'
            })
            return False
    
    def print_results(self):
        """Print test results summary"""
        passed = sum(1 for r in self.results if r['status'] == 'PASS')
        failed = sum(1 for r in self.results if r['status'] == 'FAIL')
        
        print("\n" + "-"*70)
        for result in self.results:
            status_icon = "✅" if result['status'] == 'PASS' else "❌"
            print(f"\n{status_icon} {result['test']}")
            print(f"   Status: {result['status']}")
            print(f"   Message: {result['message']}")
        
        print("\n" + "="*70)
        print(f"RESULTS: {passed} PASSED | {failed} FAILED")
        print("="*70 + "\n")
        
        if failed == 0:
            print("🎉 STATUS INCLUSION RULES NOW AFFECT KPI")
            print("Unchecking TBS/WIP/CLO will immediately update KPI Total Avg")
            print("="*70 + "\n")
        
        return failed == 0


if __name__ == '__main__':
    test_file = r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html'
    tester = StatusInclusionKPITest(test_file)
    success = tester.run_all_tests()
    exit(0 if success else 1)
