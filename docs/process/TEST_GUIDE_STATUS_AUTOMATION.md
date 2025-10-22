# STATUS AUTOMATION - MANUAL TEST GUIDE

## Quick Start Testing

### Step 1: Open Dashboard
- Open `dist/dashboard_enhanced.html` in your web browser
- Click the **⚙️ Setup Admin** button (top right)
- Navigate to **Applications** tab
- Select any **Business Unit**

### Step 2: Test Scenario 1 - Start Application

**Initial State:**
- App Name: Any existing application at 0% / TBS

**Action:**
1. Click the Progress % input field
2. Enter: `50`
3. Press Tab or click outside

**Expected Result:**
- Modal appears with title: "🚀 Start Application?"
- Message: "Ready to start '[APP_NAME]'? This will change status from TBS to WIP."
- Two buttons: "Yes, Proceed" and "Cancel"

**If YES clicked:**
- Modal closes
- Status column changes to "🚧 WIP"
- Progress shows "50"
- localStorage updates automatically

**If NO/Cancel clicked:**
- Modal closes without changes
- Progress input reverts to "0"
- Status stays "🔜 TBS"

---

### Step 3: Test Scenario 2 - Mark as Complete

**Initial State:**
- Same app from Scenario 1, now at 50% / WIP

**Action:**
1. Click the Progress % input field
2. Enter: `100`
3. Press Tab or click outside

**Expected Result:**
- Modal appears with title: "✅ Mark as Complete?"
- Message: "Ready to mark '[APP_NAME]' as complete? This will change status from WIP to CLO."
- Two buttons: "Yes, Proceed" and "Cancel"

**If YES clicked:**
- Modal closes
- Status column changes to "✅ CLO"
- Progress shows "100"
- localStorage updates automatically

**If NO/Cancel clicked:**
- Modal closes without changes
- Progress input reverts to "50"
- Status stays "🚧 WIP"

---

### Step 4: Test Scenario 3 - Reset to TBS

**Initial State:**
- Same app from Scenario 2, now at 100% / CLO

**Action:**
1. Click the Progress % input field
2. Enter: `0`
3. Press Tab or click outside

**Expected Result:**
- NO MODAL appears (automatic reset)
- Status column changes immediately to "🔜 TBS"
- Progress shows "0"
- localStorage updates automatically

---

### Step 5: Verify localStorage

**Action:**
1. Open Developer Tools: F12
2. Go to Console tab
3. Paste this code:
```javascript
Dashboard.StorageManager.loadConfig()
```

**Expected Result:**
- Look for the app you tested
- Verify `status` matches what you set (WIP, CLO, or TBS)
- Verify `progress` matches what you set (50, 100, or 0)

---

## Browser Console Testing (Advanced)

If modal doesn't appear, debug with:

```javascript
// Check if modal element exists
console.log(document.getElementById('statusConfirmationModal'));

// Check if function exists
console.log(Dashboard.AdminController.progressChangeHandler);

// Manually trigger handler
Dashboard.AdminController.progressChangeHandler(
  1,  // appId (first app)
  50, // new progress
  0   // old progress
);
```

---

## Expected Behavior Summary

| Action | Old State | Modal? | New State |
|--------|-----------|--------|-----------|
| Progress 0→50 | TBS | YES | WIP |
| Progress 50→100 | WIP | YES | CLO |
| Progress 100→50 | CLO | NO | CLO/WIP |
| Progress any→0 | Any | NO | TBS |
| Cancel modal | Any | YES | Reverted |

---

## Troubleshooting

### Modal doesn't appear
- Check browser console for errors: F12 → Console
- Verify Admin Modal is open
- Verify Business Unit is selected

### Status doesn't change
- Check that YES button was clicked
- Open localStorage to verify changes saved
- Refresh page and check if changes persisted

### Progress reverts unexpectedly
- This is expected when clicking NO/Cancel
- Changes only persist when user clicks YES

### localStorage changes not visible
- Refresh the page (F5)
- Close and reopen the Admin Modal
- Check `Dashboard.StorageManager.loadConfig()` in console

---

## Success Criteria

✅ **Test Passed If:**
- Modal appears with correct messages
- Status updates when YES clicked
- Progress updates when YES clicked
- Changes persist after page refresh
- NO/Cancel reverts input correctly
- TBS reset happens automatically without modal

✅ **All tests completed:** Implementation is SUCCESSFUL

---

## Final Verification

After testing, run this in browser console:

```javascript
// Load all apps
const apps = Dashboard.StorageManager.getAllApps();

// Check app statuses
apps.forEach(app => {
  console.log(`${app.name}: ${app.status} (${app.progress}%)`);
});

// If all statuses match your tests, you're good to go!
```

---

**Test Date:** _____________  
**Tester Name:** _____________  
**Result:** ⭕ PASS | ⭕ FAIL  
**Notes:** _______________________________

---

Questions? Open `IMPLEMENTATION_STATUS_AUTOMATION_COMPLETE.md` for full technical details.
