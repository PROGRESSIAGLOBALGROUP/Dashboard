# Formula Parameters Reference Card - English

Last Updated: October 2025

---

## DECISION MATRIX - Quick Reference

| Decision | Options | Best For | Impact |
|----------|---------|----------|--------|
| **Progress Method** | Weighted Average ⭐ | Multiple priorities | **HIGH** |
| | Simple Average | Equal importance | **HIGH** |
| | Minimum Progress | All complete | **HIGH** |
| **Status Inclusion** | Include TBS | Full picture | **HIGH** |
| | Include WIP | Active work | **HIGH** |
| | Include CLO | Completed | **HIGH** |
| **Min Weight** | 0.3 - 2.0 | Define floor | LOW |
| **Max Weight** | 1.0 - 10.0 | Define ceiling | **HIGH** |
| **Default Weight** | Min - Max | New apps | MED |
| **Low Multiplier** | 0.5 - 1.5 | Low criticality | LOW |
| **Med Multiplier** | 0.5 - 1.5 | Medium criticality | LOW |
| **High Multiplier** | 1.0 - 2.0 | High criticality | **HIGH** |
| **Global Formula** | Weighted by Size | Large BUs influence | MED |
| | Simple Average | Equal BUs | MED |

---

## QUICK CONFIGURATION TEMPLATES

### TEMPLATE A: Standard Startup

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

### TEMPLATE B: Enterprise Portfolio

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

### TEMPLATE C: Audit/Compliance

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

### TEMPLATE D: Agile/Iterative

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

---

## FORMULA MATHEMATICS

### Weighted Average (Most Common)

$$Progress = \frac{\sum (App\% \times Weight \times Criticality)}{\sum (Weight \times Criticality)}$$

Example with 2 apps:
- App A: 80%, Weight 1.0, Criticality 1.0 = 80 points
- App B: 60%, Weight 2.0, Criticality 1.2 = 144 points
- **Result**: (80+144) / (1.0 + 2.4) = 224/3.4 = **65.9%**

### Simple Average

$$Progress = \frac{\sum App\%}{Count(Apps)}$$

Example: (80 + 60) / 2 = **70%**

### Minimum Progress

$$Progress = MIN(App1\%, App2\%, ...)$$

Example: MIN(80, 60) = **60%**

---

## WEIGHT ASSIGNMENT GUIDE

| App Importance | Weight | When To Use |
|---|---|---|
| Low Priority | 0.5 - 0.7 | Not critical, can wait |
| Normal/Standard | 1.0 | Average importance |
| High Priority | 1.5 - 2.0 | Important, business impact |
| Critical | 2.5 - 3.0 | Failure stops business |
| Must-Have First | 3.5 - 5.0 | Blockers for everything else |

---

## CRITICALITY MULTIPLIER SCALE

| Level | Multiplier | When To Use | Business Impact |
|-------|-----------|-----------|-----------------|
| Low | 0.9 - 1.0 | Non-critical | Minor delays OK |
| Medium | 1.0 - 1.1 | Standard | Normal impact |
| High | 1.2 - 1.5 | Important | Significant impact |
| Critical | 1.5 - 2.0 | Do-or-die | Business-stopping |

---

## STATUS INCLUSION SCENARIOS

### Scenario 1: Full Transparency

```
Include: ✓ To Be Started
         ✓ Work in Progress
         ✓ Closed
Use Case: Show complete picture, all work states
Result: Most conservative view, shows what's NOT done
```

### Scenario 2: Active Work Focus

```
Include: ✗ To Be Started
         ✓ Work in Progress
         ✓ Closed
Use Case: Ignore future work, focus on current+done
Result: Mid-range view, realistic for execution phase
```

### Scenario 3: Delivery Only

```
Include: ✗ To Be Started
         ✗ Work in Progress
         ✓ Closed
Use Case: Only count completed work
Result: Most conservative, only "done" matters
```

### Scenario 4: Work in Progress Priority

```
Include: ✗ To Be Started
         ✓ Work in Progress
         ✗ Closed
Use Case: Focus on momentum, not final delivery
Result: Shows activity/velocity, ignores completion
```

---

## CALCULATION METHOD COMPARISON

| Method | Formula | Use Case | Conservative | Motivating |
|--------|---------|----------|--------------|-----------|
| **Weighted** | Sum(App%×Weight)/Sum(Weight) | Variable priorities | Medium | Yes |
| **Simple** | Sum(App%)/Count | Equal importance | Medium | Yes |
| **Minimum** | MIN(App%) | All must complete | Very | No |

---

## GLOBAL FORMULA (Combining BUs)

### Weighted by BU Size

```
Formula: Σ(BU% × App Count) / Σ(App Count)

Example:
BU A: 85% with 10 apps = 850 points
BU B: 60% with 2 apps = 120 points
Global: 970/12 = 80.8%

Effect: Large BUs influence more
Use When: Portfolio where size matters
```

### Simple Average

```
Formula: Σ(BU%) / Count(BUs)

Example:
BU A: 85%
BU B: 60%
Global: 145/2 = 72.5%

Effect: All BUs count equally
Use When: BUs roughly same size
```

---

## PARAMETER BOUNDS

| Parameter | Min | Max | Recommended |
|-----------|-----|-----|-------------|
| Minimum Weight | 0.1 | 2.0 | 0.5 |
| Maximum Weight | 1.0 | 10.0 | 3.0 |
| Default Weight | Min | Max | 1.0 |
| Low Multiplier | 0.5 | 1.5 | 1.0 |
| Med Multiplier | 0.5 | 1.5 | 1.0 |
| High Multiplier | 1.0 | 2.0 | 1.2 |

---

## TROUBLESHOOTING MATRIX

| Symptom | Likely Cause | Fix | Check |
|---------|------------|-----|-------|
| Progress = 0% | All apps TBS, TBS excluded | Include TBS or change app status | Status Inclusion |
| Progress too low | Heavy weighting | Decrease Max Weight or High Mult. | Weights |
| Progress too high | Light weighting | Increase Max Weight or High Mult. | Weights |
| One app dominates | Weight too high | Reduce that app's weight | Per-app weight |
| Doesn't match manual calc | Wrong method chosen | Double-check Progress Method | Method |
| Progress unchanged | Config not saved | Click "Save Configuration" | After changes |

---

## EXECUTION CHECKLIST

- [ ] Choose Progress Method (Weighted/Simple/Minimum)
- [ ] Define Status Inclusion (TBS/WIP/CLO mix)
- [ ] Set Weight Parameters (min/default/max)
- [ ] Configure Criticality Multipliers (low/med/high)
- [ ] Choose Global Formula (Weighted/Simple)
- [ ] Click "Save Configuration"
- [ ] Click "Test Calculation"
- [ ] Verify result makes sense
- [ ] Export for backup (optional)

---

## KEY FORMULAS AT A GLANCE

```
Weighted:  (App1%×W1×C1 + App2%×W2×C2) / (W1×C1 + W2×C2)
Simple:    (App1% + App2%) / 2
Minimum:   MIN(App1%, App2%)
Global WB: Σ(BU%×AppCount) / Σ(AppCount)
Global S:  Σ(BU%) / Count(BUs)
```

---

## DECISION FLOWCHART

```
START
  |
  ├─ Do apps have different importance?
  │  ├─ YES → Use WEIGHTED AVERAGE
  │  └─ NO → Do you need ALL complete?
  │      ├─ YES → Use MINIMUM PROGRESS
  │      └─ NO → Use SIMPLE AVERAGE
  |
  ├─ Include unstarted (TBS) apps?
  │  ├─ YES → Check TBS
  │  └─ NO → Uncheck TBS
  |
  ├─ Set weight range
  │  └─ Min=0.5, Max=3.0 (or customize)
  |
  ├─ Set criticality boost
  │  └─ High=1.2 (or customize)
  |
  ├─ How combine BUs?
  │  ├─ Size matters → WEIGHTED BY SIZE
  │  └─ Equal weight → SIMPLE AVERAGE
  |
  └─ SAVE & TEST
```

---

**Reference Card v1.0** | October 2025
For detailed explanations, see: FORMULA_GUIDE_EN.md and FORMULA_QUICKSTART_EN.md
