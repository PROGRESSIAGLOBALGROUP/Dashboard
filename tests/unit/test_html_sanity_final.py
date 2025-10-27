#!/usr/bin/env python3
"""
Final HTML Sanity Check
Verifies HTML structure, bracket balance, and no broken references
"""

from pathlib import Path
import re

class HTMLSanityCheck:
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_1_valid_html_structure(self):
        """Verify basic HTML structure is valid"""
        if self.content.startswith('<!DOCTYPE') and \
           '<html' in self.content and \
           '</html>' in self.content and \
           '<head>' in self.content and \
           '<body>' in self.content:
            self.results.append(('Valid HTML structure', 'PASS', 'DOCTYPE and main tags present'))
            return True
        else:
            self.results.append(('Valid HTML structure', 'FAIL', 'Basic HTML tags missing'))
            return False
    
    def test_2_bracket_balance(self):
        """Verify all brackets are balanced"""
        open_curly = self.content.count('{')
        close_curly = self.content.count('}')
        open_square = self.content.count('[')
        close_square = self.content.count(']')
        open_paren = self.content.count('(')
        close_paren = self.content.count(')')
        
        balanced = (open_curly == close_curly and 
                   open_square == close_square and 
                   open_paren == close_paren)
        
        if balanced:
            self.results.append(('Bracket balance', 'PASS', 
                               f'{open_curly} pairs {{ }}, {open_square} pairs [ ], {open_paren} pairs ( )'))
            return True
        else:
            self.results.append(('Bracket balance', 'FAIL',
                               f'{{ {open_curly}/{close_curly} }} [ {open_square}/{close_square} ] ( {open_paren}/{close_paren} )'))
            return False
    
    def test_3_no_formula_global_method_element(self):
        """Verify NO references to non-existent formula-global-method"""
        if 'formula-global-method' not in self.content:
            self.results.append(('No broken formula-global-method', 'PASS', 
                               'All references to broken element removed'))
            return True
        else:
            count = self.content.count('formula-global-method')
            self.results.append(('No broken formula-global-method', 'FAIL',
                               f'Found {count} references to broken element'))
            return False
    
    def test_4_global_method_radio_buttons_exist(self):
        """Verify global-method radio buttons exist"""
        if 'name="global-method"' in self.content and \
           'id="global-weighted"' in self.content and \
           'id="global-simple"' in self.content:
            self.results.append(('Global method radios exist', 'PASS',
                               'Both global-weighted and global-simple buttons present'))
            return True
        else:
            self.results.append(('Global method radios exist', 'FAIL',
                               'One or more radio buttons missing'))
            return False
    
    def test_5_progress_method_dropdown_exists(self):
        """Verify progress-method dropdown exists"""
        if 'id="formula-progress-method"' in self.content or \
           'name="formula-progress-method"' in self.content:
            self.results.append(('Progress method dropdown exists', 'PASS',
                               'formula-progress-method element present'))
            return True
        else:
            self.results.append(('Progress method dropdown exists', 'FAIL',
                               'Progress method element not found'))
            return False
    
    def test_6_no_syntax_errors_in_js(self):
        """Check for common JavaScript syntax errors"""
        errors = []
        
        # Check for unmatched quotes in string literals
        if self.content.count('"') % 2 != 0:
            errors.append('Odd number of double quotes')
        if self.content.count("'") % 2 != 0:
            errors.append('Odd number of single quotes')
        
        # Check for common typos
        if 'calculateBUProgres(' in self.content:  # typo
            errors.append('Typo: calculateBUProgres (missing s)')
        
        if len(errors) == 0:
            self.results.append(('JavaScript syntax', 'PASS',
                               'No common syntax errors detected'))
            return True
        else:
            self.results.append(('JavaScript syntax', 'FAIL',
                               f'Issues: {", ".join(errors)}'))
            return False
    
    def test_7_dashboard_namespace_exists(self):
        """Verify Dashboard namespace is created"""
        if "window.Dashboard = {" in self.content or \
           "if (!window.Dashboard)" in self.content:
            self.results.append(('Dashboard namespace', 'PASS',
                               'Global namespace properly initialized'))
            return True
        else:
            self.results.append(('Dashboard namespace', 'FAIL',
                               'Dashboard namespace not found'))
            return False
    
    def test_8_storage_manager_exists(self):
        """Verify StorageManager is present"""
        if 'class StorageManager' in self.content or \
           'StorageManager =' in self.content:
            self.results.append(('StorageManager class', 'PASS',
                               'StorageManager properly defined'))
            return True
        else:
            self.results.append(('StorageManager class', 'FAIL',
                               'StorageManager not found'))
            return False
    
    def test_9_ui_controller_exists(self):
        """Verify UIController is present"""
        if 'class UIController' in self.content or \
           'UIController =' in self.content:
            self.results.append(('UIController class', 'PASS',
                               'UIController properly defined'))
            return True
        else:
            self.results.append(('UIController class', 'FAIL',
                               'UIController not found'))
            return False
    
    def test_10_file_size_reasonable(self):
        """Verify file size is reasonable (not corrupted)"""
        size_mb = len(self.content) / (1024 * 1024)
        
        if 1 < size_mb < 5:  # Expect between 1-5 MB
            self.results.append(('File size reasonable', 'PASS',
                               f'File size: {size_mb:.2f} MB (within expected range)'))
            return True
        else:
            self.results.append(('File size reasonable', 'FAIL',
                               f'File size: {size_mb:.2f} MB (unexpected size)'))
            return False
    
    def test_11_formula_labels_exist(self):
        """Verify formula labels for both methods"""
        weighted_label = 'Weighted by BU Size' in self.content or \
                        'Weighted Formula' in self.content
        simple_label = 'Simple BU Average' in self.content or \
                      'Simple Average' in self.content
        
        if weighted_label and simple_label:
            self.results.append(('Formula labels', 'PASS',
                               'Both Weighted and Simple labels present'))
            return True
        else:
            self.results.append(('Formula labels', 'FAIL',
                               f'Weighted: {weighted_label}, Simple: {simple_label}'))
            return False
    
    def test_12_calculation_functions_exist(self):
        """Verify calculation functions are present"""
        has_calc_global = 'calculateGlobalProgress' in self.content
        has_calc_bu = 'calculateBUProgress' in self.content
        has_calc_app = 'calculateAppProgress' in self.content
        
        if has_calc_global and has_calc_bu and has_calc_app:
            self.results.append(('Calculation functions', 'PASS',
                               'All calculation functions present'))
            return True
        else:
            self.results.append(('Calculation functions', 'FAIL',
                               f'Global: {has_calc_global}, BU: {has_calc_bu}, App: {has_calc_app}'))
            return False
    
    def run_all_tests(self):
        print("\n" + "="*80)
        print("FINAL HTML SANITY CHECK - dashboard_enhanced.html")
        print("="*80 + "\n")
        
        tests = [
            self.test_1_valid_html_structure,
            self.test_2_bracket_balance,
            self.test_3_no_formula_global_method_element,
            self.test_4_global_method_radio_buttons_exist,
            self.test_5_progress_method_dropdown_exists,
            self.test_6_no_syntax_errors_in_js,
            self.test_7_dashboard_namespace_exists,
            self.test_8_storage_manager_exists,
            self.test_9_ui_controller_exists,
            self.test_10_file_size_reasonable,
            self.test_11_formula_labels_exist,
            self.test_12_calculation_functions_exist,
        ]
        
        for test in tests:
            test()
        
        passed = sum(1 for r in self.results if r[1] == 'PASS')
        failed = sum(1 for r in self.results if r[1] == 'FAIL')
        
        for name, status, message in self.results:
            icon = "✅" if status == 'PASS' else "❌"
            print(f"{icon} {name}")
            print(f"   └─ {message}\n")
        
        print("="*80)
        print(f"Results: {passed} passed, {failed} failed out of {len(self.results)} tests")
        print("="*80 + "\n")
        
        if failed == 0:
            print("🎉 SANITY CHECK PASSED")
            print("HTML file structure is intact and all references are valid\n")
        else:
            print(f"⚠️  {failed} issue(s) detected\n")
        
        return failed == 0

if __name__ == '__main__':
    import sys
    checker = HTMLSanityCheck()
    success = checker.run_all_tests()
    sys.exit(0 if success else 1)
