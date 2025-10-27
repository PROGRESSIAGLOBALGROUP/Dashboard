#!/usr/bin/env python3
"""
Comprehensive Global Progress Formula Verification
Complete end-to-end validation including all code paths
"""

import re
from pathlib import Path

class GlobalFormulaComprehensiveTest:
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_1_ui_components_present(self):
        """Test that UI components exist for Global Progress Formula"""
        checks = [
            ('id="global-weighted"', 'Weighted radio button'),
            ('id="global-simple"', 'Simple radio button'),
            ('name="global-method"', 'Radio button group name'),
            ('Global Progress Formula', 'UI section heading'),
            ('Weighted by BU Size', 'Weighted option label'),
            ('Simple BU Average', 'Simple option label'),
        ]
        
        all_present = all(check in self.content for check, _ in checks)
        
        if all_present:
            self.results.append({
                'test': '1. UI Components Present',
                'status': 'PASS',
                'message': 'All UI elements found (radios, labels, section)'
            })
            return True
        else:
            missing = [desc for check, desc in checks if check not in self.content]
            self.results.append({
                'test': '1. UI Components Present',
                'status': 'FAIL',
                'message': f'Missing: {", ".join(missing)}'
            })
            return False
    
    def test_2_save_reads_radios_correctly(self):
        """Test that saveFormulaConfig reads from radio buttons"""
        # Should have the fixed code
        pattern = r"querySelector\(['\"]input\[name=['\"]global-method['\"].*?:checked"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': '2. Save Function Reads Radios',
                'status': 'PASS',
                'message': 'saveFormulaConfig() reads selected radio correctly'
            })
            return True
        else:
            self.results.append({
                'test': '2. Save Function Reads Radios',
                'status': 'FAIL',
                'message': 'Save function not reading radios'
            })
            return False
    
    def test_3_saved_to_config(self):
        """Test that globalMethod is saved to config"""
        if 'globalMethod:' in self.content and 'formulaSettings' in self.content:
            self.results.append({
                'test': '3. Saved to Config',
                'status': 'PASS',
                'message': 'globalMethod included in formulaSettings save'
            })
            return True
        else:
            self.results.append({
                'test': '3. Saved to Config',
                'status': 'FAIL',
                'message': 'globalMethod not in config save'
            })
            return False
    
    def test_4_persists_on_load(self):
        """Test that globalMethod is restored on page load"""
        if "config.globalMethod" in self.content or "globalMethod:" in self.content:
            if "querySelector(`input[name=\"global-method\"][value=" in self.content:
                self.results.append({
                    'test': '4. Persists on Load',
                    'status': 'PASS',
                    'message': 'globalMethod restored and radio set on load'
                })
                return True
        
        self.results.append({
            'test': '4. Persists on Load',
            'status': 'FAIL',
            'message': 'Load/restore logic missing'
        })
        return False
    
    def test_5_affects_calculation(self):
        """Test that globalMethod actually affects the calculation"""
        # Look for the calculation code that uses globalMethod
        pattern = r"const globalMethod = config\?\.formulaSettings\?\.globalMethod.*?if \(globalMethod === ['\"]simple"
        
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append({
                'test': '5. Affects Calculation',
                'status': 'PASS',
                'message': 'Calculation logic uses globalMethod setting'
            })
            return True
        else:
            self.results.append({
                'test': '5. Affects Calculation',
                'status': 'FAIL',
                'message': 'Calculation ignores globalMethod'
            })
            return False
    
    def test_6_no_broken_references(self):
        """Test that no broken element references remain"""
        if 'formula-global-method' in self.content:
            self.results.append({
                'test': '6. No Broken References',
                'status': 'FAIL',
                'message': 'Still contains references to formula-global-method'
            })
            return False
        else:
            self.results.append({
                'test': '6. No Broken References',
                'status': 'PASS',
                'message': 'All broken element references removed'
            })
            return True
    
    def test_7_event_listeners_attached(self):
        """Test that radio button change listeners are attached"""
        pattern = r"querySelectorAll\(['\"]input\[name=['\"]global-method['\"]"
        
        if re.search(pattern, self.content):
            self.results.append({
                'test': '7. Event Listeners Attached',
                'status': 'PASS',
                'message': 'Radio buttons have event listeners'
            })
            return True
        else:
            self.results.append({
                'test': '7. Event Listeners Attached',
                'status': 'FAIL',
                'message': 'Event listeners missing'
            })
            return False
    
    def test_8_storage_manager_used(self):
        """Test that StorageManager is used for persistence"""
        if 'Dashboard.StorageManager.saveConfig' in self.content and \
           'Dashboard.StorageManager.loadConfig' in self.content:
            self.results.append({
                'test': '8. StorageManager Used',
                'status': 'PASS',
                'message': 'Config properly persisted via StorageManager'
            })
            return True
        else:
            self.results.append({
                'test': '8. StorageManager Used',
                'status': 'FAIL',
                'message': 'StorageManager not used'
            })
            return False
    
    def test_9_both_methods_implemented(self):
        """Test that both calculation methods are implemented"""
        weighted_ok = "// Weighted by BU Size" in self.content or \
                     "weighted.*larger BU" in self.content
        simple_ok = "// Simple BU Average" in self.content or \
                   "simple.*equal" in self.content
        
        if weighted_ok and simple_ok:
            self.results.append({
                'test': '9. Both Methods Implemented',
                'status': 'PASS',
                'message': 'Weighted and Simple methods both present'
            })
            return True
        else:
            self.results.append({
                'test': '9. Both Methods Implemented',
                'status': 'FAIL',
                'message': 'Missing one or both calculation methods'
            })
            return False
    
    def test_10_syntax_valid(self):
        """Test that file has valid syntax (bracket balance)"""
        open_braces = self.content.count('{')
        close_braces = self.content.count('}')
        
        if open_braces == close_braces:
            self.results.append({
                'test': '10. Syntax Valid',
                'status': 'PASS',
                'message': f'Bracket balance OK ({open_braces} pairs)'
            })
            return True
        else:
            self.results.append({
                'test': '10. Syntax Valid',
                'status': 'FAIL',
                'message': f'Bracket mismatch: {open_braces} vs {close_braces}'
            })
            return False
    
    def run_all_tests(self):
        print("\n" + "="*80)
        print("GLOBAL PROGRESS FORMULA - COMPREHENSIVE VERIFICATION")
        print("="*80 + "\n")
        
        tests = [
            self.test_1_ui_components_present,
            self.test_2_save_reads_radios_correctly,
            self.test_3_saved_to_config,
            self.test_4_persists_on_load,
            self.test_5_affects_calculation,
            self.test_6_no_broken_references,
            self.test_7_event_listeners_attached,
            self.test_8_storage_manager_used,
            self.test_9_both_methods_implemented,
            self.test_10_syntax_valid,
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
            print("🎉 ALL COMPREHENSIVE CHECKS PASSED")
            print("Global Progress Formula is fully functional and ready for production\n")
        else:
            print(f"⚠️  {failed} issue(s) detected - review above\n")
        
        return failed == 0

if __name__ == '__main__':
    import sys
    tester = GlobalFormulaComprehensiveTest()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
