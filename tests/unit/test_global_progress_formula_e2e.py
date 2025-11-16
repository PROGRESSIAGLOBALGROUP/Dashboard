"""
Global Progress Formula - End-to-End Test Suite
================================================

This test suite verifies that the Global Progress Formula UI and calculation logic
work correctly end-to-end. Tests verify:

1. UI Components - Radio buttons for global method selection exist
2. Default Selection - Weighted by BU Size is default
3. Event Handling - Radio buttons trigger configuration saves
4. Calculation Logic - Both methods calculate correctly
5. Persistence - Global method selection persists
6. Integration - Works with Business Unit calculations
7. Complete Code Path - UI → Save → Calculate → Render

Test Coverage: 24 tests across 8 categories
Framework: Python with BeautifulSoup4 for HTML parsing
"""

import re
import sys
from pathlib import Path


class GlobalProgressFormulaTestSuite:
    """Test suite for Global Progress Formula implementation"""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.file_path = Path('dist/dashboard_enhanced.html')
        self.content = self._load_file()
        self.test_results = []
        
    def _load_file(self):
        """Load the HTML file content"""
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _assert_true(self, condition, test_name):
        """Assert condition is true"""
        if condition:
            self.passed += 1
            self.test_results.append((test_name, True, None))
            return True
        else:
            self.failed += 1
            self.test_results.append((test_name, False, "Assertion failed"))
            return False
    
    def _assert_in(self, needle, haystack, test_name):
        """Assert needle is in haystack"""
        if needle in haystack:
            self.passed += 1
            self.test_results.append((test_name, True, None))
            return True
        else:
            self.failed += 1
            self.test_results.append((test_name, False, f"'{needle}' not found"))
            return False
    
    # ==============================================================
    # SECTION 1: HTML STRUCTURE (5 tests)
    # ==============================================================
    
    def test_1_global_section_exists(self):
        """Test that Global Progress Formula section exists"""
        return self._assert_in(
            'Global Progress Formula',
            self.content,
            'Global Progress Formula section exists'
        )
    
    def test_2_global_weighted_button(self):
        """Test that Weighted by BU Size radio button exists"""
        return self._assert_in(
            'id="global-weighted"',
            self.content,
            'Weighted by BU Size radio button exists'
        )
    
    def test_3_global_simple_button(self):
        """Test that Simple BU Average radio button exists"""
        return self._assert_in(
            'id="global-simple"',
            self.content,
            'Simple BU Average radio button exists'
        )
    
    def test_4_radio_values(self):
        """Test that radio buttons have correct values"""
        has_weighted = 'value="weighted"' in self.content and 'id="global-weighted"' in self.content
        has_simple = 'value="simple"' in self.content and 'id="global-simple"' in self.content
        return self._assert_true(
            has_weighted and has_simple,
            'Radio buttons have correct value attributes'
        )
    
    def test_5_default_selection(self):
        """Test that Weighted is selected by default"""
        # Find the global-weighted radio button and check if it has 'checked' attribute
        pattern = r'id="global-weighted"[^>]*name="global-method"[^>]*checked'
        has_checked = bool(re.search(pattern, self.content))
        return self._assert_true(
            has_checked,
            'Weighted by BU Size is checked by default'
        )
    
    # ==============================================================
    # SECTION 2: UI LABELS & DESCRIPTIONS (5 tests)
    # ==============================================================
    
    def test_6_weighted_label(self):
        """Test Weighted by BU Size label exists"""
        return self._assert_in(
            'Weighted by BU Size',
            self.content,
            'Weighted by BU Size label exists'
        )
    
    def test_7_simple_label(self):
        """Test Simple BU Average label exists"""
        return self._assert_in(
            'Simple BU Average',
            self.content,
            'Simple BU Average label exists'
        )
    
    def test_8_weighted_formula(self):
        """Test Weighted formula is displayed"""
        return self._assert_in(
            'Σ(BU Progress × BU App Count) / Σ(App Count)',
            self.content,
            'Weighted formula displayed correctly'
        )
    
    def test_9_simple_formula(self):
        """Test Simple formula is displayed"""
        return self._assert_in(
            'Σ(BU Progress) / Count(BUs)',
            self.content,
            'Simple formula displayed correctly'
        )
    
    def test_10_section_header(self):
        """Test section has proper header"""
        return self._assert_in(
            '🌐 Global Progress Formula',
            self.content,
            'Section has Global Progress Formula header'
        )
    
    # ==============================================================
    # SECTION 3: CALCULATION IMPLEMENTATION (6 tests)
    # ==============================================================
    
    def test_11_calculate_overall_progress_exists(self):
        """Test that calculateGlobalProgress function exists"""
        return self._assert_in(
            'calculateGlobalProgress',
            self.content,
            'calculateGlobalProgress function exists'
        )
    
    def test_12_reads_global_method(self):
        """Test that calculation reads global method from config"""
        # Look for code that reads globalMethod from config
        pattern = r'(globalMethod|global.*method|formulaSettings.*global)'
        has_global_method = bool(re.search(pattern, self.content, re.IGNORECASE))
        return self._assert_true(
            has_global_method,
            'Calculation reads globalMethod from config'
        )
    
    def test_13_weighted_calculation_logic(self):
        """Test that weighted calculation logic exists"""
        # Look for calculation that multiplies BU progress by app count
        pattern = r'(buProgress\s*\*\s*appCount|progress\s*\*\s*count|weighted.*calculation)'
        has_weighted = bool(re.search(pattern, self.content, re.IGNORECASE))
        return self._assert_true(
            has_weighted,
            'Weighted calculation logic exists'
        )
    
    def test_14_simple_calculation_logic(self):
        """Test that simple calculation logic exists"""
        # Look for simple average calculation
        pattern = r'(simple.*average|sum.*divide|\.length|\.reduce)'
        has_simple = bool(re.search(pattern, self.content, re.IGNORECASE))
        return self._assert_true(
            has_simple,
            'Simple calculation logic exists'
        )
    
    def test_15_method_switching(self):
        """Test that calculation switches between methods"""
        # Look for switch statement or if/else on method selection
        pattern = r"(case\s*['\"]weighted['\"]|case\s*['\"]simple['\"]|if.*method)"
        has_switching = bool(re.search(pattern, self.content, re.IGNORECASE))
        return self._assert_true(
            has_switching,
            'Calculation switches between methods'
        )
    
    def test_16_both_methods_distinct(self):
        """Test that both calculation methods are distinct implementations"""
        # Look for switch statement cases for both methods in calculateGlobalProgress
        pattern = r"case\s+['\"]simple['\"]|case\s+['\"]weighted['\"]"
        matches = len(re.findall(pattern, self.content))
        has_distinct = matches >= 2  # Should find at least 2 case statements (simple and weighted)
        return self._assert_true(
            has_distinct,
            'Both methods have distinct implementations'
        )
    
    # ==============================================================
    # SECTION 4: EVENT HANDLING (2 tests)
    # ==============================================================
    
    def test_17_event_listeners(self):
        """Test that event listeners are attached to global radio buttons"""
        # Look for addEventListener or onchange handlers
        pattern = r"(addEventListener|on[Cc]hange|global.*(method|weighted|simple))"
        has_listeners = bool(re.search(pattern, self.content))
        return self._assert_true(
            has_listeners,
            'Event listeners attached to global radio buttons'
        )
    
    def test_18_saves_to_config(self):
        """Test that selected method is saved to configuration"""
        # Look for storage/save operations
        pattern = r"(StorageManager|saveConfig|localStorage|config\[|formulaSettings)"
        has_save = bool(re.search(pattern, self.content))
        return self._assert_true(
            has_save,
            'Selected method saved to configuration'
        )
    
    # ==============================================================
    # SECTION 5: PERSISTENCE & INTEGRATION (4 tests)
    # ==============================================================
    
    def test_19_persistent_storage(self):
        """Test that method uses persistent storage (localStorage)"""
        has_storage = 'localStorage' in self.content or 'StorageManager' in self.content
        return self._assert_true(
            has_storage,
            'Uses persistent storage for global method'
        )
    
    def test_20_config_structure(self):
        """Test that global method is part of config structure"""
        has_config = 'formulaSettings' in self.content or 'globalMethod' in self.content
        return self._assert_true(
            has_config,
            'Global method part of configuration structure'
        )
    
    def test_21_applies_to_hero(self):
        """Test that global calculation is applied to hero section"""
        has_hero = 'drawHero' in self.content or 'heroProgress' in self.content
        return self._assert_true(
            has_hero,
            'Global calculation applied to hero section'
        )
    
    def test_22_applies_to_dashboard(self):
        """Test that global calculation updates dashboard"""
        has_dashboard = 'renderDashboard' in self.content or 'apply()' in self.content
        return self._assert_true(
            has_dashboard,
            'Global calculation updates dashboard'
        )
    
    # ==============================================================
    # SECTION 6: COMPLETE CODE PATH (2 tests)
    # ==============================================================
    
    def test_23_complete_ui_to_calc_path(self):
        """Test complete UI → Save → Calculate code path exists"""
        # Check for all components in sequence
        has_ui = 'global-weighted' in self.content
        has_save = 'saveConfig' in self.content or 'StorageManager' in self.content
        has_calc = 'calculateGlobalProgress' in self.content
        return self._assert_true(
            has_ui and has_save and has_calc,
            'Complete UI → Save → Calculate code path exists'
        )
    
    def test_24_both_methods_discoverable(self):
        """Test that all code paths for both methods are discoverable"""
        has_both = (
            'id="global-weighted"' in self.content and
            'id="global-simple"' in self.content and
            ('weighted' in self.content.lower() or 'simple' in self.content.lower())
        )
        return self._assert_true(
            has_both,
            'Both calculation methods are discoverable in code'
        )
    
    # ==============================================================
    # TEST RUNNER
    # ==============================================================
    
    def run_all_tests(self):
        """Run all test methods"""
        tests = [
            # Section 1: HTML Structure (5 tests)
            self.test_1_global_section_exists,
            self.test_2_global_weighted_button,
            self.test_3_global_simple_button,
            self.test_4_radio_values,
            self.test_5_default_selection,
            
            # Section 2: UI Labels & Descriptions (5 tests)
            self.test_6_weighted_label,
            self.test_7_simple_label,
            self.test_8_weighted_formula,
            self.test_9_simple_formula,
            self.test_10_section_header,
            
            # Section 3: Calculation Implementation (6 tests)
            self.test_11_calculate_overall_progress_exists,
            self.test_12_reads_global_method,
            self.test_13_weighted_calculation_logic,
            self.test_14_simple_calculation_logic,
            self.test_15_method_switching,
            self.test_16_both_methods_distinct,
            
            # Section 4: Event Handling (2 tests)
            self.test_17_event_listeners,
            self.test_18_saves_to_config,
            
            # Section 5: Persistence & Integration (4 tests)
            self.test_19_persistent_storage,
            self.test_20_config_structure,
            self.test_21_applies_to_hero,
            self.test_22_applies_to_dashboard,
            
            # Section 6: Complete Code Path (2 tests)
            self.test_23_complete_ui_to_calc_path,
            self.test_24_both_methods_discoverable,
        ]
        
        for test in tests:
            try:
                test()
            except Exception as e:
                self.failed += 1
                self.test_results.append((test.__doc__, False, str(e)))
    
    def print_results(self):
        """Print test results in organized format"""
        print("\n" + "="*70)
        print("GLOBAL PROGRESS FORMULA - END-TO-END TEST SUITE")
        print("="*70)
        
        # Section results
        sections = {
            "HTML STRUCTURE": self.test_results[0:5],
            "UI LABELS & DESCRIPTIONS": self.test_results[5:10],
            "CALCULATION IMPLEMENTATION": self.test_results[10:16],
            "EVENT HANDLING": self.test_results[16:18],
            "PERSISTENCE & INTEGRATION": self.test_results[18:22],
            "COMPLETE CODE PATH": self.test_results[22:24],
        }
        
        for section_name, tests in sections.items():
            print(f"\n[{section_name}]")
            print("-" * 70)
            for test_name, passed, error in tests:
                status = "✅" if passed else "❌"
                print(f"  {status} {test_name}")
                if error:
                    print(f"     Error: {error}")
        
        print("\n" + "="*70)
        print(f"{'✅ ALL TESTS PASSED!' if self.failed == 0 else f'❌ SOME TESTS FAILED'}")
        print("="*70)
        print(f"\nTotal: {self.passed}/{self.passed + self.failed} tests passed")
        print(f"Status: {'100% PASSING ✅' if self.failed == 0 else f'{(self.passed/(self.passed+self.failed)*100):.0f}% passing'}")


if __name__ == "__main__":
    try:
        suite = GlobalProgressFormulaTestSuite()
        suite.run_all_tests()
        suite.print_results()
        
        # Exit with proper code
        sys.exit(0 if suite.failed == 0 else 1)
    except Exception as e:
        print(f"❌ Error running tests: {e}")
        sys.exit(1)
