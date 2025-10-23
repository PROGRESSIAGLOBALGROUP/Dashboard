# 🚪 GATE 2: Sufficiency Gate

**Purpose**: Verify that we have enough data/information to make sound decisions  
**Blocking Criteria**: Missing critical information, insufficient data, incomplete context  
**Output Required**: Complete information package for proceeding with work  

---

## 🎯 Your Mission

Ensure that before proceeding, **all necessary information is available**:
- ✅ Problem details sufficient
- ✅ Context complete
- ✅ Dependencies identified
- ✅ Constraints documented
- ✅ Resources available
- ✅ No critical gaps

---

## 🚫 BLOCKING CRITERIA (Must All Be Satisfied)

❌ **BLOCK if**:
1. Critical information missing
2. Context incomplete or unclear
3. Dependencies not identified
4. Constraints not documented
5. Required resources unavailable
6. Questions remain unanswered

---

## ✅ PASSING CRITERIA (All Must Be True)

✅ **PASS if**:
1. All problem details provided
2. Full context available
3. Dependencies explicitly mapped
4. Constraints clearly stated
5. Required resources identified
6. No critical questions remain

---

## 🔍 SUFFICIENCY GATE CHECKLIST

Before information is deemed sufficient:

- [ ] Problem details complete and specific
- [ ] All context provided (history, background, related work)
- [ ] Dependencies identified (files, modules, systems affected)
- [ ] Constraints documented (technical, business, time-based)
- [ ] Required resources available (tools, access, expertise)
- [ ] Acceptance criteria defined
- [ ] Success metrics quantified
- [ ] Risks identified and assessed

---

## 💬 GATE RESPONSE

### ✅ When Information is Sufficient:

```
"✅ GATE 2: Sufficiency - PASSED

INFORMATION PACKAGE COMPLETE:

Problem Details: [Sufficient]
- [Key detail 1]
- [Key detail 2]

Context: [Complete]
- [Contextual info 1]
- [Contextual info 2]

Dependencies: [Mapped]
- [Dependency 1: Impact level]
- [Dependency 2: Impact level]

Constraints: [Documented]
- [Constraint 1]
- [Constraint 2]

Resources: [Available]
- [Resource 1: Status]
- [Resource 2: Status]

Status: Ready to proceed to Gate 3"
```

### 🚫 When Information is Insufficient:

```
"🚫 GATE 2: Sufficiency - BLOCKED

CRITICAL INFORMATION GAPS IDENTIFIED:

Missing Information:
1. [Missing detail 1] - Why needed: [reasoning]
2. [Missing detail 2] - Why needed: [reasoning]
3. [Missing detail 3] - Why needed: [reasoning]

Incomplete Context:
1. [Context gap 1]
2. [Context gap 2]

Unidentified Dependencies:
1. [Potential dependency 1]
2. [Potential dependency 2]

Action Required:
[Specific instructions for gathering missing information]

Once provided, please resubmit."
```

---

## 📋 SUFFICIENCY VALIDATION PROCESS

1. **Assess Problem Details**
   - Is problem completely described?
   - Are edge cases addressed?
   - Are all variants covered?

2. **Evaluate Context**
   - Do we understand the background?
   - Are we aware of related work?
   - Do we know why this matters?

3. **Map Dependencies**
   - What files/modules are affected?
   - What systems need integration?
   - What external resources needed?

4. **Document Constraints**
   - Technical constraints?
   - Business constraints?
   - Time/resource constraints?
   - Architectural constraints?

5. **Verify Resource Availability**
   - Do we have needed tools?
   - Do we have required access?
   - Do we have necessary expertise?

---

## 📊 Sufficiency Quality Examples

### ❌ INSUFFICIENT Information:

```
"Create a weight calculator"

Missing:
- What inputs?
- What algorithm?
- What outputs?
- Where used?
- Performance requirements?
- Integration points?
- Test data?
```

### ✅ SUFFICIENT Information:

```
"Create weighted progress calculator for Dashboard.

Inputs:
- Applications array (status, weight, progress)
- Business units array (relationships)

Algorithm:
- Sum(progress × weight) for apps where status ≠ 'TBS'
- Divide by Sum(weight) for included apps
- Result 0-100, rounded to 1 decimal

Outputs:
- Progress percentage
- Individual app contributions
- Status indicators

Integration:
- Called from DataProcessor.calculateBUProgress()
- Results cached in StorageManager
- Updates trigger UIController.apply()

Constraints:
- Must handle empty datasets (return 0)
- Must handle null values gracefully
- Must not modify input arrays

Test coverage:
- Normal cases (2-5 apps)
- Edge cases (single app, all TBS)
- Error cases (null inputs, malformed data)

Performance: < 1ms calculation time required
"
```

---

## 🎓 Sufficiency Dimensions

### 1. Information Completeness
- **Sufficient**: All required information provided
- **Insufficient**: Key information missing
- **Partially Sufficient**: Some gaps remain

### 2. Context Clarity
- **Sufficient**: Full context understood
- **Insufficient**: Background missing
- **Partially Sufficient**: Some context gaps

### 3. Dependency Mapping
- **Sufficient**: All dependencies identified
- **Insufficient**: Unknown dependencies
- **Partially Sufficient**: Some dependencies unmapped

### 4. Constraint Documentation
- **Sufficient**: All constraints explicit
- **Insufficient**: Constraints undefined
- **Partially Sufficient**: Some constraints unclear

### 5. Resource Availability
- **Sufficient**: All resources available
- **Insufficient**: Critical resources missing
- **Partially Sufficient**: Some resources unavailable

---

## 🎯 Critical Information Categories

### For Code Changes:
- ✅ Current implementation (what is)
- ✅ Desired implementation (what should be)
- ✅ Affected systems/modules
- ✅ Integration points
- ✅ Testing requirements
- ✅ Performance constraints

### For Documentation:
- ✅ Target audience
- ✅ Scope and coverage
- ✅ Related documentation
- ✅ Update frequency
- ✅ Approval requirements
- ✅ Distribution method

### For Features:
- ✅ User requirements
- ✅ Acceptance criteria
- ✅ Technical requirements
- ✅ Performance targets
- ✅ Security requirements
- ✅ Accessibility requirements

---

## 🚀 When You Pass Gate 2

All necessary information is available. Proceed to **Gate 3: Logic Gate**.

---

*Gate 2 of 7 - Data sufficiency barrier  
Failure Point: Missing critical information  
Prevention: Ensure complete information before proceeding*
