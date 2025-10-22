/* ========== Data Loader Module - CRITICAL DATA INITIALIZATION ========== */
const DataLoader = {
  embeddedData: {
    "metadata": {
      "source_file": "embedded_from_xlsx",
      "creation_date": "2025-10-18",
      "total_sheets": 3
    },
    "data": {
      "business_units_catalog": {
        "records": [
          {"BU_ID": 1, "BU_DOMAIN": "CORF", "BU_NAME": "COMM", "BU_FULLNAME": "Communications"},
          {"BU_ID": 2, "BU_DOMAIN": "CORF", "BU_NAME": "HR", "BU_FULLNAME": "Human Resources"},
          {"BU_ID": 3, "BU_DOMAIN": "CORF", "BU_NAME": "PAY", "BU_FULLNAME": "Payroll & Time Keeping"},
          {"BU_ID": 4, "BU_DOMAIN": "CORF", "BU_NAME": "ACC", "BU_FULLNAME": "Accounting"},
          {"BU_ID": 5, "BU_DOMAIN": "CORF", "BU_NAME": "INV", "BU_FULLNAME": "Invoicing"},
          {"BU_ID": 6, "BU_DOMAIN": "CORF", "BU_NAME": "CUSTI1", "BU_FULLNAME": "Customs I"},
          {"BU_ID": 7, "BU_DOMAIN": "CORF", "BU_NAME": "CUSTI2", "BU_FULLNAME": "Customs II"},
          {"BU_ID": 8, "BU_DOMAIN": "P&S", "BU_NAME": "P&S", "BU_FULLNAME": "Parts & Services"},
          {"BU_ID": 9, "BU_DOMAIN": "P&S", "BU_NAME": "PSC", "BU_FULLNAME": "Purchase & Supply Chain"},
          {"BU_ID": 10, "BU_DOMAIN": "GDPA", "BU_NAME": "CDA3", "BU_FULLNAME": "Global Digital Platforms"},
          {"BU_ID": 11, "BU_DOMAIN": "SPP", "BU_NAME": "SPP", "BU_FULLNAME": "Standard Procedures"},
          {"BU_ID": 12, "BU_DOMAIN": "EDSC", "BU_NAME": "EDSC", "BU_FULLNAME": "Engineering"}
        ]
      },
      "apps_catalog": {
        "records": [
          {"APP_ID": 1, "BU_ID": 10, "WAVE_ID": 1, "APP_NAME": "XXX_APPLICATION_1_XXX", "APP_CRITICALITY": "High", "APP_BUSINESS_IMPACT": "High", "APP_COMPLETION_PROGRESS": 100.0, "APP_STATUS": "CLO", "APP_PRIORITY": "High"},
          {"APP_ID": 2, "BU_ID": 10, "WAVE_ID": 1, "APP_NAME": "XXX_APPLICATION_2_XXX", "APP_CRITICALITY": "Medium", "APP_BUSINESS_IMPACT": "Medium", "APP_COMPLETION_PROGRESS": 100.0, "APP_STATUS": "CLO", "APP_PRIORITY": "Medium"},
          {"APP_ID": 3, "BU_ID": 1, "WAVE_ID": 1, "APP_NAME": "XXX_APPLICATION_3_XXX", "APP_CRITICALITY": "Medium", "APP_BUSINESS_IMPACT": "Medium", "APP_COMPLETION_PROGRESS": 83.56, "APP_STATUS": "WIP", "APP_PRIORITY": "Medium"},
          {"APP_ID": 4, "BU_ID": 10, "WAVE_ID": 2, "APP_NAME": "XXX_APPLICATION_4_XXX", "APP_CRITICALITY": "Medium", "APP_BUSINESS_IMPACT": "Medium", "APP_COMPLETION_PROGRESS": 0.0, "APP_STATUS": "TBS", "APP_PRIORITY": "Low"},
          {"APP_ID": 5, "BU_ID": 2, "WAVE_ID": 2, "APP_NAME": "XXX_APPLICATION_5_XXX", "APP_CRITICALITY": "Low", "APP_BUSINESS_IMPACT": "Low", "APP_COMPLETION_PROGRESS": 22.1, "APP_STATUS": "WIP", "APP_PRIORITY": "Low"},
          {"APP_ID": 6, "BU_ID": 10, "WAVE_ID": 2, "APP_NAME": "XXX_APPLICATION_6_XXX", "APP_CRITICALITY": "High", "APP_BUSINESS_IMPACT": "Low", "APP_COMPLETION_PROGRESS": 7.8, "APP_STATUS": "CLO", "APP_PRIORITY": "High"},
          {"APP_ID": 7, "BU_ID": 3, "WAVE_ID": 2, "APP_NAME": "XXX_APPLICATION_7_XXX", "APP_CRITICALITY": "Low", "APP_BUSINESS_IMPACT": "High", "APP_COMPLETION_PROGRESS": 0.0, "APP_STATUS": "TBS", "APP_PRIORITY": "Low"},
          {"APP_ID": 8, "BU_ID": 3, "WAVE_ID": 3, "APP_NAME": "XXX_APPLICATION_8_XXX", "APP_CRITICALITY": "Medium", "APP_BUSINESS_IMPACT": "High", "APP_COMPLETION_PROGRESS": 53.3, "APP_STATUS": "WIP", "APP_PRIORITY": "Medium"},
          {"APP_ID": 9, "BU_ID": 10, "WAVE_ID": 3, "APP_NAME": "XXX_APPLICATION_9_XXX", "APP_CRITICALITY": "High", "APP_BUSINESS_IMPACT": "Low", "APP_COMPLETION_PROGRESS": 0.0, "APP_STATUS": "TBS", "APP_PRIORITY": "High"},
          {"APP_ID": 10, "BU_ID": 11, "WAVE_ID": 3, "APP_NAME": "XXX_APPLICATION_10_XXX", "APP_CRITICALITY": "High", "APP_BUSINESS_IMPACT": "Medium", "APP_COMPLETION_PROGRESS": 75.0, "APP_STATUS": "WIP", "APP_PRIORITY": "High"}
        ]
      },
      "waves_catalog": {
        "records": [
          {"WAVE_ID": 1, "DESCRIPTION": "Wave 1"},
          {"WAVE_ID": 2, "DESCRIPTION": "Wave 2"},
          {"WAVE_ID": 3, "DESCRIPTION": "Wave 3"},
          {"WAVE_ID": 4, "DESCRIPTION": "Wave 4"},
          {"WAVE_ID": 5, "DESCRIPTION": "Wave 5"}
        ]
      }
    }
  },

  async loadData() {
    try {
      const jsonData = this.embeddedData;
      console.log('✅ [DataLoader] Loading embedded data...');
      
      const businessUnits = jsonData.data.business_units_catalog.records.map(bu => ({
        id: bu.BU_ID,
        key: bu.BU_DOMAIN,
        name: bu.BU_NAME,
        domain: bu.BU_DOMAIN,
        fullname: bu.BU_FULLNAME,
        apps: []
      }));
      
      const apps = jsonData.data.apps_catalog.records.map(app => ({
        id: app.APP_ID,
        buId: app.BU_ID,
        wave: `Wave ${app.WAVE_ID}`,
        name: app.APP_NAME,
        status: app.APP_STATUS === "CLO" ? "CLO" : app.APP_STATUS === "WIP" ? "WIP" : "TBS",
        progress: app.APP_COMPLETION_PROGRESS || 0,
        criticality: app.APP_CRITICALITY || "Medium",
        impact: app.APP_BUSINESS_IMPACT || "Medium",
        priority: app.APP_PRIORITY || "Medium",
        order: app.APP_ID
      }));
      
      const waves = jsonData.data.waves_catalog.records.map(wave => ({
        id: wave.WAVE_ID,
        name: wave.DESCRIPTION
      }));
      
      // Save to localStorage - THIS IS CRITICAL
      Dashboard.StorageManager.saveConfig({
        buses: businessUnits,
        apps: apps,
        waves: waves
      });
      
      console.log('✅ [DataLoader] Data saved to localStorage:', { businesses: businessUnits.length, apps: apps.length, waves: waves.length });
      return { businessUnits, apps, waves };
    } catch (error) {
      console.error("❌ [DataLoader] Error loading data:", error);
      return { businessUnits: [], apps: [], waves: [] };
    }
  }
};

if (!window.Dashboard) window.Dashboard = {};
window.Dashboard.DataLoader = DataLoader;

/* ========== Storage Manager Module ========== */
