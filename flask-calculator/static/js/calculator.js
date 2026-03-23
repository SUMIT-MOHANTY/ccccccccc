document.addEventListener('DOMContentLoaded', () => {
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const operationSelect = document.getElementById('operation');
    const calculateBtn = document.getElementById('calculate-btn');
    const resultSpan = document.getElementById('result');
    const errorMessage = document.getElementById('error-message');

    // Clear error when inputs change
    [num1Input, num2Input, operationSelect].forEach(element => {
        element.addEventListener('input', () => {
            errorMessage.textContent = '';
        });
    });

    calculateBtn.addEventListener('click', async () => {
        try {
            // Reset display
            errorMessage.textContent = '';
            resultSpan.textContent = 'Calculating...';

            // Validate inputs
            const num1 = num1Input.value.trim();
            const num2 = num2Input.value.trim();
            const operation = operationSelect.value;

            if (num1 === '' || num2 === '') {
                throw new Error('Please enter both numbers');
            }

            // Check for division by zero client-side
            if (operation === '/' && parseFloat(num2) === 0) {
                throw new Error('Cannot divide by zero');
            }

            // Send calculation request
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    num1: parseFloat(num1),
                    num2: parseFloat(num2),
                    operation: operation
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Calculation failed');
            }

            resultSpan.textContent = data.result;
        } catch (error) {
            resultSpan.textContent = '--';
            errorMessage.textContent = error.message || 'An unexpected error occurred';
            console.error('Calculator error:', error);
        }
    });
});
