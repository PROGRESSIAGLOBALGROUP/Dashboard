# Complete Formula Configuration Guide (English)

**Last Updated**: October 2025  
**For**: Expert Administrators, Data Analysts, Auditors  
**Time**: 30 minutes  
**Languages**: English & Spanish

---

## Table of Contents

1. [Introduction](#introduction)
2. [Accessing the Formula Panel](#accessing-the-formula-panel)
3. [Main Parameters Explained](#main-parameters-explained)
4. [Understanding Weighted Calculation](#understanding-weighted-calculation)
5. [Mathematical Deep Dive](#mathematical-deep-dive)
6. [Practical Scenarios](#practical-scenarios)
7. [Troubleshooting Matrix](#troubleshooting-matrix)
8. [Advanced Topics](#advanced-topics)
9. [Frequently Asked Questions](#frequently-asked-questions)

---

## Introduction

Dashboard Enhanced uses **weighted formulas** to calculate overall progress for each Business Unit (BU). These formulas aggregate individual application progress into meaningful metrics.

### Key Concepts

**Application (App)**: A project or system being tracked (has progress 0-100%).

**Business Unit (BU)**: Groups applications and displays their weighted progress.

**Formula**: Algorithm combining individual app progress into a single BU progress value.

**Weight**: Multiplier showing app importance (ranges 0.3 to 10.0).

**Status Inclusion**: Controls whether TBS/WIP/CLO apps are included in calculation.

**Criticality**: Additional multiplier for app severity (ranges 0.5 to 2.0).

### Why Formulas Matter

Different formulas produce different results:
- **Same data, different formula = different insights**
- Formula choice affects: executive reporting, resource allocation, deadline decisions
- Must match organizational needs and governance rules

---

## Accessing the Formula Panel

### Step 1: Open Admin Panel
In Dashboard Enhanced, click the **⚙️ Admin** button in the top-right corner.

### Step 2: Click "Calculation Formulas"
In the admin menu, click the **Calculation Formulas** tab.

### Step 3: Formula Configuration Panel Opens
You'll see a form with sections:
- Progress Calculation Method
- Status Inclusion Rules
- Application Weights
- Criticality Multipliers
- Global Formula

### Step 4: Make Changes (Don't Auto-Save!)
**Important**: Changes are NOT automatically saved. Modifications display in real-time ONLY for testing.

### Step 5: Test Your Changes
Click **"Test Calculation"** to see results without saving.

### Step 6: Save When Ready
Click **"Save Configuration"** to persist changes to localStorage.

---

## Main Parameters Explained

### 1. Progress Calculation Method

**Purpose**: Defines algorithm for combining app progress values.

**Options**:

#### A. Weighted Average (Recommended)

**Formula**:
$$BU Progress = \frac{\sum (App \% \times Weight \times Criticality)}{\sum (Weight \times Criticality)}$$

**How it works**:
1. Multiply each app progress by its weight
2. Multiply that result by criticality multiplier
3. Sum all results
4. Divide by sum of all (weight × criticality) pairs

**Use when**:
- Apps have different importance
- Some apps are more critical than others
- Realistic governance model exists

**Example**:
```
App1: 50% progress × 2.0 weight × 1.0 criticality = 100 points
App2: 80% progress × 1.0 weight × 1.2 criticality = 96 points

Divisor: (2.0 × 1.0) + (1.0 × 1.2) = 3.2 points

BU Progress: (100 + 96) / 3.2 = 61.25%
```

**Pros**: Realistic, accounts for priority, customizable
**Cons**: Requires maintenance, more complex

---

#### B. Simple Average

**Formula**:
$$BU Progress = \frac{\sum App \%}{Count(Apps)}$$

**How it works**:
1. Add all app progress percentages
2. Divide by number of apps

**Use when**:
- All apps equally important
- Simple governance preferred
- New to metrics

**Example**:
```
App1: 50%
App2: 80%
App3: 100%

BU Progress: (50 + 80 + 100) / 3 = 76.67%
```

**Pros**: Simple, transparent, no tuning needed
**Cons**: Ignores priority, unrealistic for heterogeneous apps

---

#### C. Minimum Progress

**Formula**:
$$BU Progress = MIN(App1 \%, App2 \%, ...)$$

**How it works**:
1. Find app with lowest progress
2. That becomes the BU progress

**Use when**:
- ALL apps must be complete
- Compliance/audit focused
- Critical path methodology

**Example**:
```
App1: 50%
App2: 80%
App3: 100%

BU Progress: 50% (the minimum)
```

**Pros**: Emphasizes bottlenecks, very conservative
**Cons**: Ignores most data, single app can block

---

### 2. Status Inclusion Rules

**Purpose**: Controls whether apps in each status are included.

**Status Meanings**:
- **TBS** = To Be Started (not yet begun)
- **WIP** = Work In Progress (active)
- **CLO** = Closed/Completed (finished)

**Options** (combinable):

#### Include TBS (To Be Started)
- ✓ Include = future work counted as 0%
- ✗ Exclude = future work ignored

#### Include WIP (Work In Progress)
- ✓ Include = active work counted (recommended)
- ✗ Exclude = active work ignored (unusual)

#### Include CLO (Closed/Completed)
- ✓ Include = finished work counted as 100%
- ✗ Exclude = finished work ignored

**Common Presets**:

| Preset | TBS | WIP | CLO | Use Case |
|--------|-----|-----|-----|----------|
| **Future-Focused** | ✓ | ✓ | ✓ | Include everything; realistic timeline |
| **Active Only** | ✗ | ✓ | ✗ | Focus on current work; ignore past/future |
| **Through Completion** | ✗ | ✓ | ✓ | Track active + finished; ignore planned |
| **Conservative** | ✗ | ✗ | ✓ | Only count finished work (very strict) |

**Recommended**: Future-Focused (TBS + WIP + CLO)
- **Reason**: Reflects reality that future work exists
- **Effect**: More conservative progress (0% pull down from TBS)

---

### 3. Application Weights

**Purpose**: Assign relative importance to each app.

**Range**: 0.3 (low importance) to 10.0 (critical importance)

**Default**: 1.0 (neutral)

**Meaning**:
- 0.3 = "This app is 30% as important as default"
- 1.0 = "This app is standard importance"
- 3.0 = "This app is 3× more important than standard"
- 10.0 = "This app is critically important"

**How to assign**:

1. **Identify importance tiers**:
   - Tier 1 (Critical): Weight 2.0 - 10.0
   - Tier 2 (Standard): Weight 0.8 - 1.2
   - Tier 3 (Minor): Weight 0.3 - 0.7

2. **Set for each app** in the form

3. **Test with calculation** to see impact

**Examples**:

| App | Importance | Weight | Reason |
|-----|-----------|--------|--------|
| Core Banking System | Critical | 5.0 | Revenue-blocking |
| Mobile App | High | 2.0 | Customer-facing |
| Data Pipeline | Standard | 1.0 | Default |
| Admin Dashboard | Low | 0.5 | Internal only |

---

### 4. Criticality Multipliers

**Purpose**: Applies additional urgency/severity to weight.

**Scale**: 0.5 (low concern) to 2.0 (extreme concern)

**Default**: 1.0 (no adjustment)

**Meaning**:
- 0.5 = "Half as critical as its weight suggests"
- 1.0 = "Weight is accurate as-is"
- 1.5 = "50% more urgent than weight suggests"
- 2.0 = "Double the urgency due to severity"

**When to use**:
- App has regulatory requirement → 1.5-2.0
- App has contract SLA → 1.2-1.5
- App has internal only impact → 0.8-1.0
- App is non-critical → 0.5-0.8

**Example**:
```
Core Banking System
  Weight: 5.0
  Criticality: 1.5 (regulatory deadline)
  Effective: 5.0 × 1.5 = 7.5 point weight

Mobile App
  Weight: 2.0
  Criticality: 1.2 (customer SLA)
  Effective: 2.0 × 1.2 = 2.4 point weight

Admin Dashboard
  Weight: 0.5
  Criticality: 0.8 (low impact)
  Effective: 0.5 × 0.8 = 0.4 point weight
```

---

### 5. Global Formula

**Purpose**: Determines how BU progress aggregates to organizational level.

**Options**:

#### A. Weighted by Business Unit Size

**Logic**: Larger BUs have higher weight in company total.

**Use when**:
- BUs have different sizes/budgets
- Reflect organizational structure
- Realistic weighting needed

#### B. Simple Average

**Logic**: All BUs contribute equally.

**Use when**:
- BUs are similar size
- Equal governance desired
- Simplicity preferred

---

## Understanding Weighted Calculation

### The Complete Formula

$$Weighted Progress = \frac{\sum_{i=1}^{n} (Progress_i \times Weight_i \times Criticality_i)}{\sum_{i=1}^{n} (Weight_i \times Criticality_i)}$$

Where:
- $Progress_i$ = Individual app progress (0-100%)
- $Weight_i$ = App importance factor (0.3-10.0)
- $Criticality_i$ = Urgency multiplier (0.5-2.0)
- $n$ = Number of apps in calculation

### Step-by-Step Example

**Scenario**: Manufacturing company with 3 key systems

**Input Data**:
| App | Progress | Weight | Criticality | Reason |
|-----|----------|--------|-------------|--------|
| ERP System | 65% | 3.0 | 1.5 | Core ops, regulatory |
| Supply Chain | 85% | 2.0 | 1.0 | Important, stable |
| Analytics | 40% | 1.0 | 0.8 | Supporting tool |

**Calculation**:

**Step 1**: Calculate weighted value for each app
```
ERP:         65% × 3.0 × 1.5 = 0.65 × 3.0 × 1.5 = 2.925
Supply:      85% × 2.0 × 1.0 = 0.85 × 2.0 × 1.0 = 1.700
Analytics:   40% × 1.0 × 0.8 = 0.40 × 1.0 × 0.8 = 0.320
```

**Step 2**: Sum numerator
```
Total Numerator = 2.925 + 1.700 + 0.320 = 4.945
```

**Step 3**: Calculate divisor (sum of weight × criticality)
```
ERP:         3.0 × 1.5 = 4.5
Supply:      2.0 × 1.0 = 2.0
Analytics:   1.0 × 0.8 = 0.8

Total Divisor = 4.5 + 2.0 + 0.8 = 7.3
```

**Step 4**: Divide
```
BU Progress = 4.945 / 7.3 = 67.74%
```

**Result**: Manufacturing BU = 67.74% progress

### Understanding the Result

Why not 63.33% (simple average)?
- **ERP** is critical and heavily weighted (pulls up the average)
- **Supply Chain** is doing well and important (maintains progress)
- **Analytics** is low but low-importance (minimal drag)

Result is higher than simple average because:
- Numerator emphasizes high-performing, high-weight apps
- Divisor normalizes by importance

---

## Mathematical Deep Dive

### Weighted vs. Simple Average

**Scenario**: Company deciding on formula

**Three Apps**:
- App A: 30% (Weight 1.0)
- App B: 50% (Weight 1.0)
- App C: 90% (Weight 1.0)

#### Simple Average:
$$Progress = (30 + 50 + 90) / 3 = 56.67\%$$

#### Weighted Average (Uniform):
$$Progress = \frac{(30 \times 1) + (50 \times 1) + (90 \times 1)}{(1 + 1 + 1)} = 56.67\%$$

**Result**: Same! (Because all weights equal.)

---

### Adding Realistic Weights

**New scenario**: App C is critical, A is experimental

- App A: 30% (Weight 0.5)
- App B: 50% (Weight 1.0)
- App C: 90% (Weight 3.0)

#### Simple Average (ignoring weights):
$$Progress = 56.67\%$$

#### Weighted Average:
$$Progress = \frac{(30 \times 0.5) + (50 \times 1) + (90 \times 3)}{(0.5 + 1 + 3)}$$
$$= \frac{15 + 50 + 270}{4.5} = \frac{335}{4.5} = 74.44\%$$

**Interpretation**: With realistic weights, company shows 74.44% (not 56.67%).
- **Reason**: Well-performing critical app (C at 90%) has high weight
- **Effect**: More optimistic but realistic view

---

### Impact of Criticality Multipliers

**Adding urgency** to scenario above:

- App A: 30% (Weight 0.5, Criticality 1.0)
- App B: 50% (Weight 1.0, Criticality 1.2) [SLA concern]
- App C: 90% (Weight 3.0, Criticality 0.9) [Less urgent than appears]

#### With Criticality:
$$Numerator = (30 \times 0.5 \times 1.0) + (50 \times 1.0 \times 1.2) + (90 \times 3.0 \times 0.9)$$
$$= 15 + 60 + 243 = 318$$

$$Divisor = (0.5 \times 1.0) + (1.0 \times 1.2) + (3.0 \times 0.9)$$
$$= 0.5 + 1.2 + 2.7 = 4.4$$

$$Progress = 318 / 4.4 = 72.27\%$$

**Interpretation**: From 74.44% → 72.27% (lower).
- **Reason**: App B urgency up (multiplier 1.2), C urgency down (0.9)
- **Effect**: Balanced against other factors

---

## Practical Scenarios

### Scenario 1: Startup (18 months, funding-sensitive)

**Characteristics**:
- Few apps (2-4)
- All equally important
- Timeline to launch critical
- No finished apps yet

**Recommended Configuration**:

```
Calculation Method:    Simple Average
Status Inclusion:      WIP + CLO (exclude TBS to avoid 0% drag)
Weights:               All 1.0 (equal importance)
Criticality:           All 1.0 (standard urgency)
Global Formula:        N/A (single BU)
```

**Rationale**:
- Simple governance matches startup stage
- Exclude TBS because all work is active
- Equal weights until differentiation needed
- Focus on active work momentum

---

### Scenario 2: Enterprise (Complex structure)

**Characteristics**:
- Many apps (20+)
- Heterogeneous importance
- Regulatory requirements
- Multiple finished apps

**Recommended Configuration**:

```
Calculation Method:    Weighted Average
Status Inclusion:      TBS + WIP + CLO (complete picture)
Weights:               Varies (0.5-5.0) by app type
Criticality:           Varies (0.8-1.5) by regulatory/SLA
Global Formula:        Weighted by BU Size
```

**Rationale**:
- Weighted reflects organizational reality
- Include all statuses for complete visibility
- Differentiate by business impact
- Use criticality for compliance/SLA apps
- Global formula reflects company structure

**Example Distribution**:
- Critical systems (ERP, Core): Weight 3-5, Criticality 1.3-1.5
- Standard systems (CRM, HCM): Weight 1.0-2.0, Criticality 1.0
- Supporting tools (Analytics, Admin): Weight 0.5-1.0, Criticality 0.8

---

### Scenario 3: Audit/Compliance

**Characteristics**:
- All apps equally important
- Only completed work counts
- Evidence trail required
- Conservative approach

**Recommended Configuration**:

```
Calculation Method:    Minimum Progress
Status Inclusion:      CLO only (only finished)
Weights:               Not applicable
Criticality:           Not applicable
Global Formula:        Simple Average (all BUs equal)
```

**Rationale**:
- Minimum ensures nothing gets missed
- CLO-only is conservative/auditable
- Weights unnecessary with Minimum
- Simple average for fairness

**Result**: Very conservative progress (bottleneck-driven).

---

### Scenario 4: Agile/Project-Based

**Characteristics**:
- Work organized in waves/sprints
- Rapid status changes
- Focus on active work
- Completion important but not blocking

**Recommended Configuration**:

```
Calculation Method:    Weighted Average
Status Inclusion:      WIP + CLO (active + finished)
Weights:               By priority/story points
Criticality:           By sprint importance (0.9-1.2)
Global Formula:        Simple Average (team equality)
```

**Rationale**:
- Weighted reflects story point allocations
- Include WIP + CLO to track momentum
- Exclude TBS (sprints plan ahead)
- Criticality reflects sprint goals
- Simple global for team fairness

---

## Troubleshooting Matrix

| Symptom | Cause | Solution |
|---------|-------|----------|
| **Progress too low (20-30%)** | Too many TBS apps, or very low-progress apps | Increase weights of high-progress apps; consider excluding TBS |
| **Progress too high (90%+)** | Weights favor complete apps, or excluding incomplete | Lower weights of complete apps; include TBS/WIP |
| **One app dominates** | App has very high weight | Reduce weight to 1-2 range; check criticality |
| **Progress doesn't move** | Minimum method selected | Change to Weighted/Simple; check status inclusion |
| **Unexpected result** | Weights/criticality misconfigured | Use Test Calculation; verify each app's input |
| **Can't lower progress** | Minimum method with all CLO apps | Switch method; add incomplete apps |
| **Changes not saving** | Forgot to click Save | After changes, click "Save Configuration" |
| **Changes reverted** | Didn't save before leaving admin panel | Repeat and click "Save Configuration" |

---

## Advanced Topics

### Topic 1: Dynamic Weight Adjustment

**Scenario**: Apps change importance over time.

**Solution**:
1. Access Calculation Formulas tab
2. Modify weights for affected apps
3. Click "Test Calculation" to preview
4. Click "Save Configuration"

**Timeline Example**:
```
Month 1:  Feature A (1.0), Feature B (2.0)
Month 2:  Feature A (2.0), Feature B (1.0)  [Switch focus]
Month 3:  Feature A (1.5), Feature B (1.5)  [Balance]
```

### Topic 2: Status-Based Adjustment

**Pattern**: Change status inclusion by project phase.

**Phase 1 - Planning**:
- Include TBS/WIP/CLO
- Show total commitment

**Phase 2 - Execution**:
- Include WIP/CLO
- Focus on active work

**Phase 3 - Closure**:
- Include CLO only
- Measure completion

### Topic 3: Validation Strategy

**Always test before deploying**:

1. Note current progress
2. Make adjustment
3. Click "Test Calculation"
4. Compare results
5. If satisfied: "Save Configuration"
6. If not: Try different values

**Test Cases to Verify**:
- ✓ Adding an app changes formula result
- ✓ Changing app progress updates percentage
- ✓ Weight changes impact total
- ✓ Status inclusion affects apps included
- ✓ Export/import preserves settings

---

## Frequently Asked Questions (FAQ)

### Q1: What's the difference between Weight and Criticality?

**Weight** = How important is this app?
**Criticality** = How urgent is completion?

**Example**:
- App might be Weight 3.0 (very important) but Criticality 0.8 (not urgent)
- Another app might be Weight 1.0 (standard importance) but Criticality 1.5 (deadline pressure)

### Q2: When should I use Simple Average instead of Weighted?

Use Simple Average when:
- Apps are genuinely equal importance
- Governance prefers simplicity
- You're unsure (start simple, customize later)

Use Weighted when:
- Apps have different impact
- Realistic weighting exists
- Organization requires differentiation

### Q3: How often should I adjust the formula?

**Typical Frequency**:
- Monthly review (quarterly adjustment)
- When organizational structure changes
- When new apps added/removed
- When regulations change

**Not every day**: Formula should be stable for meaningful trend tracking.

### Q4: Can I have different formulas for different BUs?

**Current**: One formula applies to all BUs.

**Workaround**: Adjust weights/criticality per app (which can differ by BU if desired).

**Future**: Custom per-BU formulas possible but not implemented.

### Q5: What if an app has no data?

**Handling**: Apps without progress default to 0%.

**Recommendation**: Remove app temporarily or assign placeholder value (5-10%) if expected.

### Q6: How does export/import work?

**Export**: Current formula configuration saved in JSON.
**Import**: Load previously saved configuration.

**Use case**: Share configuration across teams or backup before changes.

### Q7: Can I revert to a previous formula?

**Direct undo**: No. Plan: Take note of settings before changes.

**Alternative**: Use export/import to save configurations as checkpoints.

### Q8: What's the impact of Minimum Progress method?

**Effect**: Very conservative (only as good as worst app).

**Use sparingly**: Usually for audit/compliance only.

**Example**:
```
Apps: 90%, 85%, 50%, 95%
Simple Average: 80%
Weighted Average: ~85%
Minimum: 50% (the bottleneck)
```

### Q9: How do weights interact with criticality?

**Formula**: App Impact = Weight × Criticality

**Interaction**:
- Weight 2.0 + Criticality 1.5 = 3.0× effective weight
- Weight 3.0 + Criticality 0.8 = 2.4× effective weight

**Best practice**: Adjust both for realistic scaling.

### Q10: Is there a "best" formula?

**No universal best**. Choose based on:
- Organization size (startup vs. enterprise)
- Industry (manufacturing vs. startup)
- Governance style (simple vs. rigorous)
- Your specific needs

**Start here**: Use recommended presets, customize as needed.

---

## Support & Resources

**Problems?**
1. Check "Troubleshooting Matrix" above
2. Review "Practical Scenarios" for your type
3. Read "FAQ" for common questions

**Want to learn more?**
- See `FORMULA_QUICKSTART_EN.md` for fast reference
- See `FORMULA_REFERENCE_CARD_EN.md` for lookup tables
- See `README_FORMULAS_EN.md` for navigation

**Ready to configure?**
1. Open Dashboard Enhanced
2. Click Admin ⚙️
3. Click "Calculation Formulas"
4. Follow "Accessing the Formula Panel" section

---

**Last Updated**: October 2025  
**Version**: 1.0 (Complete)  
**Languages**: English & Spanish
