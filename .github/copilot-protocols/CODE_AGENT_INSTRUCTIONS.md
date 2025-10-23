# 🎯 GitHub Copilot - Code Agent Instructions

**Version**: 2.0  
**Project**: Dashboard Enhanced  
**Purpose**: Prevent unnecessary files and ensure proper organization

---

## 🚨 MANDATORY READING - CRITICAL INSTRUCTIONS

### GOLDEN RULE: ASK FIRST, CREATE SECOND
**NEVER create documentation files (.md) unless user explicitly requests them.**

Examples of what NOT to do:
- ❌ "I'll create a summary of the changes..."
- ❌ "Let me document this implementation..."  
- ❌ "I'll generate a report for this..."
- ❌ "Creating documentation for completeness..."

Examples of what TO do:
- ✅ "Would you like me to document this change?"
- ✅ "Should I create a report for this implementation?"
- ✅ Wait for user to say "create documentation" or "make a report"

---

## 📁 STRICT DIRECTORY STRUCTURE

### Root Directory (Keep Clean)
Only these files belong in root:
```
README.md, package.json, dashboard_enhanced.html, index.html
```

### Documentation (docs/)
```
docs/
├── reports/           ← Executive summaries, final reports
├── implementations/   ← Technical implementation details  
├── features/         ← Feature-specific documentation
├── fixes/            ← Problem diagnosis and solutions
├── technical/        ← Technical specs, formulas, architecture
├── guides/           ← User guides, testing procedures
├── process/          ← Process docs, cleanup reports
└── releases/         ← Version info, delivery notes
```

### Source Code (src/)
```
src/
├── modules/          ← JavaScript modules (.js)
├── styles/           ← CSS files (.css)
└── template.html     ← HTML templates
```

### Scripts (scripts/)
```
scripts/
├── fixes/            ← Temporary fix scripts
├── build/            ← Build and compilation scripts
└── data/             ← Data processing scripts
```

---

## 🤖 CODE AGENT BEHAVIOR RULES

### File Creation Protocol

1. **VALIDATE REQUEST**
   ```
   Is user explicitly asking for file creation?
   - YES: Proceed with path validation
   - NO: Do NOT create any files
   ```

2. **VALIDATE PATH**
   ```
   Where does this file type belong?
   - Code → src/modules/ or scripts/
   - Documentation → docs/[category]/
   - Tests → tests/[type]/
   - Config → root or appropriate subdirectory
   ```

3. **VALIDATE PURPOSE**
   ```
   Does this file serve an immediate, specific need?
   - YES: Create with proper naming
   - NO: Ask user to clarify need
   ```

### Response Templates

#### When Code Changes Are Made
```
❌ BAD: "I've made the changes. Let me create a summary report..."
✅ GOOD: "I've made the changes. The functionality is now working as requested."
```

#### When User Asks for Documentation
```
✅ GOOD: "I'll create [specific doc type] in docs/[category]/. Should I proceed?"
```

#### When Unsure About File Creation
```
✅ GOOD: "Would you like me to create documentation for this? If so, what type and where?"
```

---

## 📋 FILE TYPE ROUTING

| User Says | File Type | Correct Path | Example |
|-----------|-----------|--------------|---------|
| "Create module/component" | Code | `src/modules/` | `UserManager.js` |
| "Add styles" | CSS | `src/styles/` | `dashboard.css` |
| "Create fix script" | Script | `scripts/fixes/` | `tooltip_fix.js` |
| "Document implementation" | Doc | `docs/implementations/` | `FEATURE_IMPL.md` |
| "Create report" | Doc | `docs/reports/` | `PROGRESS_REPORT.md` |
| "User guide" | Doc | `docs/guides/` | `USER_GUIDE.md` |
| "Technical specs" | Doc | `docs/technical/` | `API_SPECS.md` |
| "Bug diagnosis" | Doc | `docs/fixes/` | `BUG_ANALYSIS.md` |

---

## 🛡️ PREVENTION CHECKLIST

Before creating ANY file, check:

- [ ] Did user explicitly request this file?
- [ ] Am I creating this for "completeness" or "best practices"? (If yes, STOP)
- [ ] Is this the correct directory for this file type?
- [ ] Does this file solve a specific, immediate problem?
- [ ] Am I auto-generating documentation? (If yes, STOP)

---

## 💻 CODING STANDARDS

### JavaScript Modules (src/modules/)
```javascript
// File: src/modules/ExampleModule.js
// Header with purpose
class ExampleModule {
    // Implementation
}

// Export pattern matching project
if (!window.Dashboard) window.Dashboard = {};
window.Dashboard.ExampleModule = ExampleModule;
```

### CSS Files (src/styles/)
```css
/* File: src/styles/example.css */
/* Component: Example Component Styles */

.example-class {
    /* Properties */
}
```

### Fix Scripts (scripts/fixes/)
```javascript
// File: scripts/fixes/example_fix.js  
// Purpose: Fix specific issue XYZ
// Usage: Include in HTML or run directly

(function() {
    // Fix implementation
    console.log('Fix applied: [description]');
})();
```

---

## 📝 NAMING CONVENTIONS

### Documentation Files
- `FEATURE_NAME_REPORT.md` - Reports  
- `IMPLEMENTATION_DETAILS.md` - Implementation docs
- `USER_GUIDE_FEATURE.md` - User guides
- `BUG_FIX_DESCRIPTION.md` - Fix documentation

### Code Files  
- `ModuleName.js` - PascalCase for modules
- `component-name.css` - kebab-case for styles
- `feature_fix.js` - snake_case for fix scripts

### Directory Names
- Always lowercase
- Use underscores for separation: `user_guides`
- Be descriptive: `implementations` not `impl`

---

## 🎯 QUALITY GATES

### Before File Creation
1. User explicitly requested it? ✅/❌
2. Correct directory selected? ✅/❌  
3. Proper naming convention? ✅/❌
4. Serves immediate purpose? ✅/❌
5. Not created for "completeness"? ✅/❌

### After File Creation
1. File in correct location? ✅/❌
2. Proper header/documentation? ✅/❌
3. Follows project patterns? ✅/❌
4. User need satisfied? ✅/❌

---

## 🚫 ANTI-PATTERNS TO AVOID

### Documentation Anti-Patterns
```
❌ Auto-creating SUMMARY.md after changes
❌ Making IMPLEMENTATION_REPORT.md without request  
❌ Creating README.md in every directory
❌ Generating "complete documentation"
❌ Making reports "for future reference"
```

### Path Anti-Patterns
```
❌ Putting .md files in src/
❌ Putting .js files in docs/
❌ Creating files in root unnecessarily
❌ Wrong category in docs/ (putting guides in reports/)
```

### Code Anti-Patterns
```
❌ Creating placeholder files
❌ Making "skeleton" implementations
❌ Creating files "for structure"
❌ Adding unnecessary config files
```

---

## ✅ SUCCESS EXAMPLES

### Good Interaction Flow
```
User: "Add hover effect to buttons"
Agent: Creates src/styles/button-effects.css
Agent: "I've added the hover effect styles. The buttons now have the requested animation."
✅ No unsolicited documentation created
```

```
User: "Fix the tooltip issue and document the solution"
Agent: Creates scripts/fixes/tooltip_fix.js AND docs/fixes/TOOLTIP_FIX_SOLUTION.md
Agent: "I've fixed the tooltip issue and documented the solution as requested."
✅ Documentation created because user specifically requested it
```

### Bad Interaction Flow
```
User: "Add hover effect to buttons"  
Agent: Creates src/styles/button-effects.css
Agent: Creates docs/implementations/BUTTON_HOVER_IMPLEMENTATION.md (WRONG!)
❌ User didn't request documentation
```

---

## 🏆 FINAL REMINDER

**The goal is a clean, organized project where every file has a purpose and is in the right place. Only create what is explicitly requested, and always in the correct location.**

**When in doubt, ASK THE USER instead of creating files proactively.**