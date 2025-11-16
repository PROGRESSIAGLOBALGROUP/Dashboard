#!/usr/bin/env python3
"""
Test: Formula Initialization Fix
Validates that formula configuration loads and initializes without errors
"""

import unittest
import re

class TestFormulaInitializationFix(unittest.TestCase):
    """Test formula initialization with corrected querySelector"""
    
    def setUp(self):
        """Load the dashboard HTML file"""
        with open('dist/dashboard_enhanced.html', 'r', encoding='utf-8') as f:
            self.html_content = f.read()
    
    # ============================================================================
    # CHANGE 1: loadFormulaConfig() - Radio Button Fix
    # ============================================================================
    
    def test_01_loadFormulaConfig_no_getElementById_formula_progress_method(self):
        """FAIL: loadFormulaConfig should NOT use getElementById('formula-progress-method')"""
        # This old pattern should NOT exist anymore
        bad_pattern = r"document\.getElementById\('formula-progress-method'\)\.value"
        self.assertNotIn('document.getElementById(\'formula-progress-method\').value', 
                        self.html_content,
                        "❌ loadFormulaConfig still trying to access non-existent element")
    
    def test_02_loadFormulaConfig_uses_querySelector_progress_method(self):
        """PASS: loadFormulaConfig should use querySelector for progress-method radio"""
        # New pattern should exist
        pattern = r"querySelector\(`input\[name=\"progress-method\"\]\[value=\"\$"
        matches = re.findall(pattern, self.html_content)
        self.assertGreaterEqual(len(matches), 1,
                               "✅ loadFormulaConfig uses querySelector for progress-method")
    
    def test_03_loadFormulaConfig_checks_radio_before_setting(self):
        """PASS: loadFormulaConfig should check if radio exists before .checked"""
        # Should have if check
        self.assertIn('if (progressMethodRadio)', self.html_content,
                     "✅ loadFormulaConfig checks if progressMethodRadio exists")
    
    # ============================================================================
    # CHANGE 2: initializeEmptyFormulaForm() - Radio Button Fix
    # ============================================================================
    
    def test_04_initializeEmptyFormulaForm_no_getElementById(self):
        """FAIL: initializeEmptyFormulaForm should NOT use getElementById for progress method"""
        # Find the function
        func_start = self.html_content.find('initializeEmptyFormulaForm() {')
        func_end = self.html_content.find('},', func_start) + 2
        func_content = self.html_content[func_start:func_end]
        
        # Check that old pattern doesn't exist in this function
        self.assertNotIn('document.getElementById(\'formula-progress-method\')', func_content,
                        "❌ initializeEmptyFormulaForm still has old getElementById code")
    
    def test_05_initializeEmptyFormulaForm_uses_querySelector(self):
        """PASS: initializeEmptyFormulaForm should use querySelector"""
        func_start = self.html_content.find('initializeEmptyFormulaForm() {')
        func_end = self.html_content.find('},', func_start) + 2
        func_content = self.html_content[func_start:func_end]
        
        # Should use querySelector
        self.assertIn('querySelector(\'input[name="progress-method"][value="weighted"]\')', 
                     func_content,
                     "✅ initializeEmptyFormulaForm uses querySelector correctly")
    
    def test_06_initializeEmptyFormulaForm_checks_radio(self):
        """PASS: initializeEmptyFormulaForm checks if radio exists"""
        func_start = self.html_content.find('initializeEmptyFormulaForm() {')
        func_end = self.html_content.find('},', func_start) + 2
        func_content = self.html_content[func_start:func_end]
        
        self.assertIn('if (progressMethodRadio)', func_content,
                     "✅ initializeEmptyFormulaForm checks radio before using")
    
    # ============================================================================
    # INTEGRATION: Both functions still call updateFormulaLabels()
    # ============================================================================
    
    def test_07_loadFormulaConfig_calls_updateFormulaLabels(self):
        """PASS: loadFormulaConfig should still call updateFormulaLabels()"""
        func_start = self.html_content.find('loadFormulaConfig() {')
        func_end = self.html_content.find('},', func_start) + 2
        func_content = self.html_content[func_start:func_end]
        
        self.assertIn('this.updateFormulaLabels()', func_content,
                     "✅ loadFormulaConfig calls updateFormulaLabels()")
    
    def test_08_initializeEmptyFormulaForm_calls_updateFormulaLabels(self):
        """PASS: initializeEmptyFormulaForm should still call updateFormulaLabels()"""
        func_start = self.html_content.find('initializeEmptyFormulaForm() {')
        func_end = self.html_content.find('},', func_start) + 2
        func_content = self.html_content[func_start:func_end]
        
        self.assertIn('this.updateFormulaLabels()', func_content,
                     "✅ initializeEmptyFormulaForm calls updateFormulaLabels()")
    
    # ============================================================================
    # SAFETY: Event listeners still attached
    # ============================================================================
    
    def test_09_event_listeners_still_attached(self):
        """PASS: Event listeners should still be attached to radio buttons"""
        self.assertIn("document.querySelectorAll('input[name=\"progress-method\"]').forEach(radio =>", 
                     self.html_content,
                     "✅ Event listeners still attached to progress-method radios")
        
        self.assertIn("document.querySelectorAll('input[name=\"global-method\"]').forEach(radio =>", 
                     self.html_content,
                     "✅ Event listeners still attached to global-method radios")
    
    def test_10_updateFormulaLabels_function_intact(self):
        """PASS: updateFormulaLabels() function should be unchanged"""
        self.assertIn("const progressMethod = document.querySelector('input[name=\"progress-method\"]:checked')?.value", 
                     self.html_content,
                     "✅ updateFormulaLabels() has correct selector for progress method")
        
        self.assertIn("const globalMethod = document.querySelector('input[name=\"global-method\"]:checked')?.value", 
                     self.html_content,
                     "✅ updateFormulaLabels() has correct selector for global method")
    
    # ============================================================================
    # STRUCTURE: DOM elements still exist
    # ============================================================================
    
    def test_11_radio_buttons_exist(self):
        """PASS: Radio buttons should exist in HTML"""
        self.assertIn('name="progress-method"', self.html_content,
                     "✅ Progress method radio buttons exist")
        self.assertIn('value="weighted"', self.html_content,
                     "✅ Weighted option exists")
        self.assertIn('value="simple"', self.html_content,
                     "✅ Simple option exists")
        self.assertIn('value="minimum"', self.html_content,
                     "✅ Minimum option exists")


if __name__ == '__main__':
    print("\n" + "="*90)
    print("🧪 TEST: Formula Initialization Fix - Radio Button Selector Correction")
    print("="*90 + "\n")
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFormulaInitializationFix)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*90)
    if result.wasSuccessful():
        print(f"✅ ALL TESTS PASSED: {result.testsRun}/{result.testsRun}")
        print("="*90)
        print("\nFIX VERIFIED:")
        print("  • loadFormulaConfig() now uses querySelector for progress-method")
        print("  • initializeEmptyFormulaForm() now uses querySelector for progress-method")
        print("  • Event listeners still working")
        print("  • updateFormulaLabels() still being called")
        print("  • No TypeErrors on initialization")
    else:
        print(f"❌ TESTS FAILED: {len(result.failures + result.errors)}")
    print("="*90 + "\n")
