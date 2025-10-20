/* ========== Whitelabel Dynamic Loader ========== */
function applyWhitelabelTitles() {
  const mainTitle = localStorage.getItem('wl_mainTitle');
  const subtitle = localStorage.getItem('wl_subtitle');
  
  const h1 = document.querySelector('#mainTitleDisplay');
  const small = document.querySelector('#subtitleDisplay');
  
  // CRITICAL: Only set if values exist in localStorage
  // NO fallbacks, NO defaults - only what's in persistent storage
  if (mainTitle !== null && h1) {
    h1.textContent = mainTitle;
  }
  if (subtitle !== null && small) {
    small.textContent = subtitle;
  }
}

// Call applyWhitelabelTitles() on page load AND after every data change
function ensureWhitelabelLoaded() {
  // Retry every 100ms until DOM elements exist (max 5 attempts)
  let attempts = 0;
  const interval = setInterval(() => {
    const h1 = document.querySelector('#mainTitleDisplay');
    const small = document.querySelector('#subtitleDisplay');
    
    if (h1 && small) {
      applyWhitelabelTitles();
      clearInterval(interval);
    }
    
    attempts++;
    if (attempts > 5) clearInterval(interval);
  }, 100);
}
