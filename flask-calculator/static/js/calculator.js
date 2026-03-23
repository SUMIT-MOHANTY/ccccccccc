async function calculate() {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = '';

    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);
    const operation = document.getElementById('operation').value;

    if (isNaN(a) || isNaN(b)) {
        errorDiv.textContent = 'Please enter valid numbers';
        return;
    }

    try {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ operation, a, b })
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById('result').value = data.result;
        } else {
            errorDiv.textContent = data.error || 'Calculation failed';
        }
    } catch (error) {
        errorDiv.textContent = 'Network error occurred';
        console.error('Error:', error);
    }
}

// Allow Enter key to calculate
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') calculate();
    });
});
