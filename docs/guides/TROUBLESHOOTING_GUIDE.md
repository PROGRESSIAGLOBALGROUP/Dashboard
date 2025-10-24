# 🆘 Troubleshooting Guide - Dashboard Enhanced

**Last Updated**: October 24, 2025  
**Version**: 1.2.0  
**Application**: Dashboard Enhanced (100% Client-Side)  
**Status**: Active Reference  

---

## 🎯 Quick Troubleshooting Map

**Choose your problem:**

| Issue | Fast Solution | Full Section |
|-------|---------------|--------------|
| Dashboard won't load | Rebuild & refresh | [Dashboard Won't Load](#dashboard-wont-load) |
| Data doesn't persist | Check localStorage | [Data Not Persisting](#data-not-persisting) |
| Setup fails | Run verify script | [Setup Issues](#setup-issues) |
| Build script errors | Check Python version | [Build Issues](#build-issues) |
| Console errors | F12 → Console tab | [Console Errors](#console-errors) |
| Import/Export broken | Validate JSON | [Import/Export Issues](#importexport-issues) |
| Responsive broken | Clear cache | [Responsive Design Issues](#responsive-design-issues) |
| Calculations wrong | Check status values | [Calculation Issues](#calculation-issues) |

---

## 🔴 Critical Issues

### Dashboard Won't Load

**Symptoms:**

- Blank white screen
- Nothing appears after 5 seconds
- Browser shows error in tab

**Step-by-Step Fix:**

```powershell
# STEP 1: Check file exists
Test-Path "dist/dashboard_enhanced.html" -PathType Leaf
# Result: Should show "True"

# STEP 2: If file missing, rebuild
python build/build_enhanced_dashboard.py

# STEP 3: Clear browser cache
# Ctrl+Shift+Delete (Windows)
# Cmd+Shift+Delete (Mac)
# Then: Select "Cookies and cached images"

# STEP 4: Hard refresh
# Ctrl+F5 (Windows)
# Cmd+Shift+R (Mac)

# STEP 5: Open again
Start-Process dist/dashboard_enhanced.html
```

**If Still Not Working:**

1. Check browser console (F12 → Console)
2. Look for red error messages
3. Note the exact error
4. See [Console Errors](#console-errors) section

---

### Data Not Persisting

**Symptoms:**

- Make changes, refresh page → changes gone
- Data reverts to default
- localStorage not working

**Root Causes & Fixes:**

#### Cause 1: Private/Incognito Mode

```
Problem: Private browsing blocks localStorage
Solution: Exit private mode and reload
```

**Fix:**
```
1. Close current browser tab
2. Open dashboard in NORMAL (not private) mode
3. Make change
4. Refresh
5. Change should persist
```

#### Cause 2: Browser Storage Disabled

**Chrome/Edge:**
```
Settings → Privacy and Security → Cookies and other site data
→ Check "Allow all cookies"
```

**Firefox:**
```
Preferences → Privacy & Security → Cookies and Site Data
→ Check "Accept cookies and site data by default"
```

**Safari:**
```
Settings → Privacy → Cookies
→ Choose "Allow from websites I visit"
```

#### Cause 3: Storage is Full

```powershell
# Check localStorage in DevTools
# F12 → Application → Storage → localStorage
# Look for: dashboard_config_v1

# If entry is huge (>5MB), it's corrupted
# Solution: Clear it and start fresh
```

**Fix:**
```javascript
// In browser console (F12 → Console):
localStorage.removeItem('dashboard_config_v1');
location.reload();
```

---

### Setup Issues

**Symptoms:**
- Commands don't run
- "Command not found"
- Scripts fail silently

**Diagnosis:**

```powershell
# Check Git
git --version
# Should show: git version 2.x.x

# Check Python
python --version
# Should show: Python 3.9 or higher

# Check Node (for testing)
npm --version
# Should show: npm version 7+

# If any missing, see installation guides below
```

---

## 🟡 Common Issues & Solutions

### Build Issues

**Issue: "Build script fails"**

```
Error: ModuleNotFoundError: No module named 'X'
```

**Solution:**

```powershell
# 1. Check Python version first
python --version
# Must be 3.9+

# 2. Install missing module
pip install --upgrade pip

# 3. Try build again
python build/build_enhanced_dashboard.py
```

**Issue: "SyntaxError in build output"**

```
Error: SyntaxError: Unexpected token
```

**Solution:**

```powershell
# 1. Verify source files have no syntax errors
python -m py_compile src/modules/*.py

# 2. Check JSON data is valid
python scripts/data/verify_json.py

# 3. Rebuild from scratch
python build/build_enhanced_dashboard.py --clean
```

---

### Console Errors

**How to Read Browser Console:**

```
Press F12 (or Cmd+Option+I on Mac)
Click "Console" tab
Look for red error messages
```

#### Common Error: "StorageManager is not defined"

```javascript
Error: StorageManager is not defined at line 45
```

**Cause**: Module failed to load

**Fix:**

```powershell
# 1. Rebuild dashboard
python build/build_enhanced_dashboard.py

# 2. Clear cache
# Ctrl+Shift+Delete

# 3. Refresh page
# F5
```

#### Common Error: "localStorage is not available"

```javascript
ReferenceError: localStorage is not defined
```

**Cause**: Private browsing mode or storage disabled

**Fix**: Exit private mode (see [Data Not Persisting](#data-not-persisting))

#### Common Error: "Cannot read property 'x' of undefined"

```javascript
TypeError: Cannot read property 'data' of undefined
```

**Cause**: Data loaded incorrectly

**Fix:**

```javascript
// In console:
Dashboard.StorageManager.loadConfig();
Dashboard.UIController.apply();
```

#### Common Error: "JSON Parse Error"

```javascript
SyntaxError: Unexpected token < in JSON at position 0
```

**Cause**: HTML returned instead of JSON (corrupted data)

**Fix:**

```javascript
// In console:
localStorage.removeItem('dashboard_config_v1');
location.reload();
```

---

### Import/Export Issues

**Issue: "Export creates corrupt file"**

**Symptoms:**
- File downloaded but won't import
- "Invalid JSON" error when importing

**Debug:**

```powershell
# 1. Verify exported file
# Open in text editor
# Should start with: {
# Should end with: }
# Should be valid JSON

# 2. Validate JSON online
# Go to: jsonlint.com
# Paste file content
# Check for errors
```

**Fix:**

```javascript
// If corrupted, reset and re-export:
localStorage.removeItem('dashboard_config_v1');
location.reload();
// Make changes
// Export again
```

**Issue: "Import doesn't accept file"**

**Symptoms:**
- File picker opens but no files appear
- Selected file is ignored
- No error message

**Debug:**

```powershell
# 1. Check file type
# Must be .json file
# Rename if needed: export.txt → export.json

# 2. Check file size
# Should be < 1 MB
# If larger, split into smaller exports

# 3. Try different browser
# Some browsers handle file input differently
```

**Fix:**

```powershell
# Use sample JSON to test:
# Create test.json with valid data
# Try importing
# If works: your file is corrupt
# If fails: browser issue
```

---

### Responsive Design Issues

**Issue: "Layout broken on mobile"**

**Symptoms:**
- Text too small/large
- Elements overlap
- Not properly centered
- Buttons not clickable

**Debug:**

```powershell
# 1. Check browser zoom
# Ctrl+0 resets to 100%

# 2. Check viewport
# F12 → Device Toolbar
# Select mobile device
# Check width in px

# 3. Try different browser
# Some mobile browsers zoom differently
```

**Fix:**

```powershell
# 1. Clear cache
Ctrl+Shift+Delete

# 2. Hard refresh
Ctrl+F5

# 3. Try in different browser
# Chrome mobile, Firefox mobile, Safari mobile
```

---

### Calculation Issues

**Issue: "Progress calculation seems wrong"**

**Symptoms:**
- Progress % doesn't match manual calculation
- Progress doesn't update
- Progress jumps unexpectedly

**Debug:**

```javascript
// In console:
// Check raw data
Dashboard.StorageManager.loadConfig();
const config = Dashboard.StorageManager.getCurrentConfig();
console.log(config.apps);

// Check calculation
const progress = Dashboard.DataProcessor.calculateBUProgress('BU_ID');
console.log(progress);

// Check which apps are included
const filtered = config.apps.filter(app => app.status !== 'TBS');
console.log('Apps included:', filtered.length);
```

**Common Cause: Status is 'TBS' (To Be Started)**

```
Formula: Σ(progress × weight) / Σ(weight)
Only includes apps where status ≠ 'TBS'

If app has status='TBS', it's EXCLUDED from calculation
This is by design!
```

**Fix:**

```javascript
// If app should be included:
// 1. Change status from 'TBS' to 'WIP' or 'DONE'
// 2. Save changes
// 3. Progress updates automatically
```

**Common Cause: Weight is 0 or NULL**

```
Formula includes: Σ(weight) in denominator
If all weights are 0, division fails
```

**Debug:**

```javascript
// In console:
config.apps.forEach(app => {
  if (!app.weight || app.weight === 0) {
    console.warn(`App ${app.APP_ID} has invalid weight:`, app.weight);
  }
});
```

**Fix:**

```
Ensure all apps have weight > 0
```

---

## 🔧 Environment Issues

### Python Not Found

**Error:**
```
'python' is not recognized as an internal or external command
```

**Cause**: Python not installed or not in PATH

**Fix for Windows:**

```powershell
# OPTION 1: Install from Windows Store (Recommended)
python
# This opens Windows Store → Click "Get"
# Wait for installation
# Restart terminal
# Try again

# OPTION 2: Download from python.org
# Go to: https://python.org/downloads
# Download Python 3.11 or higher
# During install: CHECK "Add Python to PATH"
# Restart computer
# Try again
```

**Fix for Mac:**

```bash
# Install using Homebrew
brew install python3
# Then use:
python3 --version
```

**Fix for Linux:**

```bash
# Ubuntu/Debian
sudo apt install python3
# Fedora
sudo dnf install python3
# Then use:
python3 --version
```

---

### Git Not Found

**Error:**
```
'git' is not recognized
```

**Cause**: Git not installed

**Fix:**

```powershell
# Windows: Download from git-scm.com
# macOS: brew install git
# Linux: sudo apt install git
```

---

### npm Not Found

**Error:**
```
'npm' is not recognized
```

**Cause**: Node.js not installed

**Fix:**

```powershell
# Windows/Mac: Download from nodejs.org
# Linux: sudo apt install nodejs npm

# Verify:
npm --version
# Should show: 8.x or higher
```

---

## 🔍 Advanced Debugging

### Enable Debug Mode

```javascript
// In browser console, add logging:
const originalLog = console.log;
console.debug = function(...args) {
  originalLog('%cDEBUG:', 'color: blue', ...args);
};

// Then operations will show debug info
```

### Check Network Activity

```
F12 → Network tab
Perform action that's failing
Look for failed requests (red X)
Most shouldn't exist (client-side app!)
If external requests appear, that's the issue
```

### Check Application Storage

```
F12 → Application tab
→ Storage (or Local Storage)
→ Expand "file://" or domain
→ Check "dashboard_config_v1"

Click to see the data
Verify structure looks correct
```

### Performance Issues

```
F12 → Performance tab
Click "Record"
Perform action
Stop recording
Look for long bars = slow operations

If calculation slow:
- Too many apps?
- Large dataset?
- Try with fewer apps first
```

---

## 📞 When to Escalate

### Contact Team Lead If:

- ❌ Error not in this guide
- ❌ Fix doesn't work after trying multiple times
- ❌ Issue happens in all browsers consistently
- ❌ Data mysteriously appears/disappears
- ❌ Browser crashes when using app
- ❌ Performance extremely slow (>5 sec loads)

**Provide**:
- Exact error message (screenshot if possible)
- Browser & version
- Steps to reproduce
- What you already tried
- Whether issue is consistent or random

---

## ✅ Quick Fixes Checklist

When something's broken, try these in order:

```
□ 1. Clear cache: Ctrl+Shift+Delete
□ 2. Hard refresh: Ctrl+F5 or Cmd+Shift+R
□ 3. Check console: F12 → Console
□ 4. Rebuild: python build/build_enhanced_dashboard.py
□ 5. Verify data: python scripts/data/verify_json.py
□ 6. Try different browser
□ 7. Exit private/incognito mode
□ 8. Restart computer
□ 9. Check localhost isn't blocked
□ 10. Contact team lead
```

**Most issues resolved by step 4!**

---

## 🎓 Understanding the Tech

### Why Client-Side Only?

```
✅ No servers to break
✅ No backend to maintain
✅ Works completely offline
✅ Instant updates (no server lag)
❌ Data stored in browser (localStorage)
❌ Can't sync across devices easily
```

### How Data Persists

```javascript
// When you make a change:
1. UIController detects change
2. StorageManager.saveConfig() is called
3. Data serialized to JSON
4. Stored in localStorage['dashboard_config_v1']
5. Persists until localStorage cleared

// When page loads:
1. StorageManager.loadConfig() runs
2. Data retrieved from localStorage
3. UIController renders it
4. User sees previous state
```

### What Could Go Wrong

```
❌ localStorage cleared (user did Ctrl+Shift+Delete)
❌ Storage exceeded (app data > 10MB)
❌ Private browsing (localStorage disabled)
❌ Browser storage disabled in settings
❌ Corrupted JSON (won't parse)
❌ Module load failed (console error)
❌ Browser cache stale (need hard refresh)
```

---

## 📊 Verification Checklist

**Before reporting a bug, verify:**

```
□ Browser is supported (Chrome/Edge/Firefox/Safari)
□ Not in private/incognito mode
□ localStorage enabled in settings
□ Cache cleared (Ctrl+Shift+Delete)
□ Hard refresh done (Ctrl+F5)
□ Tried different browser
□ Python version 3.9+
□ build script ran successfully
□ verify_json.py shows no errors
□ No console errors (F12)
```

---

## 🚀 Performance Tips

**To keep Dashboard fast:**

```
✅ Keep app count reasonable (< 1000)
✅ Clear old export files
✅ Don't keep too many browser tabs open
✅ Close other extensions
✅ Regular browser cache clear (monthly)
✅ Use latest browser version
```

---

## 📝 Common Scenarios

### Scenario 1: "I reloaded and everything's gone"

```
Likely Cause: localStorage cleared or private mode
Solution:
1. Check you exited private mode
2. Check browser settings allow localStorage
3. If data was important, check backup JSON exports
```

### Scenario 2: "Export works but import fails"

```
Likely Cause: JSON corrupted or file incompatible
Solution:
1. Validate JSON at jsonlint.com
2. Ensure file is .json type
3. Try exporting fresh and importing that
4. If it works: old file was corrupted
```

### Scenario 3: "Setup worked but then dashboard broke"

```
Likely Cause: Cache issue or incomplete build
Solution:
1. Rebuild: python build/build_enhanced_dashboard.py
2. Clear cache: Ctrl+Shift+Delete
3. Hard refresh: Ctrl+F5
4. If still broken: restore from backup
```

### Scenario 4: "Works on Chrome but not Firefox"

```
Likely Cause: Browser-specific issue
Solution:
1. Clear Firefox cache
2. Check if extensions blocking localStorage
3. Try with Firefox private browsing disabled
4. Try different versions
```

---

## ✨ When Everything Works!

**If Dashboard loads and works:**
```
✅ Setup was successful
✅ Data persisting correctly
✅ Browser compatible
✅ No errors in console
✅ Calculations working

You're good to go! 🎉
```

---

**Still stuck? Ask your team lead for help. We're here to help! 🚀**
