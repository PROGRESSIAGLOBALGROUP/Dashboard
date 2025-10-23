# BU ANALYTICS EXPORT/IMPORT - IMPLEMENTATION PLAN

## Vision
Create a **world-class premium component** that allows users to:
1. Select a Business Unit
2. Export its complete analytics (apps, progress, stats)
3. Share with team members
4. Import stats from other team members' BUs and merge into main report

## Design Principles
- **Visually Stunning** - Premium gradient, smooth animations, modern UI
- **User-Centric** - Clear workflow, helpful hints, visual feedback
- **Professional** - Enterprise-grade data handling, validation, error recovery
- **Collaborative** - Seamless sharing and integration of distributed data
- **Data Integrity** - No data loss, comprehensive validation, rollback capability

## Technical Approach
- NO external dependencies (pure HTML/CSS/JS)
- NO hardcoded data
- Full validation before export/import
- StorageManager for all persistence
- Modal-based workflow for BU selection
- Real-time preview before import

## Components
1. **BU Selection Card** - Choose which BU to export
2. **Export Dialog** - Preview and export options
3. **Import Dialog** - Select file and merge strategy
4. **Analytics Data** - All apps, progress, stats for BU
5. **Merge Strategy** - How to handle conflicts

## File Format (JSON)
```json
{
  "format": "bu-analytics-v1",
  "exportedAt": "2025-10-21T...",
  "buData": {
    "id": 1,
    "key": "COMM",
    "name": "Communications",
    "domain": "CORF",
    "fullname": "Communications Department",
    "color": "#5b9dff",
    "manager": "John Doe"
  },
  "apps": [
    {
      "id": 101,
      "buId": 1,
      "name": "App Name",
      "status": "WIP",
      "progress": 75,
      "weight": 2.5,
      "criticality": "High",
      "businessImpact": "High",
      "priority": "High"
    }
  ],
  "statistics": {
    "totalApps": 5,
    "completedApps": 1,
    "wipApps": 3,
    "tbsApps": 1,
    "averageProgress": 68.5,
    "weightedProgress": 72.1
  }
}
```

## Locations to Add

1. **New Settings Card** - Before "Clear All Data" (Line 3724)
   - BU Selection Dropdown
   - Export Button
   - Import File Input
   - Preview Stats

2. **New Modal** - statusConfirmationModal level
   - Export Preview Modal
   - Import Confirmation Modal

3. **New Functions in AdminController**
   - exportBUAnalytics(buId)
   - importBUAnalytics(file)
   - previewBUAnalytics(buId)
   - mergeBUAnalytics(importedData, mergeStrategy)

4. **New CSS Styles**
   - Premium gradients
   - Smooth animations
   - Responsive design
   - Dark theme integration
