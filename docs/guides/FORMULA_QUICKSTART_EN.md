# Formula Configuration Quick Start - English

**For use in 5 minutes** | **Version**: 1.0

---

## 🎯 Your First Configuration

### Step 1: Open Setup

Dashboard → **Setup** button → **Calculation Formulas** tab

### Step 2: Select Method

```
Which best describes your project?

[A] Some apps are more important than others
    └─ Choose: Weighted Average ⭐ RECOMMENDED

[B] All apps have equal importance
    └─ Choose: Simple Average

[C] ALL must be complete for success
    └─ Choose: Minimum Progress
```

### Step 3: Define States to Include

```
Do you want to count unstarted apps?

[A] No, only active work and completed
    └─ Unchecked: To Be Started
       ✓ Work in Progress
       ✓ Closed

[B] Yes, everything including unstarted
    └─ ✓ To Be Started
       ✓ Work in Progress
       ✓ Closed

[C] Only completed work (audit)
    └─ Unchecked: To Be Started
       Unchecked: Work in Progress
       ✓ Closed
```

### Step 4: Configure Weights (if Weighted)

```
Minimum Weight:  0.5  (default: less important apps)
Maximum Weight:  3.0  (default: very important apps)
Default Weight:  1.0  (default: normal apps)

How to assign to each app?
- 0.5 = NOT important compared to others
- 1.0 = Normal/standard importance
- 2.0 = MORE important than normal
- 3.0 = VERY CRITICAL, failure stops everything
```

### Step 5: Criticality Boosting

```
Which apps are strategically critical?

Multipliers (defaults):
- Low Criticality:    1.0  (no boost)
- Medium Criticality: 1.0  (no boost)
- High Criticality:   1.2  (20% boost)

Increase if you have apps that if they fail, everything fails:
- Change High to: 1.5 or 2.0
```

### Step 6: Global Formula

```
How to combine BUs in overall report?

[A] Large BUs influence more
    └─ Choose: Weighted by BU Size

[B] All BUs count equally
    └─ Choose: Simple Average
```

### Step 7: Save and Test

```
[Button] Save Configuration     → Saves changes
[Button] Test Calculation       → See result in real-time
[Button] Reset to Defaults      → Back to default values
```

---

## 📊 Understanding Your Progress

### Formula = Smart Average

```
Imagine you have 3 apps:

APP 1          APP 2          APP 3
70% done       100% done      30% done
Weight: 1      Weight: 3      Weight: 0.5

┌─────────────────────────────────────────┐
│ Calculation:                            │
│                                         │
│ (70×1) + (100×3) + (30×0.5)             │
│ ─────────────────────────────────      │
│         1 + 3 + 0.5                     │
│                                         │
│ = 70 + 300 + 15 = 385                   │
│   ───────────────   ──                  │
│       4.5            4.5                │
│                                         │
│ = 85.6% ✓                               │
│                                         │
│ APP 2 (weight 3) influences A LOT       │
│ APP 1 (weight 1) influences NORMAL      │
│ APP 3 (weight 0.5) influences LITTLE    │
└─────────────────────────────────────────┘
```

### Why it Weighs More

```
Important Application         Normal Application
(weight 3.0)                  (weight 1.0)

At 100% progress             At 100% progress
Contributes: 300 points      Contributes: 100 points

Result? 3 times more important
```

### With Criticality

```
Normal App                    Critical App
Weight: 2.0                   Weight: 2.0
Criticality: Medium (1.0)     Criticality: High (1.2)

Contribution: 2.0 × 1.0       Contribution: 2.0 × 1.2
           = 2.0                           = 2.4

Critical app counts 20% more
```

---

## 🎨 Ready-to-Use Presets

### Preset 1: Startup/Small Team

```
Progress Method:        Weighted Average
Status Include:         ✓TBS ✓WIP ✓CLO
Min Weight:            0.5
Max Weight:            2.0
Default Weight:        1.0
Low Multiplier:        1.0
Med Multiplier:        1.1
High Multiplier:       1.3
Global Formula:        Simple Average
```

**When to use**: Small team, few apps.

---

### Preset 2: Large Enterprise/Portfolio

```
Progress Method:        Weighted Average
Status Include:         ✗TBS ✓WIP ✓CLO
Min Weight:            0.3
Max Weight:            5.0
Default Weight:        1.0
Low Multiplier:        0.9
Med Multiplier:        1.0
High Multiplier:       1.5
Global Formula:        Weighted by BU Size
```

**When to use**: Large portfolio, apps with different importance.

---

### Preset 3: Completed Only (Audit)

```
Progress Method:        Minimum Progress
Status Include:         ✗TBS ✗WIP ✓CLO
Min Weight:            1.0
Max Weight:            1.0
Default Weight:        1.0
Low Multiplier:        1.0
Med Multiplier:        1.0
High Multiplier:       1.0
Global Formula:        Simple Average
```

**When to use**: Only completed matters (compliance, audit).

---

### Preset 4: Agile/Iterative

```
Progress Method:        Weighted Average
Status Include:         ✗TBS ✓WIP ✓CLO
Min Weight:            0.5
Max Weight:            3.0
Default Weight:        1.0
Low Multiplier:        1.0
Med Multiplier:        1.1
High Multiplier:       1.2
Global Formula:        Weighted by BU Size
```

**When to use**: Iterative methodology, emphasis on WIP.

---

## ⚡ Common Changes

### "I want critical apps to impact MORE"

```
Current:  High Criticality = 1.2
Change to: High Criticality = 1.5  (25% more)
           or even         = 2.0   (100% more)
```

### "I don't want to count unstarted apps"

```
Current:  To Be Started ✓ (checked)
Change to: To Be Started ☐ (unchecked)
```

### "I want all apps to matter equally"

```
Change to: Simple Average
Or set all weights = 1.0
       all multipliers = 1.0
```

### "I want to be more conservative"

```
Change to: Minimum Progress
(progress = the app with least progress)
```

---

## ✅ Validation

### How to Know If It's Right

```
1. Click: Test Calculation
   ↓
2. See: Formulas applied step by step
   ↓
3. Ask yourself: Does this number make sense?
   ↓
4. If NO: Adjust parameters and repeat
   ↓
5. If YES: Click Save Configuration ✓
```

### Problem Indicators

```
❌ Progress very low
   → Increase Max Weight
   → Increase Criticality Multipliers
   → Exclude TBS

❌ Progress very high
   → Decrease Max Weight
   → Decrease Criticality Multipliers
   → Include TBS

❌ One app dominates everything
   → Decrease that app's weight
   → Decrease its criticality multiplier
```

---

## 📌 Remember

1. **Weights**: How important each app is
2. **Criticality**: How strategic it is
3. **States**: Which work to count (TBS/WIP/CLO)
4. **Method**: How to aggregate (weighted/simple/minimum)
5. **Global**: How to combine BUs

---

## 🔄 Export/Import

```
Save configuration:
Setup → Calculation Formulas → Save Configuration
  ↓
Settings → Export Configuration
  ↓
JSON file with ALL parameters

Restore:
Settings → Import Configuration
  ↓
Select JSON file
  ↓
Automatically restores EVERYTHING
```

---

## 🆘 Quick SOS

| Problem | Solution |
|---------|----------|
| No progress appears | Include at least one status (WIP or CLO) |
| Progress = 0% | Apps in TBS, change status or exclude TBS |
| One app dominates | Reduce its weight or criticality |
| Result doesn't make sense | Run Test Calculation, see step by step |
| Want to go back to defaults | Click Reset to Defaults button |

---

**Version**: 1.0 | **Quick Start**: 5 minutes | **Last Updated**: October 2025
