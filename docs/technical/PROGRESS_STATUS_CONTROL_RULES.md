# 📊 Progress & Status Control Rules - Specification

**Version**: 1.0  
**Date**: October 23, 2025  
**Status**: PENDING USER CONFIRMATION  
**Authority**: User requirements + expert analysis

---

## 🎯 CORE RULES (USER-PROVIDED)

### Rule 1: Initial State
```
Condition: Progress = 0
Result: Status = TBS (automatic, no confirmation)
Trigger: On application creation or when progress reset
```

### Rule 2: Start Activity
```
Condition: Progress = 0 → Progress = X (where X > 0)
Popup: "🚀 Iniciar actividad?"
   Si usuario CANCELA/RECHAZA:
     • No change to Progress
     • No change to Status
     • Return to initial state
   Si usuario CONFIRMA:
     • Update Progress = X
     • Update Status = WIP (automatic)
     • Save to localStorage
     • Re-render table with new values
```

### Rule 3: Reopen Activity
```
Condition: Progress = 100 → Progress = Y (where Y < 100)
Popup: "🔄 Volver a abrir actividad?"
   Si usuario CANCELA/RECHAZA:
     • No change to Progress
     • No change to Status
     • Remain at Progress = 100
   Si usuario CONFIRMA:
     • Update Progress = Y
     • Update Status = WIP (automatic)
     • Save to localStorage
     • Re-render table with new values
```

### Rule 4: Reset to Zero
```
Condition: Progress = X (where X > 0) → Progress = 0
Popup: "⚠️ ¿Volver a poner la actividad en ceros?"
   Si usuario CANCELA/RECHAZA:
     • No change to Progress
     • No change to Status
     • Retain current Progress value
   Si usuario CONFIRMA:
     • Update Progress = 0
     • Update Status = TBS (automatic)
     • Save to localStorage
     • Re-render table with new values
```

---

## 🔧 IMPLEMENTATION DETAILS

### Status Auto-Calculation Logic

```javascript
function calculateStatusFromProgress(progress) {
  if (progress === 0) return 'TBS';           // To Be Started
  if (progress === 100) return 'CLO';         // Completed
  if (0 < progress < 100) return 'WIP';       // Work In Progress
  return 'INVALID';                            // Error state
}
```

### Progress Transition Detection

```javascript
function getTransitionType(oldProgress, newProgress) {
  // No change
  if (oldProgress === newProgress) return 'NONE';
  
  // Critical transitions (require popup)
  if (oldProgress === 0 && newProgress > 0) return 'START';
  if (oldProgress === 100 && newProgress < 100) return 'REOPEN';
  if (oldProgress > 0 && newProgress === 0) return 'RESET';
  
  // Intermediate transitions (no popup)
  if (oldProgress > 0 && oldProgress < 100 && 
      newProgress > 0 && newProgress < 100) return 'UPDATE';
  
  // Invalid transitions
  return 'INVALID';
}
```

### Input Validation

```javascript
function validateProgressInput(value) {
  // Check type
  if (typeof value !== 'number') return { valid: false, error: 'Progress debe ser número' };
  
  // Check range
  if (value < 0 || value > 100) return { valid: false, error: 'Progress debe estar entre 0 y 100' };
  
  // Check for NaN
  if (isNaN(value)) return { valid: false, error: 'Progress inválido' };
  
  // Valid
  return { valid: true, error: null };
}
```

---

## 🎪 POPUP FLOW DIAGRAM

```
User edits Progress cell
        ↓
Validate input (0-100, numeric)
        ↓ INVALID
    Show error
    No changes
        ↓ VALID
Detect transition type
        ↓
    NONE/UPDATE          CRITICAL (START/REOPEN/RESET)
    (No popup)           (Show popup)
        ↓                     ↓
Direct apply        Show confirmation dialog
Auto-calc Status    Wait for user response
Save & re-render         ↓
                    CANCEL        CONFIRM
                      ↓              ↓
                   Dismiss      Apply changes
                   No changes   Auto-calc Status
                              Save & re-render
```

---

## 💾 DATA FLOW - COMPLETE SEQUENCE

### Scenario: User changes Progress 0 → 25

```
1. User clicks Progress cell
   → Enters edit mode
   
2. User types "25" and presses Enter
   → Input event triggered
   
3. validateProgressInput(25)
   → { valid: true }
   
4. getTransitionType(0, 25)
   → 'START'
   
5. Show popup: "🚀 Iniciar actividad?"
   
6. User clicks "Confirmar"
   → onProgressConfirmed(25)
   
7. oldStatus = 'TBS'
   newProgress = 25
   newStatus = calculateStatusFromProgress(25) = 'WIP'
   
8. Update app object:
   {
     ...app,
     progress: 25,
     status: 'WIP',
     updatedAt: new Date().toISOString()
   }
   
9. StorageManager.updateApp(app)
   → Save to localStorage
   
10. UIController.apply()
    → Re-render table
    
11. Popup closes
    Progress cell shows: 25
    Status cell shows: 🔄 In Progress
```

### Scenario: User changes Progress 50 → 75 (Intermediate)

```
1. User enters "75"
   → Input event triggered
   
2. validateProgressInput(75)
   → { valid: true }
   
3. getTransitionType(50, 75)
   → 'UPDATE' (no popup needed)
   
4. Direct apply:
   newStatus = calculateStatusFromProgress(75) = 'WIP'
   
5. Update app:
   { ...app, progress: 75, status: 'WIP' }
   
6. StorageManager.updateApp(app)
   → Save
   
7. UIController.apply()
   → Re-render immediately
   
(No popup shown - user sees change instantly)
```

---

## 🚨 EDGE CASES & HANDLING

### Edge Case 1: Progress = 0.0001
```
Condition: User enters 0.0001
Flow:
  validateProgressInput(0.0001) → valid
  getTransitionType(0, 0.0001) → 'START'
  Show popup
  
Recommendation: Allow decimals, but round to 2 places for display
```

### Edge Case 2: Progress = 99.5 → 100
```
Condition: User enters 100 from 99.5
Flow:
  getTransitionType(99.5, 100) → 'UPDATE' (not REOPEN)
  No popup
  newStatus = 'CLO'
  
This makes sense: user is completing the activity
```

### Edge Case 3: Progress = 100, user tries to set to 100
```
Condition: Redundant change
Flow:
  getTransitionType(100, 100) → 'NONE'
  Ignore silently (no popup, no changes)
  
Best practice: Show toast "Ya estaba en 100%"
```

### Edge Case 4: Rapid clicks on Progress cell
```
Condition: User clicks and edits multiple times
Recommendation: 
  • Debounce input (300ms) before showing popup
  • Lock cell while popup is open
  • Prevent multiple popups
```

### Edge Case 5: Progress with decimals
```
Current: 50.333...
User enters: 75.5
Flow:
  Validate: valid
  Save: 75.5 (preserve decimal)
  Display: "75.50%" or "75.5%" (user preference)
  
Recommendation: Store as decimal, display with 1-2 decimal places
```

---

## 📱 UI REQUIREMENTS

### Progress Input Cell

```html
<td contenteditable="true" class="progress-cell">
  <!-- Initial state -->
  50%
  
  <!-- Edit state -->
  <input type="number" min="0" max="100" step="0.1" value="50" />
  
  <!-- Validation error -->
  <span class="error">Progress debe ser número entre 0-100</span>
</td>
```

### Confirmation Popups

```
POPUP 1: Start Activity
Title: 🚀 Iniciar Actividad
Message: ¿Cambiar status a "En Progreso" (WIP)?
Buttons: [Cancelar] [Confirmar]

POPUP 2: Reopen Activity
Title: 🔄 Volver a Abrir
Message: ¿Cambiar status a "En Progreso" desde "Completado"?
Buttons: [Cancelar] [Confirmar]

POPUP 3: Reset to Zero
Title: ⚠️ Restablecer Actividad
Message: ¿Volver a poner todo a ceros? (Status → "No Iniciado")
Buttons: [Cancelar] [Confirmar]

TOAST (success):
Message: ✅ Actividad actualizada correctamente
Duration: 3 seconds
```

---

## 🔒 VALIDATION RULES (COMPREHENSIVE)

### Input Validation
```
✓ Numeric value only (no text)
✓ Range: 0 ≤ value ≤ 100
✓ Decimals allowed: 0.1, 50.5, 99.9 ← all valid
✗ NaN, null, undefined ← reject
✗ Negative numbers ← reject
✗ > 100 ← reject
✗ Text input ← reject
```

### Permission Validation
```
✓ Admin can change any app's progress
✗ Regular user cannot change progress
(Implement role-based checks)
```

### Application State Validation
```
✓ Application exists in localStorage
✗ Application not found ← show error
✓ Application not locked ← allow edit
✗ Application locked by other user ← show warning
```

---

## 🧪 TEST CASES

### Test 1: Progress 0 → 50 (START)
```
Given: App with Progress = 0, Status = TBS
When: User changes Progress to 50
Then: 
  ✓ Popup shown: "Iniciar actividad?"
  ✓ User confirms
  ✓ Progress = 50
  ✓ Status = WIP
  ✓ Data saved
  ✓ Table re-rendered
```

### Test 2: Progress 50 → 75 (UPDATE)
```
Given: App with Progress = 50, Status = WIP
When: User changes Progress to 75
Then:
  ✓ NO popup
  ✓ Progress = 75 immediately
  ✓ Status = WIP
  ✓ Data saved
  ✓ Table re-rendered
```

### Test 3: Progress 100 → 50 (REOPEN)
```
Given: App with Progress = 100, Status = CLO
When: User changes Progress to 50
Then:
  ✓ Popup shown: "Volver a abrir?"
  ✓ User confirms
  ✓ Progress = 50
  ✓ Status = WIP
  ✓ Data saved
```

### Test 4: Progress 50 → 0 (RESET)
```
Given: App with Progress = 50, Status = WIP
When: User changes Progress to 0
Then:
  ✓ Popup shown: "Volver a poner en ceros?"
  ✓ User confirms
  ✓ Progress = 0
  ✓ Status = TBS
  ✓ Data saved
```

### Test 5: Cancel Popup
```
Given: App with Progress = 0
When: User changes to 50 and clicks Cancel
Then:
  ✓ Progress remains = 0
  ✓ Status remains = TBS
  ✓ No data saved
  ✓ Table unchanged
```

### Test 6: Invalid Input
```
Given: Progress cell active
When: User enters "abc" or "-50" or "150"
Then:
  ✓ Error message shown
  ✓ No popup
  ✓ No changes
  ✓ Cell returns to original value
```

---

## ⚠️ QUESTIONS FOR USER CONFIRMATION

Before implementation, confirm:

1. **Decimals:** ¿Aceptar Progress con decimales (50.5) o solo enteros (0-100)?
2. **Status at 100:** ¿Cuando Progress = 100, STATUS automáticamente CLO? ¿O user confirma?
3. **Intermediate updates:** ¿50→75 sin popup es correcto?
4. **Error handling:** ¿Mostrar error message en popup o en toast?
5. **Permissions:** ¿Solo admin puede cambiar Progress?
6. **Display precision:** ¿Mostrar 1 decimal (50.5%) o 2 (50.50%)?
7. **Timestamps:** ¿Guardar `updatedAt` cuando Progress cambia?

---

**Status: AWAITING USER CONFIRMATION OF EDGE CASES AND PREFERENCES**
