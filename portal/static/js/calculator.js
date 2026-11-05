/**
 * TCS iON Authentic GATE Virtual Scientific Calculator
 */

class GateCalculator {
    constructor() {
        this.displayVal = '0';
        this.historyVal = '';
        this.memoryVal = 0;
        this.angleMode = 'deg'; // 'deg' or 'rad'
        this.waitingForOperand = false;
        this.pendingOp = null;
        this.firstOperand = null;
        this.hasMemory = false;

        this.initDOM();
        this.bindEvents();
        this.makeDraggable();
    }

    initDOM() {
        let el = document.getElementById('gate-calculator-modal');
        if (!el) {
            el = document.createElement('div');
            el.id = 'gate-calculator-modal';
            el.className = 'calc-modal';
            el.innerHTML = `
                <div class="calc-header" id="calc-drag-handle">
                    <div class="calc-header-title">
                        <svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-6 2h5v3h-5V5zm-7 0h5v3H6V5zm0 5h5v3H6v-3zm7 0h5v3h-5v-3zm-7 5h5v3H6v-3zm7 0h5v3h-5v-3z"/></svg>
                        <span>GATE 2027 Scientific Calculator</span>
                    </div>
                    <button class="calc-close-btn" id="calc-close-btn" title="Close Calculator">&times;</button>
                </div>
                <div class="calc-body">
                    <div class="calc-display-container">
                        <div class="calc-history-line" id="calc-history-display"></div>
                        <input type="text" class="calc-display" id="calc-main-display" value="0" readonly />
                    </div>
                    <div class="calc-mode-bar">
                        <div class="calc-radio-group">
                            <label><input type="radio" name="calc-angle" value="deg" checked id="calc-mode-deg" /> Deg</label>
                            <label><input type="radio" name="calc-angle" value="rad" id="calc-mode-rad" /> Rad</label>
                        </div>
                        <div class="calc-memory-indicator" id="calc-mem-indicator">M: 0</div>
                    </div>
                    <div class="calc-grid">
                        <!-- Row 1: Memory & Clear -->
                        <button class="calc-btn calc-btn-mem" data-action="mc">MC</button>
                        <button class="calc-btn calc-btn-mem" data-action="mr">MR</button>
                        <button class="calc-btn calc-btn-mem" data-action="ms">MS</button>
                        <button class="calc-btn calc-btn-mem" data-action="mplus">M+</button>
                        <button class="calc-btn calc-btn-mem" data-action="mminus">M-</button>

                        <!-- Row 2: Standard Clear & Math -->
                        <button class="calc-btn calc-btn-action" data-action="clear">C</button>
                        <button class="calc-btn calc-btn-action" data-action="backspace">&larr;</button>
                        <button class="calc-btn calc-btn-op" data-action="mod">mod</button>
                        <button class="calc-btn calc-btn-op" data-action="paren-open">(</button>
                        <button class="calc-btn calc-btn-op" data-action="paren-close">)</button>

                        <!-- Row 3: Trig & Logs -->
                        <button class="calc-btn calc-btn-op" data-action="sin">sin</button>
                        <button class="calc-btn calc-btn-op" data-action="cos">cos</button>
                        <button class="calc-btn calc-btn-op" data-action="tan">tan</button>
                        <button class="calc-btn calc-btn-op" data-action="log">log</button>
                        <button class="calc-btn calc-btn-op" data-action="ln">ln</button>

                        <!-- Row 4: Hyperbolic & Powers -->
                        <button class="calc-btn calc-btn-op" data-action="sinh">sinh</button>
                        <button class="calc-btn calc-btn-op" data-action="cosh">cosh</button>
                        <button class="calc-btn calc-btn-op" data-action="tanh">tanh</button>
                        <button class="calc-btn calc-btn-op" data-action="exp">e<sup>x</sup></button>
                        <button class="calc-btn calc-btn-op" data-action="ten-power">10<sup>x</sup></button>

                        <!-- Row 5: Powers & Roots -->
                        <button class="calc-btn calc-btn-op" data-action="sqr">x<sup>2</sup></button>
                        <button class="calc-btn calc-btn-op" data-action="cube">x<sup>3</sup></button>
                        <button class="calc-btn calc-btn-op" data-action="pow">x<sup>y</sup></button>
                        <button class="calc-btn calc-btn-op" data-action="sqrt">&radic;x</button>
                        <button class="calc-btn calc-btn-op" data-action="cbrt">&#8731;x</button>

                        <!-- Row 6: Misc -->
                        <button class="calc-btn calc-btn-op" data-action="inv">1/x</button>
                        <button class="calc-btn calc-btn-op" data-action="fact">n!</button>
                        <button class="calc-btn calc-btn-op" data-action="abs">|x|</button>
                        <button class="calc-btn calc-btn-op" data-action="pi">&pi;</button>
                        <button class="calc-btn calc-btn-op" data-action="e">e</button>

                        <!-- Row 7: Digits 7 8 9 / * -->
                        <button class="calc-btn calc-btn-num" data-num="7">7</button>
                        <button class="calc-btn calc-btn-num" data-num="8">8</button>
                        <button class="calc-btn calc-btn-num" data-num="9">9</button>
                        <button class="calc-btn calc-btn-op" data-op="/">&divide;</button>
                        <button class="calc-btn calc-btn-op" data-op="*">&times;</button>

                        <!-- Row 8: Digits 4 5 6 - + -->
                        <button class="calc-btn calc-btn-num" data-num="4">4</button>
                        <button class="calc-btn calc-btn-num" data-num="5">5</button>
                        <button class="calc-btn calc-btn-num" data-num="6">6</button>
                        <button class="calc-btn calc-btn-op" data-op="-">&minus;</button>
                        <button class="calc-btn calc-btn-op" data-op="+">+</button>

                        <!-- Row 9: Digits 1 2 3 . = -->
                        <button class="calc-btn calc-btn-num" data-num="1">1</button>
                        <button class="calc-btn calc-btn-num" data-num="2">2</button>
                        <button class="calc-btn calc-btn-num" data-num="3">3</button>
                        <button class="calc-btn calc-btn-num" data-action="dot">.</button>
                        <button class="calc-btn calc-btn-op" data-action="sign">&plusmn;</button>

                        <!-- Row 10: 0 and = span -->
                        <button class="calc-btn calc-btn-num" data-num="0" style="grid-column: span 2;">0</button>
                        <button class="calc-btn calc-btn-equal" data-action="equals" style="grid-column: span 3;">=</button>
                    </div>
                </div>
            `;
            document.body.appendChild(el);
        }
        this.modal = el;
        this.mainDisplay = document.getElementById('calc-main-display');
        this.historyDisplay = document.getElementById('calc-history-display');
        this.memIndicator = document.getElementById('calc-mem-indicator');
    }

    bindEvents() {
        document.getElementById('calc-close-btn').addEventListener('click', () => this.hide());

        document.getElementById('calc-mode-deg').addEventListener('change', () => { this.angleMode = 'deg'; });
        document.getElementById('calc-mode-rad').addEventListener('change', () => { this.angleMode = 'rad'; });

        this.modal.addEventListener('click', (e) => {
            const btn = e.target.closest('button');
            if (!btn) return;

            if (btn.dataset.num !== undefined) {
                this.inputDigit(btn.dataset.num);
            } else if (btn.dataset.op !== undefined) {
                this.handleBinaryOp(btn.dataset.op);
            } else if (btn.dataset.action !== undefined) {
                this.handleAction(btn.dataset.action);
            }
        });
    }

    show() {
        this.modal.classList.add('active');
    }

    hide() {
        this.modal.classList.remove('active');
    }

    toggle() {
        if (this.modal.classList.contains('active')) {
            this.hide();
        } else {
            this.show();
        }
    }

    updateDisplay() {
        this.mainDisplay.value = this.displayVal;
        this.historyDisplay.innerText = this.historyVal;
        this.memIndicator.innerText = this.hasMemory ? `M: ${this.memoryVal}` : 'M: 0';
    }

    inputDigit(digit) {
        if (this.waitingForOperand) {
            this.displayVal = String(digit);
            this.waitingForOperand = false;
        } else {
            this.displayVal = this.displayVal === '0' ? String(digit) : this.displayVal + digit;
        }
        this.updateDisplay();
    }

    inputDot() {
        if (this.waitingForOperand) {
            this.displayVal = '0.';
            this.waitingForOperand = false;
            this.updateDisplay();
            return;
        }
        if (!this.displayVal.includes('.')) {
            this.displayVal += '.';
            this.updateDisplay();
        }
    }

    handleBinaryOp(nextOp) {
        const inputValue = parseFloat(this.displayVal);

        if (this.firstOperand === null) {
            this.firstOperand = inputValue;
            this.historyVal = `${inputValue} ${nextOp}`;
        } else if (this.pendingOp) {
            const result = this.calculate(this.firstOperand, inputValue, this.pendingOp);
            this.displayVal = `${parseFloat(result.toFixed(10))}`;
            this.firstOperand = result;
            this.historyVal = `${this.displayVal} ${nextOp}`;
        }

        this.waitingForOperand = true;
        this.pendingOp = nextOp;
        this.updateDisplay();
    }

    calculate(first, second, op) {
        switch (op) {
            case '+': return first + second;
            case '-': return first - second;
            case '*': return first * second;
            case '/': return second === 0 ? 0 : first / second;
            case 'mod': return first % second;
            case 'pow': return Math.pow(first, second);
            default: return second;
        }
    }

    handleAction(action) {
        let val = parseFloat(this.displayVal);

        switch (action) {
            case 'clear':
                this.displayVal = '0';
                this.historyVal = '';
                this.firstOperand = null;
                this.pendingOp = null;
                this.waitingForOperand = false;
                break;

            case 'backspace':
                if (this.displayVal.length > 1) {
                    this.displayVal = this.displayVal.slice(0, -1);
                } else {
                    this.displayVal = '0';
                }
                break;

            case 'dot':
                this.inputDot();
                return;

            case 'sign':
                this.displayVal = String(-parseFloat(this.displayVal));
                break;

            case 'equals':
                if (this.pendingOp && this.firstOperand !== null) {
                    const result = this.calculate(this.firstOperand, val, this.pendingOp);
                    this.historyVal = `${this.firstOperand} ${this.pendingOp} ${val} =`;
                    this.displayVal = `${parseFloat(result.toFixed(10))}`;
                    this.firstOperand = null;
                    this.pendingOp = null;
                    this.waitingForOperand = true;
                }
                break;

            // Scientific functions
            case 'sin':
                val = this.angleMode === 'deg' ? (val * Math.PI / 180) : val;
                this.displayVal = String(parseFloat(Math.sin(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'cos':
                val = this.angleMode === 'deg' ? (val * Math.PI / 180) : val;
                this.displayVal = String(parseFloat(Math.cos(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'tan':
                val = this.angleMode === 'deg' ? (val * Math.PI / 180) : val;
                this.displayVal = String(parseFloat(Math.tan(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'sinh':
                this.displayVal = String(parseFloat(Math.sinh(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'cosh':
                this.displayVal = String(parseFloat(Math.cosh(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'tanh':
                this.displayVal = String(parseFloat(Math.tanh(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'log': // base 10
                this.displayVal = val > 0 ? String(parseFloat(Math.log10(val).toFixed(10))) : 'Error';
                this.waitingForOperand = true;
                break;

            case 'ln': // natural log
                this.displayVal = val > 0 ? String(parseFloat(Math.log(val).toFixed(10))) : 'Error';
                this.waitingForOperand = true;
                break;

            case 'exp':
                this.displayVal = String(parseFloat(Math.exp(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'ten-power':
                this.displayVal = String(parseFloat(Math.pow(10, val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'sqr':
                this.displayVal = String(parseFloat((val * val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'cube':
                this.displayVal = String(parseFloat((val * val * val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'pow':
                this.handleBinaryOp('pow');
                return;

            case 'sqrt':
                this.displayVal = val >= 0 ? String(parseFloat(Math.sqrt(val).toFixed(10))) : 'Error';
                this.waitingForOperand = true;
                break;

            case 'cbrt':
                this.displayVal = String(parseFloat(Math.cbrt(val).toFixed(10)));
                this.waitingForOperand = true;
                break;

            case 'inv':
                this.displayVal = val !== 0 ? String(parseFloat((1 / val).toFixed(10))) : 'Error';
                this.waitingForOperand = true;
                break;

            case 'fact':
                let n = Math.floor(val);
                if (n < 0 || n > 170) {
                    this.displayVal = 'Error';
                } else {
                    let f = 1;
                    for (let i = 2; i <= n; i++) f *= i;
                    this.displayVal = String(f);
                }
                this.waitingForOperand = true;
                break;

            case 'abs':
                this.displayVal = String(Math.abs(val));
                this.waitingForOperand = true;
                break;

            case 'pi':
                this.displayVal = String(Math.PI);
                this.waitingForOperand = true;
                break;

            case 'e':
                this.displayVal = String(Math.E);
                this.waitingForOperand = true;
                break;

            // Memory
            case 'mc':
                this.memoryVal = 0;
                this.hasMemory = false;
                break;
            case 'mr':
                this.displayVal = String(this.memoryVal);
                this.waitingForOperand = true;
                break;
            case 'ms':
                this.memoryVal = val;
                this.hasMemory = true;
                break;
            case 'mplus':
                this.memoryVal += val;
                this.hasMemory = true;
                break;
            case 'mminus':
                this.memoryVal -= val;
                this.hasMemory = true;
                break;
        }

        this.updateDisplay();
    }

    makeDraggable() {
        const header = document.getElementById('calc-drag-handle');
        const modal = this.modal;
        let isDragging = false;
        let startX, startY, initialX, initialY;

        header.addEventListener('mousedown', (e) => {
            isDragging = true;
            startX = e.clientX;
            startY = e.clientY;
            const rect = modal.getBoundingClientRect();
            initialX = rect.left;
            initialY = rect.top;

            document.addEventListener('mousemove', onMouseMove);
            document.addEventListener('mouseup', onMouseUp);
        });

        function onMouseMove(e) {
            if (!isDragging) return;
            const dx = e.clientX - startX;
            const dy = e.clientY - startY;
            modal.style.left = `${initialX + dx}px`;
            modal.style.top = `${initialY + dy}px`;
            modal.style.right = 'auto';
        }

        function onMouseUp() {
            isDragging = false;
            document.removeEventListener('mousemove', onMouseMove);
            document.removeEventListener('mouseup', onMouseUp);
        }
    }
}

// Global instance
window.gateCalculator = null;
document.addEventListener('DOMContentLoaded', () => {
    window.gateCalculator = new GateCalculator();
});

