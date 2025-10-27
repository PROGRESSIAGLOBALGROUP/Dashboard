# 🔧 GitHub Copilot - Code Modification Protocol

**Version**: 2.0  
**Last Updated**: October 22, 2025  
**Scope**: Dashboard Enhanced Project  
**Purpose**: Mandatory code modification standards and code_surgeon protocol compliance

---

## 🚨 CRITICAL: CODE MODIFICATION MANDATE

### MANDATORY PROTOCOL: code_surgeon COMPLIANCE
```
🔴 ABSOLUTE REQUIREMENT: ALL code modifications to dist/dashboard_enhanced.html 
   MUST use code_surgeon protocol WITHOUT EXCEPTION.

✅ DO: Use code_surgeon workflow with complete job specification
❌ DON'T: Make direct edits to dist/dashboard_enhanced.html
❌ DON'T: Use terminal commands to modify production files
❌ DON'T: Bypass code_surgeon for "quick fixes"
```

---

## 📋 CODE MODIFICATION DECISION MATRIX

### When to Use code_surgeon vs Direct Edit

| Target File | Type | Use code_surgeon | Use Direct Edit | Reason |
|------------|------|-----------------|-----------------|--------|
| `dist/dashboard_enhanced.html` | Production | ✅ **REQUIRED** | ❌ NEVER | Audit trail, rollback capability |
| `src/modules/*.js` | Source | ⚠️ Create job | ✅ OK | Build pipeline handles compilation |
| `src/styles/*.css` | Source | ⚠️ Create job | ✅ OK | Build pipeline handles compilation |
| `src/template.html` | Source | ⚠️ Create job | ✅ OK | Build pipeline handles compilation |
| Configuration files | Config | ✅ Recommended | ✅ OK | Depends on criticality |
| Documentation `.md` | Docs | ✅ Recommended | ✅ OK | Version control sufficient |

---

## 🔴 MANDATORY code_surgeon WORKFLOW

### 🚨 CRITICAL TESTING MANDATE (NEW REQUIREMENT)

**EVERY code modification must follow this sequence:**

```
1️⃣ CREATE/UPDATE test script BEFORE making changes
   └─ Specify what will be tested
   └─ Define acceptance criteria
   
2️⃣ APPLY the code change
   └─ Document in code_surgeon job
   └─ Create backup file
   
3️⃣ RUN UNIT TESTS immediately after change
   └─ Verify modified function works correctly
   └─ Use real test data (not mocks)
   
4️⃣ RUN INTEGRATION TESTS
   └─ Verify no side effects on other modules
   └─ Test complete event chains
   └─ Validate UI/calculation consistency
   
5️⃣ DOCUMENT results
   └─ Pass/fail status
   └─ Test output and metrics
   └─ Any regressions detected
```

**VIOLATION**: Skipping tests before commit = automatic rejection

---

### Step 1: CREATE/UPDATE TEST SCRIPT

**BEFORE making ANY changes**, create or update the test script that will validate the change:

- Location: `tests/unit/` or `tests/integration/`
- Language: Python (pytest) or JavaScript (Jest)
- Content: Test cases that verify the exact change being made
- Execution: Must pass after change is applied

**Example Test Script Creation:**
```bash
# Create test file for the feature being modified
# Include:
# - Test case 1: Verify primary functionality
# - Test case 2: Verify secondary effects
# - Test case 3: Verify no regressions
# - Test case 4: Edge cases and error handling
```

---

### Step 2: ANALYZE TARGET FILE

**Required Information:**
```
File: dist/dashboard_enhanced.html
Location: Line number range of target
Current Code: Exact current implementation
Change Type: Fix/Feature/Refactor/Optimization
Impact Scope: What will change
Risk Level: Low/Medium/High
```

### Step 2: CREATE code_surgeon JOB

**Mandatory Job Structure:**
```json
{
  "file": "dist/dashboard_enhanced.html",
  "operation": "[replace|insert|delete|refactor]",
  "targetLine": [line_start, line_end],
  "description": "Exact description of change",
  "originalCode": "Exact original code block",
  "newCode": "Exact new code block",
  "validation": {
    "beforeExecute": "Condition to check before",
    "afterExecute": "Condition to verify after",
    "rollbackCondition": "When to trigger rollback"
  },
  "rollback": {
    "enabled": true,
    "keepBackup": true,
    "backupName": "descriptive_backup_name"
  },
  "testing": {
    "unitTests": ["test1", "test2"],
    "integrationTests": ["integration_test1"],
    "manualTests": ["manual_verification_steps"]
  },
  "approval": {
    "requiresReview": true,
    "reviewers": ["developer"],
    "testCoverage": "Required percentage"
  }
}
```

### Step 3: EXECUTE code_surgeon JOB

**Location:** `surgery/jobs/` directory

**File Naming:** `[timestamp]_[descriptive_name].json`

**Example:**
```
surgery/jobs/20251022_fix_tooltip_visibility.json
```

### Step 4: VERIFY & DOCUMENT

**Post-Execution Checklist:**
- [ ] Job file created in `surgery/jobs/`
- [ ] Original file backed up
- [ ] Modification applied successfully
- [ ] All validation checks passed
- [ ] Unit tests pass (if applicable)
- [ ] Integration tests pass (if applicable)
- [ ] Manual verification complete
- [ ] Documentation updated
- [ ] Rollback capability confirmed

---

## 🔍 CODE PARSING REQUIREMENTS

### Mandatory Parsing Standards

#### 1. **EXACT STRING MATCHING**
```javascript
// ❌ WRONG: Approximate match
"function someMethod() {"

// ✅ CORRECT: Exact match including whitespace
"    function someMethod() {
        // Implementation
    }"
```

#### 2. **CONTEXT INCLUSION**
```javascript
// ❌ WRONG: No surrounding context
const oldCode = "console.log('test');";

// ✅ CORRECT: Include 3-5 lines of context
const oldCode = `
    },

    /**
     * Main method
     */
    execute() {
        console.log('test');
    },

    /**
`;
```

#### 3. **WHITESPACE PRESERVATION**
```javascript
// ❌ WRONG: Inconsistent indentation
"function test(){\nreturn 42;\n}"

// ✅ CORRECT: Preserve exact whitespace
"    function test() {\n        return 42;\n    }"
```

#### 4. **SYNTAX VALIDATION**
```javascript
// ❌ WRONG: Unclosed braces in new code
"newCode": "if (condition) { doSomething();"

// ✅ CORRECT: Complete, balanced syntax
"newCode": "if (condition) { doSomething(); }"
```

---

## 📝 code_surgeon JOB TEMPLATE

### Minimal Job Template
```json
{
  "file": "dist/dashboard_enhanced.html",
  "operation": "replace",
  "description": "[Clear, specific description of change]",
  "originalCode": "[EXACT original code with context]",
  "newCode": "[EXACT new code with context]",
  "validation": {
    "beforeExecute": "[Condition to verify]",
    "afterExecute": "[Condition to verify success]"
  },
  "rollback": {
    "enabled": true,
    "keepBackup": true
  }
}
```

### Complete Job Template with Full Details
```json
{
  "metadata": {
    "timestamp": "2025-10-22T10:30:00Z",
    "version": "1.0",
    "author": "GitHub Copilot",
    "project": "Dashboard Enhanced"
  },
  "file": "dist/dashboard_enhanced.html",
  "operation": "replace",
  "targetLine": {
    "start": null,
    "end": null,
    "searchAfter": "[Previous distinctive code block]",
    "searchBefore": "[Next distinctive code block]"
  },
  "description": "[Detailed description]",
  "rationale": "[Why this change is necessary]",
  "impact": "[What will change in behavior]",
  "riskLevel": "Low|Medium|High",
  "originalCode": "[EXACT original code]",
  "newCode": "[EXACT new code]",
  "validation": {
    "beforeExecute": {
      "checks": [
        "File exists: dist/dashboard_enhanced.html",
        "Original code found in file",
        "File syntax valid"
      ]
    },
    "afterExecute": {
      "checks": [
        "New code is in place",
        "File syntax still valid",
        "Related functionality working"
      ]
    },
    "rollbackCondition": "If any check fails"
  },
  "rollback": {
    "enabled": true,
    "keepBackup": true,
    "backupName": "dashboard_enhanced_[timestamp]_backup.html",
    "maxBackups": 5
  },
  "testing": {
    "unitTests": {
      "required": true,
      "tests": ["test_name_1", "test_name_2"]
    },
    "integrationTests": {
      "required": false,
      "tests": []
    },
    "manualTests": {
      "required": true,
      "steps": [
        "Step 1: Verify behavior X",
        "Step 2: Check integration Y",
        "Step 3: Validate result Z"
      ]
    }
  },
  "approval": {
    "requiresReview": true,
    "reviewers": ["developer"],
    "testCoverage": "Minimum 80%"
  },
  "documentation": {
    "updated": true,
    "files": [
      "docs/fixes/FIX_DESCRIPTION.md",
      "docs/technical/CHANGE_LOG.md"
    ]
  }
}
```

---

## ⚙️ code_surgeon EXECUTION PROCESS

### Process Flow
```
1. PREPARE
   ├── Analyze target file
   ├── Identify exact code location
   ├── Extract context (5 lines minimum)
   └── Validate syntax

2. CREATE JOB
   ├── Generate job JSON
   ├── Include validation checks
   ├── Enable rollback
   └── Add testing requirements

3. EXECUTE
   ├── Load job file
   ├── Run pre-execution validation
   ├── Apply modification
   ├── Verify syntax
   └── Run post-execution validation

4. TEST
   ├── Run unit tests
   ├── Run integration tests
   ├── Manual verification
   └── Validate rollback capability

5. DOCUMENT
   ├── Update documentation
   ├── Create implementation record
   ├── Archive job file
   └── Update changelog
```

---

## 🛡️ VALIDATION GATES

### Pre-Execution Validation (REQUIRED)

Before ANY modification:
```javascript
// 1. File Existence Check
if (!fileExists('dist/dashboard_enhanced.html')) {
    throw new Error('Target file not found');
}

// 2. Syntax Validation
if (!isValidHTML(currentFile)) {
    throw new Error('File contains syntax errors');
}

// 3. Original Code Location
if (!findInFile(originalCode, targetFile)) {
    throw new Error('Original code not found at expected location');
}

// 4. Backup Creation
createBackup(targetFile, backupName);

// 5. Job File Integrity
if (!validateJobJSON(jobFile)) {
    throw new Error('Job file invalid or incomplete');
}
```

### Post-Execution Validation (REQUIRED)

After EVERY modification:
```javascript
// 1. Modification Verification
if (!findInFile(newCode, targetFile)) {
    throw new Error('New code not found in file');
}

// 2. Syntax Check
if (!isValidHTML(modifiedFile)) {
    rollback(backupName);
    throw new Error('Modification introduced syntax errors');
}

// 3. Context Preservation
if (!verifyContext(targetFile, contextMarkers)) {
    rollback(backupName);
    throw new Error('Surrounding code was corrupted');
}

// 4. File Integrity
if (!verifyFileIntegrity(targetFile)) {
    rollback(backupName);
    throw new Error('File integrity compromised');
}

// 5. Test Execution (CRITICAL)
if (!runUnitTests()) {
    rollback(backupName);
    throw new Error('Unit tests failed after modification');
}

// 6. Integration Test Execution (CRITICAL)
if (!runIntegrationTests()) {
    rollback(backupName);
    throw new Error('Integration tests failed after modification');
}

// 7. Real Data Validation
if (!verifyWithRealData()) {
    rollback(backupName);
    throw new Error('Modification fails with real dashboard data');
}
```

### Test Execution Requirements (MANDATORY)

**Unit Tests** must verify:
- ✅ The modified function works correctly in isolation
- ✅ Input/output contracts are satisfied
- ✅ Edge cases and error conditions handled
- ✅ Real test data (not mocks) used for verification

**Integration Tests** must verify:
- ✅ No side effects on dependent modules
- ✅ Complete event chains work end-to-end
- ✅ Data flow across module boundaries is intact
- ✅ UI updates reflect calculation changes
- ✅ Persistence layer correctly stores/retrieves data

**Example Test Commands:**
```bash
# Unit tests for specific functionality
pytest tests/unit/test_status_inclusion.py -v

# Integration tests for the complete feature
pytest tests/integration/test_status_inclusion_flow.py -v

# All tests to verify no regressions
pytest tests/ -v --tb=short

# Coverage report to ensure tested code
pytest tests/ --cov=src/ --cov-report=html
```

---

## 🛡️ VALIDATION GATES// 2. Syntax Check
if (!isValidHTML(modifiedFile)) {
    rollback(backupName);
    throw new Error('Modification introduced syntax errors');
}

// 3. Context Preservation
if (!verifyContext(targetFile, contextMarkers)) {
    rollback(backupName);
    throw new Error('Surrounding code was corrupted');
}

// 4. File Integrity
if (!verifyFileIntegrity(targetFile)) {
    rollback(backupName);
    throw new Error('File integrity compromised');
}

// 5. Test Execution
if (!runTests(testSuite)) {
    rollback(backupName);
    throw new Error('Tests failed after modification');
}
```

---

## 🚫 PROHIBITED PATTERNS

### NEVER Use Direct Edits for Production Files
```javascript
// ❌ ABSOLUTELY FORBIDDEN
replace_string_in_file({
    filePath: 'dist/dashboard_enhanced.html',
    oldString: '...',
    newString: '...'
});

// ❌ ABSOLUTELY FORBIDDEN  
run_in_terminal({
    command: 'sed -i "s/old/new/" dist/dashboard_enhanced.html'
});

// ✅ MANDATORY: Use code_surgeon
createCodeSurgeonJob({
    file: 'dist/dashboard_enhanced.html',
    originalCode: '...',
    newCode: '...'
});
```

### NEVER Skip Parsing Requirements
```javascript
// ❌ WRONG: Incomplete context
originalCode: "someFunction() {"

// ✅ CORRECT: Full context with surrounding code
originalCode: `
    // Previous method
    previousMethod() {
        // implementation
    },

    /**
     * Some Function
     */
    someFunction() {
`
```

---

## 📊 code_surgeon JOB CHECKLIST

Before creating ANY job file:

- [ ] **File Identification**: Target file is `dist/dashboard_enhanced.html`?
- [ ] **Operation Type**: Clear operation (replace/insert/delete)?
- [ ] **Exact Parsing**: Original code includes 5+ lines of context?
- [ ] **Syntax Valid**: Both original and new code have valid syntax?
- [ ] **Context Markers**: Clear before/after markers identified?
- [ ] **Validation Checks**: Pre and post-execution checks defined?
- [ ] **Rollback Setup**: Rollback enabled with backup?
- [ ] **Testing Plan**: Unit/integration/manual tests specified?
- [ ] **Documentation**: Related docs files identified?
- [ ] **Risk Assessment**: Risk level evaluated?

---

## 🎯 RESPONSE TEMPLATES FOR code_surgeon

### When User Requests Code Modification
```
"I'll create a code_surgeon job to implement this change safely.

Job Details:
- File: dist/dashboard_enhanced.html
- Operation: [replace/insert/delete]
- Change: [Clear description]
- Risk Level: [Low/Medium/High]

The job will include:
- Complete context (5+ lines before/after)
- Pre/post-execution validation
- Automatic rollback capability
- Testing requirements

Job file: surgery/jobs/[timestamp]_[name].json

Should I proceed with job creation?"
```

### When Job Execution is Complete
```
"Code_surgeon job executed successfully:

✅ File Modified: dist/dashboard_enhanced.html
✅ Validation Passed: All pre/post checks completed
✅ Backup Created: [backup_filename]
✅ Tests Passed: [test count] tests successful
✅ Documentation Updated: [files updated]

Modification Details:
- Lines Modified: [line range]
- Change Type: [type]
- Rollback Available: Yes (backup: [name])

The change is now live and fully validated."
```

### When Issues Occur
```
"⚠️ code_surgeon Job Failed - Automatic Rollback Triggered

Error: [Specific error]
Action: Automatic rollback to backup

Investigation:
1. Original file restored from backup
2. Pre-execution validation failed at: [checkpoint]
3. No modifications applied to production

Next Steps:
1. Review the original code parsing
2. Verify job file syntax
3. Resubmit corrected job
```

---

## 🏆 code_surgeon BEST PRACTICES

### 1. **Always Use Complete Context**
```javascript
// Parse minimum 5 lines before and after target code
// Include all braces, parentheses, and brackets
// Preserve exact whitespace and indentation
```

### 2. **Validate Syntax Before Submission**
```javascript
// Check for balanced braces/parentheses
// Verify no incomplete statements
// Test that original code actually exists
```

### 3. **Enable Full Rollback Capability**
```javascript
// Always: "rollback": { "enabled": true }
// Always: Create backup file
// Always: Keep previous backups
```

### 4. **Specify All Test Requirements**
```javascript
// List all affected unit tests
// Identify integration test scenarios
// Document manual verification steps
```

### 5. **Document Everything**
```javascript
// Clear description of change
// Explicit rationale for modification
// Impact assessment on system
// Risk level evaluation
```

---

## 🔐 EXCEPTION HANDLING

### ONLY Exception to code_surgeon Requirement
```
Source code files (src/modules/, src/styles/) can use direct edit
IF AND ONLY IF:
1. Build pipeline will recompile to dist/
2. Tests pass after modification
3. Build succeeds without errors
4. Resulting dist/ file is validated

Even then, consider code_surgeon for audit trail.
```

### NEVER Exception to code_surgeon Requirement
```
❌ dist/dashboard_enhanced.html ALWAYS requires code_surgeon
❌ No "quick fixes" without job file
❌ No "temporary changes" without validation
❌ No "urgent modifications" without rollback
```

---

## 📋 MODIFICATION REQUEST WORKFLOW

### When User Requests Code Change

```
User: "Fix the tooltip issue in the admin panel"

Step 1: CLARIFY
├── What exact behavior needs changing?
├── What is the current problematic code?
├── What should the new behavior be?
└── Where in the file is this located?

Step 2: PARSE
├── Locate exact code in dist/dashboard_enhanced.html
├── Extract 5+ lines of context before/after
├── Verify code syntax validity
└── Identify surrounding context markers

Step 3: CREATE JOB
├── Generate complete code_surgeon job
├── Include validation checks
├── Enable rollback
└── Specify testing requirements

Step 4: CONFIRM
├── Show user the exact changes
├── Explain validation approach
├── Request approval to proceed
└── Create job file

Step 5: EXECUTE (upon approval)
├── Run job file through code_surgeon
├── Verify all validations pass
├── Run test suite
└── Document completion

Step 6: VERIFY
├── Manual testing of changed feature
├── Check for side effects
├── Validate related functionality
└── Update documentation
```

---

## 🏆 SUCCESS CRITERIA

A successful code modification:

- ✅ Uses code_surgeon workflow (NO EXCEPTIONS for dist/)
- ✅ Includes complete context parsing (5+ lines)
- ✅ Has valid before/after syntax
- ✅ Passes all pre-execution validation
- ✅ Passes all post-execution validation
- ✅ All tests pass successfully
- ✅ Rollback capability confirmed
- ✅ Documentation fully updated
- ✅ Clear audit trail maintained

---

## 🚫 FAILURE CRITERIA

A modification fails if:

- ❌ code_surgeon not used for dist/ modifications
- ❌ Incomplete context parsing (< 5 lines)
- ❌ Invalid or unbalanced syntax
- ❌ Pre-execution validation fails
- ❌ Post-execution validation fails
- ❌ Tests fail
- ❌ Rollback not enabled
- ❌ No backup created
- ❌ Documentation not updated

---

*This protocol is MANDATORY. Code modifications to dist/dashboard_enhanced.html without code_surgeon compliance will be rejected. The parsing requirements are strict and MUST be followed exactly for every modification.*