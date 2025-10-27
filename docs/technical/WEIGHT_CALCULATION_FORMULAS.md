# 📊 Weight Calculation Formulas - Complete Technical Guide

**Document Version:** 2.0  
**Last Updated:** October 26, 2025  
**Status:** Production Ready  
**Audience:** Technical Architects, Data Analysts, Developers

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Level 1: Application Weight](#level-1-application-weight)
3. [Level 2: Business Unit Progress](#level-2-business-unit-progress)
4. [Level 3: Global Progress](#level-3-global-progress)
5. [Excel Implementation](#excel-implementation)
6. [Dashboard Implementation](#dashboard-implementation)
7. [Real-World Examples](#real-world-examples)
8. [Edge Cases & Validation](#edge-cases--validation)

---

## 🎯 Overview

The Dashboard uses a **3-level hierarchical weighted calculation system** to compute progress across the entire organization:

```
┌─────────────────────────────────────────────────┐
│ LEVEL 3: GLOBAL PROGRESS (All BUs)              │
│ Formula: Σ(BU Progress × BU Weight) / Σ(Weight) │
└──────────────┬──────────────────────────────────┘
               │
        ┌──────┼──────┬──────────┐
        │      │      │          │
┌───────▼──┐ ┌─▼─────┐ ┌────────▼───┐
│ BU #1    │ │ BU #2 │ │ BU #3      │  LEVEL 2: Business Unit Progress
│ Progress │ │ Prog. │ │ Progress   │  Formula: Σ(App Progress × Weight) / Σ(Weight)
└──────┬───┘ └───┬───┘ └────┬───────┘
       │         │          │
    ┌──┴──┐   ┌──┴──┐    ┌──┴──┐
    │ App │   │ App │    │ App │     LEVEL 1: Application Weight
    │     │   │     │    │     │     Formula: [(C × I × P) ÷ 27] × 3
    └─────┘   └─────┘    └─────┘
```

### Key Characteristics:
- **Weighted System**: More critical applications have greater impact on overall progress
- **Hierarchical**: Progress rolls up from applications → BUs → Global
- **Dynamic**: Changes in any application automatically propagate to higher levels
- **Normalized**: All weights fall within 0.11 - 3.00 range for consistency

---

## 🔧 Level 1: Application Weight

### Purpose
Calculate the relative importance of each application based on three business factors.

### Formula

```
Weight = [ (Criticality × Business Impact × Priority) ÷ 27 ] × 3
```

### Parameters

| Parameter | Range | Scale | Definition |
|-----------|-------|-------|-----------|
| **Criticality** | 1-3 | Low-High | How critical is this app to business operations? |
| **Business Impact** | 1-3 | Low-High | What's the business impact if this fails? |
| **Priority** | 1-3 | Low-High | What's the strategic priority of this app? |

### Range & Precision
- **Minimum Weight**: 0.11 (when all factors = 1)
- **Maximum Weight**: 3.00 (when all factors = 3)
- **Precision**: 0.01 (rounded to 2 decimal places)

### Mathematical Explanation

**Why divide by 27?**
- Maximum combination: 3 × 3 × 3 = 27
- This normalizes the score to 0-1 range

**Why multiply by 3?**
- Scales the 0-1 range to 0-3 range for business readability
- Allows single weights to be significant in calculations

### Calculation Examples

#### Example 1: Low-Priority Application
```
Criticality = 1  (Low critical)
Impact       = 1  (Low impact)
Priority     = 1  (Low priority)

Weight = [ (1 × 1 × 1) ÷ 27 ] × 3
       = [ 1 ÷ 27 ] × 3
       = 0.037 × 3
       = 0.11 ✓
```

#### Example 2: Medium-Importance Application
```
Criticality = 1  (Low critical)
Impact       = 2  (Medium impact)
Priority     = 3  (High priority)

Weight = [ (1 × 2 × 3) ÷ 27 ] × 3
       = [ 6 ÷ 27 ] × 3
       = 0.222 × 3
       = 0.67 ✓
```

#### Example 3: High-Priority Application
```
Criticality = 2  (Medium critical)
Impact       = 2  (Medium impact)
Priority     = 3  (High priority)

Weight = [ (2 × 2 × 3) ÷ 27 ] × 3
       = [ 12 ÷ 27 ] × 3
       = 0.444 × 3
       = 1.33 ✓
```

#### Example 4: Critical Application
```
Criticality = 3  (Highly critical)
Impact       = 3  (High impact)
Priority     = 3  (High priority)

Weight = [ (3 × 3 × 3) ÷ 27 ] × 3
       = [ 27 ÷ 27 ] × 3
       = 1.0 × 3
       = 3.00 ✓ (Maximum)
```

### Weight Distribution Table

| C | I | P | Calculation | Weight | Impact |
|---|---|---|-------------|--------|--------|
| 1 | 1 | 1 | (1/27)×3 | **0.11** | Minimal |
| 1 | 1 | 2 | (2/27)×3 | **0.22** | Very Low |
| 1 | 1 | 3 | (3/27)×3 | **0.33** | Very Low |
| 1 | 2 | 3 | (6/27)×3 | **0.67** | Low-Medium |
| 2 | 2 | 2 | (8/27)×3 | **0.89** | Medium |
| 2 | 2 | 3 | (12/27)×3 | **1.33** | Medium-High |
| 2 | 3 | 3 | (18/27)×3 | **2.00** | High |
| 3 | 3 | 3 | (27/27)×3 | **3.00** | Maximum |

---

## 📈 Level 2: Business Unit Progress

### Purpose
Calculate the overall progress of a Business Unit by considering the weighted progress of all its applications.

### Formula

```
BU Progress = Σ(Application Progress × Application Weight) / Σ(Application Weight)
```

Where:
- **Σ** = Summation (sum of all)
- **Application Progress** = Percentage completion (0-100%)
- **Application Weight** = Calculated from Level 1 formula

### Explanation

This is a **weighted average** that ensures:
1. Applications with higher weight (more critical) have greater impact
2. A single critical application at 0% significantly reduces BU progress
3. Multiple non-critical applications at 100% cannot fully compensate for a critical app at 0%

### Practical Example: CDA3 Business Unit

**Scenario**: CDA3 has 5 applications with different weights and progress levels.

| App ID | App Name | Weight | Progress | Weight × Progress |
|--------|----------|--------|----------|-------------------|
| 1 | XXX_APPLICATION_1_XXX | 0.67 | 100% | 0.67 |
| 2 | XXX_APPLICATION_2_XXX | 0.67 | 100% | 0.67 |
| 3 | XXX_APPLICATION_3_XXX | 0.67 | 84% | 0.56 |
| 4 | XXX_APPLICATION_4_XXX | 1.33 | 0% | 0.00 |
| 5 | XXX_APPLICATION_5_XXX | 2.00 | 22% | 0.44 |
| **TOTALS** | | **5.34** | | **2.34** |

```
CDA3 Progress = 2.34 / 5.34
              = 43.8%
```

**Interpretation**: Although 2 apps are at 100% and 1 at 84%, the BU progress is only 43.8% because:
- App #4 (weight 1.33) is completely stalled (0%)
- App #5 (weight 2.00) is barely started (22%)

---

### Real-World Scenarios

#### Scenario A: Uniform Progress
```
All apps have Weight = 1.0 and Progress = 75%

BU Progress = (1.0×75 + 1.0×75 + 1.0×75 + 1.0×75) / (1.0+1.0+1.0+1.0)
            = (75 + 75 + 75 + 75) / 4
            = 300 / 4
            = 75% ✓
```

#### Scenario B: Mixed Weights & Progress
```
Weight: [0.67, 1.33, 2.00]
Progress: [100%, 80%, 20%]

BU Progress = (0.67×100 + 1.33×80 + 2.00×20) / (0.67+1.33+2.00)
            = (67 + 106.4 + 40) / 4.00
            = 213.4 / 4.00
            = 53.35%
```

The high-weight critical app (2.00) at only 20% significantly drags down the overall progress.

---

## 🌍 Level 3: Global Progress

### Purpose
Calculate the organization-wide progress considering the weighted progress of each Business Unit.

### Formula

```
Global Progress = Σ(BU Progress × BU Weight) / Σ(BU Weight)
```

Where:
- **BU Progress** = Calculated from Level 2 formula
- **BU Weight** = Sum of all application weights in that BU
- **Σ** = Summation across all Business Units

### Explanation

This is a **weighted average of weighted averages**:
1. Each BU's progress is weighted by the sum of its application weights
2. BUs with more critical applications have greater impact on global progress
3. The organization-wide progress reflects true business criticality

### Extended Example: All Organization

**Scenario**: The organization has 3 Business Units with different application portfolios.

#### Step 1: Calculate Individual BU Weights

```
CDA3 BU:
├─ App1: Weight = 0.67
├─ App2: Weight = 0.67
├─ App3: Weight = 0.67
└─ BU TOTAL WEIGHT = 2.01

COMM BU:
├─ App4: Weight = 1.33
├─ App5: Weight = 1.33
└─ BU TOTAL WEIGHT = 2.66

HR BU:
├─ App6: Weight = 2.00
└─ BU TOTAL WEIGHT = 2.00
```

#### Step 2: Calculate BU Progress (Using Level 2 Formula)

```
CDA3 Progress = (0.67×100 + 0.67×100 + 0.67×84) / 2.01
              = (67 + 67 + 56.28) / 2.01
              = 190.28 / 2.01
              = 94.6%

COMM Progress = (1.33×80 + 1.33×60) / 2.66
              = (106.4 + 79.8) / 2.66
              = 186.2 / 2.66
              = 69.9%

HR Progress = (2.00×22) / 2.00
            = 44 / 2.00
            = 22.0%
```

#### Step 3: Calculate Global Progress (Level 3)

| BU | Progress | Weight | Progress × Weight |
|----|----------|--------|-------------------|
| CDA3 | 94.6% | 2.01 | 190.25 |
| COMM | 69.9% | 2.66 | 185.93 |
| HR | 22.0% | 2.00 | 44.00 |
| **TOTAL** | | **6.67** | **420.18** |

```
Global Progress = 420.18 / 6.67
                = 62.98%
                = 63.0% (rounded)
```

**Interpretation**: Despite CDA3 being at 94.6%, the organization is only at 63% because:
- HR is significantly lagging at 22%
- HR has the highest-weight application (2.00)
- This critical delay pulls down the entire organization

---

## 🔢 Excel Implementation

### Column Setup

```
Column A: ID
Column B: Application Name
Column C: Business Unit
Column D: Criticality (1-3)
Column E: Business Impact (1-3)
Column F: Business Priority (1-3)
Column G: Weight (CALCULATED)
Column H: Progress % (MANUAL)
Column I: Weight × Progress (CALCULATED)
```

### Level 1: Application Weight Formula

**Cell G2** (for first application):
```excel
=ROUND(((D2*E2*F2)/27)*3, 2)
```

**Copy down** to all application rows.

**Explanation**:
- `D2*E2*F2` → Multiply the three factors
- `÷27` → Normalize to 0-1 range
- `×3` → Scale to 0-3 range
- `ROUND(..., 2)` → Round to 2 decimal places

### Helper Column: Weight × Progress

**Cell I2**:
```excel
=G2*(H2/100)
```

This multiplies weight by progress percentage (H2/100 converts to decimal).

### Level 2: Business Unit Progress

**For each BU in summary table**:
```excel
=SUMIF($C$2:$C$100, BU_NAME, $I$2:$I$100) / SUMIF($C$2:$C$100, BU_NAME, $G$2:$G$100)
```

Where `BU_NAME` is the cell containing the BU name.

**Explanation**:
- `SUMIF(..., $I$2:$I$100)` → Sum of (Weight × Progress) for this BU
- `SUMIF(..., $G$2:$G$100)` → Sum of weights for this BU
- Division gives weighted average progress

### Level 3: Global Progress

**In summary cell**:
```excel
=SUM(BU_Progress_Range * BU_Weight_Range) / SUM(BU_Weight_Range)
```

Or as array formula:
```excel
=SUMPRODUCT(BU_Progress_Range, BU_Weight_Range) / SUM(BU_Weight_Range)
```

### Complete Excel Template Example

```
ROW 1: HEADERS
A    B                      C          D    E    F    G       H    I
ID   Application Name       BU         Crit Imp  Prio Weight  %    Wtd×Prog

ROW 2-N: DATA
1    XXX_APPLICATION_1_XXX  CDA3       1    2    3    0.67    100  0.67
2    XXX_APPLICATION_2_XXX  CDA3       1    2    3    0.67    100  0.67
3    XXX_APPLICATION_3_XXX  COMM       2    2    3    1.33    80   1.06
...

SUMMARY SECTION:
BU        Weight  Progress  Wtd×Prog
CDA3      1.34    =FORMULA  =FORMULA
COMM      1.33    =FORMULA  =FORMULA
HR        2.00    =FORMULA  =FORMULA

GLOBAL    4.67    =FORMULA  ← Overall progress
```

---

## 💻 Dashboard Implementation

### JavaScript Calculation (from dashboard_enhanced.html)

#### Level 1: Application Weight
```javascript
function calculateAppWeight(criticality, businessImpact, priority) {
  const numerator = criticality * businessImpact * priority;
  const normalized = (numerator / 27) * 3;
  return Math.round(normalized * 100) / 100; // 2 decimal places
}

// Example usage:
const weight = calculateAppWeight(1, 2, 3); // Returns 0.67
```

#### Level 2: Business Unit Progress
```javascript
function calculateBUProgress(apps, busUnit) {
  const buApps = apps.filter(app => app.buId === busUnit.id);
  
  if (buApps.length === 0) return 0;
  
  let weightedSum = 0;
  let totalWeight = 0;
  
  buApps.forEach(app => {
    const weight = calculateAppWeight(
      app.criticality, 
      app.businessImpact, 
      app.priority
    );
    const progress = app.progress || 0;
    
    weightedSum += (progress / 100) * weight;
    totalWeight += weight;
  });
  
  const buProgress = (totalWeight === 0) ? 0 : (weightedSum / totalWeight) * 100;
  return Math.round(buProgress * 10) / 10; // 1 decimal place
}
```

#### Level 3: Global Progress
```javascript
function calculateGlobalProgress(allBUs, apps) {
  let globalWeightedSum = 0;
  let globalTotalWeight = 0;
  
  allBUs.forEach(bu => {
    const buProgress = calculateBUProgress(apps, bu);
    const buWeight = calculateBUTotalWeight(bu, apps);
    
    globalWeightedSum += (buProgress / 100) * buWeight;
    globalTotalWeight += buWeight;
  });
  
  const globalProgress = (globalTotalWeight === 0) ? 0 : 
                         (globalWeightedSum / globalTotalWeight) * 100;
  return Math.round(globalProgress * 10) / 10; // 1 decimal place
}

function calculateBUTotalWeight(bu, apps) {
  return apps
    .filter(app => app.buId === bu.id)
    .reduce((sum, app) => {
      const weight = calculateAppWeight(
        app.criticality, 
        app.businessImpact, 
        app.priority
      );
      return sum + weight;
    }, 0);
}
```

---

## 📊 Real-World Examples

### Example 1: Small Organization (1 BU, 3 Apps)

**Setup**:
```
Business Unit: ENGINEERING
├─ Migration Platform
│  ├─ Criticality: 3 (Highly critical)
│  ├─ Impact: 3 (High impact)
│  ├─ Priority: 3 (High priority)
│  └─ Progress: 45%
│
├─ Data Pipeline
│  ├─ Criticality: 2
│  ├─ Impact: 2
│  ├─ Priority: 2
│  └─ Progress: 78%
│
└─ Analytics Dashboard
   ├─ Criticality: 1
   ├─ Impact: 2
   ├─ Priority: 1
   └─ Progress: 92%
```

**Calculations**:

Step 1: Calculate Weights
```
Migration:    [(3×3×3)/27]×3 = 3.00
Data Pipe:    [(2×2×2)/27]×3 = 0.89
Analytics:    [(1×2×1)/27]×3 = 0.22
Total Weight: 4.11
```

Step 2: Calculate BU Progress
```
Weighted Sum = (45/100×3.00) + (78/100×0.89) + (92/100×0.22)
             = 1.35 + 0.69 + 0.20
             = 2.24

BU Progress = (2.24 / 4.11) × 100 = 54.5%
```

**Result**: Despite Analytics Dashboard at 92%, the organization is only at 54.5% because the critical Migration Platform (weight 3.00) is still only 45% complete.

---

### Example 2: Large Organization (3 BUs, 10 Apps)

**CDA3 Business Unit**:
- 4 Applications, Total Weight: 5.34
- Calculated Progress: 43.8% (Example from Level 2)

**COMM Business Unit**:
```
├─ Workflow Engine (W: 1.33, P: 80%)
├─ Rules Engine (W: 1.33, P: 60%)
└─ Audit System (W: 0.67, P: 100%)
Total Weight: 3.33
Weighted Progress = (1.33×80 + 1.33×60 + 0.67×100) / 3.33 = 77.8%
```

**HR Business Unit**:
```
├─ Payroll System (W: 3.00, P: 22%)
├─ Leave Management (W: 0.67, P: 100%)
└─ Benefits Portal (W: 0.67, P: 85%)
Total Weight: 4.34
Weighted Progress = (3.00×22 + 0.67×100 + 0.67×85) / 4.34 = 41.9%
```

**Global Progress**:
```
Global = (43.8%×5.34 + 77.8%×3.33 + 41.9%×4.34) / (5.34+3.33+4.34)
       = (233.89 + 258.97 + 181.85) / 13.01
       = 674.71 / 13.01
       = 51.86%
       = 51.9% (rounded)
```

**Interpretation**: The organization is at 51.9% overall progress. The HR Payroll System (weight 3.00, only 22% complete) is the main bottleneck.

---

## ⚠️ Edge Cases & Validation

### Edge Case 1: Empty Business Unit

**Scenario**: A Business Unit exists but has no applications.

```javascript
function calculateBUProgress(apps, busUnit) {
  const buApps = apps.filter(app => app.buId === busUnit.id);
  
  if (buApps.length === 0) return 0; // Return 0, not undefined
  
  // ... rest of calculation
}
```

### Edge Case 2: All Applications at 0%

**Scenario**: BU has applications but all are at 0% progress.

```
Apps: W1=0.67 P=0%, W2=1.33 P=0%

BU Progress = (0.67×0 + 1.33×0) / (0.67+1.33) = 0 / 2.0 = 0%
```

Correctly returns 0%.

### Edge Case 3: Single Application BU

**Scenario**: BU has only one critical application.

```
Single App: Weight=3.00, Progress=50%

BU Progress = (3.00 × 0.50) / 3.00 = 1.50 / 3.00 = 50%
```

Progress equals the single application's progress (as expected).

### Edge Case 4: Extreme Weight Differences

**Scenario**: BU has one critical app and many trivial apps.

```
Critical App:  W=3.00, P=0%
Trivial App 1: W=0.11, P=100%
Trivial App 2: W=0.11, P=100%
Trivial App 3: W=0.11, P=100%

Total Weight = 3.33
Weighted Sum = (3.00×0 + 0.11×1 + 0.11×1 + 0.11×1) = 0.33

BU Progress = (0.33 / 3.33) × 100 = 9.9%
```

The 100% completion of trivial apps barely moves the needle (0.11/3.33 each = 3.3% impact).

### Validation Rules

1. **Weight Range Validation**:
   - Expected: 0.11 ≤ Weight ≤ 3.00
   - If outside: Flag as data error

2. **Progress Range Validation**:
   - Expected: 0% ≤ Progress ≤ 100%
   - If outside: Clamp to range [0, 100]

3. **Factor Range Validation**:
   - Expected: 1 ≤ Criticality, Impact, Priority ≤ 3
   - If outside: Flag as input error

4. **Total Weight Validation**:
   - If TotalWeight = 0: Return progress as 0%
   - Prevents division by zero errors

---

## 🔍 Verification Checklist

- [ ] All applications have valid weights (0.11-3.00 range)
- [ ] All progress values are 0-100%
- [ ] All criticality/impact/priority values are 1-3
- [ ] BU progress is between 0-100%
- [ ] Global progress is between 0-100%
- [ ] Formulas recalculate when any input changes
- [ ] Excel formulas use absolute/relative references correctly
- [ ] Dashboard updates in real-time as progress changes

---

## 📚 References

- **Dashboard Version**: v1.2.0+
- **Implementation File**: `dist/dashboard_enhanced.html`
- **Source Module**: `src/modules/DataProcessor.js`
- **Storage**: `localStorage['dashboard_config_v1']`

---

## 💬 Questions & Support

**Q: Why use a weighted system instead of simple average?**
A: Weighted systems reflect business reality where some applications are more critical than others. A 0% stalled critical app should impact progress more than a 0% stalled trivial app.

**Q: Can I change the formula?**
A: Yes, but all three levels must be recalibrated. The current formula is optimized for 0.11-3.00 range and 3-level hierarchy.

**Q: What if an application has no weight data?**
A: Default to Weight=1.0 (neutral) or exclude from calculations depending on business rules.

**Q: How often should I recalculate?**
A: Automatically on every progress update. Manual recalculation only for data corrections.

---

**Document prepared for technical reference and implementation guidance.**
