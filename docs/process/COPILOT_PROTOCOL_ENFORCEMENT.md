# 🤖 Copilot Protocol Enforcement - Guidelines

**Date**: October 22, 2025  
**Status**: ✅ ACTIVE  
**Version**: 1.0  

---

## 📋 Overview

This document describes the **mandatory file organization protocol** enforced in the Copilot instructions (`.github/copilot-instructions.md`) to maintain code quality and professional repository structure.

---

## 🎯 Core Principle

**"Root directory contains ONLY: `README.md`, `package.json`, `dashboard_enhanced.html`, `index.html`, `.github/`, and source folders (`src/`, `dist/`, `docs/`, `data/`, `scripts/`, `tests/`, `code_surgeon/`)."**

---

## 📁 File Organization Rules (MANDATORY)

### ✅ Correct Locations

| File Type | Location | Examples | Reason |
|-----------|----------|----------|--------|
| `.md` - Technical Docs | `docs/technical/` | Architecture specs, implementation details | Technical reference |
| `.md` - User Guides | `docs/guides/` | Tutorials, how-to docs, user instructions | User documentation |
| `.md` - Release Notes | `docs/releases/` | Version history, deployment notes | Version tracking |
| `.md` - Process Docs | `docs/process/` | Checklists, test plans, workflows | Operational procedures |
| `README.md` | ROOT ONLY | Project overview, quick start | Exception to rule |
| `.js` - Scripts | `scripts/` | Helper scripts, build helpers, automation | Automation tools |
| `.js` - Modules | `src/modules/` | Application logic, reusable components | Source code |
| `.ps1` - PowerShell | `scripts/` | Automation, batch operations | Administrative tasks |
| `.json` - Config/Data | `data/` or `scripts/` | External data, configuration files | Data management |
| `.html` - Dist | `dist/` ONLY | Compiled/built files, final artifacts | Distribution |

### ❌ Never in Root

```
❌ *.md (except README.md)
❌ *.js (except index.js if it's root entry point)
❌ *.ps1
❌ *.json (except package.json)
❌ Temporary files
❌ Build artifacts
❌ Helper scripts
```

---

## 🚨 Enforcement Rules (FOR COPILOT AI AGENTS)

### **ALWAYS (Pre-Creation)**
- ✅ Identify the file type BEFORE creation
- ✅ Determine correct destination folder from the table above
- ✅ Check if a similar file already exists in the correct location
- ✅ Create the file in its final location immediately

### **ALWAYS (Post-Creation)**
- ✅ Verify the file is in the correct folder
- ✅ Update any references to point to new location
- ✅ Commit with message: `chore: organize <filename> to <folder>/`
- ✅ Never leave files in root to "clean up later"

### **NEVER**
- ❌ Create `.js`, `.md`, `.ps1` files in root
- ❌ Create temporary files in root
- ❌ Assume a markdown belongs in root just because initial context showed it there
- ❌ Leave helper scripts or automation scattered in root
- ❌ Create new folders at root level (only use predefined: `src/`, `dist/`, `docs/`, `data/`, `scripts/`, `tests/`, `code_surgeon/`)

---

## 📝 Pre-Commit File Organization Checklist

**Before EVERY git commit, answer these questions:**

```
[ ] 1. Does this commit add or modify any .md files?
      If YES → Are they in docs/{guides|technical|releases|process}/?
      If NO → ABORT and move them immediately

[ ] 2. Does this commit add or modify any .js files?
      If YES → Are they in scripts/, src/modules/, or build/?
      If NO → ABORT and move them immediately

[ ] 3. Does this commit add or modify any .ps1 files?
      If YES → Are they in scripts/?
      If NO → ABORT and move them immediately

[ ] 4. Are there any new temporary or helper files?
      If YES → Are they in scripts/ or surgery/jobs/?
      If NO → ABORT and move them immediately

[ ] 5. Does root directory contain ONLY expected files?
      Expected: README.md, package.json, dashboard_enhanced.html, index.html, 
      .github/, src/, dist/, docs/, data/, scripts/, tests/, code_surgeon/
      If NO → Clean up immediately before committing
```

---

## 🔧 How to Fix Misplaced Files

**If you find a misplaced file in root:**

### Step 1: Identify Correct Location
```powershell
# Example: EXAMPLE_REPORT.md found in root
# Q: Is it a release note? Yes → docs/releases/
# Q: Is it a technical doc? Yes → docs/technical/
# Q: Is it a user guide? Yes → docs/guides/
# Q: Is it a process/workflow? Yes → docs/process/
```

### Step 2: Move File
```powershell
Move-Item -Path "C:\path\EXAMPLE_REPORT.md" `
          -Destination "C:\path\docs\folder\EXAMPLE_REPORT.md" `
          -Force
```

### Step 3: Commit with Organization Message
```bash
git add -A
git commit -m "chore: organize EXAMPLE_REPORT.md to docs/folder/"
git push origin main
```

---

## 📚 Real-World Examples

### Example 1: Adding a User Guide
```
❌ WRONG: Create docs/TUTORIAL.md in root
✅ RIGHT: Create docs/guides/TUTORIAL.md immediately

Command: New-Item -Path "docs/guides/TUTORIAL.md" -Type File
Commit: "docs: add tutorial guide to docs/guides/"
```

### Example 2: Creating a Build Helper Script
```
❌ WRONG: Create build_helper.js in root, then move later
✅ RIGHT: Create scripts/build_helper.js from the start

Command: New-Item -Path "scripts/build_helper.js" -Type File
Commit: "scripts: add build helper to scripts/"
```

### Example 3: Documentation Reorganization
```
❌ WRONG: Leave VERIFICATION_CHECKLIST.md in root
✅ RIGHT: Move to docs/process/VERIFICATION_CHECKLIST.md

Command: Move-Item VERIFICATION_CHECKLIST.md -Destination docs/process/
Commit: "chore: organize VERIFICATION_CHECKLIST.md to docs/process/"
```

---

## 🎯 Benefits of This Protocol

| Benefit | Impact |
|---------|--------|
| **Maintainability** | Easy to find files by type and purpose |
| **Scalability** | Repository stays organized as it grows |
| **Professional** | Follows ISO 9001 and enterprise standards |
| **Clarity** | Clear separation of concerns |
| **Automation** | Scripts can reliably expect file locations |
| **Onboarding** | New contributors know where to put files |

---

## 🔄 Updates to Copilot Instructions

This protocol is defined in `.github/copilot-instructions.md`:

- **Section**: "File Organization Protocol (MANDATORY)"
- **Tables**: File type mapping, enforcement rules
- **Checklist**: Pre-commit validation steps
- **Manifest**: Root directory canonical source

**All AI agents MUST follow this protocol when creating or moving files.**

---

## 📞 Questions & Clarifications

- **Q**: Can I create a .md file in root?
  - **A**: Only `README.md` (project overview). All others go to `docs/`.

- **Q**: Where do temporary fix scripts go?
  - **A**: `scripts/` folder or `surgery/jobs/` for production patches.

- **Q**: What if I create a file in the wrong place accidentally?
  - **A**: Move it immediately and commit with `chore: organize` message.

- **Q**: Can I use different folder names?
  - **A**: No. Use only: `src/`, `dist/`, `docs/`, `data/`, `scripts/`, `tests/`, `code_surgeon/`.

---

## ✅ Compliance Verification

**Last Verified**: October 22, 2025  
**Status**: ✅ COMPLIANT

Root directory contents:
```
✅ README.md
✅ package.json
✅ dashboard_enhanced.html
✅ index.html
✅ .github/
✅ src/
✅ dist/
✅ docs/
✅ data/
✅ scripts/
✅ tests/
✅ code_surgeon/
✅ surgery/

❌ NO .md files (except README.md)
❌ NO .js scripts
❌ NO .ps1 scripts
❌ NO temporary files
✅ CLEAN ROOT DIRECTORY
```

---

**Last Updated**: October 22, 2025  
**Author**: GitHub Copilot AI Agent  
**Status**: ✅ ENFORCED

