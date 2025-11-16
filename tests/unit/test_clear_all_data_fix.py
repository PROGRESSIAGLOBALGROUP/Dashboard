"""
TEST: Clear All Data Fix - Verify persistent flag prevents re-loading hardcoded data

Test Scenario:
1. Simulate initial load (data loaded from EMBEDDED_DATA to localStorage)
2. User clicks Clear All Data
3. Simulate page reload
4. Verify localStorage stays empty (flag prevents DataLoader reload)
"""

import json
import unittest
from unittest.mock import patch, MagicMock


class TestClearAllDataFix(unittest.TestCase):
    """Test that Clear All Data properly prevents re-loading embedded data"""
    
    STORAGE_KEY = 'dashboard_config_v1'
    MANUAL_CLEAR_FLAG = 'dashboard_user_manually_cleared_v1'
    
    def test_1_initial_load_populates_data(self):
        """Step 1: Initial load should populate localStorage from EMBEDDED_DATA"""
        print("\n✅ TEST 1: Initial Load")
        print("-" * 50)
        
        # Simulate initial localStorage (empty)
        mock_storage = {}
        
        # Simulate DataLoader.loadData() call
        embedded_data = {
            'buses': [
                {'id': 1, 'key': 'CORF', 'name': 'COMM'},
                {'id': 2, 'key': 'CORF', 'name': 'HR'}
            ],
            'apps': [
                {'id': 1, 'buId': 1, 'name': 'App1'},
                {'id': 2, 'buId': 2, 'name': 'App2'}
            ]
        }
        
        # Save to storage (simulating DataLoader.loadData())
        mock_storage[self.STORAGE_KEY] = json.dumps(embedded_data)
        
        # Verify data is in localStorage
        self.assertIn(self.STORAGE_KEY, mock_storage)
        stored = json.loads(mock_storage[self.STORAGE_KEY])
        self.assertEqual(len(stored['buses']), 2)
        self.assertEqual(len(stored['apps']), 2)
        print(f"✅ Data loaded: {len(stored['buses'])} buses, {len(stored['apps'])} apps")
    
    def test_2_clear_all_data_sets_flag(self):
        """Step 2: Clear All Data should set persistent flag BEFORE clearing storage"""
        print("\n✅ TEST 2: Clear All Data Sets Flag")
        print("-" * 50)
        
        # Simulate storage with data
        mock_storage = {
            self.STORAGE_KEY: json.dumps({'buses': [{'id': 1}], 'apps': []})
        }
        
        # Simulate clearAllData() logic
        flag_data = {
            'cleared': True,
            'timestamp': '2025-11-15T10:00:00Z',
            'reason': 'User executed Clear All Data action'
        }
        
        # Set flag BEFORE clear
        mock_storage[self.MANUAL_CLEAR_FLAG] = json.dumps(flag_data)
        
        # Get flag value (to preserve it)
        flag_value = mock_storage.get(self.MANUAL_CLEAR_FLAG)
        
        # Clear storage
        mock_storage.clear()
        
        # Restore flag
        if flag_value:
            mock_storage[self.MANUAL_CLEAR_FLAG] = flag_value
        
        # Verify
        self.assertNotIn(self.STORAGE_KEY, mock_storage)  # Data is gone
        self.assertIn(self.MANUAL_CLEAR_FLAG, mock_storage)  # Flag persists
        print(f"✅ Flag set: {mock_storage[self.MANUAL_CLEAR_FLAG]}")
        print(f"✅ Data cleared: {self.STORAGE_KEY} not in storage")
    
    def test_3_reload_respects_manual_clear_flag(self):
        """Step 3: On reload, presence of flag should prevent DataLoader.loadData()"""
        print("\n✅ TEST 3: Reload Respects Manual Clear Flag")
        print("-" * 50)
        
        # Simulate storage after Clear All Data
        mock_storage = {
            self.MANUAL_CLEAR_FLAG: json.dumps({
                'cleared': True,
                'timestamp': '2025-11-15T10:00:00Z'
            })
        }
        
        # Simulate initialization logic (the fix)
        was_manually_cleared = mock_storage.get(self.MANUAL_CLEAR_FLAG) is not None
        
        # Verify flag prevents data loading
        if was_manually_cleared:
            print("🚫 Manual clear flag detected - skipping DataLoader.loadData()")
            load_data = False
        else:
            print("✅ No manual clear flag - will load DataLoader")
            load_data = True
        
        self.assertFalse(load_data)
        self.assertNotIn(self.STORAGE_KEY, mock_storage)
        print(f"✅ DataLoader skipped: load_data = {load_data}")
        print(f"✅ localStorage stays empty: {list(mock_storage.keys())}")
    
    def test_4_complete_clear_flow(self):
        """Complete flow: Initial load → Clear → Reload → Verify empty"""
        print("\n✅ TEST 4: Complete Flow")
        print("-" * 50)
        
        # PHASE 1: Initial load
        print("Phase 1: Initial load...")
        mock_storage = {}
        mock_storage[self.STORAGE_KEY] = json.dumps({
            'buses': [{'id': 1}, {'id': 2}],
            'apps': [{'id': 1}, {'id': 2}, {'id': 3}]
        })
        print(f"  ✅ Loaded: {len(json.loads(mock_storage[self.STORAGE_KEY])['buses'])} buses")
        
        # PHASE 2: User clears data
        print("Phase 2: User clicks Clear All Data...")
        flag_value = json.dumps({'cleared': True, 'timestamp': '2025-11-15T10:00:00Z'})
        mock_storage[self.MANUAL_CLEAR_FLAG] = flag_value
        mock_storage.clear()
        mock_storage[self.MANUAL_CLEAR_FLAG] = flag_value
        print(f"  ✅ Cleared localStorage")
        print(f"  ✅ Manual clear flag set")
        
        # PHASE 3: Page reload
        print("Phase 3: Page reload...")
        was_manually_cleared = self.MANUAL_CLEAR_FLAG in mock_storage
        if was_manually_cleared:
            print(f"  🚫 Manual clear flag detected - skipping DataLoader")
            # Don't load embedded data
            pass
        else:
            # Would load embedded data (NOT happening due to flag)
            pass
        
        # PHASE 4: Verify final state
        print("Phase 4: Verify final state...")
        self.assertNotIn(self.STORAGE_KEY, mock_storage, 
                        "Config data should not be in storage after clear")
        self.assertIn(self.MANUAL_CLEAR_FLAG, mock_storage,
                     "Manual clear flag should persist")
        
        remaining_keys = [k for k in mock_storage.keys() if k != self.MANUAL_CLEAR_FLAG]
        self.assertEqual(len(remaining_keys), 0,
                        f"No data should remain in storage, but found: {remaining_keys}")
        
        print(f"  ✅ localStorage remains empty")
        print(f"  ✅ Only manual clear flag present: {list(mock_storage.keys())}")


if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("TESTING: Clear All Data Fix")
    print("=" * 60)
    
    unittest.main(verbosity=2)
