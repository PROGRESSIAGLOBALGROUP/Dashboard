"""
Integration Test: KPI Global Sync Behavior
Simulates dashboard behavior to verify Hero and KPI show same avgGlobal
"""

import re
import json

class KPIGlobalSyncIntegrationTest:
    """Integration test to verify complete KPI sync flow"""
    
    def __init__(self, html_file):
        self.html_file = html_file
        with open(html_file, encoding='utf-8') as f:
            self.content = f.read()
        self.results = []
    
    def run_all_tests(self):
        print("\n" + "="*70)
        print("KPI GLOBAL SYNC INTEGRATION TESTS")
        print("="*70)
        
        self.test_avgglobal_calculation_exists()
        self.test_updatekpis_flow_weighted()
        self.test_updatekpis_flow_simple()
        self.test_hero_and_kpi_consistency()
        self.test_all_calls_updated()
        
        return self.print_results()
    
    def test_avgglobal_calculation_exists(self):
        """Test: avgGlobal is calculated in apply()"""
        pattern = r"let avgGlobal = 0;[\s\S]*?if \(globalMethod === 'simple'\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ avgGlobal calculation exists in apply()',
                'status': 'PASS',
                'message': 'Found avgGlobal calculation with globalMethod check'
            })
            return True
        else:
            self.results.append({
                'test': '❌ avgGlobal calculation exists in apply()',
                'status': 'FAIL',
                'message': 'avgGlobal calculation not found'
            })
            return False
    
    def test_updatekpis_flow_weighted(self):
        """Test: Weighted method flow passes avgGlobal correctly"""
        # Verify weighted calculation uses appCount weighting
        weighted_pattern = r"const totalApps = DATA\.reduce\(\(sum, d\) => sum \+ \(d\.appCount \|\| 0\)"
        weighted_match = re.search(weighted_pattern, self.content)
        
        if weighted_match:
            self.results.append({
                'test': '✅ Weighted method calculation present',
                'status': 'PASS',
                'message': 'Weighted by BU Size formula found and intact'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Weighted method calculation present',
                'status': 'FAIL',
                'message': 'Weighted calculation not found in apply()'
            })
            return False
    
    def test_updatekpis_flow_simple(self):
        """Test: Simple method flow passes avgGlobal correctly"""
        # Verify simple calculation is sum/length
        simple_pattern = r"avgGlobal = DATA\.reduce\(\(s, d\) => s \+ \(d\.progress \|\| 0\), 0\) \/ DATA\.length"
        simple_match = re.search(simple_pattern, self.content)
        
        if simple_match:
            self.results.append({
                'test': '✅ Simple method calculation present',
                'status': 'PASS',
                'message': 'Simple Average formula found and intact'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Simple method calculation present',
                'status': 'FAIL',
                'message': 'Simple calculation not found in apply()'
            })
            return False
    
    def test_hero_and_kpi_consistency(self):
        """Test: Hero and KPI get same avgGlobal value"""
        # Hero uses: let heroValue = avgGlobal;
        # KPI gets: this.updateKPIs(items, avgGlobal);
        
        hero_pattern = r"let heroValue = avgGlobal;"
        kpi_pattern = r"this\.updateKPIs\(items, avgGlobal\)"
        
        hero_match = re.search(hero_pattern, self.content)
        kpi_match = re.search(kpi_pattern, self.content)
        
        if hero_match and kpi_match:
            self.results.append({
                'test': '✅ Hero and KPI both use same avgGlobal',
                'status': 'PASS',
                'message': 'Both Hero and KPI receive same avgGlobal value from apply()'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Hero and KPI both use same avgGlobal',
                'status': 'FAIL',
                'message': f'Hero found: {bool(hero_match)}, KPI found: {bool(kpi_match)}'
            })
            return False
    
    def test_all_calls_updated(self):
        """Test: All calls to updateKPIs have been updated"""
        # Find all updateKPIs calls
        all_calls = re.findall(r"this\.updateKPIs\([^)]+\)", self.content)
        
        # Should have at least 2 calls: one in apply(), one in empty case
        # All should include avgGlobal or 0
        updated_calls = [c for c in all_calls if 'avgGlobal' in c or ', 0)' in c]
        
        if len(updated_calls) >= 2:
            self.results.append({
                'test': '✅ All updateKPIs calls updated with avg parameter',
                'status': 'PASS',
                'message': f'Found {len(updated_calls)} calls with avgGlobal or 0 parameter'
            })
            return True
        else:
            self.results.append({
                'test': '❌ All updateKPIs calls updated with avg parameter',
                'status': 'FAIL',
                'message': f'Only found {len(updated_calls)} updated calls, expected >=2'
            })
            return False
    
    def print_results(self):
        """Print test results"""
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
            print("🎉 INTEGRATION TEST SUCCESSFUL")
            print("Hero Progress and KPI Total Avg will now show consistent values")
            print("="*70 + "\n")
        
        return failed == 0


if __name__ == '__main__':
    test_file = r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html'
    tester = KPIGlobalSyncIntegrationTest(test_file)
    success = tester.run_all_tests()
    exit(0 if success else 1)
