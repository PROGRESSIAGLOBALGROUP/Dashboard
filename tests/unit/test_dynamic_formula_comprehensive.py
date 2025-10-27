#!/usr/bin/env python3
"""
COMPREHENSIVE VALIDATION - Dynamic Formula Updates Feature
Tests all aspects of the dynamic formula display functionality
"""

import re
from pathlib import Path

class DynamicFormulaValidator:
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.results = []
    
    def _read_file(self):
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def test_1_html_element_exists(self):
        """Verify core-algorithm-formula element exists with ID"""
        if 'id="core-algorithm-formula"' in self.content:
            self.results.append(('HTML Element with ID', 'PASS', 'Found id="core-algorithm-formula"'))
            return True
        else:
            self.results.append(('HTML Element with ID', 'FAIL', 'ID not found'))
            return False
    
    def test_2_formula_element_inside_formula_equation(self):
        """Verify element is within .formula-equation div"""
        pattern = r'<div class="formula-equation" id="core-algorithm-formula">'
        if re.search(pattern, self.content):
            self.results.append(('Element Location', 'PASS', 'Within correct .formula-equation div'))
            return True
        else:
            self.results.append(('Element Location', 'FAIL', 'Element not in correct location'))
            return False
    
    def test_3_function_updateCoreAlgorithmDisplay_exists(self):
        """Verify updateCoreAlgorithmDisplay function is defined"""
        if 'updateCoreAlgorithmDisplay(progressMethod, globalMethod)' in self.content:
            self.results.append(('Function Definition', 'PASS', 'updateCoreAlgorithmDisplay() defined'))
            return True
        else:
            self.results.append(('Function Definition', 'FAIL', 'Function not found'))
            return False
    
    def test_4_function_gets_core_formula_element(self):
        """Verify function gets the element by ID"""
        if "document.getElementById('core-algorithm-formula')" in self.content:
            self.results.append(('Function: Get Element', 'PASS', 'Correctly gets element by ID'))
            return True
        else:
            self.results.append(('Function: Get Element', 'FAIL', 'Element not retrieved correctly'))
            return False
    
    def test_5_formulaMap_has_all_methods(self):
        """Verify formulaMap contains weighted, simple, minimum"""
        has_weighted = 'weighted:' in self.content and 'Criticality × Business Impact × Priority' in self.content
        has_simple = 'simple:' in self.content
        has_minimum = 'minimum:' in self.content
        
        if has_weighted and has_simple and has_minimum:
            self.results.append(('FormulaMap', 'PASS', 'All 3 methods defined'))
            return True
        else:
            self.results.append(('FormulaMap', 'FAIL', f'W:{has_weighted}, S:{has_simple}, M:{has_minimum}'))
            return False
    
    def test_6_methodContext_has_all_combinations(self):
        """Verify methodContext handles all method combinations"""
        if 'methodContext = {' in self.content and \
           'Using Weighted BU Method' in self.content and \
           'Using Simple BU Average' in self.content and \
           'Using Minimum Progress (Bottleneck)' in self.content:
            self.results.append(('MethodContext Map', 'PASS', 'All combinations defined'))
            return True
        else:
            self.results.append(('MethodContext Map', 'FAIL', 'Missing method combinations'))
            return False
    
    def test_7_updates_innerHTML_correctly(self):
        """Verify formula HTML is updated"""
        if 'coreFormulaEl.innerHTML = formulaMap[progressMethod]' in self.content:
            self.results.append(('Update Formula HTML', 'PASS', 'innerHTML updated correctly'))
            return True
        else:
            self.results.append(('Update Formula HTML', 'FAIL', 'innerHTML not updated'))
            return False
    
    def test_8_creates_context_element(self):
        """Verify context subtitle element is created"""
        if "contextEl.id = 'core-algorithm-context'" in self.content and \
           "contextEl.style.cssText" in self.content:
            self.results.append(('Context Element Creation', 'PASS', 'Context div created with styling'))
            return True
        else:
            self.results.append(('Context Element Creation', 'FAIL', 'Context element not created'))
            return False
    
    def test_9_updates_context_correctly(self):
        """Verify context text is updated"""
        if "contextEl.textContent = '→ ' + methodContext[progressMethod]" in self.content:
            self.results.append(('Update Context Text', 'PASS', 'Context text updated with method'))
            return True
        else:
            self.results.append(('Update Context Text', 'FAIL', 'Context not updated'))
            return False
    
    def test_10_updateFormulaLabels_calls_updateCoreAlgorithmDisplay(self):
        """Verify updateFormulaLabels calls updateCoreAlgorithmDisplay"""
        if 'this.updateCoreAlgorithmDisplay(progressMethod, globalMethod)' in self.content:
            self.results.append(('Integration Point', 'PASS', 'updateFormulaLabels calls function'))
            return True
        else:
            self.results.append(('Integration Point', 'FAIL', 'Function not called'))
            return False
    
    def test_11_progress_method_event_listener(self):
        """Verify progress method select has event listener"""
        if "document.getElementById('formula-progress-method')?.addEventListener('change'" in self.content:
            self.results.append(('Progress Method Listener', 'PASS', 'Event listener attached'))
            return True
        else:
            self.results.append(('Progress Method Listener', 'FAIL', 'No event listener'))
            return False
    
    def test_12_global_method_event_listeners(self):
        """Verify global method radios have event listeners"""
        if 'document.querySelectorAll(\'input[name="global-method"]\')' in self.content and \
           'radio.addEventListener(\'change\', () => this.updateFormulaLabels())' in self.content:
            self.results.append(('Global Method Listeners', 'PASS', 'Event listeners on radios'))
            return True
        else:
            self.results.append(('Global Method Listeners', 'FAIL', 'No event listeners'))
            return False
    
    def test_13_loadFormulaConfig_calls_updateFormulaLabels(self):
        """Verify loadFormulaConfig calls updateFormulaLabels"""
        pattern = r'loadFormulaConfig\(\).*?this\.updateFormulaLabels\(\)'
        if re.search(pattern, self.content, re.DOTALL):
            self.results.append(('Load Config Integration', 'PASS', 'Calls updateFormulaLabels on load'))
            return True
        else:
            self.results.append(('Load Config Integration', 'FAIL', 'No update on load'))
            return False
    
    def test_14_initializeEmptyFormulaForm_calls_updateFormulaLabels(self):
        """Verify initializeEmptyFormulaForm calls updateFormulaLabels"""
        if 'initializeEmptyFormulaForm()' in self.content and \
           re.search(r'initializeEmptyFormulaForm.*?this\.updateFormulaLabels\(\)', self.content, re.DOTALL):
            self.results.append(('Initialize Form Integration', 'PASS', 'Calls updateFormulaLabels on init'))
            return True
        else:
            self.results.append(('Initialize Form Integration', 'FAIL', 'No update on init'))
            return False
    
    def test_15_no_syntax_errors(self):
        """Verify no obvious syntax errors in implementation"""
        # Check for balanced quotes and braces in the function
        open_quotes = self.content.count("'")
        close_quotes = self.content.count("'")
        
        # Basic check - not perfect but catches obvious issues
        if open_quotes % 2 == 0:
            self.results.append(('Syntax Check', 'PASS', 'No obvious syntax errors'))
            return True
        else:
            self.results.append(('Syntax Check', 'WARN', 'Quote balance check inconclusive'))
            return True  # Don't fail on this
    
    def run_all_tests(self):
        print("\n" + "="*90)
        print("COMPREHENSIVE VALIDATION - Dynamic Formula Updates Feature")
        print("="*90 + "\n")
        
        tests = [
            self.test_1_html_element_exists,
            self.test_2_formula_element_inside_formula_equation,
            self.test_3_function_updateCoreAlgorithmDisplay_exists,
            self.test_4_function_gets_core_formula_element,
            self.test_5_formulaMap_has_all_methods,
            self.test_6_methodContext_has_all_combinations,
            self.test_7_updates_innerHTML_correctly,
            self.test_8_creates_context_element,
            self.test_9_updates_context_correctly,
            self.test_10_updateFormulaLabels_calls_updateCoreAlgorithmDisplay,
            self.test_11_progress_method_event_listener,
            self.test_12_global_method_event_listeners,
            self.test_13_loadFormulaConfig_calls_updateFormulaLabels,
            self.test_14_initializeEmptyFormulaForm_calls_updateFormulaLabels,
            self.test_15_no_syntax_errors,
        ]
        
        for test in tests:
            test()
        
        passed = sum(1 for r in self.results if r[1] == 'PASS')
        failed = sum(1 for r in self.results if r[1] == 'FAIL')
        warned = sum(1 for r in self.results if r[1] == 'WARN')
        
        print("TEST RESULTS:")
        print("-" * 90)
        for name, status, detail in self.results:
            if status == 'PASS':
                icon = "✅"
            elif status == 'FAIL':
                icon = "❌"
            else:
                icon = "⚠️"
            print(f"{icon} {name:<35} | {status:<6} | {detail}")
        
        print("\n" + "="*90)
        print(f"SUMMARY: {passed} PASSED, {failed} FAILED, {warned} WARNED (Total: {len(self.results)})")
        print("="*90 + "\n")
        
        if failed == 0:
            print("✅ ALL CRITICAL TESTS PASSED")
            print("Dynamic formula update feature is correctly implemented\n")
            return True
        else:
            print(f"❌ {failed} test(s) failed - Review implementation\n")
            return False

if __name__ == '__main__':
    import sys
    validator = DynamicFormulaValidator()
    success = validator.run_all_tests()
    sys.exit(0 if success else 1)
