# 📋 Code Review Guidelines - Dashboard Enhanced

**Last Updated**: October 24, 2025  
**Version**: 1.2.0  
**Audience**: All developers on Dashboard Enhanced team  
**Status**: Active Standard  

---

## 🎯 Our Code Review Philosophy

We believe code review is **not inspection**, it's **collaboration**:

- **Shared Ownership**: We all own the codebase
- **Learning**: Review is an opportunity to teach and learn
- **Quality**: We catch issues early, before production
- **Culture**: Reviews are respectful and constructive

**Golden Rule**: "How can I help this PR be even better?"

---

## 📊 When Code Review Happens

### Before Review
✅ Developer runs local tests: `npm test`  
✅ Developer builds dashboard: `python build/build_enhanced_dashboard.py`  
✅ Developer verified in browser locally  
✅ Commit messages are clear and descriptive  
✅ Branch follows naming convention  

### During Review
👀 Assigned reviewer has **48 hours** to review  
💬 Feedback is constructive and specific  
✅ At least **2 approvals** required for merge  
🔍 All automated checks (tests, lint) must pass  

### After Review
✅ Author addresses feedback (requests changes count as "needs work")  
✅ Re-request review when ready  
✅ Once approved, author merges to `main`  
✅ Delete feature branch after merge  

---

## 🌿 Branch Naming Convention

### Format
```
type/short-description
```

### Types

| Type | Purpose | Example |
|------|---------|---------|
| **feature/** | New functionality | `feature/dashboard-export-import` |
| **fix/** | Bug fixes | `fix/tooltip-calculation-error` |
| **docs/** | Documentation | `docs/api-specification` |
| **refactor/** | Code reorganization | `refactor/storage-manager-cleanup` |
| **test/** | Test additions/improvements | `test/unit-tests-admin-panel` |
| **style/** | CSS/styling changes | `style/responsive-mobile-layout` |
| **perf/** | Performance improvements | `perf/weighted-progress-optimization` |
| **chore/** | Build/tooling/dependencies | `chore/update-jest-config` |

### Examples - DO ✅

```
feature/application-status-automation
fix/progress-calculation-exclude-tbs
docs/import-export-workflow
refactor/ui-controller-separation
test/storage-manager-persistence
```

### Examples - DON'T ❌

```
dashboard-fix              ← Too vague
Feature/new-stuff          ← Wrong capitalization
fix_tooltip_bug            ← Using underscore
my-changes                 ← No type prefix
update                     ← Not descriptive
```

---

## 💬 Commit Message Format

### Format
```
type(scope): description

[optional body]

[optional footer]
```

### Types

| Type | Use When |
|------|----------|
| **feat** | Adding a new feature |
| **fix** | Fixing a bug |
| **docs** | Documentation changes |
| **style** | CSS/formatting (no logic change) |
| **refactor** | Restructuring code (no feature/fix) |
| **perf** | Performance improvement |
| **test** | Adding or fixing tests |
| **chore** | Dependencies, build config, etc. |

### Scope Examples
```
(ui)              ← UIController changes
(data)            ← DataProcessor changes
(storage)         ← StorageManager changes
(admin)           ← AdminPanel changes
(build)           ← Build system changes
```

### Examples - DO ✅

```
feat(storage): add JSON export functionality

Allow users to export dashboard configuration as JSON file.
Includes validation and error handling.

Fixes #42
```

```
fix(ui): correct weighted progress calculation

The progress calculation was excluding completed apps incorrectly.
Now only excludes apps with status 'TBS' as designed.

Fixes #89
```

```
docs(guides): update quick-start with python setup

Added Windows Store Python installation option.
Clarified PATH configuration requirement.
```

### Examples - DON'T ❌

```
fixed stuff                    ← Too vague, wrong type
feat: new feature              ← Missing scope
update dashboard               ← No type
Fixed the bug                  ← Capitalized
```

---

## 🔍 Code Review Checklist

Use this checklist **before submitting** and **while reviewing**.

### Functionality ✅

- [ ] Code does what it's supposed to do
- [ ] Feature works as described in PR description
- [ ] No obvious bugs or logic errors
- [ ] Edge cases are handled
- [ ] Code handles errors gracefully (no silent failures)
- [ ] No console errors or warnings
- [ ] Related functionality still works (verified by reviewer)

### Architecture & Design ✅

- [ ] Follows the 3-layer separation (UI → Logic → Storage)
- [ ] Changes are in the correct module/layer
- [ ] No hardcoded values (except constants)
- [ ] No duplicate code (DRY principle)
- [ ] Functions have single responsibility
- [ ] Data flow is clear and logical
- [ ] Naming is clear and descriptive

### Code Quality ✅

- [ ] Code is readable (clear variable/function names)
- [ ] Comments explain WHY, not WHAT
- [ ] No dead code or unused variables
- [ ] Consistent with existing code style
- [ ] No overly complex functions (< 50 lines ideal)
- [ ] Follows the project's patterns and conventions
- [ ] ES6+ standards used appropriately

### Testing ✅

- [ ] All tests pass locally (`npm test`)
- [ ] New functionality has tests (if applicable)
- [ ] Edge cases are tested
- [ ] Tests are clear and maintainable
- [ ] No flaky tests (random failures)
- [ ] Coverage hasn't decreased

### Documentation ✅

- [ ] Code is commented where necessary (WHY, not WHAT)
- [ ] Complex functions have JSDoc comments
- [ ] PR description explains the changes
- [ ] Related docs updated (if needed)
- [ ] No obvious confusion about how code works

### Performance & Security ✅

- [ ] No performance regressions
- [ ] No memory leaks (especially in event listeners)
- [ ] No security vulnerabilities
- [ ] No sensitive data in code/commits
- [ ] localStorage usage is appropriate
- [ ] No external dependencies added unexpectedly

### Browser Compatibility ✅

- [ ] Works in Chrome/Edge (latest)
- [ ] Works in Firefox (latest)
- [ ] Works in Safari (latest)
- [ ] Mobile responsive (if UI change)
- [ ] No IE11 code (we don't support it)

---

## 👀 How to Review Code

### 1. Understand the Purpose
```
Read the PR description carefully:
- What problem does this solve?
- What feature does it add?
- Why was this approach chosen?
```

### 2. Check the Changes
```
Look at the files changed:
- Is this the minimal set of changes?
- Are there unrelated changes? (mention them)
- Is anything missing? (related updates, tests, docs)
```

### 3. Review the Code
```
Using the checklist above:
- Does it follow our patterns?
- Is it maintainable?
- Can you understand it?
- Are there better approaches?
```

### 4. Test Locally (if needed)
```
For significant changes:
- npm test (run tests)
- python build/build_enhanced_dashboard.py (rebuild)
- Open in browser and verify
```

### 5. Leave Feedback

**REQUEST CHANGES** when:
- Critical bugs found
- Architecture violated
- Tests failing
- Security concern
- Significant improvement needed

**COMMENT** when:
- Minor issues or suggestions
- Questions about approach
- Alternatives to consider
- Praise for good work

**APPROVE** when:
- Code is solid
- All concerns addressed
- Checklist items satisfied
- Ready to merge

---

## 💬 Writing Review Comments

### Format: Be Specific & Constructive

#### ❌ Bad Comments
```
"This code is bad"
"Why did you do it this way?"
"This won't work"
```

#### ✅ Good Comments
```
"This calculation might overflow for large values. 
Consider using BigInt or checking for bounds first."

"I notice you're mutating the array directly here. 
According to our patterns, we should use StorageManager.update(). 
Would that work better?"

"The function does three different things. 
Could we split this into smaller functions for clarity?"
```

### Suggestion Pattern
```
"Consider X instead of Y because:
- Reason 1
- Reason 2
- This would make it clearer/faster/more maintainable"
```

### Praise Pattern
```
"Great use of destructuring here! Much clearer than the original approach."

"Love how you handled the edge case with null values. 
This prevents the crash we had before."
```

---

## ✅ Approval Requirements

### Before Merging, Check:

- [ ] **2 Approvals**: At least 2 developers approved
- [ ] **No Requested Changes**: All concerns resolved
- [ ] **Tests Pass**: CI/CD checks all green ✅
- [ ] **Lint Passes**: No linting errors
- [ ] **PR Description Clear**: Easy to understand
- [ ] **Branch is Up-to-Date**: No merge conflicts
- [ ] **Related Docs Updated**: If applicable

### Merging

```powershell
# Ensure branch is up-to-date
git pull origin main

# Merge to main
git merge --ff-only feature/branch-name
git push origin main

# Delete feature branch
git branch -d feature/branch-name
git push origin --delete feature/branch-name
```

### Merge Strategies

**We use**: **Linear History** (--ff-only / rebase)  
**Why**: Clean, easy to understand, easy to bisect/revert

---

## 🚨 Common Issues & How to Handle Them

### Issue: Reviewer Hasn't Responded

**What to do**:
1. Wait 24 hours (reasonable time)
2. @ mention in PR: "@reviewer could you take a look?"
3. If still no response after 48 hours, ask another reviewer
4. Escalate to tech lead if blocking

### Issue: Disagreement Between Reviewers

**What to do**:
1. Both reviewers discuss in comments
2. Reference architecture docs/conventions
3. If can't agree, tech lead makes decision
4. Update guidelines if precedent-setting

### Issue: Author Keeps Adding Changes

**What to do**:
1. If small fix: approve after changes
2. If significant: Request a new review
3. Comment: "This is good, but X changed - let me take another look"

### Issue: PR Has Been Open Too Long

**What to do**:
1. If > 1 week: Check if still relevant
2. If conflicts: Rebase and notify reviewers
3. If stalled: Ask author for update
4. If no response: Archive and re-do later

---

## 🎓 Learning & Improvement

### For Reviewers

**Get Better At Reviewing**:
- Read others' reviews and learn from them
- Ask questions when you don't understand something
- Look for teaching opportunities
- Share knowledge in comments

**Red Flags to Watch For**:
- Code that's hard to understand (probably needs refactoring)
- Complex calculations without comments
- Side effects not obvious from function name
- Mixing concerns (storage + UI together)
- Ignoring our established patterns

### For Authors

**Get Better At Writing Code**:
- Address feedback respectfully
- Explain your reasoning if you disagree
- Learn from reviewer suggestions
- Apply feedback to future PRs
- Ask questions if feedback is unclear

**Before Submitting**:
- Review your own code first (you'll catch ~80% of issues)
- Run tests locally
- Read the checklist and verify
- Write a clear PR description
- Consider edge cases

---

## 📞 Getting Help

**During Code Review**:
- "I'm not sure about this - what do you think?"
- "Can you explain why we should use StorageManager here?"
- "Is this the right approach or should we try X?"

**After Feedback**:
- "I've addressed your feedback - take another look?"
- "I disagreed at first, but now I understand - thanks!"
- "Can you clarify what you mean by X?"

**Team Lead / Tech Lead**:
- Disputes that can't be resolved
- Clarification on patterns/conventions
- Architectural questions
- Performance/security concerns

---

## 📊 Review Time Expectations

### Typical PR Size & Review Time

| Size | Files Changed | Review Time |
|------|---------------|-------------|
| **Tiny** | 1-3 files | 15-30 min |
| **Small** | 4-10 files | 30-60 min |
| **Medium** | 11-20 files | 1-2 hours |
| **Large** | 20+ files | 2+ hours |

**Target**: Reviews completed within **48 hours**

### Keep PRs Small

- ✅ Easier to understand
- ✅ Faster to review
- ✅ Easier to revert if needed
- ✅ Better for bisecting
- ❌ Large PRs take longer to review
- ❌ Higher chance of issues slipping through

**Ideal PR**: 1 feature = 1 PR, < 400 lines changed

---

## 🏆 Excellence in Code Review

### What Makes a Great Reviewer

- 🎯 Understands the codebase deeply
- 🤝 Reviews with empathy and curiosity
- 💬 Explains WHY, not just WHAT
- 🧠 Knows when to approve vs. request changes
- 🚀 Helps ship quality code faster
- 📚 Shares knowledge and teaches
- ⏰ Responds in timely manner
- 🤓 Continues learning and improving

### What Makes a Great PR Author

- 📝 Clear, descriptive PR description
- 🔍 Self-reviews before requesting review
- 🧪 All tests pass and verified locally
- 📋 Follows conventions and patterns
- 💭 Explains decisions when non-obvious
- 🙏 Accepts feedback gracefully
- 🎯 Keeps changes focused and small
- 🚀 Addresses feedback promptly

---

## 📚 Documentation References

| Document | Purpose |
|----------|---------|
| `docs/technical/CRITICAL_ARCHITECTURE_CLARIFICATION.md` | Architecture overview |
| `src/modules/` | Code organization |
| `README.md` | Project overview |
| `tests/unit/` | Test examples |

---

## ⚖️ Code Review Rights & Responsibilities

### Reviewer's Rights
- Ask clarifying questions
- Request changes if needed
- Suggest improvements
- Ask for tests/documentation

### Reviewer's Responsibilities
- Respond within 48 hours
- Be constructive and respectful
- Focus on code, not person
- Understand before approving
- Explain your feedback

### Author's Rights
- Ask clarifying questions
- Propose alternatives
- Disagree respectfully
- Request help/guidance

### Author's Responsibilities
- Address feedback promptly
- Test locally before requesting review
- Write clear descriptions
- Respond to comments
- Don't push back on every comment

---

## 🚀 Quick Start for New Reviewers

1. **Read this guide** (15 min)
2. **Review a small PR** with another reviewer (30 min)
3. **Ask questions** if confused (5 min)
4. **Review solo** on your next PR (1+ hour)
5. **Improve over time** through practice

---

## 📞 Questions?

**For Questions About**:
- **Code patterns**: Check `src/modules/` and existing PRs
- **Our conventions**: See this guide or ask in Slack/Teams
- **Architecture decisions**: See `docs/technical/`
- **Specific PR feedback**: Reply in the PR comment
- **Process issues**: Contact tech lead

---

## ✨ Summary

**Our code review culture is**:
- ✅ Collaborative, not adversarial
- ✅ Respectful and professional
- ✅ Focused on learning and growth
- ✅ Timely and efficient
- ✅ High quality, maintainable code
- ✅ Built on trust and shared ownership

**We review because**:
- We care about quality
- We're stronger together
- We want to learn from each other
- We build sustainable code
- We prevent bugs and debt
- We build our team

---

**Welcome to our code review culture! 🚀**
