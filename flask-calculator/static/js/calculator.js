class Calculator {
  constructor() {
    this.form        = document.getElementById('calculator-form');
    this.expression  = document.getElementById('expression') || document.getElementById('expression-input');
    this.display     = document.getElementById('display');
    this.resultDiv   = document.getElementById('result') || document.getElementById('result-display');
    this.errorDiv    = document.getElementById('error');
    this.loadingDiv  = document.getElementById('loading') || document.getElementById('loading-indicator');
    this.clearBtn    = document.getElementById('clear-btn');

    if (this.display) this.bindOldUI();
    else              this.bindNewUI();

    if (this.clearBtn) this.clearBtn.addEventListener('click', () => this.clear());
  }

  bindOldUI() {
    this.btnAppend = (v) => { this.display.value += v; };
    window.appendToDisplay = (v) => { this.display.value += v; };
    window.clearDisplay    = () => { this.display.value = ''; };
    window.calculate       = () => this.handleLegacySubmit();
  }

  bindNewUI() {
    this.form?.addEventListener('submit', (e) => this.handleSubmit(e));
    this.expression?.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') this.handleSubmit(e);
    });
  }

  async handleLegacySubmit() {
    const expression = this.display.value.trim();
    if (!expression) return;

    this.hideError();
    this.showLoading(true);

    try {
      const data = await this.calculateExpression(expression);
      this.display.value = data.result !== undefined ? data.result : '';
      if (data.error) this.showError(data.error);
    } catch (error) {
      this.showError('Network error.');
    } finally {
      this.showLoading(false);
    }
  }

  async handleSubmit(e) {
    e?.preventDefault();
    const expression = this.expression?.value.trim() || this.display?.value.trim();
    if (!expression) {
      this.showError('Please enter an expression');
      return;
    }

    this.showLoading(true);
    this.hideError();
    this.hideResult();

    try {
      const data = await this.calculateExpression(expression);
      if (data.result !== undefined) this.showResult(data.result);
      else this.showError(data.error || 'Calculation failed');
    } catch (error) {
      this.showError('Network error.');
    } finally {
      this.showLoading(false);
    }
  }

  async calculateExpression(expr) {
    const response = await fetch('/api/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ expression: expr })
    });

    if (!response.ok) throw new Error('Bad response');

    return response.json();
  }

  showResult(result) {
    if (this.resultDiv) {
      this.resultDiv.textContent = `Result: ${result}`;
      this.resultDiv.classList.remove('hidden');
    }
  }

  showError(message) {
    if (this.errorDiv) {
      this.errorDiv.textContent = message;
      this.errorDiv.classList.remove('hidden');
    }
  }

  hideResult()   { this.resultDiv?.classList?.add?.('hidden'); }
  hideError()    { this.errorDiv?.classList?.add?.('hidden'); }

  showLoading(show = true) {
    if (!this.loadingDiv) return;
    this.loadingDiv.classList.toggle('hidden', !show);
  }

  clear() {
    if (this.expression) this.expression.value = '';
    if (this.display)    this.display.value = '';
    this.hideResult();
    this.hideError();
    this.expression?.focus();
  }
}

document.addEventListener('DOMContentLoaded', () => new Calculator());
