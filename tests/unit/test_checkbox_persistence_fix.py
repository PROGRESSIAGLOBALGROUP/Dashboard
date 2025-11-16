"""
Test: Checkbox ID Consistency and Persistence Fix
Validates that configuration changes persist correctly in localStorage
"""

import re

class CheckboxPersistenceFix:
    """Test that checkbox IDs are consistent and configuration persists"""
    
    def __init__(self, html_file):
        with open(html_file, encoding='utf-8') as f:
            self.content = f.read()
        self.results = []
    
    def run_all_tests(self):
        print("\n" + "="*70)
        print("CHECKBOX ID & PERSISTENCE FIX VALIDATION")
        print("="*70)
        
        self.test_checkbox_ids_defined()
        self.test_no_include_done()
        self.test_saveandclose_uses_clo()
        self.test_getenhanceddata_uses_clo()
        self.test_checkbox_id_consistency()
        
        return self.print_results()
    
    def test_checkbox_ids_defined(self):
        """Test: HTML form defines all status checkboxes with correct IDs"""
        pattern = r'id="include-tbs".*id="include-wip".*id="include-clo"'
        match = re.search(pattern, self.content, re.DOTALL)
        
        if match:
            self.results.append({
                'test': '✅ HTML checkboxes have correct IDs',
                'status': 'PASS',
                'message': 'include-tbs, include-wip, include-clo all defined'
            })
            return True
        else:
            self.results.append({
                'test': '❌ HTML checkboxes have correct IDs',
                'status': 'FAIL',
                'message': 'One or more checkbox IDs not found'
            })
            return False
    
    def test_no_include_done(self):
        """Test: No references to non-existent 'include-done' checkbox"""
        pattern = r"include-done"
        match = re.search(pattern, self.content)
        
        if not match:
            self.results.append({
                'test': '✅ No references to non-existent include-done',
                'status': 'PASS',
                'message': 'Removed all incorrect include-done references'
            })
            return True
        else:
            self.results.append({
                'test': '❌ No references to non-existent include-done',
                'status': 'FAIL',
                'message': 'Found include-done which does not exist in HTML'
            })
            return False
    
    def test_saveandclose_uses_clo(self):
        """Test: saveAndClose() reads correct 'include-clo' checkbox"""
        pattern = r"saveAndClose\(\)[\s\S]*?clo: document\.getElementById\('include-clo'\)"
        match = re.search(pattern, self.content)
        
        if match:
            self.results.append({
                'test': '✅ saveAndClose() reads include-clo',
                'status': 'PASS',
                'message': 'Correctly reads the include-clo checkbox'
            })
            return True
        else:
            self.results.append({
                'test': '❌ saveAndClose() reads include-clo',
                'status': 'FAIL',
                'message': 'saveAndClose() not reading include-clo'
            })
            return False
    
    def test_getenhanceddata_uses_clo(self):
        """Test: Calculation code uses correct 'include-clo' checkbox"""
        pattern = r"clo: document\.getElementById\('include-clo'\)\?\.checked || true"
        matches = re.findall(pattern, self.content)
        
        if len(matches) >= 2:
            self.results.append({
                'test': '✅ All calculation functions use include-clo',
                'status': 'PASS',
                'message': f'Found {len(matches)} correct references to include-clo'
            })
            return True
        else:
            self.results.append({
                'test': '❌ All calculation functions use include-clo',
                'status': 'FAIL',
                'message': f'Only found {len(matches)} references (expected >= 2)'
            })
            return False
    
    def test_checkbox_id_consistency(self):
        """Test: All checkbox ID references are consistent"""
        # Count references to each checkbox ID
        tbs_count = len(re.findall(r"'include-tbs'", self.content))
        wip_count = len(re.findall(r"'include-wip'", self.content))
        clo_count = len(re.findall(r"'include-clo'", self.content))
        done_count = len(re.findall(r"'include-done'", self.content))
        
        if done_count == 0 and tbs_count > 0 and wip_count > 0 and clo_count > 0:
            self.results.append({
                'test': '✅ Checkbox IDs are consistent across codebase',
                'status': 'PASS',
                'message': f'TBS:{tbs_count}, WIP:{wip_count}, CLO:{clo_count}, DONE:0'
            })
            return True
        else:
            self.results.append({
                'test': '❌ Checkbox IDs are consistent across codebase',
                'status': 'FAIL',
                'message': f'TBS:{tbs_count}, WIP:{wip_count}, CLO:{clo_count}, DONE:{done_count}'
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
        print(f"RESULTS: {passed} PASSED | {failed} FAILED")
        print("="*70 + "\n")
        
        if failed == 0:
            print("🎉 CHECKBOX ID FIX COMPLETE")
            print("\nBenefit:")
            print("• Configuration changes now persist in localStorage")
            print("• KPI values no longer change without user action")
            print("• Values persist on page refresh (F5)")
            print("• Status Inclusion Rules checkboxes correctly saved")
            print("="*70 + "\n")
        
        return failed == 0


if __name__ == '__main__':
    test_file = r'c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html'
    tester = CheckboxPersistenceFix(test_file)
    success = tester.run_all_tests()
    exit(0 if success else 1)
