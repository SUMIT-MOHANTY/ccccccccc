/**
 * Frontend calculator logic for flask-calculator
 */

let displayValue = '';

function updateDisplay() {
    document.getElementById('display').value = displayValue || '0';
}

function clearDisplay() {
    displayValue = '';
    updateDisplay();
}

function appendToDisplay(value) {
    displayValue += value;
    updateDisplay();
}

function calculate() {
    if (!displayValue) return;

    // Clear error message
    document.getElementById('error').textContent = '';

    // Parse the expression
    const operatorMatch = displayValue.match(/[+\-*/]/);
    if (!operatorMatch) {
        showError('Invalid expression');
        return;
    }

    const operator = operatorMatch[0];
    const parts = displayValue.split(operator);

    if (parts.length !== 2) {
        showError('Invalid expression');
        return;
    }

    const a = parseFloat(parts[0]);
    const b = parseFloat(parts[1]);

    if (isNaN(a) || isNaN(b)) {
        showError('Invalid numbers');
        return;
    }

    // Send to API
    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({a: a, b: b, op: operator})
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            showError(data.error);
        } else {
            displayValue = data.result.toString();
            updateDisplay();
        }
    })
    .catch(err => {
        showError('Server error');
    });
}

function showError(message) {
    document.getElementById('error').textContent = message;
}
