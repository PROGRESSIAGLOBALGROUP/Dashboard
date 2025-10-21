/* Main entry point */
document.addEventListener('DOMContentLoaded', async function() {
    // Check if we should load data from JSON file
    const shouldLoadFromJSON = true; // You can set this to false to use default data instead
    
    if (shouldLoadFromJSON) {
        try {
            // Load data from embedded JSON and update Dashboard.DATA
            const loadedData = await Dashboard.DataLoader.loadData();
            if (loadedData && loadedData.length > 0) {
                // Replace the default DATA with loaded data
                Dashboard.DATA = loadedData;
                console.log("Data loaded successfully:", loadedData);
            }
        } catch (error) {
            console.error("Error loading data from JSON:", error);
            // In case of error, we'll use the default DATA
        }
    } else {
        // Use default data from DataProcessor.js
        Dashboard.StorageManager.init();
    }
    
    // Initialize other modules in the correct order
    Dashboard.AdminController.init();
    Dashboard.UIController.init();
});