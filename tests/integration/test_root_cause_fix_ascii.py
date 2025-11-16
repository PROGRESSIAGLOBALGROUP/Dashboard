#!/usr/bin/env python3
"""Root Cause Fix Validation - ASCII Version"""

import re
import sys

class RootCauseFixer:
    """Validates root cause fix implementation"""
    
    def __init__(self):
        self.file_path = 'dist/dashboard_enhanced.html'
        with open(self.file_path, 'r', encoding='utf-8', errors='ignore') as f:
            self.content = f.read()
    
    def _get_css_block(self, pattern):
        """Extract CSS block matching pattern"""
        match = re.search(pattern, self.content)
        return match.group(1) if match else None
    
    def test_1(self):
        """Test modal-content height"""
        pattern = r'\.modal-content\{\s*([^}]+)\}'
        css_block = self._get_css_block(pattern)
        if not css_block:
            return False
        return 'height:100%' in css_block
    
    def test_2(self):
        """Test scroll container overflow"""
        pattern = r'\.modal-scroll-container\{\s*([^}]+)\}'
        css_block = self._get_css_block(pattern)
        if not css_block:
            return False
        return 'overflow:hidden' in css_block
    
    def test_3(self):
        """Test tabpanel scroll point"""
        pattern = r'\.modal-tabpanel\.active\{\s*([^}]+)\}'
        css_block = self._get_css_block(pattern)
        if not css_block:
            return False
        return 'overflow-y:auto' in css_block
    
    def test_4(self):
        """Test no double scrolling"""
        scroll = self._get_css_block(r'\.modal-scroll-container\{\s*([^}]+)\}')
        tabpanel = self._get_css_block(r'\.modal-tabpanel\.active\{\s*([^}]+)\}')
        
        if not scroll or not tabpanel:
            return False
        
        scroll_ok = 'overflow:hidden' in scroll
        tabpanel_ok = 'overflow-y:auto' in tabpanel
        
        return scroll_ok and tabpanel_ok
    
    def test_5(self):
        """Test flex structure"""
        modal_content = self._get_css_block(r'\.modal-content\{\s*([^}]+)\}')
        modal_scroll = self._get_css_block(r'\.modal-scroll-container\{\s*([^}]+)\}')
        
        if not modal_content or not modal_scroll:
            return False
        
        checks = [
            'display:flex' in modal_content,
            'flex-direction:column' in modal_content,
            'height:100%' in modal_content,
            'flex:1' in modal_scroll,
            'overflow:hidden' in modal_scroll,
        ]
        
        return all(checks)
    
    def run_all_tests(self):
        """Run all tests"""
        tests = [
            ('Modal Content Height 100%', self.test_1),
            ('Scroll Container Overflow Hidden', self.test_2),
            ('Tabpanel Scroll Point', self.test_3),
            ('No Double Scrolling', self.test_4),
            ('Flex Layout Structure', self.test_5),
        ]
        
        print("=" * 70)
        print("ROOT CAUSE FIX VALIDATION TEST SUITE")
        print("=" * 70)
        print()
        
        results = {}
        for test_name, test_func in tests:
            result = test_func()
            results[test_name] = result
            symbol = "[PASS]" if result else "[FAIL]"
            print(f"{symbol} {test_name}: {result}")
        
        passed = sum(1 for v in results.values() if v)
        total = len(results)
        
        print()
        print("=" * 70)
        print(f"Results: {passed}/{total} tests PASSED")
        print("=" * 70)
        
        if passed == total:
            print()
            print("SUCCESS: ROOT CAUSE FIX APPLIED")
            print("  - Modal content now uses height: 100%")
            print("  - Scroll container now uses overflow: hidden")
            print("  - Single scroll point at tabpanel level")
            print("  - All tab heights now identical and responsive")
            return 0
        else:
            print(f"\nFAILURE: {total - passed} test(s) failed")
            return 1

if __name__ == '__main__':
    fixer = RootCauseFixer()
    exit_code = fixer.run_all_tests()
    sys.exit(exit_code)
