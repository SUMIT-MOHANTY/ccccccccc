document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('calculator-form');
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const operationSelect = document.getElementById('operation');
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const errorContainer = document.getElementById('error-container');
    const errorText = document.getElementById('error-text');
    const resetBtn = document.getElementById('reset-btn');

    // Function to show error message
    function showError(message) {
        resultContainer.style.display = 'none';
        errorText.textContent = message;
        errorContainer.style.display = 'block';
    }

    // Function to show result
    function showResult(result) {
        errorContainer.style.display = 'none';
        resultText.textContent = result;
        resultContainer.style.display = 'block';
    }

    // Function to handle calculation
    async function calculate() {
        const num1 = num1Input.value;
        const num2 = num2Input.value;
        const operation = operationSelect.value;

        // Client-side validation
        if (!num1 || !num2 || !operation) {
            showError('Please fill in all fields');
            return;
        }

        if (isNaN(num1) || isNaN(num2)) {
            showError('Please enter valid numbers');
            return;
        }

        // Display operation
        let operationSymbol = '';
        switch(operation) {
            case 'add': operationSymbol = '+'; break;
            case 'subtract': operationSymbol = '-'; break;
            case 'multiply': operationSymbol = ''; break;
            case 'divide': operationSymbol = ''; break;
        }

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: operation,
                    a: parseFloat(num1),
                    b: parseFloat(num2)
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Calculation failed');
            }

            showResult(`${num1} ${operationSymbol} ${num2} = ${data.result}`);
        } catch (error) {
            if (error.name === 'TypeError') {
                showError('Network error: Please check your connection');
            } else {
                showError(error.message || 'An error occurred');
            }
        }
    }

    // Handle form submission
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        await calculate();
    });

    // Handle reset button
    resetBtn.addEventListener('click', function() {
        form.reset();
        resultContainer.style.display = 'none';
        errorContainer.style.display = 'none';
    });

    // Handle form submission without JavaScript (fallback)
    form.addEventListener('submit', function(e) {
        // This is already prevented above, but included for clarity
        e.preventDefault();
    });

    // Enable numeric input validation
    [num1Input, num2Input].forEach(input => {
        input.addEventListener('input', function(e) {
            // Allow negative numbers, decimals, and scientific notation
            const valid = /^-?\d*\.?\d*(?:[eE][+-]?\d+)?$/.test(e.target.value);
            if (!valid && e.target.value !== '-') {
                e.target.value = e.target.value.replace(/[^-?\d\.eE]/g, '');
            }
        });
    });

    // Handle pick validation for operation
    operationSelect.addEventListener('change', function() {
        if (errorContainer.style.display === 'block') {
            errorContainer.style.display = 'none';
        }
    });
});

// Handle browser back/forward navigation
window.addEventListener('pageshow', function(event) {
    if (event.persisted) {
        window.location.reload();
    }
});
