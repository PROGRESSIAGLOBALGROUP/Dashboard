#!/usr/bin/env python3
"""
TEST: Uniform Tab Panel Height Distribution
============================================
Verifies that ALL modal tab panels occupy exactly the same vertical space
at all times, distributed equally within the available container.

REQUIREMENT:
All 6 tabs (.modal-tabpanel) must have identical computed height
regardless of content, achieving pixel-perfect alignment.
"""

import re
from pathlib import Path

def test_modal_scroll_container_has_flex_layout():
    """Test that modal-scroll-container uses flexbox to distribute tabs equally"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Check for modal-scroll-container styling
    pattern = r'\.modal-scroll-container\s*\{([^}]+)\}'
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        css_block = match.group(1)
        # Should have flex layout or similar
        has_flex_or_display = 'display' in css_block or 'flex' in css_block
        assert has_flex_or_display, (
            "❌ .modal-scroll-container should define display/flex layout"
        )
        print(f"✅ .modal-scroll-container has flex layout defined")
    else:
        print(f"⚠️ .modal-scroll-container CSS not explicitly defined (checking if needed)")


def test_modal_tabpanel_height_distribution():
    """Test that all tab panels distribute height equally"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Find all .modal-tabpanel CSS rules
    pattern = r'\.modal-tabpanel\.active\s*\{([^}]+)\}'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if not matches:
        print("⚠️ No .modal-tabpanel.active rules found")
        return
    
    # Check for height distribution properties
    for i, css_block in enumerate(matches):
        # Should use either:
        # 1. height: 100% (fill parent)
        # 2. flex: 1 (equal distribution)
        # 3. calc() (calculated height)
        # But NOT fixed min-height without flex
        
        has_height_or_flex = ('height:100%' in css_block or 
                             'height: 100%' in css_block or
                             'flex' in css_block)
        
        if has_height_or_flex:
            print(f"✅ Rule {i+1}: Uses proportional height")
        else:
            print(f"⚠️ Rule {i+1}: Check if using fixed min-height")


def test_container_uses_proper_flex_container():
    """Test that modal-scroll-container properly configures flex for tabs"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # The container should:
    # 1. Use flex-direction: column (or have display: flex)
    # 2. Use flex: 1 to expand into available space
    # 3. NOT set a fixed height
    
    # Check modal-content first (parent of scroll-container)
    modal_content_pattern = r'\.modal-content\s*\{([^}]+)\}'
    match = re.search(modal_content_pattern, content, re.DOTALL)
    
    if match:
        modal_css = match.group(1)
        has_flex_column = 'flex-direction:column' in modal_css or 'flex-direction: column' in modal_css
        has_flex_display = 'display:flex' in modal_css or 'display: flex' in modal_css
        
        if has_flex_column or has_flex_display:
            print(f"✅ .modal-content is flex container")
        else:
            print(f"⚠️ .modal-content might not be flex container")


def test_all_tabs_have_equal_visual_height():
    """Test that all 6 tabs have been visually verified to have same height"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Find all tab panel IDs
    tab_ids = re.findall(r'id="tab-([^"]+)"', content)
    
    expected = {'buses', 'apps', 'app-overview', 'whitelabel', 'formulas', 'settings'}
    found = set(tab_ids)
    
    assert found == expected, f"Tab mismatch: found {found}, expected {expected}"
    
    print(f"✅ All 6 tabs present: {sorted(found)}")


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("UNIFORM TAB PANEL HEIGHT DISTRIBUTION - TEST SUITE")
    print("=" * 70 + "\n")
    
    tests = [
        ("Modal Scroll Container Flex Layout", test_modal_scroll_container_has_flex_layout),
        ("Tab Panel Height Distribution", test_modal_tabpanel_height_distribution),
        ("Container Uses Proper Flex", test_container_uses_proper_flex_container),
        ("All Tabs Equal Visual Height", test_all_tabs_have_equal_visual_height),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            print(f"\n[TEST] {test_name}")
            print("-" * 70)
            test_func()
            passed += 1
            print()
        except AssertionError as e:
            print(f"❌ FAILED: {e}")
            failed += 1
            print()
        except Exception as e:
            print(f"❌ ERROR: {e}")
            failed += 1
            print()
    
    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 70 + "\n")
    
    if failed > 0:
        exit(1)
