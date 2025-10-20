/* ========== Data Loader Module ========== */
const DataLoader = {
  // Embedded JSON data to avoid CORS issues with local file access
  embeddedData: {
    "metadata": {
      "source_file": "C:\\PROYECTOS\\Dashboard\\tables.xlsx",
      "creation_date": "2025-10-18 21:03:56",
      "total_sheets": 3,
      "sheet_names": [
        "business_units_catalog",
        "apps_catalog",
        "waves_catalog"
      ]
    },
    "data": {
      "business_units_catalog": {
        "records": [
          {
            "BU_ID": 1,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "COMM",
            "BU_FULLNAME": "Communications"
          },
          {
            "BU_ID": 2,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "HR",
            "BU_FULLNAME": "Human Resources"
          },
          {
            "BU_ID": 3,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "PAY",
            "BU_FULLNAME": "Payroll & Time Keeping"
          },
          {
            "BU_ID": 4,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "ACC",
            "BU_FULLNAME": "Accounting"
          },
          {
            "BU_ID": 5,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "INV",
            "BU_FULLNAME": "Invoicing"
          },
          {
            "BU_ID": 6,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "CUSTI1",
            "BU_FULLNAME": "Customs I (CCCCCS)"
          },
          {
            "BU_ID": 7,
            "BU_DOMAIN": "CORF",
            "BU_NAME": "CUSTI1",
            "BU_FULLNAME": "Customs II (MX Applications)"
          },
          {
            "BU_ID": 8,
            "BU_DOMAIN": "P&S",
            "BU_NAME": "P&S",
            "BU_FULLNAME": "Parts & Services"
          },
          {
            "BU_ID": 9,
            "BU_DOMAIN": "P&S",
            "BU_NAME": "PSC",
            "BU_FULLNAME": "Purchase & Supply Chain"
          },
          {
            "BU_ID": 10,
            "BU_DOMAIN": "GDPA",
            "BU_NAME": "CDA3",
            "BU_FULLNAME": "Global Digital Platforms and Automation"
          },
          {
            "BU_ID": 11,
            "BU_DOMAIN": "SPP",
            "BU_NAME": "SPP",
            "BU_FULLNAME": "Standard Procedures & Performance"
          },
          {
            "BU_ID": 12,
            "BU_DOMAIN": "EDSC",
            "BU_NAME": "EDSC",
            "BU_FULLNAME": "Engineering"
          }
        ],
        "record_count": 12
      },
      "apps_catalog": {
        "records": [
          {
            "APP_ID": 1,
            "BU_ID": 10,
            "WAVE_ID": 1,
            "APP_NAME": "XXX_APPLICATION_1_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "High",
            "APP_BUSINESS_IMPACT": "High",
            "APP_COMPLETION_PROGRESS": 100.0,
            "APP_STATUS": "Completed"
          },
          {
            "APP_ID": 2,
            "BU_ID": 10,
            "WAVE_ID": 1,
            "APP_NAME": "XXX_APPLICATION_2_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "Medium",
            "APP_BUSINESS_IMPACT": "Medium",
            "APP_COMPLETION_PROGRESS": 100.0,
            "APP_STATUS": "Completed"
          },
          {
            "APP_ID": 3,
            "BU_ID": 1,
            "WAVE_ID": 1,
            "APP_NAME": "XXX_APPLICATION_3_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "Medium",
            "APP_BUSINESS_IMPACT": "Medium",
            "APP_COMPLETION_PROGRESS": 83.56,
            "APP_STATUS": "WIP"
          },
          {
            "APP_ID": 4,
            "BU_ID": 10,
            "WAVE_ID": 2,
            "APP_NAME": "XXX_APPLICATION_4_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "Medium",
            "APP_BUSINESS_IMPACT": "Medium",
            "APP_COMPLETION_PROGRESS": 0.0,
            "APP_STATUS": "TBS"
          },
          {
            "APP_ID": 5,
            "BU_ID": 2,
            "WAVE_ID": 2,
            "APP_NAME": "XXX_APPLICATION_5_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "Low",
            "APP_BUSINESS_IMPACT": "Low",
            "APP_COMPLETION_PROGRESS": 22.1,
            "APP_STATUS": "WIP"
          },
          {
            "APP_ID": 6,
            "BU_ID": 10,
            "WAVE_ID": 2,
            "APP_NAME": "XXX_APPLICATION_6_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "High",
            "APP_BUSINESS_IMPACT": "Low",
            "APP_COMPLETION_PROGRESS": 7.8,
            "APP_STATUS": "Completed"
          },
          {
            "APP_ID": 7,
            "BU_ID": 3,
            "WAVE_ID": 2,
            "APP_NAME": "XXX_APPLICATION_7_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "Low",
            "APP_BUSINESS_IMPACT": "High",
            "APP_COMPLETION_PROGRESS": 0.0,
            "APP_STATUS": "TBS"
          },
          {
            "APP_ID": 8,
            "BU_ID": 3,
            "WAVE_ID": 3,
            "APP_NAME": "XXX_APPLICATION_8_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "Medium",
            "APP_BUSINESS_IMPACT": "High",
            "APP_COMPLETION_PROGRESS": 53.3,
            "APP_STATUS": "WIP"
          },
          {
            "APP_ID": 9,
            "BU_ID": 10,
            "WAVE_ID": 3,
            "APP_NAME": "XXX_APPLICATION_9_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "High",
            "APP_BUSINESS_IMPACT": "Low",
            "APP_COMPLETION_PROGRESS": 0.0,
            "APP_STATUS": "TBS"
          },
          {
            "APP_ID": 10,
            "BU_ID": 11,
            "WAVE_ID": 3,
            "APP_NAME": "XXX_APPLICATION_10_XXX",
            "APP_PRIORITY_ORDER": null,
            "APP_CRITICALITY": "High",
            "APP_BUSINESS_IMPACT": "Medium",
            "APP_COMPLETION_PROGRESS": 75.0,
            "APP_STATUS": "WIP"
          }
        ],
        "record_count": 10
      },
      "waves_catalog": {
        "records": [
          {
            "WAVE_ID": 1,
            "DESCRIPTION": "Wave 1"
          },
          {
            "WAVE_ID": 2,
            "DESCRIPTION": "Wave 2"
          },
          {
            "WAVE_ID": 3,
            "DESCRIPTION": "Wave 3"
          }
        ],
        "record_count": 3
      }
    }
  },
  
  async loadData() {
    try {
      // Use embedded data instead of fetching from file
      // to avoid CORS issues with local file access
      const jsonData = this.embeddedData;
      console.log("JSON data loaded from embedded source:", jsonData);
      
      // Process business units data from the JSON
      const businessUnits = jsonData.data.business_units_catalog.records.map(bu => ({
        id: bu.BU_ID,
        key: bu.BU_DOMAIN,
        name: bu.BU_NAME,
        domain: bu.BU_DOMAIN,
        fullname: bu.BU_FULLNAME,
        progress: 0 // Will be calculated from apps
      }));
      
      // Process apps data from the JSON
      const apps = jsonData.data.apps_catalog.records.map(app => ({
        id: app.APP_ID,
        buId: app.BU_ID,
        name: app.APP_NAME,
        status: app.APP_STATUS === "Completed" ? "CLO" : 
                app.APP_STATUS === "WIP" ? "WIP" : "TBS",
        progress: app.APP_COMPLETION_PROGRESS || 0,
        criticality: app.APP_CRITICALITY || "Medium",
        weight: app.APP_CRITICALITY === "High" ? 3 :
               app.APP_CRITICALITY === "Medium" ? 2 : 1
      }));
      
      // Process waves data from the JSON
      const waves = jsonData.data.waves_catalog.records.map(wave => ({
        id: wave.WAVE_ID,
        name: wave.DESCRIPTION
      }));
      
      // Save the loaded data to localStorage
      Dashboard.StorageManager.saveConfig({
        buses: businessUnits,
        apps: apps,
        waves: waves
      });
      
      // Return processed data for immediate use
      return businessUnits.map(bu => {
        // Calculate progress for each BU based on its apps
        const buApps = apps.filter(app => app.buId === bu.id);
        let progress = 0;
        if (buApps.length > 0) {
          const totalWeight = buApps.reduce((sum, app) => sum + (app.weight || 1), 0);
          const weightedProgress = buApps.reduce((sum, app) => 
            sum + (app.progress * (app.weight || 1)), 0);
          progress = totalWeight > 0 ? weightedProgress / totalWeight : 0;
        }
        return {
          key: bu.key,
          name: bu.name,
          progress: progress
        };
      });
    } catch (error) {
      console.error("Error loading JSON data:", error);
      // Return empty data or default data in case of error
      return [];
    }
  }
};

// Export module for namespace compatibility
(function(app) {
  app.DataLoader = DataLoader;
})(window.Dashboard = window.Dashboard || {});