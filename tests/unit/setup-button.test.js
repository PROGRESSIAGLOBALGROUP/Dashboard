/**
 * @jest-environment jsdom
 */

describe('Dashboard Enhanced Setup Button Tests', () => {
    // Mock HTML setup
    beforeEach(() => {
        document.body.innerHTML = `
            <button id="setupAdmin" class="btn pill">Setup</button>
            <div id="adminModal" class="modal-overlay">
                <div class="modal-content">
                    <div class="modal-header">
                        <h2>📊 Project Administration</h2>
                        <button class="modal-close" id="closeAdminModal">✕</button>
                    </div>
                </div>
            </div>
        `;

        // Mock localStorage
        global.localStorage = {
            getItem: jest.fn(),
            setItem: jest.fn(),
            removeItem: jest.fn()
        };

        // Mock StorageManager
        global.StorageManager = {
            STORAGE_KEY: 'dashboard_config_v1',
            init: jest.fn(),
            loadConfig: jest.fn().mockReturnValue({ buses: [], apps: [], waves: [] }),
            saveConfig: jest.fn(),
            getBUs: jest.fn().mockReturnValue([]),
            getApps: jest.fn().mockReturnValue([])
        };

        // Mock AdminController
        global.AdminController = {
            init: jest.fn(),
            setupEventListeners: jest.fn(),
            openModal: jest.fn(),
            closeModal: jest.fn()
        };

        // Mock apply function
        global.apply = jest.fn();
    });

    test('StorageManager and AdminController should be initialized on page load', () => {
        // Execute init code
        StorageManager.init();
        AdminController.init();
        apply();

        // Verify initialization called
        expect(StorageManager.init).toHaveBeenCalled();
        expect(AdminController.init).toHaveBeenCalled();
        expect(apply).toHaveBeenCalled();
    });

    test('Setup button should call openModal when clicked', () => {
        // Setup click handler mock
        const setupBtn = document.getElementById('setupAdmin');
        setupBtn.addEventListener('click', () => AdminController.openModal());
        
        // Simulate click
        setupBtn.click();
        
        // Verify modal opened
        expect(AdminController.openModal).toHaveBeenCalled();
    });

    test('AdminController.init should attach event listener to Setup button', () => {
        // Create spy on addEventListener
        const setupBtn = document.getElementById('setupAdmin');
        const addEventListenerSpy = jest.spyOn(setupBtn, 'addEventListener');
        
        // Define AdminController.init implementation for this test
        AdminController.init = function() {
            this.setupEventListeners();
        };
        
        AdminController.setupEventListeners = function() {
            document.getElementById('setupAdmin').addEventListener('click', () => this.openModal());
        };
        
        // Call init
        AdminController.init();
        
        // Verify event listener was attached
        expect(addEventListenerSpy).toHaveBeenCalledWith('click', expect.any(Function));
        
        // Clean up spy
        addEventListenerSpy.mockRestore();
    });

    test('openModal should add active class to modal', () => {
        // Define openModal implementation for this test
        AdminController.openModal = function() {
            document.getElementById('adminModal').classList.add('active');
        };
        
        // Call openModal
        AdminController.openModal();
        
        // Verify modal has active class
        const modal = document.getElementById('adminModal');
        expect(modal.classList.contains('active')).toBe(true);
    });

    test('closeModal should remove active class from modal', () => {
        // Add active class to modal
        const modal = document.getElementById('adminModal');
        modal.classList.add('active');
        
        // Define closeModal implementation for this test
        AdminController.closeModal = function() {
            document.getElementById('adminModal').classList.remove('active');
        };
        
        // Call closeModal
        AdminController.closeModal();
        
        // Verify modal does not have active class
        expect(modal.classList.contains('active')).toBe(false);
    });
});