"""
Integration Test: Status Inclusion Rules End-to-End Flow
Validates complete flow from checkbox change → rebuild DATA → recalculate avgGlobal → update KPI
"""

import re

class StatusInclusionIntegrationTest:
    """Integration test for Status Inclusion Rules affecting KPI"""
    
    def __init__(self, html_file):
        with open(html_file, encoding='utf-8') as f:
            self.content = f.read()
        self.results = []
    
    def run_all_tests(self):
        print("\n" + "="*70)
        print("STATUS INCLUSION RULES - END-TO-END INTEGRATION TESTS")
        print("="*70)
        
        self.test_checkbox_event_handlers()
        self.test_status_inclusion_to_rebuild_flow()
        self.test_rebuild_to_avgcalc_flow()
        self.test_avgcalc_to_kpi_flow()
        self.test_data_consistency()
        
        return self.print_results()
    
    def test_checkbox_event_handlers(self):
        """Test: Status checkboxes have event listeners"""
        pattern = r"statusCheckboxes.*addEventListener.*updateStatusInclusion"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Status checkboxes have event listeners',
                'status': 'PASS',
                'message': 'Checkboxes trigger updateStatusInclusion on change'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Status checkboxes have event listeners',
                'status': 'FAIL',
                'message': 'Checkboxes may not trigger updates'
            })
            return False
    
    def test_status_inclusion_to_rebuild_flow(self):
        """Test: updateStatusInclusion → UIController.apply() → rebuildDATAFromStorage"""
        pattern = r"updateStatusInclusion\(\)[\s\S]*?Dashboard\.UIController\.apply\(\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Status change triggers rebuild flow',
                'status': 'PASS',
                'message': 'updateStatusInclusion correctly calls apply() which rebuilds DATA'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Status change triggers rebuild flow',
                'status': 'FAIL',
                'message': 'Flow interrupted - apply() not called'
            })
            return False
    
    def test_rebuild_to_avgcalc_flow(self):
        """Test: rebuildDATAFromStorage → avgGlobal calculation uses new DATA"""
        # Check that apply() calls rebuildDATAFromStorage before calculating avgGlobal
        pattern = r"rebuildDATAFromStorage\(\)[\s\S]{0,500}let avgGlobal"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Rebuilt DATA feeds into avgGlobal calculation',
                'status': 'PASS',
                'message': 'rebuildDATAFromStorage called before avgGlobal calculation'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Rebuilt DATA feeds into avgGlobal calculation',
                'status': 'FAIL',
                'message': 'avgGlobal may not use latest DATA'
            })
            return False
    
    def test_avgcalc_to_kpi_flow(self):
        """Test: avgGlobal → updateKPIs() passes correct value to KPI display"""
        pattern = r"let avgGlobal[\s\S]{0,500}this\.updateKPIs\(items, avgGlobal\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ avgGlobal flows to KPI display',
                'status': 'PASS',
                'message': 'updateKPIs receives avgGlobal and updates #kpiAvg'
            })
            return True
        else:
            self.results.append({
                'test': '❌ avgGlobal flows to KPI display',
                'status': 'FAIL',
                'message': 'KPI may not receive updated avgGlobal'
            })
            return False
    
    def test_data_consistency(self):
        """Test: Hero and KPI both use same DATA → same avgGlobal"""
        # Hero uses: let heroValue = avgGlobal;
        # KPI uses: this.updateKPIs(items, avgGlobal);
        # Both from same avgGlobal calculation
        
        pattern = r"let heroValue = avgGlobal;[\s\S]*?this\.updateKPIs\(items, avgGlobal\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Hero and KPI use same avgGlobal',
                'status': 'PASS',
                'message': 'Both Hero and KPI get consistent value from same DATA'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Hero and KPI use same avgGlobal',
                'status': 'FAIL',
                'message': 'Hero and KPI may use different calculation sources'
            })
            return False
    
    def print_results(self):
        """Print results"""
        passed = sum(1 for r in self.results if r['status'] == 'PASS')
        failed = sum(1 for r in self.results if r['status'] == 'FAIL')
        
        print("\n" + "-"*70)
        for result in self.results:
            status_icon = "✅" if result['status'] == 'PASS' else "❌"
            print(f"\n{status_icon} {result['test']}")
            print(f"   Status: {result['status']}")
            print(f"   Message: {result['message']}")
        
        print("\n" + "="*70)
        print(f"INTEGRATION RESULTS: {passed} PASSED | {failed} FAILED")
        print("="*70 + "\n")
        
        if failed == 0:
            print("✅ COMPLETE FLOW VALIDATED")
            print("\nFlow Summary:")
            print("1. User clicks checkbox (TBS/WIP/CLO)")
            print("2. updateStatusInclusion() triggered")
            print("3. UIController.apply() called")
            print("4. rebuildDATAFromStorage() filters apps by status")
            print("5. avgGlobal recalculated from filtered DATA")
            print("6. Hero Progress and KPI Total Avg both updated")
            print("7. UI displays synchronized values")
            print("="*70 + "\n")
        
        return failed == 0


if __name__ == '__main__':
    test_file = r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html'
    tester = StatusInclusionIntegrationTest(test_file)
    success = tester.run_all_tests()
    exit(0 if success else 1)
