/**
 * Frontend logic for arithmetic expression calculator
 * Handles form submission, AJAX requests, and result display
 */

// Wait for DOM to be loaded
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculator-form');
    const input = document.getElementById('expression-input');
    const resultDisplay = document.getElementById('result-display');
    const loadingIndicator = document.getElementById('loading-indicator');

    /**
     * Sends expression to backend for calculation
     * @param {string} expression - The arithmetic expression to calculate
     */
    async function calculateExpression(expression) {
        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expression: expression.trim() })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error:', error);
            return { error: 'Failed to connect to server' };
        }
    }

    /**
     * Displays the result or error message
     * @param {Object} data - Response data from server
     * @param {number|string} [data.result] - The calculation result
     * @param {string} [data.error] - Error message if calculation failed
     */
    function displayResult(data) {
        resultDisplay.textContent = '';
        resultDisplay.className = '';

        if (data.error) {
            resultDisplay.textContent = data.error;
            resultDisplay.classList.add('error');
        } else {
            resultDisplay.textContent = `Result: ${data.result}`;
            resultDisplay.classList.add('success');
        }
    }

    /**
     * Shows or hides the loading indicator
     * @param {boolean} show - Whether to show the loading indicator
     */
    function setLoading(show) {
        if (show) {
            loadingIndicator.style.display = 'block';
            resultDisplay.style.display = 'none';
        } else {
            loadingIndicator.style.display = 'none';
            resultDisplay.style.display = 'block';
        }
    }

    /**
     * Validates input before submission
     * @param {string} value - The input value to validate
     * @returns {boolean} - Whether the input is valid
     */
    function validateInput(value) {
        if (!value || value.trim().length === 0) {
            displayResult({ error: 'Please enter an expression' });
            return false;
        }
        return true;
    }

    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const expression = input.value;

        // Clear previous results
        resultDisplay.textContent = '';
        resultDisplay.className = '';

        // Validate input
        if (!validateInput(expression)) {
            return;
        }

        // Clear focus from input
        input.blur();

        // Show loading state
        setLoading(true);

        // Send to backend
        const result = await calculateExpression(expression);

        // Hide loading state
        setLoading(false);

        // Display result
        displayResult(result);
    });

    // Allow Enter key submission
    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            form.dispatchEvent(new Event('submit'));
        }
    });

    // Focus input on page load
    input.focus();
});
