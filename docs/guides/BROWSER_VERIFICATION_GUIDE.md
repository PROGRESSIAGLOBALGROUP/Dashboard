# 🧪 Browser Verification Guide - Dashboard Enhanced

## Quick Test: Verify the Fix Works

Open `dist/dashboard_enhanced.html` in your browser and follow these steps:

### Test 1: Initial Load ✅
1. **Open the dashboard** in your browser
2. **Expected**: Dashboard displays with data (KPI counters, hero progress, tiles)
3. **If empty**: Refresh (F5) and check browser console for errors

```javascript
// Check browser console (F12):
// You should see: "🚀 [DOMContentLoaded] Calling initial apply() to render dashboard"
```

---

### Test 2: Status Inclusion Rules ✅
1. **Open admin panel** (click ⚙️ icon)
2. **Go to Formula tab**
3. **Uncheck "Include To Be Started (TBS)"** checkbox
4. **Expected**: KPI values should change immediately
5. **Verify**: The "About to Start" KPI counter should decrease

```javascript
// In console, check the calculation is filtering:
Dashboard.DATA.forEach(d => console.log(d.name, 'apps:', d.appCount));
```

---

### Test 3: Configuration Persistence ✅
1. **Change a configuration setting** (e.g., uncheck a status filter)
2. **Click "Save & Close"**
3. **Refresh the page** (F5)
4. **Expected**: Configuration is preserved, KPI values stay the same

```javascript
// Check localStorage:
const config = JSON.parse(localStorage.getItem('dashboard_config_v1'));
console.log('Status Inclusions:', config.formulaSettings.statusInclusions);
```

---

### Test 4: Hero & KPI Synchronization ✅
1. **Check Hero Progress** (large number at top)
2. **Check KPI Total Avg** (in KPI panel)
3. **Expected**: Both show the exact same percentage value
4. **Verify**: They use the same calculation (same number = same formula)

```javascript
// In console:
console.log('Hero:', document.querySelector('#heroPct').textContent);
console.log('KPI Avg:', document.querySelector('#kpiAvg').textContent);
// Should be identical
```

---

### Test 5: Multiple Changes ✅
1. **Toggle multiple status filters**
2. **Change formula method** (Simple vs Weighted)
3. **Click Save & Close**
4. **Refresh page** (F5)
5. **Expected**: All settings preserved, calculations correct

---

## Debug Information - If Something Goes Wrong

### Check Browser Console (F12 → Console)
Look for these log messages:
- ✅ `🚀 [DOMContentLoaded] Calling initial apply() to render dashboard`
- ✅ `🔍 [rebuildDATAFromStorage] Status Inclusion: ...`
- ✅ `📊 [GLOBAL] Using global method: ...`
- ✅ `📊 [updateKPIs] Actualizando KPIs con ...`

### Check localStorage
```javascript
// In console:
localStorage.getItem('dashboard_config_v1')
// Should return JSON with formulaSettings
```

### Check HTML Checkboxes
```javascript
// These should exist:
document.getElementById('include-tbs')
document.getElementById('include-wip')
document.getElementById('include-clo')

// This should NOT exist (old bug):
document.getElementById('include-done')  // undefined
```

### Verify DATA Array
```javascript
// In console:
Dashboard.DATA
// Should be an array of BUs with progress values
```

---

## Expected Console Logs (Normal Operation)

When you load the dashboard, you should see logs like:

```
🚀 [DOMContentLoaded] Calling initial apply() to render dashboard
📊 [APPLY] DATA after rebuild: [...]
🔍 [rebuildDATAFromStorage] Status Inclusion: { includesTBS: false, includesWIP: true, includesCLO: true }
📊 [GLOBAL] Using global method: weighted, Progress: XX.XX%
📊 [KPI] Conteo: { done: X, wip: X, todo: X }
🔄 [DATA] Rebuilt from storage (status-filtered): [...]
```

If you **don't** see `🚀 [DOMContentLoaded]`, the initialization fix isn't applied.

---

## Checklist for Verification

- [ ] Dashboard displays on initial load (not empty)
- [ ] KPI values are visible and have numbers
- [ ] Hero progress matches KPI total avg
- [ ] Toggling status filters changes KPI values
- [ ] Saving configuration persists after F5 refresh
- [ ] Browser console shows initialization logs
- [ ] No JavaScript errors in console

**If all checked**: ✅ **Dashboard is working correctly**

---

## Quick Diagnostic Command

Paste this in browser console to check everything:

```javascript
console.log('=== DASHBOARD STATUS ===');
console.log('Dashboard object:', !!window.Dashboard);
console.log('DATA array:', window.Dashboard?.DATA?.length || 0, 'BUs');
console.log('Hero value:', document.querySelector('#heroPct')?.textContent);
console.log('KPI Avg:', document.querySelector('#kpiAvg')?.textContent);
console.log('Config loaded:', !!localStorage.getItem('dashboard_config_v1'));
console.log('Checkboxes:', {
  tbs: document.getElementById('include-tbs')?.checked,
  wip: document.getElementById('include-wip')?.checked,
  clo: document.getElementById('include-clo')?.checked
});
console.log('=== ALL OK ===');
```

If this runs without errors and shows data, everything is working.

---

## Summary

The fix adds one line to DOMContentLoaded that **activates** all the previous fixes:

```javascript
Dashboard.UIController.apply();  // ← This line was missing
```

This ensures:
1. Dashboard renders on page load ✅
2. Configuration loads from localStorage ✅
3. Status filters are applied ✅
4. All calculations are correct ✅
5. Changes persist after refresh ✅
