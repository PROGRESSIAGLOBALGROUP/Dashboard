# 📊 PROGRESS & STATUS CONTROL - SPECIFICATION FINAL v2.0

**Date**: October 23, 2025  
**Version**: 2.0 (Final, User-Confirmed)  
**Status**: READY FOR CODE_SURGEON IMPLEMENTATION  
**Author**: User Requirements + Technical Analysis

---

## ✅ USER CONFIRMATIONS (BINDING)

| Question | Answer | Impact |
|----------|--------|--------|
| Decimales en Progress | ❌ NO - Solo 1-100 enteros | Input validation: rechazar 50.5, 99.9 |
| Confirmación en 100% | ✅ SÍ + Popup celebración | 2 popups: START y COMPLETION |
| Popup para updates intermedios | ❌ NO - Solo en límites | 50→75 sin popup, directo |
| Control de roles | 🔓 Sin roles - Cualquiera puede | Leader de BU edita su módulo, exporta JSON |
| Precisión display | 🔢 Individuales: X.XX% / Principal: X% | Conditional formatting en render |
| Timestamp (updatedAt) | ✅ SÍ - Crítico para audit | Guardar con cada cambio |
| Excepciones TBS (0%) | ❌ NINGUNA - Siempre TBS | Si Progress=0 → Status=TBS sin excepciones |

---

## 🎯 CORE RULES (CONFIRMED & FINAL)

### Rule 1: Initial State (NO POPUP)
```
IF Progress = 0
  THEN Status = TBS
  AND NO popup shown
  AND automatic state
  
Trigger: On creation OR after user confirms reset
```

### Rule 2: Start Activity (POPUP + Confirmation)
```
IF Progress = 0 → Progress = X (where 1 ≤ X ≤ 100)
  THEN Show popup: "🚀 Start Activity?"
  
  IF User confirms:
    • Set Progress = X
    • Set Status = WIP
    • Save updatedAt = NOW
    • Save to localStorage
    • Re-render table
    
  IF User cancels:
    • Restore Progress = 0
    • Restore Status = TBS
    • No changes saved
```

### Rule 3: Complete Activity (POPUP + Celebration 🎉)
```
IF Progress = X (where 0 < X < 100) → Progress = 100
  THEN Show popup: "🎉 Congratulations! Task Completed!"
  
  IF User confirms:
    • Set Progress = 100
    • Set Status = CLO
    • Show celebration animation
    • Save updatedAt = NOW
    • Save to localStorage
    • Re-render table
    
  IF User cancels:
    • Restore previous Progress
    • Restore previous Status
    • No changes saved
    
NOTE: This includes 99→100, not just smaller values
```

### Rule 4: Reopen Activity (POPUP + Sadness 😢)
```
IF Progress = 100 → Progress = Y (where Y < 100)
  THEN Show popup: "😢 Reopening Completed Task?"
  
  IF User confirms:
    • Set Progress = Y
    • Set Status = WIP
    • Save updatedAt = NOW
    • Save to localStorage
    • Re-render table
    
  IF User cancels:
    • Restore Progress = 100
    • Restore Status = CLO
    • No changes saved
```

### Rule 5: Reset to Zero (POPUP + Confirmation)
```
IF Progress = X (where X > 0) → Progress = 0
  THEN Show popup: "⚠️ Reset Activity to Zero?"
  
  IF User confirms:
    • Set Progress = 0
    • Set Status = TBS
    • Save updatedAt = NOW
    • Save to localStorage
    • Re-render table
    
  IF User cancels:
    • Restore Progress = X
    • Restore Status = (previous)
    • No changes saved
```

### Rule 6: Intermediate Updates (NO POPUP - Direct Apply)
```
IF Progress = X AND (0 < X < 100) → Progress = Y AND (0 < Y < 100)
  THEN:
    • NO popup shown
    • Directly update Progress = Y
    • Status remains WIP
    • Save updatedAt = NOW
    • Save to localStorage
    • Re-render table immediately
    
Example: 25→50, 50→75, 99→98 ← All direct, no confirmation
```

---

## 🔧 TRANSITION DETECTION LOGIC

```javascript
function detectProgressTransition(oldProgress, newProgress) {
  // Validation first
  if (!isValidProgressValue(newProgress)) {
    return { type: 'INVALID', requiresPopup: true };
  }
  
  // No change
  if (oldProgress === newProgress) {
    return { type: 'NONE', requiresPopup: false };
  }
  
  // START: 0 → X (where 0 < X ≤ 100)
  if (oldProgress === 0 && newProgress > 0) {
    return { type: 'START', requiresPopup: true };
  }
  
  // COMPLETION: X → 100 (where 0 < X < 100)
  if (oldProgress < 100 && newProgress === 100) {
    return { type: 'COMPLETION', requiresPopup: true, celebration: true };
  }
  
  // REOPEN: 100 → Y (where Y < 100)
  if (oldProgress === 100 && newProgress < 100) {
    return { type: 'REOPEN', requiresPopup: true, sadness: true };
  }
  
  // RESET: X → 0 (where X > 0)
  if (oldProgress > 0 && newProgress === 0) {
    return { type: 'RESET', requiresPopup: true };
  }
  
  // INTERMEDIATE: X → Y (both between 0 and 100, exclusive)
  if (oldProgress > 0 && oldProgress < 100 && newProgress > 0 && newProgress < 100) {
    return { type: 'UPDATE', requiresPopup: false };
  }
  
  // Unknown transition
  return { type: 'INVALID', requiresPopup: true };
}

function isValidProgressValue(value) {
  // Must be integer 0-100
  if (typeof value !== 'number') return false;
  if (!Number.isInteger(value)) return false;  // Reject decimals
  if (value < 0 || value > 100) return false;
  if (isNaN(value)) return false;
  return true;
}

function calculateStatusFromProgress(progress) {
  if (progress === 0) return 'TBS';         // To Be Started
  if (0 < progress && progress < 100) return 'WIP';  // Work In Progress
  if (progress === 100) return 'CLO';       // Completed
  return 'INVALID';
}
```

---

## 📱 POPUP SPECIFICATIONS

### POPUP 1: "Start Activity" (Green Theme)
```
Title: 🚀 Start Activity
Subtitle: You're about to begin this task
Message: "Change status from 'To Be Started' to 'In Progress'?"

Buttons:
  [Cancel]      [Start Task] ← Primary/Green
  
On Cancel:
  → Close popup
  → Progress remains 0
  → Status remains TBS
  
On Confirm:
  → Close popup
  → Set Progress = newValue
  → Set Status = WIP
  → Show toast: "✅ Task started!"
  → Re-render
```

### POPUP 2: "Complete Task" (Gold/Celebration Theme) 🎉
```
Title: 🎉 Congratulations!
Subtitle: You've completed this task!
Message: "Change status from 'In Progress' to 'Completed'?"

Visual Feedback:
  • Celebration animation (confetti, fireworks)
  • Gold/bright yellow theme
  • Trophy emoji 🏆
  • Uplifting sound (optional)

Buttons:
  [Cancel]           [Celebrate & Complete] ← Primary/Gold
  
On Cancel:
  → Close popup
  → Progress remains previous
  → Status remains WIP
  
On Confirm:
  → Close popup
  → Set Progress = 100
  → Set Status = CLO
  → Show celebration animation (3-5 seconds)
  → Show toast: "🏆 Task completed! Great job!"
  → Re-render table with task highlighted
  
Post-Completion:
  → Task row shows as "COMPLETED" styling
  → Progress bar shows 100% in green
  → Status badge shows "✅ Completed"
```

### POPUP 3: "Reopen Task" (Gray/Sad Theme) 😢
```
Title: 😢 Reopening Completed Task
Subtitle: This task was marked as completed
Message: "Are you sure? This will change status back to 'In Progress'."

Visual Feedback:
  • Gray/muted theme
  • Sad emoji 😢
  • Subtle animation (not celebratory)

Buttons:
  [Keep as Completed]    [Reopen Task] ← Primary/Gray
  
On Cancel:
  → Close popup
  → Progress remains 100
  → Status remains CLO
  
On Confirm:
  → Close popup
  → Set Progress = newValue
  → Set Status = WIP
  → Show toast: "↩️ Task reopened"
  → Re-render table
  
Post-Reopen:
  → Task row returns to normal styling
  → Progress bar shows new percentage
  → Status badge shows "🔄 In Progress"
```

### POPUP 4: "Reset to Zero" (Warning Theme) ⚠️
```
Title: ⚠️ Reset Activity to Zero
Subtitle: This will mark as "Not Started"
Message: "This action will remove all progress. Continue?"

Visual Feedback:
  • Warning/orange theme
  • Warning emoji ⚠️
  • Emphasize: all progress will be lost

Buttons:
  [Keep Progress]        [Reset to Zero] ← Primary/Orange
  
On Cancel:
  → Close popup
  → Progress remains previous
  → Status remains previous
  
On Confirm:
  → Close popup
  → Set Progress = 0
  → Set Status = TBS
  → Show toast: "🔄 Activity reset to zero"
  → Re-render table
```

---

## 💾 DATA PERSISTENCE

### Update Flow (Every Change)
```
1. User modifies Progress cell
2. Validate input (0-100, integer)
3. Detect transition type
4. IF requires popup:
     → Show popup
     → Wait for user response
     → IF cancel: abort
     → IF confirm: proceed
5. Create updated app object:
   {
     ...app,
     progress: newProgress,
     status: newStatus,
     updatedAt: new Date().toISOString(),
     updatedBy: "Local Edit"  // or get from context
   }
6. StorageManager.updateApp(updatedApp)
7. Save to localStorage['dashboard_config_v1']
8. Audit log entry (separate export flow)
9. UIController.apply()
10. Re-render affected rows
11. Show success toast
```

### Timestamp Format
```
ISO 8601 Standard:
  "2025-10-23T14:30:45.123Z"
  
Stored in app object:
  app.updatedAt = "2025-10-23T14:30:45.123Z"
  
Display format (when needed):
  "Oct 23, 2:30 PM"
  
Audit log (exported separately):
  • app.id
  • app.name
  • oldProgress
  • newProgress
  • oldStatus
  • newStatus
  • updatedAt
  • action: "progress_changed"
```

---

## 🎨 DISPLAY PRECISION RULES

### Individual Metrics (Progress Cells)
```
Display format: X.XX%
Examples:
  0 → "0.00%"
  1 → "1.00%"
  50 → "50.00%"
  99 → "99.00%"
  100 → "100.00%"
  
Color coding:
  0% → Red (#ff5f7a) - TBS
  1-99% → Yellow (#ffd166) - WIP
  100% → Green (#32e685) - CLO
```

### Main/Primary Indicator (KPI)
```
Display format: X%
Examples:
  0 → "0%"
  1 → "1%"
  50 → "50%"
  99 → "99%"
  100 → "100%"
  
Color coding: Same as individual
```

### Implementation
```javascript
function formatProgressDisplay(progress, isMainIndicator = false) {
  if (isMainIndicator) {
    // Main KPI: "50%"
    return `${progress}%`;
  } else {
    // Individual: "50.00%"
    return `${progress.toFixed(2)}%`;
  }
}

function getProgressColor(progress) {
  if (progress === 0) return '#ff5f7a';      // Red - TBS
  if (progress === 100) return '#32e685';    // Green - CLO
  if (0 < progress && progress < 100) return '#ffd166';  // Yellow - WIP
  return '#999999';  // Gray - invalid
}
```

---

## 🏗️ IMPLEMENTATION ARCHITECTURE

### Modified Module: AdminPanel.js (approx lines)
```
New methods to add:
  • onProgressEdit(app, newValue)
  • validateProgressInput(value)
  • showProgressPopup(type, oldProgress, newProgress, app)
  • confirmProgressChange(app, newProgress, transitionType)
  • updateAppProgress(app, newProgress, newStatus)
  
Modified methods:
  • renderApplicationsTable() - Add event listeners
  • refreshApplicationsView() - Re-render with new data
```

### Modified Module: UIController.js
```
New methods:
  • showCelebration() - Celebration animation for completion
  • showSadness() - Sad animation for reopen
  • showToast(message, duration) - Toast notifications
  
Modified methods:
  • color(progress) - Already exists, verify works
  • render() - Apply display precision rules
```

### Modified Module: StorageManager.js
```
New fields in app object:
  • updatedAt: "2025-10-23T14:30:45.123Z"
  • updatedBy: "Local Edit" (or user identifier)
  
Modified methods:
  • updateApp(app) - Save with timestamp
  • saveConfig() - Persist to localStorage
```

---

## 📋 COMPLETE TEST SCENARIOS

### Test 1: START (0 → 50)
```
Given: App with Progress=0, Status=TBS
When: User edits cell, enters 50, presses Enter
Then:
  ✓ Popup shows: "🚀 Start Activity?"
  ✓ User clicks "Start Task"
  ✓ Progress = 50
  ✓ Status = WIP
  ✓ updatedAt set to NOW
  ✓ Toast shows: "✅ Task started!"
  ✓ Table re-renders
  ✓ Progress cell shows "50.00%"
```

### Test 2: COMPLETION (99 → 100)
```
Given: App with Progress=99, Status=WIP
When: User edits cell, enters 100, presses Enter
Then:
  ✓ Popup shows: "🎉 Congratulations! Task Completed!" with celebration
  ✓ User clicks "Celebrate & Complete"
  ✓ Celebration animation plays (3-5 sec)
  ✓ Progress = 100
  ✓ Status = CLO
  ✓ updatedAt set to NOW
  ✓ Toast shows: "🏆 Task completed! Great job!"
  ✓ Table re-renders with CLO styling
  ✓ Progress cell shows "100.00%"
```

### Test 3: UPDATE (50 → 75, no popup)
```
Given: App with Progress=50, Status=WIP
When: User edits cell, enters 75, presses Enter
Then:
  ✓ NO popup shown
  ✓ Progress immediately = 75
  ✓ Status remains WIP
  ✓ updatedAt set to NOW
  ✓ NO toast (silent update)
  ✓ Table re-renders instantly
  ✓ Progress cell shows "75.00%"
```

### Test 4: REOPEN (100 → 50)
```
Given: App with Progress=100, Status=CLO
When: User edits cell, enters 50, presses Enter
Then:
  ✓ Popup shows: "😢 Reopening Completed Task?" with sad emoji
  ✓ User clicks "Reopen Task"
  ✓ Progress = 50
  ✓ Status = WIP
  ✓ updatedAt set to NOW
  ✓ Toast shows: "↩️ Task reopened"
  ✓ Table re-renders with WIP styling
  ✓ Progress cell shows "50.00%"
```

### Test 5: RESET (50 → 0)
```
Given: App with Progress=50, Status=WIP
When: User edits cell, enters 0, presses Enter
Then:
  ✓ Popup shows: "⚠️ Reset Activity to Zero?"
  ✓ User clicks "Reset to Zero"
  ✓ Progress = 0
  ✓ Status = TBS
  ✓ updatedAt set to NOW
  ✓ Toast shows: "🔄 Activity reset to zero"
  ✓ Table re-renders with TBS styling
  ✓ Progress cell shows "0.00%"
```

### Test 6: CANCEL on START
```
Given: App with Progress=0, Status=TBS
When: User enters 50, popup shows, clicks "Cancel"
Then:
  ✓ Popup closes
  ✓ Progress remains 0
  ✓ Status remains TBS
  ✓ NO data saved
  ✓ Table unchanged
```

### Test 7: INVALID INPUT
```
Given: Progress cell active
When: User enters "abc" or "50.5" or "150"
Then:
  ✓ Error shown: "Progress must be integer 0-100"
  ✓ NO popup
  ✓ Cell returns to original value
  ✓ NO changes saved
```

### Test 8: RAPID EDITS
```
Given: Multiple rapid edits
When: User edits, presses Enter, edits again quickly
Then:
  ✓ First popup shows
  ✓ User confirms
  ✓ Changes applied
  ✓ Second edit prevented until re-render completes
  ✓ No data corruption
```

---

## 🚨 EDGE CASES CLARIFIED

### Edge Case 1: Progress 0 → 100 (Skip WIP)
```
Transition type: START (not COMPLETION)
Reason: Not coming FROM WIP, but TO 100 from 0
Popup shown: "🚀 Start Activity?"
After confirmation:
  • Progress = 100
  • Status = CLO (not WIP)
  • NO celebration (only when transition TO 100)
  
Wait... should this trigger COMPLETION celebration?
ANSWER FROM USER: "Al confirmar : Le debemos poner un mensaje de FELICIDADES"
→ YES, if ending at 100, show celebration
→ Clarification needed: Should 0→100 show celebration?
→ ASSUMPTION: Celebration only if TRANSITIONING TO 100 (any from-value)
```

### Edge Case 2: Progress 100 → 100 (Redundant)
```
getTransitionType(100, 100) = 'NONE'
Action: Ignore silently
User sees: No popup, no change
```

### Edge Case 3: Decimal Input (50.5)
```
User enters: 50.5
isValidProgressValue(50.5) = FALSE
Result: Error message "Progress must be integer"
```

### Edge Case 4: Negative Input (-10)
```
User enters: -10
isValidProgressValue(-10) = FALSE
Result: Error message "Progress must be 0-100"
```

### Edge Case 5: Progress > 100 (150)
```
User enters: 150
isValidProgressValue(150) = FALSE
Result: Error message "Progress must be 0-100"
```

### Edge Case 6: Import JSON with decimal
```
Scenario: User imports JSON with Progress: 50.5 from another BU
On import:
  • Validate and round to nearest integer (50 or 51?)
  • OR reject import as invalid
  
RECOMMENDATION: Round to nearest integer
```

---

## 🎯 CELEBRATION & SADNESS ANIMATIONS

### Celebration Animation (On Completion: X → 100)
```
Duration: 3-5 seconds
Effects:
  1. Confetti burst (top of screen)
  2. Trophy emoji 🏆 animation
  3. Progress bar fills with green
  4. Task row highlights in gold
  5. "Congratulations!" message
  
Audio (optional):
  • Cheerful chime or fanfare
  • Volume: user preference
  
After animation:
  • Task row returns to normal CLO styling
  • Celebration automatically stops
  • User can continue working
```

### Sadness Animation (On Reopen: 100 → Y)
```
Duration: 1-2 seconds (shorter, subtle)
Effects:
  1. Task row fades slightly
  2. Sad emoji 😢 appears briefly
  3. Progress bar resets to new percentage
  4. Status returns to WIP styling
  
Audio (optional):
  • Subtle "oh no" sound
  • OR silent
  
After animation:
  • Task row back to normal
  • No lingering effects
```

---

## 🔐 EXCEPTION HANDLING

### What happens if Progress = 0?
```
RULE: If Progress = 0 → Status = TBS (NO EXCEPTIONS)

However, consider:
1. Import scenario: Imported app has Progress=0
   → Status automatically set to TBS
   
2. User creates app with Progress=0
   → Status automatically set to TBS
   
3. User resets app to Progress=0
   → Status automatically set to TBS
   
4. Corrupt data: Progress=0 but Status=WIP in localStorage
   → Validation: Fix on load, set Status=TBS
   
ANSWER: NO EXCEPTIONS. Always Progress=0 → Status=TBS
```

---

## ✅ READY FOR CODE_SURGEON IMPLEMENTATION

**Status**: SPECIFICATION LOCKED AND CONFIRMED

**Next Phase**: Code_surgeon jobs for:
1. **OP1**: AdminPanel.js - Add onProgressEdit() method with validation
2. **OP2**: AdminPanel.js - Add popup handlers (4 types)
3. **OP3**: AdminPanel.js - Modify table rendering with event listeners
4. **OP4**: StorageManager.js - Add updatedAt and updatedBy fields
5. **OP5**: UIController.js - Add celebration/sadness animations
6. **OP6**: UIController.js - Add toast notification system

**Dependencies**: 
- All changes isolated to AdminPanel.js, StorageManager.js, UIController.js
- No breaking changes to existing API
- Backward compatible with current data structure

---

**SPECIFICATION APPROVED AND LOCKED FOR IMPLEMENTATION**

*User confirmations embedded in every rule. Ready for code_surgeon.*
