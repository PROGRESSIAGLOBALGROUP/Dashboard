#!/usr/bin/env python3
"""
Master Test Runner: Execute All Checkbox Functionality Tests
=============================================================

This script runs all test suites and provides a comprehensive report
on checkbox functionality, data filtering, and progress calculations.

Test Suites:
1. test_checkbox_functionality.py - HTML structure and code path validation
2. test_checkbox_integration.py - Data filtering and progress calculation
3. test_data_verification.py - Embedded data and real-world scenarios
"""

import subprocess
import sys
from pathlib import Path


class TestRunner:
    """Runs all test suites and collects results."""
    
    def __init__(self):
        self.test_dir = Path("tests")
        self.test_files = [
            "test_checkbox_functionality.py",
            "test_checkbox_integration.py",
            "test_data_verification.py"
        ]
        self.results = {}
    
    def run_test_file(self, test_file: str) -> bool:
        """Run a single test file and return success status."""
        print(f"\n{'='*70}")
        print(f"Running: {test_file}")
        print(f"{'='*70}\n")
        
        cmd = [
            sys.executable,
            "-m",
            "pytest",
            str(self.test_dir / test_file),
            "-v",
            "--tb=short",
            "--color=yes"
        ]
        
        try:
            result = subprocess.run(cmd, capture_output=False)
            success = result.returncode == 0
            self.results[test_file] = success
            return success
        except Exception as e:
            print(f"❌ Error running {test_file}: {e}")
            self.results[test_file] = False
            return False
    
    def run_all(self) -> bool:
        """Run all test suites."""
        print("\n" + "="*70)
        print("🧪 CHECKBOX FUNCTIONALITY TEST SUITE")
        print("="*70)
        print("\nRunning comprehensive tests for checkbox status inclusion feature...")
        
        all_passed = True
        for test_file in self.test_files:
            if not self.run_test_file(test_file):
                all_passed = False
        
        return all_passed
    
    def print_summary(self):
        """Print summary of all test results."""
        print("\n" + "="*70)
        print("📊 TEST SUMMARY")
        print("="*70 + "\n")
        
        for test_file, passed in self.results.items():
            status = "✅ PASSED" if passed else "❌ FAILED"
            print(f"{status}: {test_file}")
        
        total = len(self.results)
        passed = sum(1 for p in self.results.values() if p)
        
        print(f"\nTotal: {passed}/{total} test suites passed\n")
        
        if passed == total:
            print("✅ ALL TESTS PASSED - Checkbox functionality is working correctly!")
        else:
            print(f"❌ {total - passed} test suite(s) failed - Please review errors above")
        
        print("\n" + "="*70)
        print("📋 WHAT WAS TESTED")
        print("="*70 + "\n")
        
        print("✅ HTML Structure & Elements:")
        print("   - Checkboxes exist with correct attributes")
        print("   - Checkboxes are checked by default")
        print("   - Event listeners are properly attached")
        
        print("\n✅ Event Handling:")
        print("   - Checkbox change events trigger handlers")
        print("   - updateStatusInclusion() is called correctly")
        print("   - UIController.apply() is invoked")
        
        print("\n✅ Data Filtering:")
        print("   - Applications filtered by status")
        print("   - Only checked statuses included")
        print("   - App count reflects filtered results")
        
        print("\n✅ Progress Calculations:")
        print("   - Progress calculated from filtered apps")
        print("   - Different filters produce different results")
        print("   - Weighted progress respects weights")
        
        print("\n✅ Complete Flow:")
        print("   - Checkbox change → Filter → Calculate → UI Update")
        print("   - Each step verified independently")
        print("   - Integration verified end-to-end")
        
        print("\n" + "="*70 + "\n")
        
        return passed == total


def main():
    """Main entry point."""
    runner = TestRunner()
    
    # Check if pytest is installed
    try:
        import pytest
    except ImportError:
        print("❌ pytest is not installed")
        print("Install with: pip install pytest beautifulsoup4")
        sys.exit(1)
    
    # Check if BeautifulSoup is installed
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        print("❌ beautifulsoup4 is not installed")
        print("Install with: pip install beautifulsoup4")
        sys.exit(1)
    
    # Run all tests
    all_passed = runner.run_all()
    
    # Print summary
    runner.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if all_passed else 1)


if __name__ == "__main__":
    main()
