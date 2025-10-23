# 🚪 GATE 3: Logic Gate

**Purpose**: Verify that reasoning is sound and conclusions are supported by evidence  
**Blocking Criteria**: Logical fallacies, unsupported conclusions, contradictions  
**Output Required**: Validated reasoning with evidence-based conclusions  

---

## 🎯 Your Mission

Ensure that the proposed solution has **sound reasoning**:
- ✅ Logic is valid
- ✅ Conclusions supported
- ✅ No contradictions
- ✅ Evidence provided
- ✅ Alternatives considered
- ✅ Trade-offs analyzed

---

## 🚫 BLOCKING CRITERIA (Must All Be Satisfied)

❌ **BLOCK if**:
1. Logical fallacies detected
2. Conclusions unsupported by evidence
3. Internal contradictions exist
4. Assumptions unvalidated
5. Alternative solutions ignored
6. Trade-offs not analyzed

---

## ✅ PASSING CRITERIA (All Must Be True)

✅ **PASS if**:
1. Reasoning is logically sound
2. Evidence supports conclusions
3. No contradictions present
4. Assumptions are explicit and valid
5. Alternatives considered and rejected
6. Trade-offs clearly documented

---

## 🔍 LOGIC GATE CHECKLIST

Before logic is validated:

- [ ] Claim: stated clearly
- [ ] Evidence: provided for each claim
- [ ] Logic chain: connected without gaps
- [ ] Assumptions: identified and validated
- [ ] Contradictions: checked and none found
- [ ] Alternatives: considered and compared
- [ ] Trade-offs: documented with rationale
- [ ] Conclusion: necessarily follows from premises

---

## 💬 GATE RESPONSE

### ✅ When Logic is Sound:

```
"✅ GATE 3: Logic - PASSED

REASONING ANALYSIS:

Premises:
1. [Premise 1] ✓ Supported by [evidence]
2. [Premise 2] ✓ Supported by [evidence]
3. [Premise 3] ✓ Supported by [evidence]

Logic Chain:
[Premise 1] + [Premise 2] + [Premise 3]
→ [Intermediate conclusion 1]
→ [Intermediate conclusion 2]
→ [Final conclusion]

Validation:
✓ No logical fallacies detected
✓ All premises supported by evidence
✓ Logic chain is continuous
✓ No contradictions present

Alternatives Considered:
- [Alternative 1]: Rejected because [reason]
- [Alternative 2]: Rejected because [reason]

Trade-offs Documented:
- [Trade-off 1]: Accepts [cost], gains [benefit]
- [Trade-off 2]: Accepts [cost], gains [benefit]

Status: Ready to proceed to Gate 4"
```

### 🚫 When Logic is Unsound:

```
"🚫 GATE 3: Logic - BLOCKED

LOGICAL FALLACIES DETECTED:

Fallacy 1: [Type of fallacy]
- Error: [Specific problem]
- Fix required: [How to correct]

Fallacy 2: [Type of fallacy]
- Error: [Specific problem]
- Fix required: [How to correct]

Unsupported Claims:
- Claim: '[Claim text]'
  Evidence provided: [None/Insufficient/[what was provided]]
  Evidence needed: [What would support this]

Contradictions Identified:
- Statement A: '[Statement text]'
- Statement B: '[Contradicts A]'
- Resolution: [How to resolve]

Unvalidated Assumptions:
- Assumption: '[Assumption text]'
- Validation needed: [What would validate]

Action Required:
[Specific instructions for correcting logic]

Once corrected, please resubmit."
```

---

## 📋 LOGIC VALIDATION PROCESS

1. **Identify All Premises**
   - What claims are being made?
   - What assumptions underlie them?
   - Are they explicitly stated?

2. **Validate Each Premise**
   - Is this claim supported by evidence?
   - Is the evidence credible?
   - Is the evidence sufficient?

3. **Check Logic Chain**
   - Does conclusion follow from premises?
   - Are there gaps in reasoning?
   - Is each step justified?

4. **Detect Fallacies**
   - Ad hominem? Appeal to authority?
   - Circular reasoning? False cause?
   - Hasty generalization? Strawman?

5. **Identify Alternatives**
   - What other conclusions possible?
   - Why rejected over chosen?
   - Trade-offs between them?

---

## 🎓 Common Logical Fallacies to Block

### 1. Ad Hominem
❌ "We should do X because expert Y said so"  
✅ "We should do X because [evidence supporting X]"

### 2. Circular Reasoning
❌ "This is true because I believe it"  
✅ "This is true because [independent evidence]"

### 3. Hasty Generalization
❌ "One case worked, so all will work"  
✅ "Multiple cases worked and we've analyzed why"

### 4. False Cause
❌ "A happened before B, so A caused B"  
✅ "A caused B because [mechanism of causation]"

### 5. Appeal to Authority
❌ "Famous person X believes this"  
✅ "Evidence shows this because [facts]"

### 6. Strawman Argument
❌ "They said [mischaracterization], so it's wrong"  
✅ "They said [accurate characterization], so [rebuttal]"

### 7. False Dilemma
❌ "Either do X or fail"  
✅ "Options are X, Y, Z with trade-offs [analysis]"

---

## 📊 Logic Quality Examples

### ❌ UNSOUND Logic:

```
"We should add the weight calculator feature because
it will make the dashboard better."

Problems:
- "Better" is undefined
- No evidence weight calculator helps
- No analysis of cost vs. benefit
- No consideration of alternatives
- No trade-off analysis
```

### ✅ SOUND Logic:

```
"We should implement weighted progress calculation because:

Premise 1: Currently, equal weight given all apps
- Evidence: Code shows simple average in calculateProgress()
- Impact: Ignores that some apps are more critical

Premise 2: Business unit leadership wants to prioritize critical apps
- Evidence: Feedback from last 3 stakeholder meetings
- Impact: Current calculation doesn't reflect business reality

Premise 3: Weighted calculation is algorithmically feasible
- Evidence: Reviewed existing code patterns, no architectural conflicts
- Impact: Low implementation cost

Conclusion: Implement weights to align calculation with business priority

Alternatives Considered:
1. Add filtering instead → Rejected: loses important context
2. Add app-level importance field → Rejected: administrative overhead
3. Weighted calculation → Selected: low cost, solves problem, maintains data

Trade-offs:
- Cost: 2 hours development, 1 hour testing
- Benefit: Accurate priority representation, stakeholder satisfaction
- Risk: Migration of existing configs (manageable with script)"
```

---

## 🎯 Logic Validation Dimensions

### 1. Premise Validity
- ✅ All premises true or reasonable
- ❌ Premises unvalidated or false

### 2. Logic Chain Continuity
- ✅ Each step follows from previous
- ❌ Gaps or missing justification

### 3. Evidence Sufficiency
- ✅ Evidence supports conclusions
- ❌ Conclusions exceed evidence

### 4. Assumption Transparency
- ✅ Assumptions explicit and valid
- ❌ Hidden or unvalidated assumptions

### 5. Alternative Analysis
- ✅ Alternatives considered and rejected
- ❌ Only one option presented

### 6. Trade-off Transparency
- ✅ Costs and benefits clear
- ❌ Hiding downsides

---

## 🚀 When You Pass Gate 3

Reasoning is sound and supported by evidence. Proceed to **Gate 4: Quality Gate**.

---

*Gate 3 of 7 - Logic and reasoning barrier  
Failure Point: Unsound reasoning or logical fallacies  
Prevention: Validate reasoning chain early*
