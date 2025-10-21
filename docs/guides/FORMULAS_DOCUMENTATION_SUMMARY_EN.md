# Formulas Documentation Summary (English)

**Last Updated**: October 2025  
**Version**: 1.0  
**Scope**: Complete formula system documentation overview

---

## What This Project Includes

This documentation package provides complete guidance for configuring weighted progress formulas in Dashboard Enhanced.

### Documentation Set

| Document | Purpose | Time | Audience |
|----------|---------|------|----------|
| **README_FORMULAS_EN.md** | Navigation & reading flows | 5 min | Everyone |
| **FORMULA_QUICKSTART_EN.md** | Fast practical guide | 5 min | Implementers |
| **FORMULA_GUIDE_EN.md** | Complete reference | 30 min | Experts |
| **FORMULA_REFERENCE_CARD_EN.md** | Quick lookup sheet | 1 min | Users |
| **FORMULA_CONFIGURATION_GUIDE_EN.md** | Exhaustive technical | 45 min | Analysts |
| **This file** | Summary & overview | 10 min | Project leads |

---

## Core Concepts Summary

### Three Formula Types Available

**1. Weighted Average** (Recommended)
- Accounts for app importance
- Customizable weights (0.3-10.0)
- Customizable criticality (0.5-2.0)
- Formula: `Σ(Progress × Weight × Criticality) / Σ(Weight × Criticality)`
- Use: Complex organizations with priority differentiation

**2. Simple Average**
- All apps equally important
- No customization needed
- Formula: `Σ(Progress) / Count(Apps)`
- Use: Startups or when simplicity preferred

**3. Minimum Progress**
- Only lowest-progress app matters
- Conservative approach
- Formula: `MIN(App1, App2, ...)`
- Use: Audit/compliance (all must complete)

### Five Main Decisions

| Decision | Impact | Options | Default |
|----------|--------|---------|---------|
| Calculation Method | Very High | Weighted / Simple / Minimum | Weighted |
| Status Inclusion | High | TBS / WIP / CLO | All three |
| App Weights | High | 0.3 - 10.0 | 1.0 |
| Criticality | High | 0.5 - 2.0 | 1.0 |
| Global Formula | Medium | Weighted / Simple | Weighted by Size |

---

## Key Learning Outcomes

After reading these documents, you will understand:

✅ How to access the formula configuration panel
✅ What each parameter does
✅ How calculations actually work
✅ When to use each formula type
✅ How to customize for your organization
✅ How to test configurations safely
✅ How to troubleshoot problems
✅ Real-world scenarios and examples
✅ How to validate your setup
✅ How to export/import configurations

---

## Implementation Patterns

### Pattern 1: Startup (Simple)

```
Method:         Simple Average
Status:         WIP + CLO
Weights:        All 1.0
Criticality:    All 1.0
Global:         N/A
Time to set up: 2 minutes
```

Result: Very transparent, easy to explain.

### Pattern 2: Enterprise (Realistic)

```
Method:         Weighted Average
Status:         TBS + WIP + CLO
Weights:        Varies (0.5-5.0)
Criticality:    Varies (0.8-1.5)
Global:         Weighted by Size
Time to set up: 30 minutes
```

Result: Reflects organizational reality.

### Pattern 3: Audit (Conservative)

```
Method:         Minimum Progress
Status:         CLO only
Weights:        N/A
Criticality:    N/A
Global:         Simple
Time to set up: 5 minutes
```

Result: Very strict, evidence-based.

---

## Configuration Workflow

### Step-by-Step Process

1. **Decide formula method** → Weighted / Simple / Minimum
2. **Define status inclusion** → Which statuses count?
3. **Assign app weights** → How important is each?
4. **Set criticalities** → Any apps more urgent?
5. **Choose global formula** → How do BUs aggregate?
6. **Test calculation** → Does result make sense?
7. **Save configuration** → Persist to storage
8. **Export for backup** → Save JSON file
9. **Document decisions** → Why you chose this
10. **Monitor over time** → Quarterly review

**Total time**: 5-45 minutes depending on complexity.

---

## Common Use Cases

### Use Case 1: Project Management Office (PMO)

**Challenge**: Multiple projects, complex priorities, need strong governance.

**Solution**:
- Weighted Average method
- Include all statuses
- Differentiate weights by project criticality
- Set criticality multipliers for deadline pressure
- Use Test Calculation frequently

**Expected result**: Realistic progress reflecting priorities.

---

### Use Case 2: Software Development Team

**Challenge**: Rapid changes, many small features, focus on velocity.

**Solution**:
- Simple Average or Weighted (if story points vary)
- Include WIP + CLO (active and finished)
- Exclude TBS (don't count future work)
- Use story points for weights
- Quarterly review/adjustment

**Expected result**: Clear momentum visibility.

---

### Use Case 3: Compliance/Audit Department

**Challenge**: All items must complete, need evidence, very conservative.

**Solution**:
- Minimum Progress method (strict)
- Include CLO only (finished work)
- Ignore weights/criticality
- Use Test Calculation for validation
- Export for audit trail

**Expected result**: Very conservative (shows bottlenecks).

---

### Use Case 4: Executive Dashboard

**Challenge**: Show organization-wide progress, high-level view.

**Solution**:
- Weighted Average method
- Include all statuses (complete picture)
- Aggregate BUs with weighted global formula
- Simple weights (1.0 mostly)
- High criticality for strategic initiatives

**Expected result**: Executive-friendly realistic overview.

---

## Frequently Needed Answers

### Q: Can I change the formula without losing data?

**A**: Yes. Formula changes only affect future calculations; historical data unchanged.

### Q: How do I know if my formula is right?

**A**: Test it. Does result match your intuition? Use "Test Calculation" before saving.

### Q: What if one app is blocking everything?

**A**: This is expected with Minimum method. Shows bottleneck. Consider:
1. Switch to Weighted Average
2. Or lower that app's weight
3. Or lower its criticality

### Q: Can I revert to old formula?

**A**: No direct undo. Export configs as checkpoints before major changes.

### Q: How often should I review?

**A**: Quarterly is reasonable. Monthly if organization changes rapidly.

### Q: Should everyone have same weights?

**A**: Not necessarily. Weights should reflect your organizational reality.

---

## Validation Checklist

Before deploying a formula to production, verify:

- [ ] Calculation method chosen and documented
- [ ] Status inclusion decided (TBS/WIP/CLO)
- [ ] All apps have weights assigned
- [ ] Criticalities set for special cases
- [ ] Global formula selected
- [ ] "Test Calculation" results reviewed
- [ ] Results match expectations
- [ ] All stakeholders agree
- [ ] Configuration saved
- [ ] Configuration exported and backed up
- [ ] Documented rationale for each decision

**Time required**: 30-60 minutes for thorough validation.

---

## Troubleshooting Quick Guide

| Problem | Quick Fix | Full Details |
|---------|-----------|--------------|
| Progress too low | Reduce low-progress app weights | FORMULA_GUIDE_EN.md § Troubleshooting |
| Progress too high | Reduce high-progress app weights | FORMULA_GUIDE_EN.md § Troubleshooting |
| Result unexpected | Click "Test Calculation" again | FORMULA_QUICKSTART_EN.md § Validation |
| Can't save | Ensure "Save Configuration" clicked | README_FORMULAS_EN.md § Access Panel |
| Formula reset | Click "Save Configuration" explicitly | README_FORMULAS_EN.md § Don't Auto-Save |
| Question on parameter | Search FORMULA_GUIDE_EN.md | FORMULA_GUIDE_EN.md § Main Parameters |

---

## Mathematical Reference

### All Three Formulas

**Weighted Average**:
$$Progress = \frac{\sum (App\% \times Weight \times Criticality)}{\sum (Weight \times Criticality)}$$

**Simple Average**:
$$Progress = \frac{\sum App\%}{Count}$$

**Minimum**:
$$Progress = MIN(App_1\%, App_2\%, ...)$$

### Key Formula Properties

| Method | Complexity | Customizable | Realistic | Use When |
|--------|-----------|--------------|-----------|----------|
| Weighted | High | Yes | Very | Apps differ in priority |
| Simple | Low | No | Medium | Apps equal importance |
| Minimum | Low | No | Low | All must be complete |

---

## Implementation Timeline

### Day 1: Setup

1. Read `README_FORMULAS_EN.md` (5 min)
2. Read `FORMULA_QUICKSTART_EN.md` (5 min)
3. Make initial configuration (5-10 min)
4. Test and save (5 min)

**Time**: 20-25 minutes

### Day 1-30: Validation

- Run "Test Calculation" several times
- Monitor results vs. expectations
- Gather feedback from team
- Make micro-adjustments as needed

**Actions**: Weekly check-ins

### Day 30: Review

1. Assess if formula meets needs
2. Document lessons learned
3. Plan next quarter adjustments
4. Archive configuration backup

**Actions**: One-time 30-minute review

---

## Success Metrics

Your formula is successful if:

✅ Results match stakeholder expectations
✅ Calculations are transparent and understandable
✅ Team agrees with methodology
✅ Trends are meaningful (not random noise)
✅ Decisions can be explained to executives
✅ System is maintainable (not overly complex)
✅ Export/import works reliably
✅ Historical consistency exists

---

## Related Documentation

| Topic | Document |
|-------|----------|
| Quick start | FORMULA_QUICKSTART_EN.md |
| Complete guide | FORMULA_GUIDE_EN.md |
| Quick lookup | FORMULA_REFERENCE_CARD_EN.md |
| Exhaustive reference | FORMULA_CONFIGURATION_GUIDE_EN.md |
| Navigation | README_FORMULAS_EN.md |
| Spanish versions | FORMULA_*.md (without _EN) |

---

## Support Resources

**In Dashboard**:
- Admin Panel → Calculation Formulas tab
- "Test Calculation" button (safe testing)
- "Save Configuration" button (persist)
- Export/Import buttons (backup/share)

**Documentation**:
- All guides in `docs/guides/` directory
- Both English (_EN suffix) and Spanish versions
- Each guide has search capability (Ctrl+F)

**Community**:
- See project README for support contact

---

## Next Steps

1. **Start here**: Read `README_FORMULAS_EN.md`
2. **Learn fast**: Read `FORMULA_QUICKSTART_EN.md`
3. **Go deep**: Read `FORMULA_GUIDE_EN.md` as needed
4. **Quick lookup**: Bookmark `FORMULA_REFERENCE_CARD_EN.md`
5. **Configure**: Open Dashboard → Admin → Calculation Formulas
6. **Test**: Use "Test Calculation" button
7. **Save**: Use "Save Configuration" button
8. **Backup**: Use "Export Configuration" button

---

## Document Versions

| Language | Complete? | Files |
|----------|-----------|-------|
| **English** | ✅ Yes | 5 files (+CN + SummaryEN) |
| **Spanish** | ✅ Yes | 5 files (+CN + SummarySP) |

---

**Last Updated**: October 2025  
**Version**: 1.0 (Complete)  
**Documentation Status**: ✅ Complete for both English and Spanish
