# Formula Calculation Configuration Guide - English

**Last Updated**: October 2025  
**Version**: 1.0  
**Audience**: Project Administrators, Analysts, Auditors

---

## Table of Contents

1. [Introduction](#introduction)
2. [Panel Access](#panel-access)
3. [Main Parameters](#main-parameters)
4. [Weighted Calculation](#weighted-calculation)
5. [Practical Examples](#practical-examples)
6. [FAQ](#faq)

---

## Introduction

### What are Calculation Formulas?

Formulas allow you to customize how the dashboard calculates the progress of each Business Unit (BU). You can adjust:

- **Calculation methods** for individual and overall progress
- **Status inclusion** (which statuses to count or ignore)
- **Application weights** (more important applications count more)
- **Criticality multipliers** (boost for critical applications)

### Why Customize Formulas?

Different organizations have different needs:

- **Agile teams**: May want more weight on work in progress
- **Critical projects**: May require high multipliers for critical apps
- **Audit**: May need to include/exclude specific statuses
- **Reporting**: May need simpler or more complex calculation methods

### Key Concepts

| Concept | Meaning |
|---------|---------|
| **BU (Business Unit)** | Department, product, or business line |
| **Application** | Software system under project control |
| **Status** | Current situation (TBS, WIP, CLO) |
| **Weight** | Relative importance (0.5=low, 3.0=high) |
| **Criticality** | Level of strategic importance |
| **Multiplier** | Factor that amplifies criticality impact |

---

## Panel Access

### Step 1: Open Setup
Click the **Setup** button (top right of dashboard).

### Step 2: Navigate to Formulas
Click the **"Calculation Formulas"** tab in the modal.

### Step 3: View Sections
The panel contains 5 main sections:

- **Progress Calculation Method**: Formula for each BU
- **Status Inclusion Rules**: Which statuses to include
- **Weight Parameters**: Range of weights
- **Criticality Multipliers**: Boost by criticality
- **Global Progress Formula**: How to combine BUs

---

## Main Parameters

### 1. Progress Calculation Method

Defines how to calculate each BU's progress.

#### Weighted Average (RECOMMENDED)

**Formula**: `BU Progress = Σ(App Progress × Weight) / Σ(Weight)`

**Example**:
- App A: 50% progress, weight 1.0
- App B: 100% progress, weight 2.0
- Result: (50×1 + 100×2) / 3 = 83%

**When to use**: When apps have different importance.

**Advantages**: Flexible, realistic.
**Disadvantages**: More complex to understand.

#### Simple Average

**Formula**: `BU Progress = Σ(App Progress) / Count(Apps)`

**Example**:
- App A: 50%
- App B: 100%
- Result: 75%

**When to use**: When all apps have equal importance.

**Advantages**: Easy to understand.
**Disadvantages**: Doesn't consider priorities.

#### Minimum Progress

**Formula**: `BU Progress = MIN(App1%, App2%, ...)`

**Example**:
- App A: 50%
- App B: 100%
- Result: 50%

**When to use**: When ALL apps must be complete.

**Advantages**: Reflects portfolio reality.
**Disadvantages**: Very conservative.

---

### 2. Status Inclusion Rules

Defines which statuses to include in calculations.

| Status | Code | Meaning | Default |
|--------|------|---------|---------|
| To Be Started | TBS | Not started | NO |
| Work in Progress | WIP | In progress | YES |
| Closed | CLO | Completed | YES |

**Behavior**:

- **Include TBS**: Unstarted apps count as 0%
- **Exclude TBS**: Unstarted apps are ignored
- **Include WIP**: In-progress apps contribute
- **Exclude WIP**: Only completed apps count

**Common scenarios**:

1. **Normal development**: Include TBS + WIP + CLO
2. **Executive reports**: Exclude TBS, include WIP + CLO
3. **Audit**: Only CLO
4. **Agile**: Exclude TBS, include WIP + CLO

---

### 3. Weight Parameters

Define the range of weights for applications.

| Parameter | Range | Default |
|-----------|-------|---------|
| Minimum Weight | 0.1 - 2.0 | 0.5 |
| Maximum Weight | 1.0 - 10.0 | 3.0 |
| Default Weight | Min - Max | 1.0 |

**Meaning**:

- **Min Weight**: Lowest allowed weight
- **Max Weight**: Highest allowed weight
- **Default**: Auto-assigned to new apps

**Usage in calculations**:

```
App Contribution = App Progress × App Weight
```

**Example**:

| App | Weight | Progress | Contribution |
|-----|--------|----------|--------------|
| CRM | 0.5 | 100% | 50% |
| Payment | 3.0 | 75% | 225% |
| Dashboard | 1.0 | 90% | 90% |
| Total | 4.5 | - | 365/450 = 81% |

---

### 4. Criticality Multipliers

Defines how app criticality amplifies impact.

| Level | Multiplier Default |
|------|-------------------|
| Low | 1.0 |
| Medium | 1.0 |
| High | 1.2 |

**How it works**:

```
Contribution = App Progress × App Weight × Criticality Multiplier
```

**Example**:

| App | Weight | Crit. | Mult. | Progress | Contrib. |
|-----|--------|-------|-------|----------|----------|
| Reporting | 1.0 | Low | 1.0 | 85% | 85% |
| Analytics | 2.0 | Med | 1.0 | 90% | 180% |
| Auth | 2.0 | High | 1.2 | 70% | 168% |
| Total | 5.0 | - | - | - | 433/600 = 72% |

**When to increase multipliers**:

- **1.2 - 1.5**: Critical business apps
- **1.5 - 2.0**: Apps that stop everything if they fail
- **No change**: Standard apps

---

### 5. Global Progress Formula

How to combine BUs in overall progress.

#### Weighted by BU Size

**Formula**: `Global = Σ(BU% × AppCount) / Σ(AppCount)`

BUs with more apps influence more.

**Example**:
- BU A (5 apps): 80% → 400
- BU B (2 apps): 60% → 120
- Total: 520/7 = 74%

#### Simple Average

**Formula**: `Global = Σ(BU%) / Count(BUs)`

All BUs count equally.

**Example**:
- BU A: 80%
- BU B: 60%
- Total: 70%

---

## Weighted Calculation

### Complete Formula

$$Progress = \frac{\sum (App\% \times Weight \times Criticality)}{\sum (Weight \times Criticality)}$$

### Step-by-Step Example

**Configuration**:
- Method: Weighted Average
- Status: TBS, WIP, CLO included
- Weights: Min=0.5, Default=1.0, Max=3.0
- Criticality: Low=1.0, Med=1.0, High=1.2

**Application Data**:

| App | Status | Progress | Weight | Crit. | Mult. |
|-----|--------|----------|--------|-------|-------|
| CRM | CLO | 100% | 1.0 | Low | 1.0 |
| Portal | WIP | 75% | 2.0 | High | 1.2 |
| API | TBS | 0% | 0.5 | Med | 1.0 |
| Reports | CLO | 90% | 1.5 | High | 1.2 |

**Calculation**:

```
Numerator:
CRM:     100 × 1.0 × 1.0 = 100
Portal:   75 × 2.0 × 1.2 = 180
API:       0 × 0.5 × 1.0 = 0
Reports:  90 × 1.5 × 1.2 = 162
                          = 442

Denominator:
CRM:     1.0 × 1.0 = 1.0
Portal:  2.0 × 1.2 = 2.4
API:     0.5 × 1.0 = 0.5
Reports: 1.5 × 1.2 = 1.8
                    = 5.7

Result: 442 / 5.7 = 77.54%
```

---

## Practical Examples

### Case 1: Small Startup

**Context**: Small team, few apps, all critical.

**Configuration**:
- Progress Method: Weighted Average
- Status: Include TBS, WIP, CLO
- Weights: Min=0.5, Default=1.0, Max=2.0
- Criticality: Low=1.0, Med=1.1, High=1.3
- Global: Simple Average

**Justification**: All apps are critical, little variance.

---

### Case 2: Large Enterprise

**Context**: Large portfolio, apps with different importance.

**Configuration**:
- Progress Method: Weighted Average
- Status: Exclude TBS, include WIP, CLO
- Weights: Min=0.3, Default=1.0, Max=5.0
- Criticality: Low=0.9, Med=1.0, High=1.5
- Global: Weighted by BU Size

**Justification**: Many variations, critical apps impact more.

---

### Case 3: Audit/Compliance

**Context**: Only cares about completion.

**Configuration**:
- Progress Method: Minimum Progress
- Status: Only CLO
- Weights: Min=1.0, Default=1.0, Max=1.0
- Criticality: All=1.0
- Global: Simple Average

**Justification**: Only completed things count, no weighting.

---

### Case 4: Agile/Iterative

**Context**: Emphasis on work in progress.

**Configuration**:
- Progress Method: Weighted Average
- Status: Exclude TBS, include WIP, CLO
- Weights: Min=0.5, Default=1.0, Max=3.0
- Criticality: Low=1.0, Med=1.1, High=1.2
- Global: Weighted by BU Size

**Justification**: Includes WIP but not TBS, allows variation.

---

## Export and Import

### Export

1. Configure desired parameters
2. Click "Save Configuration"
3. Go to Settings → Export Configuration
4. Downloads JSON with everything: BUs, Apps, Waves, **Formulas**, Whitelabel

### Import

1. Go to Settings → Import Configuration
2. Select exported JSON file
3. Automatically:
   - Restores BUs and Apps
   - **Restores formulas**
   - Restores Whitelabel
   - Recalculates progress

**Note**: Supports files without formula config (backward compatible).

---

## FAQ

### Q1: Difference between Weighted and Simple Average?

**A**: Weighted gives more importance to apps with higher weight. Simple treats all equally.

**Example**:
- Critical App: 50% (weight 3.0)
- Normal App: 100% (weight 1.0)
- Weighted: 62.5%
- Simple: 75%

### Q2: When to use Minimum Progress?

**A**: Only when ALL apps must be complete. Example: data migration.

### Q3: Can I change formulas mid-project?

**A**: Yes, but historical numbers will change. **Recommendation**: Decide at start.

### Q4: What if I don't include TBS?

**A**: They're ignored, don't affect calculation. Makes progress look higher.

### Q5: How do I know what weights to assign?

**A**: Key questions:
- Impact if it fails? → Defines criticality
- More important than others? → Higher weight
- Standard? → Weight 1.0
- Minor? → Weight 0.5

### Q6: Can multipliers be > 1.2?

**A**: Yes. Recommendations:
- 1.0 - 1.2: Small boost
- 1.2 - 1.5: Moderate boost
- > 1.5: Maximum impact

### Q7: What is "Weighted by BU Size"?

**A**: BUs with more apps influence more in global progress.

### Q8: Are formulas lost if I clear data?

**A**: No. Saved in localStorage. Reset returns to defaults.

### Q9: Export only formulas?

**A**: No. Export with complete project. Others import and get formulas automatically.

### Q10: How do I validate formulas?

**A**: Use "Test Calculation" button. Shows step-by-step application.

---

## Quick Summary

### Configuration Steps

1. Setup → Calculation Formulas
2. Choose Progress Method
3. Define Status Inclusion
4. Configure Weights
5. Adjust Criticality Multipliers
6. Choose Global Formula
7. Save with "Save Configuration"
8. Test with "Test Calculation"

### Key Variables

| Variable | Range | Default | Impact |
|----------|-------|---------|--------|
| Progress Method | 3 options | Weighted | **HIGH** |
| Status Inclusion | TBS/WIP/CLO | WIP,CLO | **HIGH** |
| Min Weight | 0.3-2.0 | 0.5 | Low |
| Max Weight | 1.0-10.0 | 3.0 | **HIGH** |
| Default Weight | Min-Max | 1.0 | Medium |
| Low Multiplier | 0.5-1.5 | 1.0 | Low |
| Med Multiplier | 0.5-1.5 | 1.0 | Low |
| High Multiplier | 1.0-2.0 | 1.2 | **HIGH** |
| Global Formula | 2 options | Weighted | Medium |

---

**Version**: 1.0 | **Last Updated**: October 2025
