# 🧭 DECISION FRAMEWORK - Step-by-Step Reasoning Process

**Purpose**: Document the complete reasoning process for all decisions  
**Version**: 1.0  
**Applicability**: Architecture, code, governance, strategy decisions  

---

## 🎯 THE UNIVERSAL DECISION PROCESS

This is how every decision is made, regardless of complexity or domain.

---

## **PHASE 0: DECISION RECOGNITION**

### Am I Making a Decision?

**Signs that a decision is needed**:
- User asks "what should I do?"
- Multiple paths forward exist
- Impact is non-trivial
- Tradeoffs are present
- Precedent matters

**If NOT a decision** (just execution):
- Proceed directly to implementation
- No framework needed
- Still validate code before delivery

**If YES, a decision is needed**:
- Proceed to Phase 1

---

## **PHASE 1: PROBLEM CLARIFICATION**

### Goal: Crystal Clear Problem Statement

**Step 1.1: State the Problem**

"What is the actual problem?" (not the symptom)

Examples:
- ❌ "Our code is messy"
- ✅ "We have 5 exact code duplicates in the auth module causing maintenance burden"

- ❌ "Performance is bad"
- ✅ "N+1 query problem causes 500ms latency on user lookup endpoint"

**Output**: One clear, measurable problem statement

---

**Step 1.2: Identify Constraints (What MUST be true)**

"What are hard requirements?"

Examples:
- "Must use existing PostgreSQL database"
- "Cannot modify API contract"
- "Must complete in 2 weeks"
- "Must pass security audit"

**Output**: Numbered list of non-negotiable constraints

---

**Step 1.3: Identify Preferences (What SHOULD be true)**

"What would be nice but isn't required?"

Examples:
- "Should reduce code by 50%"
- "Should improve readability"
- "Should maintain backward compatibility"

**Output**: Prioritized list of preferences

---

**Step 1.4: List Explicit Assumptions**

"What am I assuming?"

Examples:
- "Assuming we need to support 1M records"
- "Assuming current framework is acceptable"
- "Assuming team has Python expertise"

**Output**: All assumptions written explicitly

---

**Step 1.5: Ask Clarifying Questions**

"What is unclear?"

Examples:
- "Is this for immediate production or future planning?"
- "Who are the stakeholders?"
- "What's the actual scale (10, 100, 1000 users)?"

**Action**: If answers reveal new constraints → Go back to 1.1

**Gate**: ✅ Problem is crystal clear only when all stakeholders agree

---

## **PHASE 2: RESEARCH & EVIDENCE GATHERING**

### Goal: Fact-Based Foundation

**Step 2.1: Gather Hard Data**

"What facts do we know for certain?"

Sources:
- ✅ Current conversation
- ✅ Project documentation
- ✅ Code in repository
- ✅ Previously established facts
- ❌ Speculation
- ❌ External sources without citation
- ❌ "Common knowledge"

**Method**:
- Read conversation carefully
- Extract specific examples
- Cite exact source
- Distinguish proven vs assumed

**Output**: Numbered facts with sources

---

**Step 2.2: Challenge Weak Assumptions**

"What am I assuming that might be wrong?"

Process:
1. List each assumption
2. Ask: "What evidence supports this?"
3. Ask: "What would prove this wrong?"
4. Note confidence level (High/Medium/Low)

Examples:

**Assumption**: "JSON is faster than XML"  
**Evidence**: Not specific to our use case (Medium confidence)  
**Reframe**: "For our API, protobuf is faster than JSON"

**Assumption**: "We need a microservices architecture"  
**Evidence**: Only if we have specific scale (Low confidence)  
**Reframe**: "Do we have a specific scale requirement?"

**Output**: All assumptions with confidence levels

---

**Step 2.3: Identify Information Gaps**

"What don't we know that we need to?"

Gaps:
- Missing performance data?
- Unknown user scale?
- Unclear requirements?
- Technical unknowns?

**Action**:
- If gap is critical → Ask questions now
- If gap is minor → Note for Phase 3
- If gap is unknowable → Design for flexibility

**Output**: List of gaps and their criticality

---

**Gate**: ✅ Only proceed when you have sufficient data to decide

---

## **PHASE 3: OPTION GENERATION**

### Goal: 2-3 Realistic Alternatives

**Step 3.1: Generate Options**

"What are realistic approaches?"

Rules:
- Generate at least 2 options
- Each must satisfy ALL constraints
- Each must be realistic (not theoretical)
- Vary along different dimensions

Example for "reduce code duplication":

**Option A**: Extract to shared utility  
- Satisfies: constraint (maintain API), preference (reduce code)

**Option B**: Use inheritance/composition  
- Satisfies: constraint (maintain API), preference (improve design)

**Option C**: Use code generation  
- Satisfies: constraint (maintain API), preference (reduce maintenance)

**Output**: List of realistic options

---

**Step 3.2: Analyze Each Option**

For each option, document:

**What It Solves**:
- Which constraint does it satisfy?
- Which preference does it improve?
- What problem does it prevent?

**What It Requires**:
- Effort estimate (hours/days/weeks)
- Skill requirements
- Infrastructure needs
- Training needed

**Estimated Effort**:
- Development time
- Testing time
- Documentation time
- Deployment complexity

**Risk Level**:
- 🟢 Low: Proven, understood, minimal failure modes
- 🟡 Medium: Some unknowns, recoverable if wrong
- 🔴 High: New technology, significant risk, hard to reverse

**Long-term Implications**:
- Maintainability: easier or harder to maintain?
- Scalability: does it constrain future growth?
- Flexibility: does it enable future options?
- Technical debt: does it add or remove debt?

**When It's Best**:
- When should this approach be preferred?
- What future scenarios favor this?
- What scenarios disfavor it?

**Output**: Detailed analysis for each option

---

## **PHASE 4: RECOMMENDATION**

### Goal: Clear, Justified Recommendation

**Step 4.1: Compare Options**

Create decision matrix:

| Factor | Constraint? | Option A | Option B | Option C | Weight |
|--------|-------------|----------|----------|----------|--------|
| Solves Problem | YES | ✅ | ✅ | ✅ | 100% |
| Satisfies Constraint 1 | YES | ✅ | ✅ | ❌ | 100% |
| Satisfies Constraint 2 | YES | ✅ | ❌ | ✅ | 100% |
| Effort (lower better) | NO | 5d | 3d | 8d | 20% |
| Maintainability | NO | High | Medium | High | 15% |
| Scalability | NO | High | Medium | High | 15% |
| Risk Level (lower better) | NO | Low | Medium | High | 10% |

---

**Step 4.2: Make the Call**

"Which option best satisfies constraints AND preferences?"

Process:
1. All options must satisfy ALL constraints
2. If not → Eliminate that option
3. Among remaining options → Evaluate by weighted preferences
4. Select option that best balances all factors

**State Clearly**:
- ✅ Which option I recommend
- ✅ Why this option (3-5 reasons)
- ✅ What tradeoff we accept
- ✅ My confidence level (High/Medium/Low)

**Example**:

"I recommend **Option A: Extract to shared utility**.

**Reasons**:
1. Satisfies all constraints (maintains API contract)
2. Lowest effort (5 days vs 3 and 8 for alternatives)
3. Highest long-term maintainability
4. Creates reusable pattern for future duplicates
5. Lowest risk (proven approach)

**Tradeoff**: Slightly more complex immediate code in exchange for major future maintenance savings

**Confidence**: HIGH (this is a standard pattern, well-proven)"

---

**Step 4.3: Acknowledge Alternatives**

"Why not the other options?"

Be explicit:
- Why Option B wasn't chosen (even if close)
- Why Option C was rejected
- When those options WOULD be better

Example:

"Option B (inheritance) wasn't chosen because:
- It creates tighter coupling (maintainability concern)
- It adds complexity without proportional benefit
- It would be better IF we expected frequent changes to the shared behavior
- In this stable case, composition via utility is clearer

Option C (code generation) wasn't chosen because:
- It adds tooling complexity
- It creates maintenance burden for the build system
- It would be better for 100+ duplicates; we have 5
- It's a pattern we could adopt later if scale grows"

---

**Output**: Clear recommendation with reasoning and alternative analysis

---

## **PHASE 5: VALIDATION**

### Goal: Confirm Recommendation is Sound

**Step 5.1: Sanity Check**

Ask yourself:

- ✅ Does this recommendation actually solve the problem?
- ✅ Does it satisfy all constraints?
- ✅ Have I considered genuine alternatives?
- ✅ Is this the BEST choice or just A choice?
- ✅ Could I defend this decision to an expert?
- ✅ What could go wrong?
- ✅ Am I confident in this reasoning?

If ANY answer is "no" or "uncertain" → Go back to earlier phase

---

**Step 5.2: Confidence Level**

State clearly:

| Level | Meaning | When to use |
|-------|---------|-----------|
| 🟢 HIGH | >90% this is the right choice | Proven patterns, clear data, low risk |
| 🟡 MEDIUM | 70-90% this is right | Some unknowns, but reasonable analysis |
| 🔴 LOW | <70% this is right | Significant unknowns, high risk, or close call |

**If confidence is LOW** → Propose pilot or phased approach

---

**Step 5.3: State Assumptions**

"My recommendation depends on these assumptions:"

Examples:
- "Assuming current team can implement this"
- "Assuming PostgreSQL is acceptable"
- "Assuming we have 2 weeks"
- "Assuming this pattern won't need significant changes"

---

**Output**: Validated recommendation with confidence level and assumptions

---

## **PHASE 6: DOCUMENTATION**

### Goal: Clear Record for Future Reference

**Document**:
1. **Decision**: What was decided
2. **Context**: Why this decision was needed
3. **Problem**: What problem does it solve
4. **Constraints**: What had to be true
5. **Alternatives**: What other options existed
6. **Reasoning**: Why this option was chosen
7. **Confidence**: High/Medium/Low with why
8. **Tradeoffs**: What we're accepting/giving up
9. **Implications**: What this enables/prevents going forward
10. **Review Date**: When this should be revisited

**Format**:
```
DECISION: [One sentence decision]

PROBLEM: [What problem does this solve?]

CONSTRAINTS: [Hard requirements]

ALTERNATIVES:
- Option A: [Brief summary, why not chosen]
- Option B: [Brief summary, why not chosen]

RECOMMENDATION: [Chosen option, why]

CONFIDENCE: High/Medium/Low

TRADEOFF: [What we're accepting]

IMPLICATIONS: [What this enables/prevents]

DATE: [When decided]
REVIEW: [When to reconsider]
```

**Output**: Decision record saved for future reference

---

## **DECISION QUALITY METRICS**

### How to Evaluate if a Decision Was Good

**Before Decision**:
- ✅ Was problem clearly understood?
- ✅ Were all constraints identified?
- ✅ Were alternatives genuinely considered?
- ✅ Was reasoning transparent?
- ✅ Was confidence level honest?

**After Decision**:
- ✅ Did it solve the stated problem?
- ✅ Did constraints remain satisfied?
- ✅ Did we regret the choice?
- ✅ Would we choose differently with hindsight?
- ✅ Did unforeseen issues emerge?

**Learning**:
- ✅ What would we do differently?
- ✅ What did we learn?
- ✅ How should the framework evolve?

---

## **COMMON DECISION PATTERNS**

### Architecture Decision

**Problem**: Should we use monolith or microservices?

**Constraints**: Budget, timeline, team skills, scale requirements

**Options**: A) Monolith, B) Microservices, C) Hybrid (modular monolith)

**Analysis**: Depends entirely on scale and team (see Options analysis)

**Recommendation**: Usually Option C (modular monolith) unless massive scale proven

---

### Refactoring Decision

**Problem**: Should we refactor this code?

**Constraints**: Must maintain feature parity, must not introduce bugs

**Options**: A) Leave as-is, B) Refactor in-place, C) Rewrite

**Analysis**: Usually B (in-place refactoring) with comprehensive tests

**Recommendation**: Do it if duplication/complexity justified (DRY, SOLID)

---

### Technology Decision

**Problem**: Should we adopt new framework X?

**Constraints**: Must be production-ready, must have community, must match our skills

**Options**: A) Current framework, B) New framework, C) Hybrid

**Analysis**: Only if new framework solves concrete problem, not hypothetical

**Recommendation**: Usually stick with proven unless clear advantage

---

## 🎊 DECISION FRAMEWORK CERTIFICATION

**This framework ensures**:

✅ All decisions are evidence-based  
✅ Alternatives are genuinely considered  
✅ Constraints are explicitly stated  
✅ Reasoning is transparent  
✅ Confidence levels are honest  
✅ Tradeoffs are documented  
✅ No decisions are made on hunches  
✅ All decisions are revisitable and reviewable  

---

**Version**: 1.0  
**Created**: October 22, 2025  
**Status**: ✅ Production Ready  
**Applicability**: All decisions, universal framework
