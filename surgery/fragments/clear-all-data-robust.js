  clearAllData() {
    // Double confirmation to prevent accidents
    const confirmed = confirm('⚠️ DANGER ZONE ⚠️\n\nThis will permanently delete ALL data:\n• Business Units\n• Applications\n• Waves\n\nThis action CANNOT be undone.\n\nAre you sure?');
    
    if (!confirmed) return;
    
    const secondConfirmation = confirm('⚠️ FINAL WARNING ⚠️\n\nType OK to confirm deletion of all data.');
    if (secondConfirmation === false) return;
    
    try {
      // Clear localStorage
      localStorage.removeItem(Dashboard.StorageManager.STORAGE_KEY);
      
      // Verify deletion
      const verification = localStorage.getItem(Dashboard.StorageManager.STORAGE_KEY);
      if (verification !== null) {
        throw new Error('Failed to clear localStorage - data still exists');
      }
      
      // Clear all cached variables
      Dashboard.AdminController.currentBUId = null;
      
      console.log('✅ All data cleared successfully from localStorage');
      
      alert('✅ All data has been permanently deleted.\n\nThe dashboard will now reload with default settings.');
      
      // Reload after showing success message
      location.reload();
    } catch (err) {
      console.error('Clear All Data Error:', err);
      alert('❌ Error clearing data:\n\n' + err.message + '\n\nPlease try again or contact support.');
    }
  },