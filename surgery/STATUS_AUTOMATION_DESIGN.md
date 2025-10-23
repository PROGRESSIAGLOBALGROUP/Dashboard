# Status Automation Implementation Design

## Overview
Replace manual status selection with intelligent automation based on progress percentage.

## State Machine Logic

```
Progress Value Change Event
        ↓
    ┌─────────────────────┐
    │ Check old vs new    │
    └─────────────────────┘
        ↓
    ├─ Old=0, New=0 → TBS (no action)
    │
    ├─ Old≠0, New=0 → TBS (auto, no modal)
    │
    ├─ Old=0, New∈[1-99] → SHOW "Start Application?" Modal
    │       ├─ YES → Set status=WIP, save, refresh
    │       └─ NO  → Revert progress to 0
    │
    ├─ Old∈[1-99], New∈[1-99] → WIP (no change)
    │
    ├─ Old∈[1-99], New=100 → SHOW "Mark as Complete?" Modal
    │       ├─ YES → Set status=CLO, save, refresh
    │       └─ NO  → Revert progress to old value
    │
    └─ Old=100 → CLO (no change)
```

## New Functions in AdminController

### 1. progressChangeHandler(appId, newProgress, oldProgress)
**Purpose:** Intercept progress input changes and apply state machine logic
**Logic:**
- Normalize values (0-100)
- Detect state transition boundary
- Call appropriate handler (none/auto/modal)

### 2. showStatusConfirmation(appId, type, newProgress)
**Purpose:** Display modal for user confirmation
**Params:**
- `type`: 'start' | 'complete'
- `appId`: ID of application
- `newProgress`: New progress value
**Returns:** Promise that resolves to true/false

### 3. handleStatusTransition(appId, newStatus, newProgress)
**Purpose:** Update app with new status and progress
**Actions:**
- StorageManager.updateApp(appId, {status: newStatus, progress: newProgress})
- renderAppsEditor() to refresh UI
- UIController.apply() to refresh main dashboard

## New HTML Modal

```html
<div id="statusConfirmationModal" class="nested-modal">
  <div class="nested-modal-content">
    <h3 id="confirmTitle">Confirm Status Change</h3>
    <p id="confirmMessage"></p>
    <div style="display:flex;gap:12px;margin-top:24px">
      <button id="confirmYes" class="btn btn-primary">Yes, Proceed</button>
      <button id="confirmNo" class="btn btn-secondary">Cancel</button>
    </div>
  </div>
</div>
```

## Implementation Steps

1. **Update HTML Table in renderAppsEditor():**
   - Change progress input onchange from direct updateApp() to progressChangeHandler()
   - Store current value in data attribute for comparison

2. **Add Helper Functions to AdminController:**
   - progressChangeHandler(appId, newProgress, oldProgress)
   - showStatusConfirmation(appId, type, newProgress)
   - handleStatusTransition(appId, newStatus, newProgress)

3. **Add Modal HTML:**
   - Insert statusConfirmationModal div in admin modal

4. **Add Modal CSS (if needed):**
   - Use existing nested-modal styles

## Edge Cases Handled
- User cancels progress input → revert to previous value
- User sets progress back to 0 → auto TBS without confirmation
- Rapid clicks on confirmation buttons → debounce/disable
- Page refresh during confirmation → state recovers from localStorage

## Files to Modify
- `dist/dashboard_enhanced.html`:
  - renderAppsEditor() function
  - AdminController object (add 3 functions)
  - HTML modal structure
