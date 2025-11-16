"""
Test for KPI Global Progress Synchronization Fix
Validates that Hero Progress and KPI Total Avg show the same avgGlobal value
respecting the globalMethod configuration (weighted vs simple)
"""

import re
import json
from pathlib import Path

class KPIGlobalSyncTest:
    """Test that KPI and Hero use consistent avgGlobal calculation"""
    
    def __init__(self, html_file):
        self.html_file = Path(html_file)
        self.content = self.html_file.read_text(encoding='utf-8')
        self.results = []
        
    def run_all_tests(self):
        """Execute all tests"""
        print("\n" + "="*70)
        print("KPI GLOBAL SYNC VERIFICATION TESTS")
        print("="*70)
        
        self.test_updatekpis_accepts_avgglobal()
        self.test_updatekpis_uses_avgglobal_for_display()
        self.test_apply_passes_avgglobal()
        self.test_empty_case_passes_zero()
        self.test_no_recalculation_in_updatekpis()
        
        return self.print_results()
    
    def test_updatekpis_accepts_avgglobal(self):
        """Test: updateKPIs() signature includes avgGlobal parameter"""
        pattern = r"updateKPIs\(items,\s*avgGlobal\s*=\s*0\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ updateKPIs accepts avgGlobal parameter',
                'status': 'PASS',
                'message': 'Signature correctly updated with avgGlobal = 0 default'
            })
            return True
        else:
            self.results.append({
                'test': '❌ updateKPIs accepts avgGlobal parameter',
                'status': 'FAIL',
                'message': 'updateKPIs signature does not include avgGlobal parameter'
            })
            return False
    
    def test_updatekpis_uses_avgglobal_for_display(self):
        """Test: updateKPIs() uses avgGlobal for #kpiAvg display"""
        pattern = r"document\.querySelector\(['\"]\#kpiAvg['\"]\)\.textContent\s*=\s*avgGlobal\.toFixed"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ updateKPIs uses avgGlobal for #kpiAvg display',
                'status': 'PASS',
                'message': '#kpiAvg now displays avgGlobal instead of recalculating'
            })
            return True
        else:
            self.results.append({
                'test': '❌ updateKPIs uses avgGlobal for #kpiAvg display',
                'status': 'FAIL',
                'message': '#kpiAvg does not use avgGlobal parameter'
            })
            return False
    
    def test_apply_passes_avgglobal(self):
        """Test: apply() passes avgGlobal to updateKPIs()"""
        # Look for the pattern: this.updateKPIs(items, avgGlobal);
        pattern = r"this\.updateKPIs\(items,\s*avgGlobal\)"
        matches = re.findall(pattern, self.content)
        
        if len(matches) >= 1:
            self.results.append({
                'test': '✅ apply() passes avgGlobal to updateKPIs()',
                'status': 'PASS',
                'message': f'Found {len(matches)} call(s) with avgGlobal parameter'
            })
            return True
        else:
            self.results.append({
                'test': '❌ apply() passes avgGlobal to updateKPIs()',
                'status': 'FAIL',
                'message': 'Could not find this.updateKPIs(items, avgGlobal) call'
            })
            return False
    
    def test_empty_case_passes_zero(self):
        """Test: Empty dashboard case passes 0 to updateKPIs()"""
        pattern = r"this\.updateKPIs\(items,\s*0\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ Empty case passes 0 to updateKPIs()',
                'status': 'PASS',
                'message': 'Empty dashboard correctly passes 0 as avgGlobal'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Empty case passes 0 to updateKPIs()',
                'status': 'FAIL',
                'message': 'Empty case does not pass 0 to updateKPIs()'
            })
            return False
    
    def test_no_recalculation_in_updatekpis(self):
        """Test: updateKPIs() does NOT recalculate avg independently"""
        # Search for the old pattern that recalculates avg
        pattern = r"const avg = Dashboard\.DATA\.length > 0"
        match = re.search(pattern, self.content)
        
        if not match:
            self.results.append({
                'test': '✅ No independent avg recalculation in updateKPIs()',
                'status': 'PASS',
                'message': 'Old recalculation code removed - uses avgGlobal parameter'
            })
            return True
        else:
            self.results.append({
                'test': '❌ No independent avg recalculation in updateKPIs()',
                'status': 'FAIL',
                'message': 'updateKPIs() still contains old avg calculation logic'
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
        
        return failed == 0


if __name__ == '__main__':
    test_file = r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html'
    tester = KPIGlobalSyncTest(test_file)
    success = tester.run_all_tests()
    exit(0 if success else 1)
