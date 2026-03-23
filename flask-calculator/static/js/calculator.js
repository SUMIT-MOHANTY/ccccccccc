let currentInput = '';
let currentOperation = '';
let previousInput = '';

function addInput(num) {
    currentInput += num;
    updateDisplay();
}

function setOperation(op) {
    if (currentInput === '') return;
    previousInput = currentInput;
    currentInput = '';
    currentOperation = op;
}

function clearDisplay() {
    currentInput = '';
    previousInput = '';
    currentOperation = '';
    updateDisplay();
}

function updateDisplay() {
    document.getElementById('display').value = currentInput || '0';
}

function calculate() {
    if (currentInput === '' || previousInput === '') return;

    const payload = {
        num1: parseFloat(previousInput),
        num2: parseFloat(currentInput),
        operation: currentOperation
    };

    fetch('/api/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert('Error: ' + data.error);
        } else {
            currentInput = data.result.toString();
            previousInput = '';
            currentOperation = '';
            updateDisplay();
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Calculation failed. Please try again.');
    });
}
