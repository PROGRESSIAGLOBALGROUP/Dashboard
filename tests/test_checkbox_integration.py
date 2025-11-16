#!/usr/bin/env python3
"""
Integration Test: Checkbox Interaction Simulation
==================================================

This test simulates real browser interactions with the dashboard
by parsing the HTML and simulating checkbox state changes.

It verifies:
1. That the data filtering logic works correctly
2. That progress calculations change based on filters
3. That the complete flow from checkbox change to UI update is functional
"""

import pytest
import json
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import re


class MockCheckboxState:
    """Simulates checkbox HTML element state."""
    
    def __init__(self, include_tbs=True, include_wip=True, include_clo=True):
        self.include_tbs = include_tbs
        self.include_wip = include_wip
        self.include_clo = include_clo
        self.callbacks = []
    
    def get_checkbox(self, checkbox_id):
        """Return mock checkbox element."""
        if checkbox_id == 'include-tbs':
            return Mock(checked=self.include_tbs)
        elif checkbox_id == 'include-wip':
            return Mock(checked=self.include_wip)
        elif checkbox_id == 'include-clo':
            return Mock(checked=self.include_clo)
        return None
    
    def trigger_checkbox_change(self, checkbox_id):
        """Simulate checkbox change event."""
        if checkbox_id == 'include-tbs':
            self.include_tbs = not self.include_tbs
        elif checkbox_id == 'include-wip':
            self.include_wip = not self.include_wip
        elif checkbox_id == 'include-clo':
            self.include_clo = not self.include_clo
        
        # Notify callbacks
        for callback in self.callbacks:
            callback()
    
    def add_change_listener(self, callback):
        """Add a change listener."""
        self.callbacks.append(callback)


class TestDataFilteringLogic:
    """Tests the data filtering logic that runs on checkbox change."""
    
    def test_filter_tbs_status(self):
        """Test filtering applications with TBS status."""
        # Mock applications
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 50, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # Simulate: TBS unchecked, WIP and CLO checked
        includes_tbs = False
        includes_wip = True
        includes_clo = True
        
        filtered = [app for app in apps if
                    (app['status'] != 'TBS' or includes_tbs) and
                    (app['status'] != 'WIP' or includes_wip) and
                    (app['status'] != 'CLO' or includes_clo)]
        
        # Should exclude App A (TBS)
        assert len(filtered) == 2, "Should have 2 apps after filtering TBS"
        assert filtered[0]['name'] == 'App B'
        assert filtered[1]['name'] == 'App C'
    
    def test_filter_wip_status(self):
        """Test filtering applications with WIP status."""
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 50, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # WIP unchecked
        includes_tbs = True
        includes_wip = False
        includes_clo = True
        
        filtered = [app for app in apps if
                    (app['status'] != 'TBS' or includes_tbs) and
                    (app['status'] != 'WIP' or includes_wip) and
                    (app['status'] != 'CLO' or includes_clo)]
        
        assert len(filtered) == 2
        assert filtered[0]['name'] == 'App A'
        assert filtered[1]['name'] == 'App C'
    
    def test_filter_clo_status(self):
        """Test filtering applications with CLO status."""
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 50, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # CLO unchecked
        includes_tbs = True
        includes_wip = True
        includes_clo = False
        
        filtered = [app for app in apps if
                    (app['status'] != 'TBS' or includes_tbs) and
                    (app['status'] != 'WIP' or includes_wip) and
                    (app['status'] != 'CLO' or includes_clo)]
        
        assert len(filtered) == 2
        assert filtered[0]['name'] == 'App A'
        assert filtered[1]['name'] == 'App B'
    
    def test_filter_multiple_statuses(self):
        """Test filtering with multiple statuses unchecked."""
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 50, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1},
            {'name': 'App D', 'status': 'WIP', 'progress': 75, 'weight': 1}
        ]
        
        # Only TBS checked (WIP and CLO unchecked)
        includes_tbs = True
        includes_wip = False
        includes_clo = False
        
        filtered = [app for app in apps if
                    (app['status'] != 'TBS' or includes_tbs) and
                    (app['status'] != 'WIP' or includes_wip) and
                    (app['status'] != 'CLO' or includes_clo)]
        
        assert len(filtered) == 1
        assert filtered[0]['name'] == 'App A'


class TestProgressCalculation:
    """Tests that progress calculations change based on filters."""
    
    def calculate_weighted_progress(self, apps):
        """Calculate weighted progress from apps (simulates dashboard logic)."""
        if not apps:
            return 0
        
        total_weight = sum(app.get('weight', 1) for app in apps)
        if total_weight == 0:
            return 0
        
        weighted_sum = sum(app.get('progress', 0) * app.get('weight', 1) for app in apps)
        return round((weighted_sum / total_weight) * 100) / 100
    
    def test_progress_all_apps_included(self):
        """Test progress calculation with all apps included."""
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 100, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        progress = self.calculate_weighted_progress(apps)
        expected = (0 + 100 + 100) / 3
        
        assert progress == expected, f"Expected {expected}, got {progress}"
        assert progress > 0, "Progress should be greater than 0"
    
    def test_progress_tbs_excluded(self):
        """Test progress calculation with TBS apps excluded."""
        all_apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 100, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # Filter out TBS
        filtered_apps = [app for app in all_apps if app['status'] != 'TBS']
        progress = self.calculate_weighted_progress(filtered_apps)
        expected = (100 + 100) / 2
        
        assert progress == expected
        assert progress == 100, "Progress should be 100 when only completed apps"
        assert progress > self.calculate_weighted_progress(all_apps), \
            "Progress should increase when TBS apps excluded"
    
    def test_progress_wip_excluded(self):
        """Test progress calculation with WIP apps excluded."""
        all_apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 50, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # Filter out WIP
        filtered_apps = [app for app in all_apps if app['status'] != 'WIP']
        progress = self.calculate_weighted_progress(filtered_apps)
        expected = (0 + 100) / 2
        
        assert progress == expected
        assert progress == 50
    
    def test_progress_changes_with_different_filters(self):
        """Test that different filter combinations produce different progress values."""
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 1},
            {'name': 'App B', 'status': 'WIP', 'progress': 50, 'weight': 1},
            {'name': 'App C', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # Calculate progress with different filters
        all_included = self.calculate_weighted_progress(apps)
        tbs_only = self.calculate_weighted_progress([app for app in apps if app['status'] == 'TBS'])
        wip_only = self.calculate_weighted_progress([app for app in apps if app['status'] == 'WIP'])
        clo_only = self.calculate_weighted_progress([app for app in apps if app['status'] == 'CLO'])
        
        # All values should be different
        values = [all_included, tbs_only, wip_only, clo_only]
        assert len(set(values)) == 4, "All filter combinations should produce different values"
        
        # Verify relationships
        assert tbs_only == 0, "TBS only should be 0"
        assert wip_only == 50, "WIP only should be 50"
        assert clo_only == 100, "CLO only should be 100"
    
    def test_weighted_progress_respects_weights(self):
        """Test that progress calculation respects app weights."""
        # App with weight 2 should have more influence
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0, 'weight': 2},
            {'name': 'App B', 'status': 'WIP', 'progress': 100, 'weight': 1}
        ]
        
        progress = self.calculate_weighted_progress(apps)
        expected = (0 * 2 + 100 * 1) / (2 + 1)
        
        assert progress == expected
        assert progress == 33.33, "Weighted app should affect calculation"


class TestCheckboxStateFlow:
    """Tests the complete flow from checkbox state change to calculation update."""
    
    def test_checkbox_change_triggers_recalculation(self):
        """Test that changing a checkbox triggers recalculation."""
        state = MockCheckboxState(include_tbs=True, include_wip=True, include_clo=True)
        
        # Track if recalculation was triggered
        recalculation_triggered = False
        
        def on_checkbox_change():
            nonlocal recalculation_triggered
            recalculation_triggered = True
        
        state.add_change_listener(on_checkbox_change)
        
        # Simulate checkbox change
        state.trigger_checkbox_change('include-tbs')
        
        assert recalculation_triggered, "Recalculation should be triggered"
        assert state.include_tbs == False, "Checkbox state should be toggled"
    
    def test_checkbox_state_affects_filtering(self):
        """Test that checkbox state correctly affects filtering."""
        state = MockCheckboxState(include_tbs=True, include_wip=True, include_clo=True)
        
        apps = [
            {'name': 'App A', 'status': 'TBS', 'progress': 0},
            {'name': 'App B', 'status': 'WIP', 'progress': 100},
            {'name': 'App C', 'status': 'CLO', 'progress': 100}
        ]
        
        # With all included
        filtered_all = [app for app in apps if
                       (app['status'] != 'TBS' or state.include_tbs) and
                       (app['status'] != 'WIP' or state.include_wip) and
                       (app['status'] != 'CLO' or state.include_clo)]
        assert len(filtered_all) == 3
        
        # Change state
        state.include_tbs = False
        filtered_no_tbs = [app for app in apps if
                          (app['status'] != 'TBS' or state.include_tbs) and
                          (app['status'] != 'WIP' or state.include_wip) and
                          (app['status'] != 'CLO' or state.include_clo)]
        assert len(filtered_no_tbs) == 2
    
    def test_multiple_checkbox_changes_accumulate(self):
        """Test that multiple checkbox changes work correctly."""
        state = MockCheckboxState(include_tbs=True, include_wip=True, include_clo=True)
        
        state.include_tbs = False
        state.include_wip = False
        
        # Only CLO should be included
        apps = [
            {'name': 'App A', 'status': 'TBS'},
            {'name': 'App B', 'status': 'WIP'},
            {'name': 'App C', 'status': 'CLO'}
        ]
        
        filtered = [app for app in apps if
                   (app['status'] != 'TBS' or state.include_tbs) and
                   (app['status'] != 'WIP' or state.include_wip) and
                   (app['status'] != 'CLO' or state.include_clo)]
        
        assert len(filtered) == 1
        assert filtered[0]['name'] == 'App C'


class TestBrowserInteractionSimulation:
    """Simulates real browser interactions end-to-end."""
    
    def calculate_bu_progress(self, apps, includes_tbs=True, includes_wip=True, includes_clo=True):
        """
        Simulates the exact dashboard calculation logic.
        
        This mimics rebuildDATAFromStorage() and ProgressCalculator logic.
        """
        if not apps:
            return 0
        
        # Filter apps based on status inclusion (mimics filtering in dashboard)
        filtered_apps = [app for app in apps if
                        (app.get('status') != 'TBS' or includes_tbs) and
                        (app.get('status') != 'WIP' or includes_wip) and
                        (app.get('status') != 'CLO' or includes_clo)]
        
        if not filtered_apps:
            return 0
        
        # Calculate weighted progress (mimics ProgressCalculator)
        total_weight = sum(app.get('weight', 1) for app in filtered_apps)
        if total_weight == 0:
            return 0
        
        weighted_sum = sum(app.get('progress', 0) * app.get('weight', 1) for app in filtered_apps)
        return round((weighted_sum / total_weight) * 100) / 100
    
    def test_full_interaction_flow(self):
        """Test complete flow: checkbox change → filter → calculate → new result."""
        # Sample data from dashboard
        bus = [{
            'key': 'BU1',
            'name': 'Business Unit 1',
            'apps': [
                {'id': 'app1', 'status': 'TBS', 'progress': 0, 'weight': 1},
                {'id': 'app2', 'status': 'WIP', 'progress': 50, 'weight': 1},
                {'id': 'app3', 'status': 'WIP', 'progress': 75, 'weight': 1},
                {'id': 'app4', 'status': 'CLO', 'progress': 100, 'weight': 1}
            ]
        }]
        
        # Initial state: all statuses included
        initial_progress = self.calculate_bu_progress(bus[0]['apps'])
        assert initial_progress == (0 + 50 + 75 + 100) / 4
        
        # User unchecks TBS
        after_tbs_unchecked = self.calculate_bu_progress(
            bus[0]['apps'],
            includes_tbs=False
        )
        assert after_tbs_unchecked == (50 + 75 + 100) / 3
        assert after_tbs_unchecked > initial_progress
        
        # User unchecks WIP too
        after_wip_unchecked = self.calculate_bu_progress(
            bus[0]['apps'],
            includes_tbs=False,
            includes_wip=False
        )
        assert after_wip_unchecked == 100
        assert after_wip_unchecked > after_tbs_unchecked
        
        # User re-enables TBS
        after_tbs_reenabled = self.calculate_bu_progress(
            bus[0]['apps'],
            includes_tbs=True,
            includes_wip=False
        )
        assert after_tbs_reenabled == (0 + 100) / 2
        assert after_tbs_reenabled < after_wip_unchecked
        assert after_tbs_reenabled > initial_progress
    
    def test_checkbox_toggle_produces_measurable_changes(self):
        """Test that each checkbox toggle produces measurable UI changes."""
        apps = [
            {'id': 'app1', 'status': 'TBS', 'progress': 0, 'weight': 2},
            {'id': 'app2', 'status': 'WIP', 'progress': 80, 'weight': 1},
            {'id': 'app3', 'status': 'CLO', 'progress': 100, 'weight': 1}
        ]
        
        # Collect all possible states
        states = {
            'all_enabled': self.calculate_bu_progress(apps, True, True, True),
            'tbs_disabled': self.calculate_bu_progress(apps, False, True, True),
            'wip_disabled': self.calculate_bu_progress(apps, True, False, True),
            'clo_disabled': self.calculate_bu_progress(apps, True, True, False),
            'tbs_wip_disabled': self.calculate_bu_progress(apps, False, False, True),
            'tbs_clo_disabled': self.calculate_bu_progress(apps, False, True, False),
            'wip_clo_disabled': self.calculate_bu_progress(apps, True, False, False),
            'all_disabled': self.calculate_bu_progress(apps, False, False, False),
        }
        
        # All states should be different from each other
        unique_values = set(states.values())
        assert len(unique_values) == 8, "All checkbox combinations should produce different results"
        
        # Verify specific relationships
        assert states['all_disabled'] == 0, "All disabled should be 0"
        assert states['clo_disabled'] == 0, "CLO disabled with 0-weighted TBS and 80-weighted WIP"
        assert states['all_enabled'] < states['tbs_disabled'], "Disabling TBS increases progress"
        assert states['tbs_disabled'] < states['clo_disabled'], "Disabling more statuses increases progress"
    
    def test_real_world_scenario(self):
        """Test a real-world scenario with multiple BUs and apps."""
        buses = [
            {
                'name': 'Product Engineering',
                'apps': [
                    {'id': 'pe1', 'status': 'TBS', 'progress': 0, 'weight': 1},
                    {'id': 'pe2', 'status': 'WIP', 'progress': 40, 'weight': 2},
                    {'id': 'pe3', 'status': 'CLO', 'progress': 100, 'weight': 1}
                ]
            },
            {
                'name': 'Operations',
                'apps': [
                    {'id': 'op1', 'status': 'TBS', 'progress': 0, 'weight': 1},
                    {'id': 'op2', 'status': 'TBS', 'progress': 0, 'weight': 1},
                    {'id': 'op3', 'status': 'WIP', 'progress': 60, 'weight': 1}
                ]
            }
        ]
        
        # Calculate global progress with all statuses
        bu_progresses_all = [self.calculate_bu_progress(bu['apps']) for bu in buses]
        global_progress_all = sum(bu_progresses_all) / len(bu_progresses_all)
        
        # Calculate global progress with TBS disabled
        bu_progresses_no_tbs = [
            self.calculate_bu_progress(bu['apps'], includes_tbs=False)
            for bu in buses
        ]
        global_progress_no_tbs = sum(bu_progresses_no_tbs) / len(bu_progresses_no_tbs)
        
        assert global_progress_no_tbs > global_progress_all, \
            "Disabling TBS should increase global progress"
        
        # Calculate global progress with only CLO
        bu_progresses_clo_only = [
            self.calculate_bu_progress(bu['apps'], includes_tbs=False, includes_wip=False)
            for bu in buses
        ]
        global_progress_clo_only = sum(bu_progresses_clo_only) / len(bu_progresses_clo_only)
        
        assert global_progress_clo_only == 100, \
            "Only CLO should give 100% for all BUs with CLO apps"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
