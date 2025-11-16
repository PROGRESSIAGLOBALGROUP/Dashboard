#!/usr/bin/env python3
"""
Quick Verification Script for Progress Calculation Methods

Run this to verify that all Progress Calculation Method functionality works end-to-end.
Usage: python verify_progress_methods.py
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    """Run the Progress Calculation Methods test suite"""
    
    print("\n" + "=" * 70)
    print("PROGRESS CALCULATION METHODS - VERIFICATION")
    print("=" * 70 + "\n")
    
    test_file = Path("tests/test_progress_calculation_methods_e2e.py")
    
    if not test_file.exists():
        print("❌ ERROR: Test file not found at tests/test_progress_calculation_methods_e2e.py")
        return False
    
    try:
        result = subprocess.run(
            [sys.executable, str(test_file)],
            capture_output=False,
            text=True
        )
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ ERROR: Failed to run tests: {e}")
        return False

if __name__ == '__main__':
    print("🧪 Running Progress Calculation Methods E2E Tests...\n")
    success = run_tests()
    
    if success:
        print("\n" + "=" * 70)
        print("✅ ALL TESTS PASSED - Progress Calculation Methods Work Correctly!")
        print("=" * 70 + "\n")
        print("What was verified:")
        print("  ✓ Radio buttons for method selection exist in UI")
        print("  ✓ All three methods (Weighted, Simple, Minimum) are available")
        print("  ✓ Weighted Average is the default method")
        print("  ✓ Selected method is saved to configuration")
        print("  ✓ calculateBUProgress() reads the progressMethod setting")
        print("  ✓ All three methods have distinct implementations")
        print("  ✓ Method selection persists across page loads")
        print("  ✓ Complete end-to-end code path is functional\n")
    else:
        print("\n" + "=" * 70)
        print("❌ Some tests failed - Review output above for details")
        print("=" * 70 + "\n")
    
    sys.exit(0 if success else 1)
