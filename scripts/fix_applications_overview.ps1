# Fix Applications Overview HTML in dist/dashboard_enhanced.html
# This script replaces the Applications Overview tab content with the world-class version

$filePath = "c:\PROYECTOS\Dashboard\dist\dashboard_enhanced.html"

# Read the file
$content = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)

# Find and replace the rest of the table headers (one at a time to handle encoding issues)

# Step 1: Replace AUTO-WEIGHT header
$content = $content -replace 'title="Auto-calculated Weight">⚖️ AUTO-WEIGHT</th>', 'style="padding: 12px 14px; text-align: center; font-size: 12px; font-weight: 600; color: #aaa; text-transform: uppercase; letter-spacing: 0.5px; border-right: 1px solid var(--ring);" title="Auto-calculated Weight">⚖️ Weight</th>'

# Step 2: Replace FACTORS header  
$content = $content -replace 'title="Business Factors">🎯 FACTORS</th>', 'style="padding: 12px 14px; text-align: center; font-size: 12px; font-weight: 600; color: #aaa; text-transform: uppercase; letter-spacing: 0.5px; border-right: 1px solid var(--ring);" title="Business Factors">🎯 Factors</th>'

# Step 3: Replace PROGRESS header
$content = $content -replace 'title="Progress">📈 PROGRESS</th>', 'style="padding: 12px 14px; text-align: left; font-size: 12px; font-weight: 600; color: #aaa; text-transform: uppercase; letter-spacing: 0.5px; border-right: 1px solid var(--ring);" title="Progress">📈 Progress</th>'

# Step 4: Replace STATUS header
$content = $content -replace 'title="Status">✓ STATUS</th>', 'style="padding: 12px 14px; text-align: center; font-size: 12px; font-weight: 600; color: #aaa; text-transform: uppercase; letter-spacing: 0.5px;" title="Status">✓ Status</th>'

# Step 5: Fix the tbody styling
$content = $content -replace 'id="appsOverviewTableBody">', 'id="appsOverviewTableBody" style="background: transparent;">'

# Step 6: Update the table-header-info
$content = $content -replace '<div class="table-header-info">', '<div class="table-header-info" style="padding: 12px 16px; background: rgba(91,157,255,0.05); display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--ring);">'
$content = $content -replace '<span class="table-info-text">Showing <strong id="appsCountDisplay">0</strong> applications</span>', '<span style="font-size: 12px; color: #aaa;"><span style="font-weight: 600; color: var(--text);">📋</span> Showing <strong id="appsCountDisplay" style="color: #5b9dff;">0</strong> of <strong id="appsTotalDisplay" style="color: #5b9dff;">0</strong> applications</span><span id="filterBadges" style="font-size: 11px; color: #aaa;"></span>'

# Step 7: Add border-radius and styling to the container
$content = $content -replace '<div class="apps-table-container-premium">', '<div class="apps-table-container-premium" style="border-radius: 10px; border: 1px solid var(--ring); overflow: hidden;">'

# Step 8: Fix empty state styling
$content = $content -replace '<div class="table-empty-state" id="emptyState" style="display: none;">', '<div class="table-empty-state" id="emptyState" style="display: none; padding: 40px 20px; text-align: center;">'
$content = $content -replace '<div class="empty-state-icon">🔍</div>', '<div class="empty-state-icon" style="font-size: 48px; margin-bottom: 12px;">🔍</div>'
$content = $content -replace '<div class="empty-state-title">No applications found</div>', '<div class="empty-state-title" style="font-size: 16px; font-weight: 600; color: var(--text); margin-bottom: 8px;">No applications found</div>'
$content = $content -replace '<div class="empty-state-description">Try adjusting your filters or search criteria</div>', '<div class="empty-state-description" style="font-size: 13px; color: #aaa;">Try adjusting your filters or search criteria</div>'

# Step 9: Update thead styling
$content = $content -replace '(<table class="app-table-premium world-class" id="appsOverviewTable"[^>]*>)\s*<thead>', '$1<thead style="background: rgba(91,157,255,0.08); border-bottom: 2px solid var(--ring);">'

# Write the file back
[System.IO.File]::WriteAllText($filePath, $content, [System.Text.Encoding]::UTF8)

Write-Host "✓ Applications Overview HTML has been updated!" -ForegroundColor Green
Write-Host "Updated file: $filePath" -ForegroundColor Cyan
