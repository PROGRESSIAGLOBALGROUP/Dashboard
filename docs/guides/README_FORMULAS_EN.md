# Formula Calculation Documentation - English

**Last Updated**: October 2025  
**Versions**: English & Spanish

---

## Documentation Overview

This section contains complete guides for configuring and understanding weighted progress calculation formulas in Dashboard Enhanced.

---

## Available Guides

### 1. **Quick Start** - Start Here (5 minutes)
**File**: `FORMULA_QUICKSTART_EN.md`

Visual and practical guide for newcomers. Includes:
- 7 steps for first configuration
- Visual calculation examples
- 4 ready-to-use presets
- Common changes in 30 seconds
- Quick SOS for problems

**For who**: New administrators, quick implementers.

---

### 2. **Complete Guide** - Exhaustive Reference (30 minutes)
**File**: `FORMULA_GUIDE_EN.md`

Technical documentation complete. Includes:
- Detailed explanation of each parameter
- Complete math formulas
- Step-by-step examples
- 4 practical scenarios (Startup, Enterprise, Audit, Agile)
- 10 frequently asked questions (FAQ)
- Key variables table

**For who**: Expert administrators, analysts, auditors.

---

### 3. **Reference Card** - Quick Lookup (1 minute)
**File**: `FORMULA_REFERENCE_CARD_EN.md`

Quick reference sheet. Includes:
- Decision matrix
- 4 copy-paste templates
- Mathematical formulas
- Weight assignment guide
- Criticality scale
- Status inclusion scenarios
- Method comparison
- Troubleshooting matrix
- Parameter bounds
- Execution checklist
- Decision flowchart

**For who**: Anyone needing instant answers. Printable (2 pages).

---

## Recommended Reading Flows

### Flow 1: New Administrator (20 minutes total)

1. **Quick Start** (5 min)
   - Read 7 steps
   - Review visual examples
   - Try one of 4 presets

2. **Complete Guide** - "Panel Access" (5 min)
   - Confirm where to access

3. **Complete Guide** - "Main Parameters" (10 min)
   - Read only your method section (Weighted/Simple/Minimum)
   - Understand status needs
   - Ready to configure

### Flow 2: Auditor/Compliance (30 minutes total)

1. **Complete Guide** - "Introduction" (5 min)
   - Understand key concepts

2. **Complete Guide** - "Main Parameters" (10 min)
   - Read everything, focus on "Status Inclusion Rules"

3. **Complete Guide** - "Practical Examples" → Case 3 (5 min)
   - Audit/Compliance ready configuration

4. **Complete Guide** - "Weighted Calculation" (10 min)
   - Understand exact mathematics

### Flow 3: Data Analyst (All documents - 60 minutes)

1. Quick Start - Complete
2. Complete Guide - Complete
3. FAQ - Deep dive
4. Reference Card - For ongoing lookup

---

## Key Concepts Summary

### 5 Main Decisions

| # | Decision | Impact | Options |
|---|----------|--------|---------|
| 1 | **Calculation Method** | **VERY HIGH** | Weighted / Simple / Minimum |
| 2 | **Status Inclusion** | **HIGH** | TBS / WIP / CLO (combinable) |
| 3 | **App Weights** | **HIGH** | 0.3 - 10.0 |
| 4 | **App Criticality** | **HIGH** | 0.5 - 2.0 (multipliers) |
| 5 | **Global Formula** | **MEDIUM** | Weighted by Size / Simple |

### 3 Complexity Levels

**Level 1: Basic**
- Use defaults
- Recommended methods
- Don't adjust individual weights
- ⏱️ 5 minutes

**Level 2: Intermediate**
- Read Complete Guide
- Customize weights per app
- Adjust criticalities
- ⏱️ 30 minutes

**Level 3: Advanced**
- Understand mathematics
- Create own presets
- Validate with Test Calculation
- ⏱️ 60+ minutes

---

## Quick Troubleshooting

**Progress looks very low**
→ Go to Quick Start → "Common Changes" → First option

**Progress looks very high**
→ Go to Quick Start → "Common Changes" → Second option

**One app dominates everything**
→ Go to Quick Start → "Common Changes" → Third option

**Result doesn't make sense**
→ Go to Complete Guide → "Weighted Calculation" → "Step-by-Step Example"

**Question about a parameter**
→ Go to Complete Guide → "Main Parameters" → Search by name

---

## Formula Mathematics

### Weighted Average (Recommended)

$$BU Progress = \frac{\sum (App Progress \times Weight \times Criticality Multiplier)}{\sum (Weight \times Criticality Multiplier)}$$

**When to use**: When apps have different importance.

### Simple Average

$$BU Progress = \frac{\sum App Progress}{Count(Apps)}$$

**When to use**: When all apps are equally important.

### Minimum Progress

$$BU Progress = MIN(App1 Progress, App2 Progress, ...)$$

**When to use**: When ALL apps must be complete.

---

## Configuration Checklist

Use this to verify your setup is ready:

- [ ] Decided method (Weighted / Simple / Minimum)
- [ ] Defined status inclusion (TBS / WIP / CLO)
- [ ] Configured weights (min / default / max)
- [ ] Adjusted multipliers if needed
- [ ] Chose global formula (Weighted / Simple)
- [ ] Clicked "Save Configuration"
- [ ] Clicked "Test Calculation" and saw result
- [ ] Result makes sense
- [ ] Exported configuration for backup

---

## Document Support Map

| I need to know... | File | Section |
|-------------------|------|---------|
| How to start quickly | FORMULA_QUICKSTART_EN.md | Top |
| Parameter definition | FORMULA_GUIDE_EN.md | Main Parameters |
| How it calculates | FORMULA_GUIDE_EN.md | Weighted Calculation |
| Example of my case | FORMULA_GUIDE_EN.md | Practical Examples |
| Answer to question | FORMULA_GUIDE_EN.md | FAQ |
| Validate my setup | FORMULA_QUICKSTART_EN.md | Validation |
| Fix a problem | FORMULA_QUICKSTART_EN.md | Quick SOS |
| Quick reference | FORMULA_REFERENCE_CARD_EN.md | Any section |

---

## Achievable Goals

With these guides you can:

✅ Configure formulas in 5-30 minutes
✅ Understand what each parameter does
✅ Validate your configurations
✅ Create reusable presets
✅ Export and import configurations
✅ Troubleshoot common problems
✅ Share configurations with team
✅ Pass audits
✅ Optimize for your context

---

## File Locations

```
c:\PROYECTOS\Dashboard\docs\guides\

English:
├── FORMULA_QUICKSTART_EN.md       ← Start here (5 min)
├── FORMULA_GUIDE_EN.md            ← Complete reference (30 min)
└── FORMULA_REFERENCE_CARD_EN.md   ← Quick lookup (1 min)

Español:
├── FORMULA_QUICKSTART.md
├── FORMULA_GUIDE.md
└── FORMULA_REFERENCE_CARD.md
```

---

## Language Options

- 📄 **English**: FORMULA_*_EN.md
- 📄 **Spanish**: FORMULA_*.md (without _EN suffix)

Both versions contain identical information in their respective languages.

---

**Last Updated**: October 2025  
**Version**: 1.0  
**Languages**: English & Spanish
