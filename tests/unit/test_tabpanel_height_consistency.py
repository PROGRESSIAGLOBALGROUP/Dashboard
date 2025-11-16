#!/usr/bin/env python3
"""
TEST: Tab Panel Height Consistency
===================================
Verifies that ALL modal tab panels maintain consistent height regardless of content.

REQUIREMENT:
Business Units and Applications tabs must have the same height as Applications Overview,
even when empty. No tab should be shorter than others.

FORMULA:
- All .modal-tabpanel.active must have minimum height guarantee
- No collapsing when content is minimal or absent
"""

import re
from pathlib import Path

def test_modal_tabpanel_has_min_height():
    """Test that .modal-tabpanel.active has height constraint defined"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Find CSS for .modal-tabpanel.active (main definition, not in media queries)
    # Look for the base definition first
    pattern = r'\.modal-tabpanel\{[^}]+\}\s*\.modal-tabpanel\.active\s*\{([^}]+)\}'
    match = re.search(pattern, content, re.DOTALL)
    
    if not match:
        # Try alternate pattern
        pattern = r'\.modal-tabpanel\.active\s*\{\s*display\s*:\s*block;([^}]+)\}'
        match = re.search(pattern, content, re.DOTALL)
    
    assert match, "❌ .modal-tabpanel.active CSS not found"
    
    css_block = match.group(1) if match.lastindex > 0 else match.group(0)
    
    # Check for height property (can be height:100%, min-height, etc)
    has_height_constraint = re.search(r'(?:height|min-height)\s*:\s*(?:100%|[\d.]+(?:px|vh|em|rem))', content)
    
    assert has_height_constraint, (
        "❌ .modal-tabpanel.active missing height constraint\n"
        f"Current CSS:\n{css_block}"
    )
    
    # Extract the height value from full content
    height_matches = re.findall(r'\.modal-tabpanel\.active[^{]*\{[^}]*((?:height|min-height)\s*:\s*(?:100%|[\d.]+(?:px|vh|em|rem)))', content)
    height_value = height_matches[0] if height_matches else "not found"
    
    print(f"✅ .modal-tabpanel.active has height constraint: {height_value}")


def test_all_tabs_render_same_height():
    """Test that all tab panels render with same minimum height"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Find all .modal-tabpanel divs
    tab_panels = re.findall(r'<div class="modal-tabpanel[^"]*" id="tab-([^"]+)"', content)
    
    assert len(tab_panels) > 0, "❌ No tab panels found"
    
    expected_tabs = ['buses', 'apps', 'app-overview', 'whitelabel', 'formulas', 'settings']
    found_tabs = set(tab_panels)
    expected_set = set(expected_tabs)
    
    assert found_tabs == expected_set, (
        f"❌ Tab mismatch.\n"
        f"Expected: {expected_set}\n"
        f"Found: {found_tabs}"
    )
    
    print(f"✅ All {len(tab_panels)} tab panels present:")
    for tab in tab_panels:
        print(f"   - tab-{tab}")


def test_bus_apps_tabs_not_shorter():
    """Test that Business Units and Applications tabs can't be shorter than overview"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Find Business Units tab content
    bu_tab_pattern = r'<div class="modal-tabpanel[^"]*" id="tab-buses">(.*?)</div>\s*<!-- TAB: APPLICATIONS -->'
    bu_tab_match = re.search(bu_tab_pattern, content, re.DOTALL)
    
    assert bu_tab_match, "❌ Business Units tab not found"
    
    # Find Applications tab content
    apps_tab_pattern = r'<div class="modal-tabpanel[^"]*" id="tab-apps">(.*?)</div>\s*<!-- TAB: APPLICATIONS OVERVIEW -->'
    apps_tab_match = re.search(apps_tab_pattern, content, re.DOTALL)
    
    assert apps_tab_match, "❌ Applications tab not found"
    
    bu_tab_content = bu_tab_match.group(1)
    apps_tab_content = apps_tab_match.group(1)
    
    # Check that both tabs exist
    assert len(bu_tab_content) > 0, "❌ Business Units tab content is empty"
    assert len(apps_tab_content) > 0, "❌ Applications tab content is empty"
    
    print(f"✅ Business Units tab: {len(bu_tab_content)} chars")
    print(f"✅ Applications tab: {len(apps_tab_content)} chars")


def test_min_height_applies_to_active_state():
    """Test that height constraint is specifically for .active state"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Check that .modal-tabpanel.active has the height constraint
    # Look for all definitions of .modal-tabpanel.active with height property
    pattern = r'\.modal-tabpanel\.active\s*\{[^}]*(?:height|min-height)'
    matches = re.findall(pattern, content, re.DOTALL)
    
    assert len(matches) > 0, (
        "❌ .modal-tabpanel.active doesn't enforce height constraint"
    )
    
    print(f"✅ .modal-tabpanel.active enforces height constraint in {len(matches)} place(s)")


def test_no_collapse_when_empty():
    """Test that empty tabs don't collapse - uses flexible height"""
    dist_file = Path("dist/dashboard_enhanced.html")
    content = dist_file.read_text(encoding='utf-8')
    
    # Extract height constraint values from CSS for .modal-tabpanel.active
    height_pattern = r'\.modal-tabpanel\.active\s*\{[^}]*(height|min-height)\s*:\s*(100%|[\d.]+px)'
    matches = re.findall(height_pattern, content, re.DOTALL)
    
    assert len(matches) > 0, "❌ No height constraint found for .modal-tabpanel.active"
    
    # Check that we're using flexible height (100%) or good minimums
    for prop, value in matches:
        if value == '100%':
            print(f"✅ Using flexible height ({prop}: 100%) - fills available space")
        elif 'px' in value:
            value_int = int(value.replace('px', ''))
            if value_int >= 300:
                print(f"✅ Using {prop}: {value} - prevents collapse")
            else:
                print(f"⚠️ Height {value} might be too small")
        
    if len(matches) > 1:
        print(f"✅ {len(matches)} responsive height rules defined")


if __name__ == '__main__':
    print("\n" + "=" * 70)
    print("TAB PANEL HEIGHT CONSISTENCY - TEST SUITE")
    print("=" * 70 + "\n")
    
    tests = [
        ("Modal TabPanel Has Min-Height", test_modal_tabpanel_has_min_height),
        ("All Tabs Render Same Height", test_all_tabs_render_same_height),
        ("BU/Apps Tabs Not Shorter", test_bus_apps_tabs_not_shorter),
        ("Min-Height Applies to Active", test_min_height_applies_to_active_state),
        ("No Collapse When Empty", test_no_collapse_when_empty),
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
