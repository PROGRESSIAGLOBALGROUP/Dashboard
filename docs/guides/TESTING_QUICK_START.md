# 🧪 TESTING QUICK START

## How to Test the Whitelabel Dynamic Integration

Open this file in your browser:
```
file:///C:/PROYECTOS/Dashboard/dist/dashboard_enhanced.html
```

### Test Sequence (5 minutes)

**BEFORE YOU START**: Clear localStorage first
- Open DevTools (F12)
- Console tab
- Paste: `localStorage.clear(); location.reload();`

---

### ✅ TEST 1: Title Changes Dynamically (No Reload)
```
1. Observe H1 at top: "PROGRESSIA · Discord Project · [ Project Type ]"
2. Click "Setup" button
3. Click "Whitelabel" tab
4. In "Main Title" input, clear and type: "AWESOME PROJECT"
5. Click "Save Whitelabel Config"
6. ✅ VERIFY: H1 at TOP of page now shows "AWESOME PROJECT" 
   (WITHOUT page refresh)
7. Notice the alert confirms save
```

**Expected**: H1 updates instantly ⚡

---

### ✅ TEST 2: Subtitle Changes Dynamically (No Reload)
```
1. In Whitelabel tab, "Subtitle" field
2. Clear and type: "Epic Team Advance"
3. Click "Save Whitelabel Config"
4. ✅ VERIFY: Small text below H1 now shows "Epic Team Advance"
   (WITHOUT page refresh)
```

**Expected**: Subtitle updates instantly ⚡

---

### ✅ TEST 3: Values Persist on Refresh
```
1. Press F5 (refresh page)
2. ✅ VERIFY: H1 still shows "AWESOME PROJECT"
3. ✅ VERIFY: Subtitle still shows "Epic Team Advance"
4. Click "Setup" → "Whitelabel" tab
5. ✅ VERIFY: Form fields are populated with your values
```

**Expected**: All values survive page reload ✅

---

### ✅ TEST 4: Export Contains Whitelabel
```
1. In Admin Panel, click "Settings" tab
2. Click "Export Configuration" button
3. File downloads: dashboard_config_YYYY-MM-DD.json
4. Open with text editor (Notepad)
5. Search for: "whitelabel"
6. ✅ VERIFY: You see this structure:
   ```json
   "whitelabel": {
     "mainTitle": "AWESOME PROJECT",
     "subtitle": "Epic Team Advance",
     "leftLogo": null,
     "rightLogo": null
   }
   ```
```

**Expected**: Whitelabel object in JSON ✅

---

### ✅ TEST 5: Import Restores Whitelabel
```
1. In Whitelabel tab, click "Reset to Defaults"
2. Confirm dialog
3. ✅ VERIFY: H1 goes back to "PROGRESSIA · Discord Project · [ Project Type ]"
4. In Admin → Settings tab
5. Click "Import Configuration"
6. Select the JSON file from TEST 4
7. ✅ VERIFY: Page reloads and:
   - H1 shows "AWESOME PROJECT"
   - Subtitle shows "Epic Team Advance"
   - Admin → Whitelabel forms show your values
```

**Expected**: Everything restored correctly ✅

---

### ✅ TEST 6: Upload Logos
```
1. In Whitelabel tab
2. Left side: Click "Upload Logo"
3. Pick any image (PNG/JPG, ~200x200)
4. ✅ VERIFY: Logo shows in left preview
5. Right side: Click "Upload Logo"
6. Pick another image
7. ✅ VERIFY: Logo shows in right preview
8. Click "Save Whitelabel Config"
9. Export config
10. Open JSON file → Search for "leftLogo"
11. ✅ VERIFY: Contains "data:image/..." (base64)
```

**Expected**: Logos in export as base64 ✅

---

## DevTools Console Commands (For Advanced Testing)

```javascript
// Check localStorage values
localStorage.getItem('wl_mainTitle')
localStorage.getItem('wl_subtitle')
localStorage.getItem('wl_leftLogo')  // Shows first 50 chars
localStorage.getItem('wl_rightLogo') // Shows first 50 chars

// Manually update (test reactivity)
localStorage.setItem('wl_mainTitle', 'CONSOLE TEST');
// Then run this to see it update:
applyWhitelabelTitles();

// Export current config for inspection
const config = Dashboard.StorageManager.loadConfig();
console.log(JSON.stringify(config, null, 2));
```

---

## Success Checklist ✅

- [ ] Test 1: Title updates without reload
- [ ] Test 2: Subtitle updates without reload  
- [ ] Test 3: Values persist on F5
- [ ] Test 4: Export JSON has whitelabel object
- [ ] Test 5: Import restores everything
- [ ] Test 6: Logos upload and export as base64

**If ALL ✅**: Implementation is WORKING PERFECTLY

---

## Troubleshooting

### H1 Not Updating?
```
1. Open DevTools (F12)
2. Console tab
3. Paste: applyWhitelabelTitles()
4. Check error messages
5. If error about querySelector, check `.h-title h1` exists
```

### Export Missing Whitelabel?
```
1. Open DevTools Console
2. Paste: const cfg = Dashboard.StorageManager.loadConfig(); console.log(JSON.stringify(cfg, null, 2))
3. Should see "whitelabel" key in output
4. If not, re-save in Whitelabel tab
```

### Import Failing?
```
1. Make sure JSON has this structure:
   - "buses": [...]
   - "apps": [...]
   - "waves": [...]
   - "whitelabel": {...} (optional)
2. Old JSON without "whitelabel" should still work (backward compatible)
```

---

**Status**: All changes deployed to both root and dist files ✅
**No external dependencies**: Pure vanilla JS ✅
**No hardcoding**: All dynamic from localStorage ✅