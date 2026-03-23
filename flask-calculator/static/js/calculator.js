class Calculator {
    constructor() {
        this.form = document.getElementById('calculator-form');
        this.expressionInput = document.getElementById('expression');
        this.resultDiv = document.getElementById('result');
        this.errorDiv = document.getElementById('error');
        this.loadingDiv = document.getElementById('loading');
        this.clearBtn = document.getElementById('clear-btn');

        this.bindEvents();
    }

    bindEvents() {
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.clearBtn.addEventListener('click', () => this.clear());
        this.expressionInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                this.handleSubmit(e);
            }
        });
    }

    async handleSubmit(e) {
        e.preventDefault();

        const expression = this.expressionInput.value.trim();
        if (!expression) {
            this.showError('Please enter an expression');
            return;
        }

        this.showLoading(true);
        this.hideResult();
        this.hideError();

        try {
            const response = await fetch('/api/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expression })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                this.showResult(data.result);
            } else {
                this.showError(data.error || 'Calculation failed');
            }
        } catch (error) {
            console.error('Error:', error);
            this.showError('Network error. Please check connection.');
        } finally {
            this.showLoading(false);
        }
    }

    showResult(result) {
        this.resultDiv.textContent = `Result: ${result}`;
        this.resultDiv.classList.remove('hidden');
    }

    showError(message) {
        this.errorDiv.textContent = message;
        this.errorDiv.classList.remove('hidden');
    }

    hideResult() {
        this.resultDiv.classList.add('hidden');
        this.resultDiv.textContent = '';
    }

    hideError() {
        this.errorDiv.classList.add('hidden');
        this.errorDiv.textContent = '';
    }

    showLoading(show) {
        if (show) {
            this.loadingDiv.classList.remove('hidden');
        } else {
            this.loadingDiv.classList.add('hidden');
        }
    }

    clear() {
        this.expressionInput.value = '';
        this.hideResult();
        this.hideError();
        this.expressionInput.focus();
    }
}

// Initialize when DOM loads
document.addEventListener('DOMContentLoaded', () => {
    new Calculator();
});
