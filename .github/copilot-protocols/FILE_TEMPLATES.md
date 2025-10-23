# 📋 File Creation Templates - GitHub Copilot

**Version**: 2.0  
**Project**: Dashboard Enhanced  
**Purpose**: Standardized templates for consistent file creation

---

## 🎯 TEMPLATE SELECTION RULES

### 1. User Request Analysis
Before using any template, analyze user's request:

```
User says: "Create [X]"
↓
Determine file type:
- Code Module → Use JavaScript Module Template
- Documentation → Use Documentation Template (appropriate category)
- Fix Script → Use Fix Script Template
- Style File → Use CSS Template
- Test File → Use Test Template
```

### 2. Path Resolution
```
File Type → Correct Directory:
- .js modules → src/modules/
- .css files → src/styles/
- .md docs → docs/[category]/
- fix scripts → scripts/fixes/
- test files → tests/[type]/
```

---

## 🧩 JAVASCRIPT MODULE TEMPLATE

**Use when**: User requests functionality, components, or modules  
**Location**: `src/modules/[ModuleName].js`

```javascript
/**
 * [Module Name] - [Brief Description]
 * 
 * Purpose: [Specific purpose of this module]
 * Dependencies: [List any dependencies]
 * Usage: [How to use this module]
 * 
 * Created: [Date]
 * Project: Dashboard Enhanced
 */

class [ModuleName] {
    constructor() {
        this.initialized = false;
        // Initialize properties
    }

    /**
     * Initialize the module
     */
    init() {
        if (this.initialized) {
            console.warn('[ModuleName] already initialized');
            return;
        }

        // Initialization logic here
        this.initialized = true;
        console.log('[ModuleName] initialized successfully');
    }

    /**
     * Main functionality methods
     */
    [methodName]() {
        // Implementation
    }

    /**
     * Cleanup and destroy
     */
    destroy() {
        // Cleanup logic
        this.initialized = false;
    }
}

// Export following project pattern
if (!window.Dashboard) window.Dashboard = {};
window.Dashboard.[ModuleName] = [ModuleName];
```

---

## 🎨 CSS TEMPLATE

**Use when**: User requests styling, themes, or visual changes  
**Location**: `src/styles/[component-name].css`

```css
/**
 * [Component Name] Styles
 * 
 * Purpose: [Specific styling purpose]
 * Components: [List components styled]
 * Dependencies: [Any CSS dependencies]
 * 
 * Created: [Date]
 * Project: Dashboard Enhanced
 */

/* ==========================================
   [COMPONENT NAME] STYLES
   ========================================== */

/* Base styles */
.[component-class] {
    /* Core styling */
}

/* State variations */
.[component-class]:hover {
    /* Hover effects */
}

.[component-class].active {
    /* Active state */
}

.[component-class].disabled {
    /* Disabled state */
}

/* Responsive design */
@media (max-width: 768px) {
    .[component-class] {
        /* Mobile adjustments */
    }
}

@media (max-width: 480px) {
    .[component-class] {
        /* Small mobile adjustments */
    }
}

/* Dark theme support (if applicable) */
@media (prefers-color-scheme: dark) {
    .[component-class] {
        /* Dark theme variations */
    }
}
```

---

## 🔧 FIX SCRIPT TEMPLATE

**Use when**: User requests bug fixes or temporary solutions  
**Location**: `scripts/fixes/[issue_name]_fix.js`

```javascript
/**
 * [Issue Name] Fix Script
 * 
 * Problem: [Description of the problem being solved]
 * Solution: [Brief description of the fix]
 * Usage: [How to use this fix script]
 * Status: Temporary fix - should be integrated into main codebase
 * 
 * Created: [Date]
 * Project: Dashboard Enhanced
 */

(function() {
    'use strict';

    // Configuration
    const CONFIG = {
        debug: true,
        timeout: 1000,
        retryAttempts: 3
    };

    /**
     * Main fix function
     */
    function applyFix() {
        try {
            // Check if fix is needed
            if (!isFixNeeded()) {
                if (CONFIG.debug) console.log('[Fix] No fix needed');
                return;
            }

            // Apply the fix
            // Implementation here

            if (CONFIG.debug) console.log('[Fix] Applied successfully');
        } catch (error) {
            console.error('[Fix] Error applying fix:', error);
        }
    }

    /**
     * Check if fix is needed
     */
    function isFixNeeded() {
        // Logic to determine if fix should be applied
        return true;
    }

    /**
     * Initialize fix when DOM is ready
     */
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', applyFix);
    } else {
        // DOM already loaded
        setTimeout(applyFix, CONFIG.timeout);
    }

    // Expose globally if needed
    window.Dashboard = window.Dashboard || {};
    window.Dashboard.[FixName] = {
        apply: applyFix,
        config: CONFIG
    };

})();
```

---

## 📄 DOCUMENTATION TEMPLATE

**Use when**: User explicitly requests documentation  
**Location**: `docs/[category]/[DOCUMENT_NAME].md`

```markdown
# [Document Title]

**Date**: [Creation Date]  
**Status**: [Draft/Review/Final]  
**Category**: [Report/Implementation/Feature/Fix/Guide/Technical]  
**Author**: GitHub Copilot  

---

## 📋 Overview

[Brief description of what this document covers]

## 🎯 Purpose

[Why this document was created and what problem it solves]

## 📊 Content

### [Section 1]
[Content here]

### [Section 2]
[Content here]

## ✅ Summary

[Key takeaways and conclusions]

## 🔗 Related Documents

- [Link to related documentation]
- [Link to implementation files]

---

*Document created as requested by user for Dashboard Enhanced project.*
```

---

## 🧪 TEST TEMPLATE

**Use when**: User requests tests or testing functionality  
**Location**: `tests/[type]/[test-name].test.js`

```javascript
/**
 * [Component/Module] Tests
 * 
 * Purpose: Test [specific functionality]
 * Coverage: [What is being tested]
 * Framework: [Testing framework used]
 * 
 * Created: [Date]
 * Project: Dashboard Enhanced
 */

describe('[Component/Module Name]', () => {
    let [componentInstance];

    beforeEach(() => {
        // Setup before each test
        [componentInstance] = new [ComponentName]();
    });

    afterEach(() => {
        // Cleanup after each test
        if ([componentInstance] && typeof [componentInstance].destroy === 'function') {
            [componentInstance].destroy();
        }
    });

    describe('Initialization', () => {
        test('should initialize correctly', () => {
            expect([componentInstance]).toBeDefined();
            expect([componentInstance].initialized).toBe(false);
        });

        test('should initialize only once', () => {
            [componentInstance].init();
            expect([componentInstance].initialized).toBe(true);
            
            // Try to initialize again
            [componentInstance].init();
            expect([componentInstance].initialized).toBe(true);
        });
    });

    describe('Core Functionality', () => {
        beforeEach(() => {
            [componentInstance].init();
        });

        test('should [specific functionality]', () => {
            // Test implementation
            expect(/* assertion */).toBe(/* expected */);
        });
    });

    describe('Error Handling', () => {
        test('should handle [error condition]', () => {
            // Error condition test
            expect(() => {
                // Code that should throw
            }).toThrow();
        });
    });
});
```

---

## ⚙️ CONFIGURATION TEMPLATE

**Use when**: User requests configuration files  
**Location**: Root or appropriate subdirectory

```json
{
  "name": "[config-name]",
  "version": "1.0.0",
  "description": "[Configuration purpose]",
  "created": "[Date]",
  "project": "Dashboard Enhanced",
  "config": {
    "setting1": "value1",
    "setting2": "value2",
    "features": {
      "feature1": true,
      "feature2": false
    },
    "paths": {
      "source": "src/",
      "output": "dist/",
      "documentation": "docs/"
    }
  },
  "validation": {
    "required": ["setting1", "setting2"],
    "optional": ["features", "paths"]
  }
}
```

---

## 📝 TEMPLATE USAGE CHECKLIST

Before using any template:

- [ ] User explicitly requested this file type
- [ ] Correct template selected for file type
- [ ] Appropriate directory path determined
- [ ] Template customized with specific details
- [ ] Naming convention followed
- [ ] Purpose clearly defined in file

---

## 🎯 TEMPLATE CUSTOMIZATION GUIDE

### For JavaScript Files:
1. Replace `[ModuleName]` with actual module name (PascalCase)
2. Replace `[methodName]` with actual method names (camelCase)
3. Add specific functionality as requested
4. Update dependencies and usage sections

### For CSS Files:
1. Replace `[component-name]` with actual component name (kebab-case)
2. Replace `[component-class]` with actual CSS class names
3. Add specific styles as requested
4. Ensure responsive design if needed

### For Documentation Files:
1. Replace bracketed placeholders with actual content
2. Choose appropriate category for `docs/` subdirectory
3. Add specific sections requested by user
4. Link to related files and documentation

### For Fix Scripts:
1. Replace `[issue_name]` with descriptive issue name
2. Replace `[FixName]` with appropriate fix identifier
3. Add specific fix logic as needed
4. Update problem/solution descriptions

---

**Remember: Templates are starting points. Always customize based on user's specific requirements and project context.**