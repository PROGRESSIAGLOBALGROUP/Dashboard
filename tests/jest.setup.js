// Jest setup file
import '@testing-library/jest-dom';

// Mock global functions
global.requestAnimationFrame = callback => setTimeout(callback, 0);

// Mock console methods to reduce noise during tests
global.console = {
  ...console,
  // Uncomment to disable specific console methods during tests
  // log: jest.fn(),
  // error: jest.fn(),
  // warn: jest.fn(),
};

// Add custom matchers if needed
expect.extend({
  // Example custom matcher
  toBeInRange(received, floor, ceiling) {
    const pass = received >= floor && received <= ceiling;
    if (pass) {
      return {
        message: () => `expected ${received} not to be within range ${floor} - ${ceiling}`,
        pass: true,
      };
    } else {
      return {
        message: () => `expected ${received} to be within range ${floor} - ${ceiling}`,
        pass: false,
      };
    }
  },
});