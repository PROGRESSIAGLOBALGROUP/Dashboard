# Test-Driven Development Plan for Dashboard Enhanced

## Overview
This document outlines a comprehensive Test-Driven Development (TDD) approach for implementing and fixing the Setup button functionality in the Dashboard Enhanced application. We follow the "red, green, refactor" TDD cycle to ensure high-quality code.

> **IMPORTANT**: The Dashboard Enhanced is designed as a 100% client-side application. All tests and implementations ensure that the dashboard runs directly in the browser without requiring any server, installation processes, or external dependencies. Users must be able to open the HTML file directly in their browser without any additional setup.

## 1. Test Environment Setup

### 1.1 Testing Framework
We'll use Jest as our testing framework with jsdom to simulate browser environment.

```bash
# Setup commands
npm init -y
npm install --save-dev jest jest-environment-jsdom @testing-library/dom @testing-library/jest-dom
```

### 1.2 Project Structure
```
dashboard/
├── src/
│   ├── modules/
│   │   ├── StorageManager.js
│   │   ├── ProgressCalculator.js
│   │   ├── AdminController.js
│   │   └── UIRenderer.js
│   └── index.js
├── tests/
│   ├── unit/
│   │   ├── StorageManager.test.js
│   │   ├── ProgressCalculator.test.js
│   │   ├── AdminController.test.js
│   │   └── UIRenderer.test.js
│   └── integration/
│       └── AdminModal.test.js
├── dashboard_enhanced.html
└── package.json
```

## 2. Test Cases

### 2.1 Unit Tests: StorageManager

```javascript
// StorageManager.test.js
describe('StorageManager', () => {
  beforeEach(() => {
    // Mock localStorage
    Object.defineProperty(window, 'localStorage', {
      value: {
        getItem: jest.fn(),
        setItem: jest.fn(),
        removeItem: jest.fn(),
        clear: jest.fn(),
      },
      writable: true
    });
  });

  test('init() should initialize storage if empty', () => {
    window.localStorage.getItem.mockReturnValue(null);
    StorageManager.init();
    expect(window.localStorage.setItem).toHaveBeenCalled();
  });

  test('loadConfig() should return data from localStorage', () => {
    const mockData = JSON.stringify({ buses: [], apps: [] });
    window.localStorage.getItem.mockReturnValue(mockData);
    const result = StorageManager.loadConfig();
    expect(result).toEqual(JSON.parse(mockData));
  });

  test('saveConfig() should store data in localStorage', () => {
    const mockData = { buses: [], apps: [] };
    StorageManager.saveConfig(mockData);
    expect(window.localStorage.setItem).toHaveBeenCalledWith(
      StorageManager.STORAGE_KEY,
      JSON.stringify(mockData)
    );
  });
});
```

### 2.2 Unit Tests: AdminController

```javascript
// AdminController.test.js
describe('AdminController', () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <button id="setupAdmin"></button>
      <div id="adminModal" class="modal-overlay"></div>
    `;
  });

  test('init() should set up event listeners', () => {
    const setupBtn = document.getElementById('setupAdmin');
    const spy = jest.spyOn(setupBtn, 'addEventListener');
    
    AdminController.init();
    
    expect(spy).toHaveBeenCalledWith('click', expect.any(Function));
  });

  test('openModal() should add active class to modal', () => {
    const modal = document.getElementById('adminModal');
    
    AdminController.openModal();
    
    expect(modal.classList.contains('active')).toBe(true);
  });

  test('closeModal() should remove active class from modal', () => {
    const modal = document.getElementById('adminModal');
    modal.classList.add('active');
    
    AdminController.closeModal();
    
    expect(modal.classList.contains('active')).toBe(false);
  });

  test('setup button click should open modal', () => {
    const setupBtn = document.getElementById('setupAdmin');
    const modal = document.getElementById('adminModal');
    
    AdminController.init();
    setupBtn.click();
    
    expect(modal.classList.contains('active')).toBe(true);
  });
});
```

### 2.3 Integration Test: Admin Modal Functionality

```javascript
// AdminModal.test.js
describe('Admin Modal Integration', () => {
  beforeEach(() => {
    document.body.innerHTML = `
      <button id="setupAdmin"></button>
      <div id="adminModal" class="modal-overlay">
        <div class="modal-content">
          <button id="closeAdminModal"></button>
          <div class="modal-tabs">
            <button class="modal-tab active" data-tab="buses"></button>
            <button class="modal-tab" data-tab="apps"></button>
          </div>
          <div id="tab-buses" class="modal-tabpanel active"></div>
          <div id="tab-apps" class="modal-tabpanel"></div>
          <button id="saveAdminBtn"></button>
          <button id="cancelAdminBtn"></button>
        </div>
      </div>
    `;

    // Initialize components
    StorageManager.init();
    AdminController.init();
  });

  test('clicking Setup button should open modal', () => {
    const setupBtn = document.getElementById('setupAdmin');
    const modal = document.getElementById('adminModal');
    
    setupBtn.click();
    
    expect(modal.classList.contains('active')).toBe(true);
  });

  test('clicking Cancel button should close modal', () => {
    const modal = document.getElementById('adminModal');
    const cancelBtn = document.getElementById('cancelAdminBtn');
    
    modal.classList.add('active');
    cancelBtn.click();
    
    expect(modal.classList.contains('active')).toBe(false);
  });

  test('clicking tab should switch active panel', () => {
    const appsTab = document.querySelector('[data-tab="apps"]');
    const busesPanel = document.getElementById('tab-buses');
    const appsPanel = document.getElementById('tab-apps');
    
    appsTab.click();
    
    expect(busesPanel.classList.contains('active')).toBe(false);
    expect(appsPanel.classList.contains('active')).toBe(true);
  });
});
```

## 3. Test Implementation Plan

### 3.1 Setup Button Fix

1. **RED**: Write test that verifies clicking Setup button opens modal
2. **GREEN**: Implement fix by ensuring StorageManager and AdminController are initialized
3. **REFACTOR**: Extract event handling to separate method for better organization

### 3.2 Modal Interaction Tests

1. **RED**: Write tests for modal opening, closing and tab switching
2. **GREEN**: Implement necessary functionality
3. **REFACTOR**: Improve code structure if needed

### 3.3 Data Persistence Tests

1. **RED**: Write tests for saving and loading from localStorage
2. **GREEN**: Implement functionality
3. **REFACTOR**: Optimize storage format and access patterns

## 4. Continuous Integration Setup

```yaml
# .github/workflows/test.yml
name: Dashboard Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '16'
    - name: Install dependencies
      run: npm ci
    - name: Run tests
      run: npm test
```

## 5. Quality Checks

### 5.1 ESLint Configuration

```json
// .eslintrc.json
{
  "env": {
    "browser": true,
    "es2021": true,
    "jest": true
  },
  "extends": ["eslint:recommended"],
  "parserOptions": {
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "rules": {
    "semi": ["error", "always"],
    "quotes": ["error", "single"]
  }
}
```

### 5.2 Jest Configuration

```js
// jest.config.js
module.exports = {
  testEnvironment: 'jest-environment-jsdom',
  setupFilesAfterEnv: ['<rootDir>/tests/setup.js'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1'
  }
};
```

## 6. Testing Setup Script

```javascript
// tests/setup.js
import '@testing-library/jest-dom';

// Mock global functions
global.requestAnimationFrame = callback => setTimeout(callback, 0);
```

## 7. Example Test Run

```bash
# Run all tests
npm test

# Run specific test
npm test -- -t "AdminController"

# Run with coverage report
npm test -- --coverage
```

## 8. Modular Implementation

Extract the core functionalities into separate modules to improve maintainability:

1. StorageManager module
2. ProgressCalculator module
3. AdminController module
4. UIRenderer module

## 9. Pull Request Checklist

- [ ] All tests pass
- [ ] Code follows style guidelines
- [ ] No ESLint warnings
- [ ] Test coverage > 80%
- [ ] Documentation updated