# 📤 Import/Export Guide - Dashboard Enhanced

**Last Updated**: October 24, 2025  
**Version**: 1.2.0  
**Application**: Dashboard Enhanced (100% Client-Side)  
**Purpose**: Team Data Collaboration & Backup Strategy  

---

## 🎯 Quick Start

**Want to export your data?**
```
1. Click "Admin" button (bottom right)
2. Click "Export Configuration"
3. JSON file downloads automatically
4. Done! ✓
```

**Want to import data?**
```
1. Click "Admin" button
2. Click "Import Configuration"
3. Select .json file from computer
4. Click "Import"
5. Dashboard updates with new data
```

---

## 📋 What is Import/Export?

### **Export**
Creating a backup file of your Dashboard data in JSON format.

**What gets exported:**
- All Business Units (BUs)
- All Applications
- All Waves
- All progress calculations
- All settings

**What does NOT get exported:**
- Browser history
- Your laptop settings
- External files

**Format**: Plain text JSON file (.json)

### **Import**
Loading a previously exported JSON file back into Dashboard.

**What happens:**
1. File is read
2. Data is validated
3. **REPLACES** current Dashboard data (destructive!)
4. Dashboard refreshes with new data
5. Data saved to browser storage

---

## 💾 Why Use Import/Export?

### **Scenario 1: Backup Your Work**
```
Problem: "I made lots of changes, don't want to lose them"
Solution: Export once per week
  → Save to OneDrive/Google Drive
  → Have backup if browser storage is cleared
```

### **Scenario 2: Share Data with Team**
```
Problem: "Need to share current status with the team"
Solution: Export from your machine
  1. Export JSON file
  2. Email or upload to shared drive
  3. Team member imports same file
  4. Everyone sees same data

Result: Team stays in sync!
```

### **Scenario 3: Move to Different Computer**
```
Problem: "I'm getting a new laptop"
Solution: Export/Import approach
  1. On old laptop: Export JSON
  2. Save to USB/email/cloud
  3. On new laptop: Import JSON
  4. All data restored instantly
```

### **Scenario 4: Start Fresh**
```
Problem: "Current data is corrupted, want to reset"
Solution: Import good backup
  1. You have old backup from last week
  2. Import that backup
  3. Bad data is replaced
  4. Back to last week's state
```

### **Scenario 5: Team Merge**
```
Problem: "Two teams have separate dashboards, need to merge"
Solution: Manual merge process
  1. Export from Team A dashboard
  2. Import into Team B dashboard
  3. Manually reconcile conflicts
  4. Export merged result
  5. Share with everyone
```

---

## 🔄 Step-by-Step: Export Your Data

### **Desktop Browser (Chrome, Edge, Firefox, Safari)**

**Step 1: Open Dashboard**
```
Open: dashboard_enhanced.html
Or navigate to: localhost:3000 (if running server)
```

**Step 2: Click Admin Button**
```
Look for: "Admin" button
Location: Bottom right corner
Color: Usually blue or highlighted
```

**Step 3: Click Export**
```
Admin panel opens
Look for: "Export Configuration" button
Click it
```

**Step 4: File Downloads**
```
Browser download folder receives: dashboard_config_v1.json
File size: Usually 10-100 KB
Contains: All your Dashboard data
```

**Step 5: Save Somewhere Safe**
```
Move file from Downloads to:
  ✓ OneDrive
  ✓ Google Drive
  ✓ Dropbox
  ✓ USB drive
  ✓ Email yourself
  ✓ Network share
```

### **Mobile Browser (iOS Safari, Android Chrome)**

**Step 1-3: Same as Desktop**
```
Open Dashboard → Admin → Export
```

**Step 4: Save File**
```
iOS Safari:
  - Long-press downloaded file
  - "Save to Files" or "Save to Photos"

Android Chrome:
  - Downloaded file appears in Downloads
  - Use file manager to move to cloud storage
```

---

## 🔄 Step-by-Step: Import Data

### **Desktop Browser**

**Step 1: Open Dashboard**
```
Make sure Dashboard is already running
```

**Step 2: Click Admin**
```
Admin button (bottom right)
```

**Step 3: Click Import**
```
Look for: "Import Configuration"
Click button
```

**Step 4: Select File**
```
File picker opens
Navigate to your .json file
Click "Open"
```

**Step 5: Confirm Import**
```
Dialog appears: "Import this file?"
Click "Yes" or "Confirm"
```

**Step 6: Dashboard Updates**
```
Page refreshes automatically
New data loads
Status message: "Import successful"
```

**Step 7: Verify Data**
```
Check that data looks correct:
  ✓ Business Units showing
  ✓ Applications listed
  ✓ Progress calculations correct
  ✓ No error messages
```

### **Mobile Browser**

**Step 1-3: Same as Desktop**
```
Dashboard → Admin → Import
```

**Step 4: Select File from Device**
```
iOS: Choose from Files app
Android: Choose from Downloads or Files app
```

**Step 5-7: Same as Desktop**
```
Confirm → Dashboard updates → Verify
```

---

## ⚠️ Important Notes

### **IMPORT IS DESTRUCTIVE**
```
When you import:
  ✗ Current data is DELETED
  ✗ New data replaces it
  ✗ Cannot undo! (unless you have backup)

Always backup before importing!
```

### **File Must Be Valid JSON**
```
Valid JSON looks like:
  {
    "buses": [...],
    "apps": [...],
    "waves": [...]
  }

Invalid JSON will:
  ✗ Show error message
  ✗ Not import
  ✗ Keep current data safe
```

### **Browser Storage Limits**
```
Each browser has limit: ~10 MB per site
Dashboard typically uses: 50-500 KB
Unless you have:
  - 1000+ applications
  - Very large datasets
  You're fine!
```

### **One Dashboard Per Browser Tab**
```
If you have 2 tabs open:
  Tab 1: Dashboard with data X
  Tab 2: Dashboard with data Y
  
Warning: Whichever tab imports last wins!
  → Data from other tab gets overwritten

Solution: Only use 1 tab at a time
```

---

## 📊 JSON File Structure

### **What's Inside the Export File**

```json
{
  "exportDate": "2025-10-24T15:30:00Z",
  "version": "1.2.0",
  "buses": [
    {
      "buId": "CORF",
      "key": "CORF",
      "name": "Corporate",
      "domain": "Corporate Domain",
      "fullname": "Corporate Operations"
    }
  ],
  "apps": [
    {
      "APP_ID": "APP001",
      "name": "Authentication System",
      "buId": "CORF",
      "status": "WIP",
      "progress": 75,
      "weight": 1.0
    }
  ],
  "waves": [
    {
      "waveId": "WAVE1",
      "name": "Wave 1",
      "target_date": "2025-12-31"
    }
  ]
}
```

### **Key Sections Explained**

**exportDate**: When this file was created
- Format: ISO 8601 timestamp
- Used for: Tracking backup dates

**version**: Dashboard version that created this
- Current: 1.2.0
- Ensures: Compatibility checking

**buses**: Business Units array
- Contains: BU definitions
- Each BU has: ID, name, domain, description

**apps**: Applications array
- Contains: All applications
- Each app has: ID, name, status, progress, weight

**waves**: Waves array
- Contains: Release waves
- Each wave has: ID, name, target date

---

## 🔐 Security Considerations

### **What You're Exporting**
```
✓ Your data (Business Units, Apps, Waves)
✓ Progress calculations
✓ Project information
✗ NO passwords
✗ NO secrets
✗ NO credentials
```

### **Data Privacy**
```
When exporting:
  ✓ Data stays on YOUR computer
  ✓ Nothing sent to servers (client-side app!)
  ✓ 100% offline process
  ✓ No cloud upload
  ✓ You control the file
```

### **Safe Practices**
```
✓ Export regularly (weekly)
✓ Store in secure location (OneDrive, etc)
✓ Don't share JSON files publicly
✓ Verify file before importing
✓ Keep backups in multiple locations
```

### **Risky Practices**
```
✗ Sharing JSON files publicly
✗ Storing on unsecured USB
✗ Emailing without encryption
✗ Saving to shared network drives (if sensitive)
✗ Not verifying file before import
```

---

## 🎯 Team Collaboration Workflow

### **Scenario: Team Status Sync**

**Morning: Each Developer Exports**
```
Developer 1:
  1. Opens their Dashboard
  2. Admin → Export
  3. Gets: dashboard_status_dev1.json

Developer 2:
  1. Opens their Dashboard
  2. Admin → Export
  3. Gets: dashboard_status_dev2.json

Tech Lead:
  1. Collects both JSON files
  2. Merges manually (see next section)
```

**Merge Files: Tech Lead**
```
1. Open dashboard_status_dev1.json in text editor
2. Copy "apps" array
3. Combine with dashboard_status_dev2.json apps
4. Remove duplicates manually
5. Save as: dashboard_merged.json
```

**Afternoon: Team Imports Merged Data**
```
All developers:
  1. Open Dashboard
  2. Admin → Import
  3. Select: dashboard_merged.json
  4. Click Import
  5. Everyone sees combined data!
```

---

## 🆘 Troubleshooting Import/Export

### **Issue: Export Button Doesn't Work**

**Symptom:**
- Click Export, nothing happens
- No file downloads

**Solution:**
```
1. Check pop-up blocker
   → Allow downloads from localhost/file
   
2. Check browser download settings
   → Should ask where to save (or auto-save)
   
3. Try different browser
   → Chrome → Firefox
   → Firefox → Edge
   → Edge → Safari

4. Clear cache and try again
   Ctrl+Shift+Delete
   → Clear cookies & cache
   → Refresh page
   → Try export again
```

### **Issue: Import Button Doesn't Work**

**Symptom:**
- Click Import, file picker doesn't open
- File picker opens but crashes

**Solution:**
```
1. Check file is actual .json
   → Rename if needed: export.txt → export.json
   
2. Check file size is reasonable
   → Should be < 1 MB
   → If > 5 MB, file might be corrupted
   
3. Try opening file in text editor first
   → Make sure it contains valid JSON
   → Go to jsonlint.com and validate
   
4. Clear localStorage and try again
   → F12 → Application → Storage
   → Delete "dashboard_config_v1"
   → Refresh and try import
```

### **Issue: Import Says "Invalid Format"**

**Symptom:**
- Click Import, select file
- Error: "Invalid JSON format"

**Causes & Fixes:**

**Cause 1: File is corrupted**
```
Check: Open file in text editor
Look for: Starting with { and ending with }
Should not have: Incomplete lines, odd characters

Fix: Export fresh copy from working Dashboard
```

**Cause 2: File is wrong type**
```
Check: File extension is .json
Try: Renaming file to .json

Fix: Export fresh from Dashboard (always .json)
```

**Cause 3: File is from old Dashboard version**
```
Check: Look inside file for "version" field
Should show: "1.2.0" or close

Fix: Re-export from current Dashboard version
```

### **Issue: Import Works But Data Looks Wrong**

**Symptom:**
- Import succeeds, but:
  - Some applications missing
  - Progress calculations wrong
  - Business Units not showing

**Solution:**
```
1. Verify file contents
   → Open in text editor
   → Check structure looks correct
   
2. Verify in browser console (F12 → Console)
   → Type: Dashboard.StorageManager.getCurrentConfig()
   → Press Enter
   → Check what loaded

3. Try re-exporting fresh copy
   → Import that fresh copy
   → See if same issue appears

4. Check for partial data
   → Only some BUs imported? 
   → File might have been cut off
   → Re-export full file
```

---

## 📋 Weekly Backup Checklist

**Every Friday End-of-Day:**

```
□ 1. Open Dashboard
□ 2. Admin → Export Configuration
□ 3. File downloads automatically
□ 4. Rename: dashboard_backup_[DATE].json
     Example: dashboard_backup_2025-10-24.json
□ 5. Move to cloud storage
     → OneDrive: Shared/Backups/
     → Google Drive: Dashboard Backups folder
     → Dropbox: Project/Backups/
□ 6. Verify file size (should be 10-500 KB)
□ 7. Test import (optional but recommended)
     → Import into a test tab
     → Verify data looks correct
     → Delete test tab data

Result: Weekly backup complete! ✓
```

---

## 🚀 Advanced: Programmatic Access

### **For Developers Only**

**Access Current Configuration (DevTools Console):**
```javascript
// Get current data
const config = Dashboard.StorageManager.getCurrentConfig();
console.log(config);

// Get specific BU
const bu = config.buses.find(b => b.buId === 'CORF');
console.log(bu);

// Get all applications
console.log(config.apps);

// Export to console
JSON.stringify(config, null, 2);
```

**Import Programmatically (DevTools Console):**
```javascript
// If you have JSON data in variable
const newConfig = {
  buses: [...],
  apps: [...],
  waves: [...]
};

// Save to storage
Dashboard.StorageManager.saveConfig(newConfig);

// Refresh UI
Dashboard.UIController.apply();
```

---

## ✅ Verification Checklist

**Before Sharing JSON File:**

```
□ File opens in text editor
□ Starts with: {
□ Ends with: }
□ Contains "buses" array
□ Contains "apps" array
□ Contains "waves" array
□ File size reasonable (< 1 MB)
□ No error messages in browser console
□ Data matches what you see in Dashboard
```

**Before Importing JSON File:**

```
□ File has .json extension
□ File opens in text editor (valid format)
□ Validated at jsonlint.com (optional)
□ File size < 1 MB
□ You have current backup (export first!)
□ File from trusted source
□ Checked with team lead if needed
```

---

## 🎓 Understanding the Data Format

### **Why JSON?**
```
✓ Human readable (can open in text editor)
✓ Universal format (works everywhere)
✓ Supported by all browsers
✓ Easy to share and backup
✓ Standard for data exchange
```

### **Can I Edit the JSON File?**
```
Technically: Yes, you can edit in text editor
Practically: Not recommended unless you know JSON

What can go wrong:
  ✗ Syntax errors (missing commas, quotes)
  ✗ Corrupted data (unbalanced braces)
  ✗ Invalid values (wrong status, negative progress)
  ✗ Structural issues (missing required fields)

Better: Use Dashboard admin panel to make changes
```

### **What If I Have Multiple Dashboards?**
```
Dashboard 1 (My Laptop):
  → Export: dashboard1.json
  
Dashboard 2 (Team Server):
  → Export: dashboard2.json

To Sync:
  1. Manually merge files (or ask tech lead)
  2. Import merged version to both
  3. Everyone now has same data

To Keep Separate:
  - Don't import between them
  - Each maintains own export backups
```

---

## 🔗 Related Documentation

- **QUICK_START_GUIDE.md** - Getting started with Dashboard
- **CODE_REVIEW_GUIDELINES.md** - Development standards
- **BROWSER_COMPATIBILITY.md** - Supported browsers
- **TROUBLESHOOTING_GUIDE.md** - Common issues

---

## 📞 Quick Reference

| Task | Steps |
|------|-------|
| **Export** | Admin → Export Configuration → Save file |
| **Import** | Admin → Import Configuration → Select file → Confirm |
| **Backup** | Export weekly to cloud storage |
| **Share** | Export, email/upload JSON, team member imports |
| **Verify** | Open file in text editor, check structure |
| **Recover** | Import backup file when needed |

---

## ✨ Best Practices Summary

**DO:**
```
✓ Export weekly
✓ Store backups in cloud
✓ Test imports before production
✓ Keep multiple versions
✓ Name files with dates
✓ Validate JSON before sharing
✓ Backup before importing
```

**DON'T:**
```
✗ Share JSON publicly
✗ Delete backups too quickly
✗ Import without backup
✗ Edit JSON without validation
✗ Keep only one copy
✗ Trust corrupted files
✗ Ignore import errors
```

---

**Questions? See TROUBLESHOOTING_GUIDE.md or contact your team lead! 🚀**
