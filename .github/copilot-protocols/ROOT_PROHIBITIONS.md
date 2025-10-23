# 🚫 ROOT DIRECTORY ABSOLUTE PROHIBITIONS

**Version**: 2.0  
**Effective**: Immediately  
**Status**: MANDATORY - NO EXCEPTIONS

---

## 🛑 FILES THAT MUST NEVER BE IN ROOT

### ❌ ABSOLUTE PROHIBITIONS (NON-NEGOTIABLE)

| File Type | Pattern | Why | Action |
|-----------|---------|-----|--------|
| `.txt` | `*.txt` | Reports/logs belong in `docs/reports/` or `docs/process/` | **DELETE IMMEDIATELY** |
| `.md` (non-README) | `*.md` except `README.md` | All markdown except README goes to `docs/` | **MOVE TO docs/** |
| `.ps1` | `*.ps1` | PowerShell scripts go to `scripts/` | **MOVE TO scripts/** |
| `.js` (non-src) | `*.js` not in `src/` | JS files go to `src/modules/` or `scripts/` | **MOVE TO scripts/** |
| `.html` (non-dist) | `*.html` | HTML files go to `src/` or `dist/` | **MOVE TO src/** |
| Report files | `*REPORT*`, `*SUMMARY*`, `*STATUS*` | Go to `docs/reports/` | **MOVE IMMEDIATELY** |
| Deployment docs | `*DEPLOY*`, `*SETUP*` | Go to `docs/guides/` or `docs/process/` | **MOVE IMMEDIATELY** |
| Fix/patch docs | `*FIX*`, `*PATCH*` | Go to `docs/fixes/` | **MOVE IMMEDIATELY** |

---

## 🎯 ROOT DIRECTORY - ONLY THESE FILES ALLOWED

```text
✅ README.md                    ← Main project documentation ONLY
✅ package.json                 ← Node dependencies
✅ dashboard_enhanced.html      ← Legacy (keep for backward compatibility)
✅ index.html                   ← Landing/redirect
✅ .github/                     ← Configuration folder
✅ src/                         ← Source code
✅ dist/                        ← Compiled artifacts
✅ docs/                        ← ALL documentation (organized)
✅ data/                        ← External data files
✅ scripts/                     ← Automation scripts
✅ tests/                       ← Test files
✅ code_surgeon/                ← Patching infrastructure
✅ surgery/                     ← Patch jobs
✅ .gitignore                   ← Git configuration
✅ .env (if needed)             ← Environment secrets
✅ Makefile (if needed)         ← Build automation
```

Everything else is a violation and must be deleted or moved.

---

## 🚨 FOR GITHUB COPILOT - BINDING INSTRUCTION

### If you generate any file

1. **STOP AND ASK:**

```text
"I need to create [filename] of type [.txt/.md/.js/.ps1].
Is this:
A) Explicitly requested by user?
B) Will it go in the CORRECT location per FILE_ORGANIZATION_PROTOCOL?"
```

2. **IF ANSWER IS NO TO BOTH:** Don't create it. Ask user for clarification.

3. **IF ANSWER IS YES:** Create in the CORRECT location:

```text
.txt files    → docs/reports/ or docs/process/
.md files     → docs/{category}/ (NOT root)
.js files     → src/modules/ or scripts/
.ps1 files    → scripts/
Reports       → docs/reports/
Guides        → docs/guides/
Fix docs      → docs/fixes/
```

4. **VALIDATE BEFORE CREATION:**

- "Is this file type violating ROOT_PROHIBITIONS?"
- "Does user need this file, or is it 'for completeness'?"
- "Will this clutter the root directory?"

---

## 🔄 CLEANUP ACTION REQUIRED NOW

**Files to MOVE immediately:**

```
APPLICATIONS_OVERVIEW_COMPREHENSIVE_FIX_REPORT.txt       → docs/fixes/
APPLICATIONS_OVERVIEW_FIX_SUMMARY.txt                    → docs/reports/
BEFORE_AND_AFTER_COMPARISON.txt                          → docs/reports/
CHANGE_MANIFEST_APPLICATIONS_OVERVIEW_FIX.txt            → docs/process/
CONSOLE_DEBUGGING_GUIDE.txt                              → docs/guides/
DEPLOYMENT_COMPLETE.txt                                  → docs/reports/
DEPLOYMENT_GUIDE.txt                                     → docs/guides/
DEPLOYMENT_SUMMARY.txt                                   → docs/reports/
FINAL_STATUS_REPORT.txt                                  → docs/reports/
FINAL_SUMMARY.txt                                        → docs/reports/
GITHUB_PAGES_DEPLOYMENT_STATUS.txt                       → docs/reports/
PROJECT_COMPLETION_REPORT.txt                            → docs/reports/
QUICK_START_VERIFICATION.txt                             → docs/process/
UPGRADE_ARCHITECTURE.txt                                 → docs/technical/
WORLD_CLASS_UPGRADE_SUMMARY.txt                          → docs/reports/
```

---

## ✅ SYSTEM ENFORCEMENT

From now on:

1. **This file** (`ROOT_PROHIBITIONS.md`) is the **binding source of truth**
2. **Copilot will reference this** before creating ANY file
3. **Every protocol file** links to this document
4. **No exceptions** - not even for "important" files

---

## 📝 REMEMBER

> **Clean root = Professional project**  
> **Root clutter = Spaghetti code mentality**  
> **File organization = Respect for the codebase**

This isn't optional. This is **engineering discipline**.
