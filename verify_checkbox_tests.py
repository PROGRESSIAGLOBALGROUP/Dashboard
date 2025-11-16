#!/usr/bin/env python3
"""
Quick Verification Script - Checkbox Status Inclusion Test Suite
Runs the critical 26 tests and provides clear pass/fail status.
Usage: python verify_checkbox_tests.py
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    """Run critical checkbox tests and report results."""
    
    test_file = Path("tests/test_checkbox_functionality.py")
    
    if not test_file.exists():
        print("ERROR: Test file not found at tests/test_checkbox_functionality.py")
        return False
    
    print("\n" + "="*70)
    print("RUNNING CHECKBOX STATUS INCLUSION VERIFICATION")
    print("="*70 + "\n")
    
    # Run tests
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", 
             str(test_file), 
             "-v", "--tb=short"],
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print("\n" + "="*70)
            print("SUCCESS: All critical tests passed!")
            print("="*70)
            print("\nWhat this verification confirms:")
            print("  ✓ Checkbox HTML elements exist and are properly configured")
            print("  ✓ Event listeners are attached and functional")
            print("  ✓ State changes trigger updates")
            print("  ✓ Data filtering uses checkbox state")
            print("  ✓ Progress calculations use filtered data")
            print("  ✓ UI updates reflect calculated values")
            print("  ✓ Complete end-to-end code path works")
            print("\nConclusion: Checkbox functionality is working correctly!\n")
            return True
        else:
            print("\n" + "="*70)
            print("FAILURE: Some tests failed")
            print("="*70 + "\n")
            return False
            
    except Exception as e:
        print(f"ERROR: Failed to run tests: {e}")
        return False

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
