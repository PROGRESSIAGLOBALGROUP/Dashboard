/* ========================================
   WEIGHT FACTOR TOOLTIP - WORLD CLASS JS
   ======================================== */

(function initWeightFactorTooltip() {
  // Configuration
  const CONFIG = {
    TOOLTIP_ID: 'factor27-tooltip',
    TRIGGER_SELECTOR: '[data-tooltip-id="factor27-tooltip"]',
    ANIMATION_DURATION: 300,
    ESCAPE_KEY: 'Escape',
  };

  // State
  let isTooltipOpen = false;
  let tooltipElement = null;
  let triggerElement = null;

  /**
   * Initialize tooltip system
   */
  function init() {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', setupTooltip);
    } else {
      setupTooltip();
    }
  }

  /**
   * Setup tooltip and event listeners
   */
  function setupTooltip() {
    tooltipElement = document.getElementById(CONFIG.TOOLTIP_ID);
    triggerElement = document.querySelector(CONFIG.TRIGGER_SELECTOR);

    if (!tooltipElement || !triggerElement) {
      console.warn('⚠️ Weight Factor Tooltip elements not found');
      return;
    }

    // Event listeners for trigger
    triggerElement.addEventListener('click', handleTriggerClick);
    triggerElement.addEventListener('keydown', handleTriggerKeydown);

    // Event listeners for tooltip
    const closeButton = tooltipElement.querySelector('.tooltip-close');
    const backdrop = tooltipElement.querySelector('.tooltip-backdrop');

    if (closeButton) {
      closeButton.addEventListener('click', closeTooltip);
    }

    if (backdrop) {
      backdrop.addEventListener('click', closeTooltip);
    }

    // Global escape key
    document.addEventListener('keydown', handleEscapeKey);

    // Prevent body scroll when tooltip is open
    tooltipElement.addEventListener('wheel', handleTooltipWheel, { passive: false });

    console.log('✅ Weight Factor Tooltip initialized');
  }

  /**
   * Handle trigger click
   */
  function handleTriggerClick(event) {
    event.preventDefault();
    event.stopPropagation();
    
    if (isTooltipOpen) {
      closeTooltip();
    } else {
      openTooltip();
    }
  }

  /**
   * Handle trigger keyboard (Enter/Space)
   */
  function handleTriggerKeydown(event) {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      handleTriggerClick(event);
    }
  }

  /**
   * Handle escape key
   */
  function handleEscapeKey(event) {
    if (event.key === CONFIG.ESCAPE_KEY && isTooltipOpen) {
      closeTooltip();
    }
  }

  /**
   * Prevent wheel scroll from propagating when tooltip is open
   */
  function handleTooltipWheel(event) {
    if (isTooltipOpen) {
      event.stopPropagation();
    }
  }

  /**
   * Open tooltip with animation
   */
  function openTooltip() {
    if (isTooltipOpen) return;

    isTooltipOpen = true;

    // Set aria attributes
    tooltipElement.setAttribute('aria-hidden', 'false');
    triggerElement.setAttribute('aria-expanded', 'true');

    // Trigger animation
    tooltipElement.offsetHeight; // Force reflow

    // Add animation class
    tooltipElement.style.opacity = '1';
    tooltipElement.style.pointerEvents = 'auto';

    // Focus management
    const closeButton = tooltipElement.querySelector('.tooltip-close');
    if (closeButton) {
      setTimeout(() => closeButton.focus(), 50);
    }

    // Prevent body scroll
    document.body.style.overflow = 'hidden';

    // Analytics (optional)
    logEvent('tooltip_opened', {
      tooltip_id: CONFIG.TOOLTIP_ID,
      timestamp: new Date().toISOString(),
    });

    console.log('🔓 Tooltip opened');
  }

  /**
   * Close tooltip with animation
   */
  function closeTooltip() {
    if (!isTooltipOpen) return;

    isTooltipOpen = false;

    // Set aria attributes
    tooltipElement.setAttribute('aria-hidden', 'true');
    triggerElement.setAttribute('aria-expanded', 'false');

    // Remove animation
    tooltipElement.style.opacity = '0';
    tooltipElement.style.pointerEvents = 'none';

    // Restore body scroll
    document.body.style.overflow = '';

    // Return focus to trigger
    triggerElement.focus();

    // Analytics (optional)
    logEvent('tooltip_closed', {
      tooltip_id: CONFIG.TOOLTIP_ID,
      timestamp: new Date().toISOString(),
    });

    console.log('🔐 Tooltip closed');
  }

  /**
   * Optional: Log events (integrate with your analytics)
   */
  function logEvent(eventName, eventData) {
    // Replace with your analytics implementation
    if (window.Dashboard && window.Dashboard.Analytics) {
      window.Dashboard.Analytics.track(eventName, eventData);
    }
  }

  /**
   * Expose public API
   */
  window.WeightFactorTooltip = {
    open: openTooltip,
    close: closeTooltip,
    toggle: () => isTooltipOpen ? closeTooltip() : openTooltip(),
    isOpen: () => isTooltipOpen,
  };

  // Initialize on script load
  init();
})();
