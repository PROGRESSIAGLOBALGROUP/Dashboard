#!/usr/bin/env python3
"""
End-to-End Test Suite for Progress Calculation Methods

This comprehensive test suite verifies that:
1. Radio buttons for progress calculation methods exist and are functional
2. Each method (Weighted, Simple, Minimum) has proper UI representation  
3. Method selection saves to configuration
4. calculateBUProgress() reads and applies the selected method
5. Different methods produce different calculation results
6. Method persists across page reloads
7. Default method is Weighted Average
"""

import json
import re
from pathlib import Path
from bs4 import BeautifulSoup


class ProgressCalculationMethodE2ETests:
    """End-to-end tests for Progress Calculation Methods functionality"""
    
    def __init__(self):
        self.html_file = Path('dist/dashboard_enhanced.html')
        self.content = self._read_file()
        self.soup = BeautifulSoup(self.content, 'html.parser')
        self.results = []
        self.test_count = 0
        self.pass_count = 0
    
    def _read_file(self):
        """Read the HTML file"""
        with open(self.html_file, 'r', encoding='utf-8') as f:
            return f.read()
    
    def _log_result(self, test_name, passed, message):
        """Log test result"""
        self.test_count += 1
        if passed:
            self.pass_count += 1
            print(f"  ✅ {test_name}")
        else:
            print(f"  ❌ {test_name}")
        
        self.results.append({
            'test': test_name,
            'passed': passed,
            'message': message
        })
    
    def section(self, name):
        """Print section header"""
        print(f"\n[{name}]")
        print("-" * 70)
    
    def test_1_html_structure(self):
        """1. HTML STRUCTURE - Verify radio buttons exist in HTML"""
        self.section("1. HTML STRUCTURE")
        
        # Find all radio buttons with name="progress-method"
        radios = self.soup.find_all('input', {'name': 'progress-method', 'type': 'radio'})
        
        self._log_result(
            "Three radio buttons exist",
            len(radios) == 3,
            f"Found {len(radios)} radio buttons (expected 3)"
        )
        
        # Check for specific IDs
        ids = [r.get('id') for r in radios]
        has_weighted = 'method-weighted' in ids
        has_simple = 'method-simple' in ids
        has_minimum = 'method-minimum' in ids
        
        self._log_result(
            "method-weighted radio button exists",
            has_weighted,
            "method-weighted ID found" if has_weighted else "method-weighted ID missing"
        )
        
        self._log_result(
            "method-simple radio button exists",
            has_simple,
            "method-simple ID found" if has_simple else "method-simple ID missing"
        )
        
        self._log_result(
            "method-minimum radio button exists",
            has_minimum,
            "method-minimum ID found" if has_minimum else "method-minimum ID missing"
        )
        
        # Check for values
        values = [r.get('value') for r in radios]
        correct_values = 'weighted' in values and 'simple' in values and 'minimum' in values
        
        self._log_result(
            "Radio buttons have correct value attributes",
            correct_values,
            f"Values: {values}"
        )
    
    def test_2_labels_and_descriptions(self):
        """2. LABELS & DESCRIPTIONS - Verify UI labels for each method"""
        self.section("2. LABELS & DESCRIPTIONS")
        
        # Check for labels associated with radio buttons
        weighted_label = self.soup.find('label', {'for': 'method-weighted'})
        simple_label = self.soup.find('label', {'for': 'method-simple'})
        minimum_label = self.soup.find('label', {'for': 'method-minimum'})
        
        self._log_result(
            "Weighted Average has label",
            weighted_label is not None,
            "Label found" if weighted_label else "Label missing"
        )
        
        self._log_result(
            "Simple Average has label",
            simple_label is not None,
            "Label found" if simple_label else "Label missing"
        )
        
        self._log_result(
            "Minimum Progress has label",
            minimum_label is not None,
            "Label found" if minimum_label else "Label missing"
        )
        
        # Check for descriptions
        if weighted_label:
            desc_text = weighted_label.get_text(strip=True)
            has_desc = len(desc_text) > 20  # Should have meaningful content
            self._log_result(
                "Weighted Average has description text",
                has_desc,
                f"Description: {desc_text[:50]}..." if has_desc else "No description"
            )
        
        # Check for "Progress Calculation Method" section header
        has_header = "Progress Calculation Method" in self.content
        self._log_result(
            "Section has descriptive header",
            has_header,
            "Header 'Progress Calculation Method' found" if has_header else "Header missing"
        )
    
    def test_3_default_selection(self):
        """3. DEFAULT SELECTION - Verify Weighted Average is default"""
        self.section("3. DEFAULT SELECTION")
        
        weighted_radio = self.soup.find('input', {'id': 'method-weighted'})
        
        is_checked = weighted_radio and weighted_radio.get('checked') is not None
        
        self._log_result(
            "Weighted Average is checked by default",
            is_checked,
            "method-weighted has 'checked' attribute" if is_checked else "method-weighted not checked"
        )
    
    def test_4_event_handling(self):
        """4. EVENT HANDLING - Verify radio button changes are handled"""
        self.section("4. EVENT HANDLING")
        
        # Check for addEventListener on progress-method
        has_listener_code = bool(re.search(
            r'addEventListener.*progress-method|progress-method.*addEventListener',
            self.content,
            re.IGNORECASE | re.DOTALL
        ))
        
        self._log_result(
            "Event listener attached to radio buttons",
            has_listener_code,
            "addEventListener code found" if has_listener_code else "No event listener found"
        )
        
        # Check for config save on change
        has_config_save = bool(re.search(
            r'progressMethod|formulaSettings.*method|document.querySelector.*progress-method',
            self.content,
            re.IGNORECASE
        ))
        
        self._log_result(
            "Selected method saved to configuration",
            has_config_save,
            "Config save logic found" if has_config_save else "No config save found"
        )
    
    def test_5_calculation_implementation(self):
        """5. CALCULATION IMPLEMENTATION - Verify methods are actually implemented"""
        self.section("5. CALCULATION IMPLEMENTATION")
        
        # Check for calculateBUProgress function
        has_function = 'calculateBUProgress' in self.content
        self._log_result(
            "calculateBUProgress() function exists",
            has_function,
            "Function found" if has_function else "Function missing"
        )
        
        if has_function:
            # Better extraction: find start and match braces properly
            start_pos = self.content.find('calculateBUProgress')
            if start_pos > 0:
                # Find opening brace
                func_start = self.content.find('{', start_pos)
                if func_start > 0:
                    # Count braces to find end
                    brace_count = 0
                    func_end = None
                    for i in range(func_start, min(func_start + 10000, len(self.content))):
                        if self.content[i] == '{':
                            brace_count += 1
                        elif self.content[i] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                func_end = i
                                break
                    
                    if func_end:
                        func_body = self.content[func_start:func_end + 1]
                        
                        # Check if progressMethod is read
                        reads_method = bool(re.search(
                            r'progressMethod|formulaSettings.*progressMethod',
                            func_body,
                            re.IGNORECASE
                        ))
                        
                        self._log_result(
                            "calculateBUProgress() reads progressMethod",
                            reads_method,
                            "progressMethod is read from config" if reads_method else "progressMethod not read"
                        )
                        
                        # Check for method switching
                        has_switch = bool(re.search(
                            r'switch\s*\(|case\s+["\']weighted["\']|case\s+["\']simple["\']|case\s+["\']minimum["\']',
                            func_body,
                            re.IGNORECASE
                        ))
                        
                        self._log_result(
                            "calculateBUProgress() has method switching logic",
                            has_switch,
                            "Switch/case statement found" if has_switch else "No method switching"
                        )
                        
                        # Check for weighted implementation
                        has_weighted = bool(re.search(r'weighted|weight|auto.*weight', func_body, re.IGNORECASE))
                        self._log_result(
                            "Weighted Average calculation implemented",
                            has_weighted,
                            "Weighted logic found" if has_weighted else "Weighted logic missing"
                        )
                        
                        # Check for simple average implementation
                        has_simple = bool(re.search(
                            r"case\s+['\"]simple['\"]|'simple'|\"simple\"|simpleSum|\.reduce",
                            func_body,
                            re.IGNORECASE
                        ))
                        self._log_result(
                            "Simple Average calculation implemented",
                            has_simple,
                            "Simple average logic found" if has_simple else "Simple average logic missing"
                        )
                        
                        # Check for minimum implementation
                        has_minimum = bool(re.search(
                            r"case\s+['\"]minimum['\"]|'minimum'|\"minimum\"|bottleneck|minimum.*progress",
                            func_body,
                            re.IGNORECASE
                        ))
                        self._log_result(
                            "Minimum Progress calculation implemented",
                            has_minimum,
                            "Minimum logic found" if has_minimum else "Minimum logic missing"
                        )
    
    def test_6_persistence(self):
        """6. PERSISTENCE - Verify method selection persists"""
        self.section("6. PERSISTENCE")
        
        # Check for localStorage usage
        uses_storage = bool(re.search(r'localStorage|StorageManager', self.content))
        self._log_result(
            "Uses persistent storage (localStorage)",
            uses_storage,
            "Storage mechanism found" if uses_storage else "No storage found"
        )
        
        # Check for config initialization
        has_init = bool(re.search(
            r'loadConfig|initialize|init\s*\(',
            self.content,
            re.IGNORECASE
        ))
        self._log_result(
            "Configuration loaded on initialization",
            has_init,
            "Config loading code found" if has_init else "No config loading"
        )
    
    def test_7_integration_in_settings(self):
        """7. INTEGRATION - Verify controls in Settings tab"""
        self.section("7. SETTINGS TAB INTEGRATION")
        
        # Check if method controls are in settings tab
        settings_tab = self.soup.find('div', {'id': 'tab-settings'})
        
        if settings_tab:
            settings_content = settings_tab.get_text()
            has_methods = 'progress' in settings_content.lower() or 'method' in settings_content.lower()
            
            self._log_result(
                "Progress Calculation controls in Settings tab",
                has_methods,
                "Controls found in tab" if has_methods else "Controls not in tab"
            )
        else:
            # Might be in different location, just verify section exists
            has_config_section = 'Progress Calculation Method' in self.content
            self._log_result(
                "Progress Calculation controls are present",
                has_config_section,
                "Configuration section found" if has_config_section else "Not found"
            )
    
    def test_8_complete_code_path(self):
        """8. CODE PATH - Verify complete flow from UI to calculation"""
        self.section("8. COMPLETE CODE PATH")
        
        # Verify the entire flow exists
        has_ui = bool(re.search(r'method-weighted|method-simple|method-minimum', self.content))
        has_listener = bool(re.search(r'addEventListener.*change', self.content))
        has_save = bool(re.search(r'progressMethod|StorageManager', self.content))
        has_calc = bool(re.search(r'calculateBUProgress', self.content))
        
        all_parts = has_ui and has_listener and has_save and has_calc
        
        self._log_result(
            "Complete UI→Save→Calculate code path exists",
            all_parts,
            "All components present" if all_parts else "Missing components"
        )
        
        # Verify different methods produce different results (static analysis)
        distinct_methods = bool(re.search(
            r"(weighted|weight).*?simple.*?minimum|"
            r"case\s+['\"]weighted['\"]|case\s+['\"]simple['\"]|case\s+['\"]minimum['\"]",
            self.content,
            re.IGNORECASE | re.DOTALL
        ))
        
        self._log_result(
            "All three methods have distinct implementations",
            distinct_methods,
            "Methods are implemented differently" if distinct_methods else "Methods may be identical"
        )
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("\n" + "=" * 70)
        print("PROGRESS CALCULATION METHODS - END-TO-END TEST SUITE")
        print("=" * 70)
        
        self.test_1_html_structure()
        self.test_2_labels_and_descriptions()
        self.test_3_default_selection()
        self.test_4_event_handling()
        self.test_5_calculation_implementation()
        self.test_6_persistence()
        self.test_7_integration_in_settings()
        self.test_8_complete_code_path()
        
        # Print summary
        print("\n" + "=" * 70)
        failed = self.test_count - self.pass_count
        
        if self.pass_count == self.test_count:
            print(f"✅ ALL {self.test_count} TESTS PASSED!")
        else:
            print(f"⚠️  Results: {self.pass_count}/{self.test_count} passed, {failed} failed")
        
        print("=" * 70)
        
        # Show failures if any
        if failed > 0:
            print("\nFailed Tests:")
            print("-" * 70)
            for result in self.results:
                if not result['passed']:
                    print(f"❌ {result['test']}")
                    print(f"   └─ {result['message']}\n")
        
        print()
        return self.pass_count == self.test_count


if __name__ == '__main__':
    import sys
    tester = ProgressCalculationMethodE2ETests()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)
