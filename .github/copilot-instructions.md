# 🤖 AI Agent Instructions - Dashboard Enhanced

**Last Updated**: October 2025  
**Version**: 2.0  
**Project**: Dashboard Enhanced - [ Project Type ] Project Management

---

## 🎯 Project Overview

**Dashboard Enhanced** is a professional project management dashboard with real-time weighted progress calculation and complete admin capabilities. It's a single-file HTML application (no external dependencies) with embedded modules for data management, UI control, and administration.

### Core Values
- **Zero external dependencies** - Everything embedded in `dashboard_enhanced.html`
- **Persistent storage** - All data saved to browser's `localStorage` under `dashboard_config_v1`
- **Real-time calculation** - Weighted progress updates instantly as applications change
- **World-class UX** - Premium animations, modal interfaces, and responsive design
- **Production-ready** - No mocks, no placeholders, no simulation

---

## 🏗️ Architecture & Big Picture

### Three-Layer Architecture

```
## AI agent quick instructions — Dashboard Enhanced

This repo centers on a single-file web app: `dashboard_enhanced.html` (dist/ has a compiled copy).
Key idea: UI, business logic and storage live embedded; edits must respect the 3-layer separation: UIController → ProgressCalculator/AdminController → StorageManager.

Quick facts you must follow
- Single persistent source: localStorage key `dashboard_config_v1` (see `StorageManager` in `src/modules/StorageManager.js`).
- Never add external libs. The project is intentionally dependency-free; tests and build scripts are lightweight Python/Node helpers in `/scripts` and `/build`.
- Mutate data only via `StorageManager.*` APIs and call `UIController.apply()` after changes (examples: `AdminController.updateApp()` uses this flow).

Where to look (examples)
- UI: `src/modules/UIController.js` — drawing methods: `drawHero`, `renderTiles`, `drawBars`.
- Business/logic: `src/modules/DataProcessor.js` and `src/modules/AdminPanel.js` (contains admin modal flows).
- Persistence: `src/modules/StorageManager.js` — `loadConfig()`, `saveConfig()`, `addApp()` etc.
- Weighted progress formula in `src/modules/DataProcessor.js` (`calculateBUProgress()`): only include apps where status !== 'TBS'.

Code modification policy (required)
- Use the code_surgeon workflow under `code_surgeon/` and `surgery/` for edits intended for `dist/` or built artifacts. See `code_surgeon/README.md` for job format.
- For quick fixes while developing locally, edit `src/` files and run the build script in `/build` (see `build/build_enhanced_dashboard.py`).

Build / test / debug shortcuts
- Manual dev: open `dashboard_enhanced.html` in browser (works offline). Use DevTools console to call `Dashboard.StorageManager.loadConfig()` and `Dashboard.UIController.apply()`.
- Build script: `python build/build_enhanced_dashboard.py` or use `scripts/dashboard_work.py` for helper tasks.
- Unit tests: see `tests/` (jest) — run `npm test` (project `package.json` includes jest config).

Constraints and gotchas (from codebase)
- All runtime data is normalized into `buses`, `apps`, `waves`. `apps` reference `buId` (foreign key). Don't denormalize incorrectly.
- UI must not be changed outside `UIController` render methods; event wiring lives in `AdminPanel.js`.
- Exports/imports: Admin export uses JSON schema matching `dashboard_config_v1` — keep structure stable.

If you change behavior
- Update `docs/` and add a tiny test under `tests/unit/` that covers the changed function (follow existing jest style). Run `npm test` before raising PR.

When unsure: open these files first
- `src/modules/StorageManager.js`
- `src/modules/DataProcessor.js`
- `src/modules/UIController.js`
- `src/modules/AdminPanel.js`
- `code_surgeon/README.md` and `surgery/` for production patching

If this update looks good I can shorten or expand specific sections (build steps, code_surgeon job example, or add quick grep patterns) — tell me which parts to improve.
UIController.updateKPIs(items)           // KPI metrics update

// Utility methods
UIController.getCSS(varName)             // Get CSS variable value
UIController.color(percentage)           // Get color based on progress
```

---

## 🎨 CSS & Styling Patterns

### Theme Variables (CSS Custom Properties)
All colors/sizes defined as `--variable` in `:root`:
```css
--bg: #080b13                /* Main background */
--panel: #0e1627            /* Panel backgrounds */
--text: #e9eef7             /* Primary text */
--primary: #5b9dff          /* Action buttons */
--ok: #32e685               /* Success (100%) */
--warn: #ffd166             /* In progress (1-99%) */
--danger: #ff5f7a           /* Not started (0%) */
--ring: #1a2a48             /* Border/divider */
```

### Consistent Spacing
- **Gap/Margins**: 16px standard
- **Padding**: 16px in cards, 24px in modals
- **Border-radius**: 16px (modals), 14px (cards), 8px (inputs)

### Animation Easing
```css
/* Smooth entrance/exit */
animation: fadeIn 0.3s ease;
animation: slideIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
animation: popIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
```

---

## 🚀 Development Workflow

### To Add a Feature
1. **Identify layer**: Is it data (StorageManager), logic (ProgressCalculator), admin (AdminController), or UI (UIController)?
2. **Modify that module** - Add your method
3. **Call UIController.apply()** at the end to trigger refresh
4. **Test in DevTools**: F12 → Console → Check localStorage

### To Fix a Bug
1. **Reproduce in DevTools Console**: Check localStorage state
2. **Trace the flow**: Which module is failing?
3. **Add console.log()** in the method to debug
4. **Use code_surgeon protocol** (see `..\code_surgeon\README.md`) to apply fix safely

### To Make Data Changes Persist
```javascript
// ❌ DON'T: Modify Dashboard.DATA directly
Dashboard.DATA.push({...});

// ✅ DO: Use StorageManager
const newBU = Dashboard.StorageManager.addBU({
  key: "XYZ",
  name: "New Business Unit",
  domain: "CORF",
  fullname: "Description"
});

// ✅ THEN: Refresh UI
Dashboard.UIController.apply();
```

---

## 🔄 Code Modification Strategy

### Use code_surgeon Protocol
This project uses the **VSCode Local Surgery Kit** for safe, auditable code changes:

1. **Create a job** in `surgery/jobs/change_name.json`:
   ```json
   {
     "file": "dist/dashboard_enhanced.html",
    ## 🤖 AI agent quick instructions — Dashboard Enhanced

    Short: this repo is a single-file dashboard app (`dashboard_enhanced.html`) with source modules under `src/modules/`. AI patches should follow the project's three-layer separation: UIController (render) → DataProcessor/AdminPanel (logic) → StorageManager (persistence).

    Essential rules
    - Single source of truth: all runtime data lives in localStorage key `dashboard_config_v1`. Use `StorageManager.*` to read/write.
    - Never add external JS/CSS libraries. The app is intentionally dependency-free; builds are local scripts under `/build` and `/scripts`.
    - Edit `src/modules/*.js` for development and run the Python build to produce `dist/`/`dashboard_enhanced.html`. For production edits to `dist/` use the `code_surgeon` protocol (see `code_surgeon/README.md`).

    Where to look (quick map)
    - Persistence: `src/modules/StorageManager.js` — load/save, add/update/delete APIs.
    - Logic: `src/modules/DataProcessor.js` (progress formula) and `src/modules/AdminPanel.js` (admin modal flows).
    - Presentation: `src/modules/UIController.js` — all DOM updates and animations; do not mutate DOM elsewhere.

    Important examples & patterns
    - Weighted progress: see `DataProcessor.calculateBUProgress()` — include only apps where `status !== 'TBS'` and compute Σ(progress×weight)/Σ(weight).
    - Data shape: normalized arrays `buses`, `apps`, `waves`; `apps` reference `buId` (foreign key). Keep this normalization when transforming data.
    - When changing data: always call `StorageManager.saveConfig()` then `UIController.apply()` to trigger recalc + render.

    Build / test / debug shortcuts
    - Dev: open `dashboard_enhanced.html` in a browser and use DevTools. Useful console calls: `Dashboard.StorageManager.loadConfig()` and `Dashboard.UIController.apply()`.
    - Build: `python build/build_enhanced_dashboard.py` (see `/build`).
    - Tests: `npm test` (jest) — scripts are defined in `package.json`.

    Code-surgeon (production patching)
    - Use `code_surgeon/` and `surgery/` jobs to apply audited changes to `dist/dashboard_enhanced.html`. Job format and rollback/testing are in `code_surgeon/README.md`.

    Constraints (do not change)
    - Do not add external assets or libraries.
    - Do not mutate DOM outside `UIController` render methods.
    - Do not write to localStorage except via `StorageManager.saveConfig()`.
    - Keep export/import JSON schema compatible with `dashboard_config_v1`.

    If unclear or you need examples, open these files first: `src/modules/StorageManager.js`, `src/modules/DataProcessor.js`, `src/modules/UIController.js`, `src/modules/AdminPanel.js`.

    If you want, I can: (a) shorten this further, (b) add a sample code_surgeon job JSON, or (c) generate a quick grep list of key symbols. Which would you prefer?

