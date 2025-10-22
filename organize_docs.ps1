# Professional documentation organization script
# Reorganizes markdown files according to world-class best practices

# Create directories if they don't exist
$dirs = @(
    "docs\guides",
    "docs\technical",
    "docs\releases",
    "docs\process"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "✅ Created: $dir"
    }
}

# Move files to appropriate directories
$moves = @{
    # GUIDES (User-facing documentation)
    "SPOTLIGHT_USER_GUIDE.md" = "docs\guides\SPOTLIGHT_USER_GUIDE.md"
    "QUICK_GUIDE_TOOLTIP_AND_SAVE_BUTTON.md" = "docs\guides\QUICK_START_GUIDE.md"
    "SOLUTION_TOOLTIP_NOT_VISIBLE.md" = "docs\guides\TOOLTIP_TROUBLESHOOTING.md"
    "README_PRIORITY_BADGE.md" = "docs\guides\PRIORITY_BADGE_GUIDE.md"
    
    # RELEASES (Version history and delivery notes)
    "EXECUTIVE_SUMMARY.md" = "docs\releases\EXECUTIVE_SUMMARY_V2.md"
    "EXECUTIVE_SUMMARY_APPLICATIONS_OVERVIEW.md" = "docs\releases\APPLICATIONS_OVERVIEW_SUMMARY.md"
    "FINAL_DELIVERY_SUMMARY.md" = "docs\releases\DELIVERY_NOTES.md"
    "PHASE_3_DELIVERY.md" = "docs\releases\PHASE_3_RELEASE_NOTES.md"
    "IMPLEMENTATION_REPORT.md" = "docs\releases\IMPLEMENTATION_SUMMARY.md"
    
    # TECHNICAL (Architecture and implementation details)
    "APPLICATIONS_OVERVIEW_FINAL_REPORT.md" = "docs\technical\APPLICATIONS_OVERVIEW_ARCHITECTURE.md"
    "AUTOMATIC_WEIGHT_IMPLEMENTATION.md" = "docs\technical\WEIGHT_CALCULATION_IMPLEMENTATION.md"
    "BU_ANALYTICS_IMPLEMENTATION_COMPLETE.md" = "docs\technical\BU_ANALYTICS_COMPLETE.md"
    "BU_ANALYTICS_QUICK_REFERENCE.md" = "docs\technical\BU_ANALYTICS_API_REFERENCE.md"
    "CALCULATION_FORMULAS_TRANSFORMATION.md" = "docs\technical\CALCULATION_FORMULAS_SPEC.md"
    "FINAL_CALCULATION_FORMULAS_TRANSFORMATION.md" = "docs\technical\CALCULATION_FORMULAS_FINAL.md"
    "PRIORITY_BADGE_TECHNICAL_REPORT.md" = "docs\technical\PRIORITY_BADGE_IMPLEMENTATION.md"
    "PRIORITY_BADGE_STYLING_IMPLEMENTATION.md" = "docs\technical\PRIORITY_BADGE_STYLES.md"
    "PRIORITY_BADGE_VISUAL_REFERENCE.md" = "docs\technical\PRIORITY_BADGE_VISUAL_SPEC.md"
    "PRIORITY_SELECTOR_IMPLEMENTATION.md" = "docs\technical\PRIORITY_SELECTOR_SPEC.md"
    "SPOTLIGHT_ENHANCEMENT_SUMMARY.md" = "docs\technical\SPOTLIGHT_FEATURES.md"
    "STATUS_AUTOMATION_IMPLEMENTATION_FINAL.md" = "docs\technical\STATUS_AUTOMATION_SPEC.md"
    "TOOLTIP_AND_SAVE_BUTTON_IMPLEMENTATION.md" = "docs\technical\TOOLTIP_SAVE_BUTTON_SPEC.md"
    "TOOLTIP_DIAGNOSTIC.md" = "docs\technical\TOOLTIP_DIAGNOSTICS.md"
    "WEIGHT_FACTOR_TOOLTIP_DELIVERY_INDEX.md" = "docs\technical\WEIGHT_TOOLTIP_INDEX.md"
    "WEIGHT_FACTOR_TOOLTIP_FINAL_SUMMARY.md" = "docs\technical\WEIGHT_TOOLTIP_FINAL.md"
    
    # PROCESS (Workflow and testing documentation)
    "VERIFICATION_CHECKLIST.md" = "docs\process\VERIFICATION_CHECKLIST.md"
    "FINAL_VERIFICATION_CHECKLIST.md" = "docs\process\FINAL_VERIFICATION_ITEMS.md"
    "TEST_SCENARIOS_BU_ANALYTICS.md" = "docs\process\TEST_SCENARIOS_BU.md"
    "STATUS_AUTOMATION_TEST_GUIDE.md" = "docs\process\TEST_GUIDE_STATUS_AUTOMATION.md"
    "FIXES_APPLIED_STATUS_AUTOMATION.md" = "docs\process\FIXES_LOG_STATUS.md"
    "IMPLEMENTATION_STATUS_AUTOMATION_COMPLETE.md" = "docs\process\IMPLEMENTATION_LOG.md"
    "FIX_TOOLTIP_EMPTY_MODAL.md" = "docs\process\FIX_LOG_TOOLTIP_EMPTY.md"
    "FIX_TOOLTIP_NOT_VISIBLE.md" = "docs\process\FIX_LOG_TOOLTIP_VISIBLE.md"
    "CLEANUP_COMPLETE.md" = "docs\process\CLEANUP_LOG.md"
    "CAMBIOS_RESUMIDOS_ANTES_DESPUES.md" = "docs\process\CHANGES_SUMMARY.md"
    "DOCUMENTATION_INDEX.md" = "docs\process\DOC_INDEX.md"
    
    # Priority badges (can consolidate)
    "PRIORITY_BADGE_DOCUMENTATION_INDEX.md" = "docs\technical\PRIORITY_BADGE_DOC_INDEX.md"
    "PRIORITY_BADGE_EXECUTIVE_SUMMARY.md" = "docs\releases\PRIORITY_BADGE_SUMMARY.md"
    "PRIORITY_BADGE_FINAL_SUMMARY.md" = "docs\releases\PRIORITY_BADGE_FINAL.md"
    "PRIORITY_BADGE_MASTER_SUMMARY.md" = "docs\releases\PRIORITY_BADGE_MASTER.md"
}

# Execute moves
$moved = 0
$skipped = 0

foreach ($source in $moves.Keys) {
    $target = $moves[$source]
    
    if (Test-Path $source) {
        try {
            Move-Item -Path $source -Destination $target -Force
            Write-Host "✅ Moved: $source → $target"
            $moved++
        } catch {
            Write-Host "❌ Failed to move $source : $_"
            $skipped++
        }
    } else {
        Write-Host "⚠️  Skipped (not found): $source"
        $skipped++
    }
}

Write-Host ""
Write-Host "Summary:"
Write-Host "Successfully moved: $moved files"
Write-Host "Skipped: $skipped files"
Write-Host ""
Write-Host "Documentation structure is now organized!"
