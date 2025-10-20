/**
 * Validation script for dashboard_enhanced.html
 * Checks that the Setup button functionality is properly initialized
 */

const fs = require('fs');
const path = require('path');

// Configuration
const dashboardPath = path.join(__dirname, 'dashboard_enhanced.html');
const setupButtonId = 'setupAdmin';
const modalId = 'adminModal';

// Function to validate file
function validateSetupButton() {
    console.log('📊 DASHBOARD SETUP BUTTON VALIDATION');
    console.log('======================================');
    
    try {
        // Read the HTML file
        console.log('Reading dashboard file...');
        const html = fs.readFileSync(dashboardPath, 'utf8');
        
        // Check for initialization code
        console.log('\nChecking initialization code...');
        const hasInitCode = html.includes('StorageManager.init()') && 
                            html.includes('AdminController.init()');
        
        if (hasInitCode) {
            console.log('✅ Initialization code found');
        } else {
            console.log('❌ Initialization code missing');
            return false;
        }
        
        // Check for Setup button
        console.log('\nChecking DOM elements (static analysis)...');
        const hasSetupButton = html.includes(`id="${setupButtonId}"`);
        if (!hasSetupButton) {
            console.log('❌ Setup button not found in HTML');
            return false;
        }
        console.log('✅ Setup button found in HTML');
        
        // Check for Admin modal
        const hasModal = html.includes(`id="${modalId}"`);
        if (!hasModal) {
            console.log('❌ Admin modal not found in HTML');
            return false;
        }
        console.log('✅ Admin modal found in HTML');
        
        // Static analysis check for button click handler
        const hasClickHandlerSetup = html.includes(`$('#${setupButtonId}').addEventListener('click'`);
        
        if (hasClickHandlerSetup) {
            console.log('✅ Setup button click handler defined');
        } else {
            console.log('❌ Setup button click handler not found');
            return false;
        }
        
        console.log('\nResult: ✅ VALIDATION PASSED');
        console.log('The Setup button functionality appears to be properly initialized');
        console.log('\nNext steps:');
        console.log('1. Open dashboard_enhanced.html in your browser');
        console.log('2. Click the Setup button to verify it opens the modal');
        console.log('3. Test adding/editing business units and applications');
        
        return true;
    } catch (error) {
        console.error('\n❌ ERROR during validation:', error);
        return false;
    }
}

// Run validation
validateSetupButton();