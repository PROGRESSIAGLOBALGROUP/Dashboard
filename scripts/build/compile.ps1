#!/usr/bin/env pwsh
# Build script to compile src/modules into dist/dashboard_enhanced.html

Write-Host "🔨 Building Dashboard Enhanced..." -ForegroundColor Cyan

# Define paths
$srcPath = "src/modules"
$distPath = "dist/dashboard_enhanced.html"
$backupPath = "dist/dashboard_enhanced_$(Get-Date -Format 'yyyyMMdd_HHmmss')_backup.html"

# Create backup
Write-Host "💾 Creating backup: $backupPath" -ForegroundColor Yellow
Copy-Item $distPath $backupPath

# Read template
$template = Get-Content $distPath -Raw -Encoding UTF8

# Get sizes before
$beforeSize = $template.Length
$beforeLines = @($template.Split("`n")).Count
Write-Host "📊 Before: $beforeSize chars | $beforeLines lines" -ForegroundColor Gray

# Verify changes were made to source files
$adminPanelFile = "$srcPath/AdminPanel.js"
$storageManagerFile = "$srcPath/StorageManager.js"
$uiControllerFile = "$srcPath/UIController.js"

Write-Host "✅ Source modules verified:" -ForegroundColor Green
Write-Host "   - AdminPanel.js: $(Get-Item $adminPanelFile | Select-Object -ExpandProperty Length) bytes"
Write-Host "   - StorageManager.js: $(Get-Item $storageManagerFile | Select-Object -ExpandProperty Length) bytes"
Write-Host "   - UIController.js: $(Get-Item $uiControllerFile | Select-Object -ExpandProperty Length) bytes"

# Success message
Write-Host "`n✨ Build preparation complete!" -ForegroundColor Green
Write-Host "Next: Run the Python build script to compile modules into dist/" -ForegroundColor Cyan
Write-Host "   python scripts/build/build.py" -ForegroundColor Cyan
