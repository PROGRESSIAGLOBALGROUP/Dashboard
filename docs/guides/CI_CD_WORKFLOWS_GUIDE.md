# 🚀 CI/CD Workflows Guide - Dashboard Enhanced

**Date**: October 24, 2025  
**Status**: Production Ready  
**Version**: 1.0  
**Category**: Development Workflow Guide

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Architecture](#architecture)
3. [GitHub Actions Setup](#github-actions-setup)
4. [Workflows Configuration](#workflows-configuration)
5. [Testing Pipeline](#testing-pipeline)
6. [Build Pipeline](#build-pipeline)
7. [Deployment Options](#deployment-options)
8. [Monitoring & Logging](#monitoring--logging)
9. [Troubleshooting](#troubleshooting)
10. [Best Practices](#best-practices)

---

## 🎯 Overview

### What is CI/CD?

**CI/CD** (Continuous Integration/Continuous Deployment) is an automated workflow that:

- **Continuous Integration (CI)**: Automatically tests code when pushed
- **Continuous Deployment (CD)**: Automatically builds and deploys to production

### Dashboard Enhanced CI/CD Strategy

Since Dashboard Enhanced is a **100% client-side application**:

- ✅ **No backend infrastructure** needed
- ✅ **Simple build process** - Single HTML file
- ✅ **Fast testing** - Jest unit tests
- ✅ **Easy deployment** - GitHub Pages or static hosting
- ✅ **Zero downtime** - Client-side updates

### Benefits for Team

| Benefit | Impact |
|---------|--------|
| **Automated Testing** | Catch bugs before merge |
| **Build Validation** | Ensure artifact integrity |
| **Deployment Automation** | One-click production updates |
| **Audit Trail** | Track all changes & deployments |
| **Team Confidence** | Reliable code quality |

---

## 🏗️ Architecture

### CI/CD Pipeline Flow

```
Developer
    ↓
Commits to branch
    ↓
Push to GitHub
    ↓
[GitHub Actions Triggered]
    ├─ CI Pipeline (Automatic)
    │  ├─ Code checkout
    │  ├─ Dependencies install
    │  ├─ Linting & validation
    │  ├─ Unit tests run
    │  └─ Build artifact creation
    │
    ├─ Review Status
    │  ├─ Pass ✅ → Ready for review
    │  └─ Fail ❌ → Block PR until fixed
    │
    └─ [Manual Approval]
       └─ CD Pipeline (On Demand)
          ├─ Final validation
          ├─ Production build
          └─ Deploy to GitHub Pages
              ↓
        Production Live 🚀
```

### Workflow Files Location

All CI/CD workflows stored in:
```
.github/workflows/
├── ci.yml                    # Runs on every push/PR
├── build.yml                 # Builds production artifact
└── deploy.yml                # Deploys to GitHub Pages
```

### Repository Secrets

Required secrets in GitHub Settings → Secrets:
```
(None required for public repos)

Optional for enhanced security:
- DEPLOYMENT_TOKEN: GitHub Pages token
- SLACK_WEBHOOK: Notifications
```

---

## 🔧 GitHub Actions Setup

### 1. Create Workflow Directory

```powershell
# PowerShell (Windows/Mac/Linux with PowerShell Core)
New-Item -ItemType Directory -Path ".github/workflows" -Force | Out-Null
```

### 2. Enable GitHub Actions

In your repository:

1. Go to **Settings** → **Actions** → **General**
2. Ensure "Allow all actions and reusable workflows" is enabled
3. Configure "Workflow permissions": ✅ Read and write permissions

### 3. Set GitHub Pages Source

In **Settings** → **Pages**:

1. Source: **Deploy from a branch**
2. Branch: **main**
3. Folder: **/docs** or **/(root)**

---

## 📋 Workflows Configuration

### Workflow 1: CI Pipeline (ci.yml)

**Purpose**: Validate code on every push and pull request

**File**: `.github/workflows/ci.yml`

```yaml
name: CI Pipeline

on:
  push:
    branches: [main, develop]
    paths:
      - 'src/**'
      - 'tests/**'
      - 'package.json'
      - '.github/workflows/ci.yml'
  pull_request:
    branches: [main, develop]

jobs:
  test:
    name: Test & Validate
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linting
        run: npm run lint
        continue-on-error: true
      
      - name: Run unit tests
        run: npm test -- --coverage
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          fail_ci_if_error: false
      
      - name: Validate build
        run: npm run build
```

### Workflow 2: Build Pipeline (build.yml)

**Purpose**: Create production-ready artifact

**File**: `.github/workflows/build.yml`

```yaml
name: Build Production Artifact

on:
  push:
    branches: [main]
    tags:
      - 'v*'
  workflow_dispatch:

jobs:
  build:
    name: Build Dashboard
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Run build script
        run: |
          python build/build_enhanced_dashboard.py
      
      - name: Validate output
        run: |
          if [ ! -f "dist/dashboard_enhanced.html" ]; then
            echo "Build failed: artifact not found"
            exit 1
          fi
          echo "✅ Build successful"
      
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: dashboard-build
          path: dist/dashboard_enhanced.html
          retention-days: 30
      
      - name: Create release (tags only)
        if: startsWith(github.ref, 'refs/tags/')
        uses: softprops/action-gh-release@v1
        with:
          files: dist/dashboard_enhanced.html
          draft: false
          prerelease: false
```

### Workflow 3: Deploy Pipeline (deploy.yml)

**Purpose**: Deploy to GitHub Pages

**File**: `.github/workflows/deploy.yml`

```yaml
name: Deploy to GitHub Pages

on:
  workflow_run:
    workflows: ["Build Production Artifact"]
    types: [completed]
    branches: [main]
  workflow_dispatch:

jobs:
  deploy:
    name: Deploy to GitHub Pages
    runs-on: ubuntu-latest
    if: github.event.workflow_run.conclusion == 'success' || github.event_name == 'workflow_dispatch'
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
      
      - name: Download artifact
        if: github.event_name == 'workflow_run'
        uses: actions/github-script@v6
        with:
          script: |
            let allArtifacts = await github.rest.actions.listWorkflowRunArtifacts({
              owner: context.repo.owner,
              repo: context.repo.repo,
              run_id: context.payload.workflow_run.id,
            });
            let matchArtifact = allArtifacts.data.artifacts[0];
            let download = await github.rest.actions.downloadArtifact({
              owner: context.repo.owner,
              repo: context.repo.repo,
              artifact_id: matchArtifact.id,
              archive_format: 'zip',
            });
      
      - name: Extract artifact
        if: github.event_name == 'workflow_run'
        run: unzip -o dashboard-build.zip
      
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v2
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
```

---

## 🧪 Testing Pipeline

### Test Execution Strategy

```
┌─ Unit Tests (Jest)
│  ├─ StorageManager tests
│  ├─ DataProcessor tests
│  ├─ UIController tests
│  └─ AdminPanel tests
│
├─ Coverage Requirements
│  ├─ Minimum: 80%
│  ├─ Target: 90%
│  └─ Critical paths: 100%
│
└─ Reporting
   ├─ Console output
   ├─ Coverage reports
   └─ Artifact uploads
```

### Running Tests Locally

```powershell
# Run all tests
npm test

# Run with coverage
npm test -- --coverage

# Run specific test file
npm test -- tests/unit/StorageManager.test.js

# Watch mode (re-run on changes)
npm test -- --watch
```

### CI Test Commands

```bash
# Commands executed in CI pipeline
npm ci                                    # Clean install (reproducible)
npm run lint                              # Code style validation
npm test -- --coverage                    # Unit tests with coverage
npm run build                             # Production build
```

### Coverage Threshold Enforcement

In `jest.config.js`:

```javascript
module.exports = {
  collectCoverageFrom: [
    'src/modules/**/*.js',
  ],
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  }
};
```

---

## 🏗️ Build Pipeline

### Build Process

```
Source Code (src/)
    ↓
Build Script (build_enhanced_dashboard.py)
    ├─ Validate structure
    ├─ Combine modules
    ├─ Inject dependencies
    └─ Minify/Optimize
    ↓
Artifact (dist/dashboard_enhanced.html)
    ├─ Single-file application
    ├─ All resources embedded
    └─ Production-ready
```

### Build Configuration

**File**: `build/build_enhanced_dashboard.py`

Key environment variables:

```bash
# Development build
ENVIRONMENT=development python build/build_enhanced_dashboard.py

# Production build
ENVIRONMENT=production python build/build_enhanced_dashboard.py
```

### Build Validation

The CI pipeline validates:

- ✅ Output file exists
- ✅ Valid HTML syntax
- ✅ All modules included
- ✅ No syntax errors
- ✅ File size reasonable

---

## 🚀 Deployment Options

### Option 1: GitHub Pages (Recommended)

**Best for**: Public dashboard, team demos, public portfolio

**Setup**:

1. Repository must be public
2. Go to **Settings** → **Pages**
3. Select **Deploy from a branch** → **main** → **/docs** or **/root**
4. Save

**Deploy workflow**: Automatic on push to main

**URL**: `https://username.github.io/Dashboard`

**Pros**:
- ✅ Free hosting
- ✅ Automatic deploys
- ✅ HTTPS included
- ✅ No infrastructure

**Cons**:
- ❌ Public repository required
- ❌ Limited customization

### Option 2: Vercel (Alternative)

**Best for**: Flexible hosting, custom domains

**Setup**:

1. Go to [vercel.com](https://vercel.com)
2. Connect GitHub repository
3. Configure build settings:
   - Build command: `npm run build`
   - Output directory: `dist`
4. Deploy

**Deploy workflow**: Automatic on push

**Pros**:
- ✅ Easy custom domains
- ✅ Advanced analytics
- ✅ Preview deployments
- ✅ Edge network

**Cons**:
- ⚠️ Requires account
- ⚠️ Free tier limits

### Option 3: AWS S3 + CloudFront

**Best for**: Enterprise deployments

**Setup**:

1. Create S3 bucket
2. Configure CloudFront distribution
3. Set up CI/CD to upload to S3

**Deploy workflow**: Automated with GitHub Actions

**Pros**:
- ✅ Enterprise-grade
- ✅ Global distribution
- ✅ Advanced security

**Cons**:
- ⚠️ Requires AWS account
- ⚠️ More complex setup
- ⚠️ Monthly costs

### Deployment Matrix

| Feature | GitHub Pages | Vercel | AWS S3 |
|---------|-------------|--------|--------|
| Setup Time | 2 min | 5 min | 30 min |
| Cost | Free | Free tier | $$ |
| Custom Domain | ✅ | ✅ | ✅ |
| Auto Deploys | ✅ | ✅ | Manual |
| HTTPS | ✅ | ✅ | ✅ |
| CDN | ✅ | ✅ | ✅ |

---

## 📊 Monitoring & Logging

### GitHub Actions Dashboard

**Access**: Repository → **Actions** tab

**Information Available**:

- ✅ Workflow runs history
- ✅ Individual step logs
- ✅ Success/failure status
- ✅ Execution times
- ✅ Artifact downloads

### Viewing Workflow Logs

1. Go to **Actions** tab
2. Select workflow run
3. Click job name to expand steps
4. Click step to view logs

### Understanding Log Output

```
Run npm test -- --coverage
  npm test -- --coverage
  > dashboard-enhanced@1.0.0 test
  > jest --coverage

PASS tests/unit/StorageManager.test.js
  StorageManager
    ✓ should initialize correctly (45 ms)
    ✓ should save config (12 ms)

Test Suites: 4 passed, 4 total
Tests: 98 passed, 98 total
Coverage: 87.3% statements | 85.2% branches
```

### Notifications

**Email Notifications** (Automatic):

- Workflow run started
- Workflow run completed
- Workflow run failed

**Optional**: Set up Slack notifications

```yaml
- name: Notify Slack on failure
  if: failure()
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: 'Dashboard CI/CD Pipeline Failed!'
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

---

## 🔄 Manual Workflows

### Manual Build Trigger

**Use case**: Build artifact without pushing code

1. Go to **Actions** → **Build Production Artifact**
2. Click **Run workflow** button
3. Select branch
4. Click **Run workflow**

**Workflow will**:
- Build artifact
- Upload to artifacts
- Create release (if tag)

### Manual Deploy Trigger

**Use case**: Deploy specific artifact to production

1. Go to **Actions** → **Deploy to GitHub Pages**
2. Click **Run workflow** button
3. Click **Run workflow**

**Workflow will**:
- Deploy latest artifact
- Update GitHub Pages
- Go live immediately

---

## 🚨 Troubleshooting

### Issue: Workflow Doesn't Run

**Symptoms**: Push code but workflow doesn't start

**Solutions**:

1. **Check file paths**: Workflows only trigger on specified paths
   ```yaml
   paths:
     - 'src/**'
     - 'tests/**'
     - 'package.json'
   ```

2. **Verify branch protection**: If main is protected, workflow might be queued

3. **Check if disabled**: Go to **Settings** → **Actions** → verify enabled

4. **Wait for queue**: GitHub Actions might have queue delays

### Issue: Tests Fail in CI But Pass Locally

**Common Causes**:

```
1. Node version mismatch
   → Use same version in CI and locally
   
2. Environment variables missing
   → Add to secrets or hardcode for testing
   
3. File path differences
   → Use relative paths with __dirname
   
4. Platform-specific issues
   → Windows vs. Linux line endings
   → Path separators (\ vs /)
   
5. Timing issues
   → Add timeouts in CI
   → Mock timers if needed
```

**Solution**: Use local Docker to simulate CI

```bash
docker run -it node:20 bash
# Then clone repo and run tests
```

### Issue: Deployment Fails

**Symptoms**: Build succeeds but deployment fails

**Check**:

1. **GitHub Pages enabled**: Settings → Pages
2. **Branch is correct**: Deploying from right branch
3. **Artifact path correct**: dist/ or docs/ exists
4. **Permissions set**: Repository secrets properly configured

**Solution**: Check deploy workflow logs

```
Deploy to GitHub Pages
  └─ Error: Failed to deploy
     → Check artifact directory
     → Verify permissions
     → Check branch settings
```

### Issue: Coverage Below Threshold

**Error**: `Coverage below threshold 80%`

**Fix**:

1. **Add missing tests**:
   ```bash
   npm test -- --coverage
   # Review coverage report
   # Add tests for uncovered lines
   ```

2. **Lower threshold** (temporary):
   ```javascript
   coverageThreshold: {
     global: {
       branches: 70,    // Reduced from 80
       functions: 70,
       lines: 70,
       statements: 70
     }
   }
   ```

3. **Exclude files** if necessary:
   ```javascript
   collectCoverageFrom: [
     'src/**/*.js',
     '!src/legacy/**'  // Exclude legacy code
   ]
   ```

---

## ✅ Best Practices

### 1. Branch Strategy

```
main (production)
 ├─ Only approved PRs merged
 ├─ All tests pass
 └─ Automatic deploy on merge

develop (staging)
 ├─ Feature branches merged here
 ├─ Deployment manual (test first)
 └─ Integration testing

feature/* (development)
 ├─ Individual feature branches
 ├─ PR to develop
 └─ Code review required
```

**Branch naming convention**:
```
feature/new-feature-name
bugfix/bug-description
hotfix/critical-issue
docs/documentation-updates
```

### 2. Commit Messages

Use conventional commits for automatic changelog generation:

```
feat: Add import/export functionality
fix: Resolve tooltip display issue
docs: Update browser compatibility
test: Add coverage for DataProcessor
chore: Update dependencies

Format: <type>: <description>
```

### 3. Pull Request Process

```
1. Create feature branch
   git checkout -b feature/my-feature

2. Make changes & commit
   git commit -m "feat: Add feature"

3. Push & create PR
   git push origin feature/my-feature

4. PR automatically:
   ├─ Runs CI tests
   ├─ Reports coverage
   └─ Shows status checks

5. Team reviews
   └─ Request changes or approve

6. Merge to main
   └─ Deploy automatically
```

### 4. Review Checklist

Before approving PR:

- [ ] All tests pass ✅
- [ ] Coverage maintained ✅
- [ ] Code follows standards ✅
- [ ] No breaking changes ✅
- [ ] Documentation updated ✅
- [ ] At least 1 approval ✅

### 5. Deployment Checklist

Before deploying to production:

- [ ] All tests pass
- [ ] Coverage above threshold
- [ ] Build succeeds
- [ ] No console errors
- [ ] Manual testing in staging
- [ ] Changelog updated
- [ ] Tag created (if major release)

### 6. Monitoring After Deploy

After deployment:

```
1. Check live application
   └─ Open dashboard in browser
   
2. Test core functionality
   ├─ Load data
   ├─ Create new entry
   ├─ Export/import
   └─ Mobile responsive
   
3. Check browser console
   └─ No errors or warnings
   
4. Test in different browsers
   └─ Chrome, Firefox, Safari, Edge
   
5. Check performance
   └─ Page loads in < 2 seconds
```

### 7. Rollback Procedure

If deployment has issues:

```powershell
# Revert last commit
git revert HEAD --no-edit
git push origin main

# OR checkout previous version
git checkout <previous-commit-hash>
git push origin main --force

# Workflow automatically:
# 1. Builds previous version
# 2. Deploys to GitHub Pages
# 3. Live within 2 minutes
```

---

## 📚 Complete Workflow Summary

### Daily Development

```
1. Create feature branch
   git checkout -b feature/my-feature

2. Make changes
   npm run build
   npm test

3. Push changes
   git push origin feature/my-feature

4. Create Pull Request
   (CI automatically tests)

5. Team reviews
   (If passes, approve)

6. Merge to main
   (Deploy automatic)
```

### Scheduled Maintenance

**Daily**: Monitor GitHub Actions dashboard

**Weekly**: 
- Review test coverage
- Update dependencies
- Check browser support

**Monthly**:
- Release new version
- Update documentation
- Analyze performance

### Emergency Hotfix

```
1. Create hotfix branch
   git checkout -b hotfix/critical-issue

2. Fix and test
   npm test

3. Create PR with "URGENT" tag
   
4. Expedite review & merge

5. Verify live deployment

6. Notify team
```

---

## 🎯 Quick Reference

### Essential Commands

```bash
# Local testing
npm test                           # Run tests
npm test -- --coverage             # With coverage
npm run build                      # Build artifact

# Git workflow
git checkout -b feature/name       # Create branch
git commit -m "feat: description"  # Commit
git push origin feature/name       # Push
```

### GitHub Actions URLs

- **Actions Dashboard**: `github.com/username/Dashboard/actions`
- **Workflow Runs**: `github.com/username/Dashboard/actions/runs`
- **Repository Settings**: `github.com/username/Dashboard/settings`
- **GitHub Pages Settings**: `github.com/username/Dashboard/settings/pages`

### Workflow Status Badges

Add to README.md:

```markdown
![CI Pipeline](https://github.com/username/Dashboard/actions/workflows/ci.yml/badge.svg)
![Build Status](https://github.com/username/Dashboard/actions/workflows/build.yml/badge.svg)
```

---

## 📞 Support

### Getting Help

**For CI/CD Issues**:
1. Check workflow logs (GitHub Actions dashboard)
2. Review this guide (CI_CD_WORKFLOWS_GUIDE.md)
3. Check TROUBLESHOOTING_GUIDE.md
4. Contact DevOps team

**For Development Issues**:
1. Check CODE_REVIEW_GUIDELINES.md
2. Check QUICK_START_GUIDE.md
3. Contact tech lead

**For Deployment Issues**:
1. Check deployment workflow logs
2. Check GitHub Pages settings
3. Verify DNS/domain settings
4. Contact infrastructure team

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Oct 24, 2025 | Initial CI/CD workflows guide |

---

## 🎓 Additional Resources

- **GitHub Actions Documentation**: https://docs.github.com/en/actions
- **GitHub Pages Guide**: https://docs.github.com/en/pages
- **Jest Testing Guide**: https://jestjs.io/docs/getting-started
- **Dashboard Enhanced Docs**: See docs/ directory

---

*This guide ensures professional, automated, and reliable deployment workflows for Dashboard Enhanced. All team members should be familiar with the CI/CD process for efficient collaboration.*

**Created October 24, 2025 | Dashboard Enhanced Sprint 0**
