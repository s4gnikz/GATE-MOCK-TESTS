/**
 * Authentic GATE 2027 Examination Simulator Engine
 */

class GateExamSimulator {
    constructor() {
        this.paperNum = this.getPaperNumberFromUrl();
        this.questions = [];
        this.paperSummary = null;
        this.currentIndex = 0; // 0..64
        this.activeSection = 1; // 1: GA (1-10), 2: CS & Math (11-65)

        // Palette Status enum:
        // 0: Not Visited, 1: Not Answered, 2: Answered, 3: Marked for Review, 4: Answered & Marked for Review
        this.qStates = new Array(65).fill(0);
        this.responses = {}; // { questionNumber: responseValue }

        this.totalDurationSeconds = 180 * 60; // 10,800 seconds (3 hours)
        this.timeLeft = this.totalDurationSeconds;
        this.timerInterval = null;
        this.examStarted = false;

        this.initDOM();
    }

    getPaperNumberFromUrl() {
        const params = new URLSearchParams(window.location.search);
        const p = parseInt(params.get('paper'), 10);
        return (!isNaN(p) && p >= 1 && p <= 100) ? p : 1;
    }

    async initDOM() {
        // Load candidate profile
        this.profile = GateStorage.getProfile();
        this.updateProfileUI();

        // Fetch paper questions from backend
        try {
            const resp = await fetch(`/api/paper/${this.paperNum}`);
            const data = await resp.json();
            if (data.status !== 'success') {
                GateNotify.show(data.message || 'Failed to load paper', 'error');
                return;
            }
            this.questions = data.questions;
            this.paperSummary = data.summary;
            this.setupPreExamView();
        } catch (e) {
            console.error(e);
            GateNotify.show('Network error loading mock test', 'error');
        }
    }

    updateProfileUI() {
        const candName = this.profile.name || 'Candidate Name';
        const candRoll = this.profile.rollNumber || `GATE2027-CS-M${String(this.paperNum).padStart(3, '0')}`;
        const initials = candName.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase() || 'CS';

        document.querySelectorAll('.cand-name-text').forEach(el => el.innerText = candName);
        document.querySelectorAll('.cand-roll-text').forEach(el => el.innerText = candRoll);
        document.querySelectorAll('.cand-avatar-small, .pre-exam-avatar').forEach(el => el.innerText = initials);
    }

    setupPreExamView() {
        document.getElementById('pre-exam-title').innerText = `GATE CS 2027 — Mock Test ${String(this.paperNum).padStart(3, '0')}`;
        document.getElementById('pre-exam-roll').innerText = this.profile.rollNumber;
        document.getElementById('pre-exam-system').innerText = this.profile.systemId || 'C001';

        const termsCheckbox = document.getElementById('pre-exam-terms');
        const beginBtn = document.getElementById('btn-begin-exam');

        termsCheckbox.addEventListener('change', () => {
            beginBtn.disabled = !termsCheckbox.checked;
        });

        // Check if there is existing progress for this mock
        const saved = GateStorage.getProgress(this.paperNum);
        if (saved && saved.responses) {
            beginBtn.innerText = 'Resume Mock Examination';
            beginBtn.disabled = false;
            termsCheckbox.checked = true;
        }

        beginBtn.addEventListener('click', () => {
            this.startExam(saved);
        });
    }

    startExam(savedProgress = null) {
        document.getElementById('pre-exam-screen').style.display = 'none';
        document.getElementById('exam-live-app').style.display = 'flex';

        this.examStarted = true;

        if (savedProgress) {
            this.responses = savedProgress.responses || {};
            this.qStates = savedProgress.qStates || new Array(65).fill(0);
            this.timeLeft = savedProgress.timeLeft !== undefined ? savedProgress.timeLeft : this.totalDurationSeconds;
            this.currentIndex = savedProgress.currentIndex || 0;
            GateNotify.show('Exam resumed from last saved state.', 'info');
        } else {
            // Fresh attempt: set Q1 as Not Answered (1)
            this.qStates[0] = 1;
            this.currentIndex = 0;
        }

        this.bindExamControls();
        this.renderPaletteGrid();
        this.showQuestion(this.currentIndex);
        this.startTimer();
    }

    bindExamControls() {
        // Section switching
        document.getElementById('tab-section-ga').addEventListener('click', () => this.switchSection(1));
        document.getElementById('tab-section-cs').addEventListener('click', () => this.switchSection(2));

        // Action Buttons
        document.getElementById('btn-save-next').addEventListener('click', () => this.handleSaveNext());
        document.getElementById('btn-mark-review-next').addEventListener('click', () => this.handleMarkReviewNext());
        document.getElementById('btn-clear-response').addEventListener('click', () => this.handleClearResponse());
        document.getElementById('btn-prev').addEventListener('click', () => this.handlePrev());
        document.getElementById('btn-submit-exam').addEventListener('click', () => this.openSubmitSummaryModal());

        // Header tool buttons
        document.getElementById('btn-tool-calc').addEventListener('click', () => {
            if (window.gateCalculator) window.gateCalculator.toggle();
        });
        document.getElementById('btn-tool-instructions').addEventListener('click', () => {
            this.openInstructionsModal();
        });
        document.getElementById('btn-tool-question-paper').addEventListener('click', () => {
            this.openQuestionPaperModal();
        });

        // Modal close buttons
        document.querySelectorAll('.btn-close-modal').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const modal = e.target.closest('.gate-modal-backdrop');
                if (modal) modal.classList.remove('active');
            });
        });

        document.getElementById('btn-confirm-submit-test').addEventListener('click', () => {
            this.submitExam();
        });

        // Auto-save every 5 seconds
        setInterval(() => {
            if (this.examStarted) {
                this.saveCurrentProgress();
            }
        }, 5000);

        // Warn before tab close
        window.addEventListener('beforeunload', (e) => {
            if (this.examStarted && this.timeLeft > 0) {
                this.saveCurrentProgress();
                e.preventDefault();
                e.returnValue = '';
            }
        });
    }

    startTimer() {
        const timerDisplay = document.getElementById('exam-timer-display');
        const updateTimer = () => {
            if (this.timeLeft <= 0) {
                clearInterval(this.timerInterval);
                timerDisplay.innerText = '00:00:00';
                GateNotify.show('Time is up! Submitting your exam...', 'warning');
                setTimeout(() => this.submitExam(), 1500);
                return;
            }

            timerDisplay.innerText = GateFormatter.formatTime(this.timeLeft);

            if (this.timeLeft <= 300) { // 5 mins left
                timerDisplay.parentElement.classList.add('timer-danger');
            } else if (this.timeLeft <= 900) { // 15 mins left
                timerDisplay.parentElement.classList.add('timer-warning');
            }

            this.timeLeft--;
        };

        updateTimer();
        this.timerInterval = setInterval(updateTimer, 1000);
    }

    switchSection(sectionId) {
        this.activeSection = sectionId;
        document.getElementById('tab-section-ga').classList.toggle('active', sectionId === 1);
        document.getElementById('tab-section-cs').classList.toggle('active', sectionId === 2);

        // If current question is not in this section, jump to first question of section
        const isGA = this.currentIndex < 10;
        if (sectionId === 1 && !isGA) {
            this.navigateToQuestion(0);
        } else if (sectionId === 2 && isGA) {
            this.navigateToQuestion(10);
        }
    }

    showQuestion(index) {
        if (index < 0 || index >= this.questions.length) return;
        this.currentIndex = index;
        const q = this.questions[index];
        const qNum = index + 1;

        // Auto-sync section tab
        const sec = qNum <= 10 ? 1 : 2;
        if (sec !== this.activeSection) {
            this.activeSection = sec;
            document.getElementById('tab-section-ga').classList.toggle('active', sec === 1);
            document.getElementById('tab-section-cs').classList.toggle('active', sec === 2);
        }

        // Set state to Not Answered if it was Not Visited
        if (this.qStates[index] === 0) {
            this.qStates[index] = 1;
        }

        // Question header
        document.getElementById('q-number-title').innerText = `Question No. ${qNum}`;
        document.getElementById('q-type-badge').innerText = q.type;
        document.getElementById('q-subject-badge').innerText = `${q.subject} — ${q.subtopic || ''}`;

        // Marks scheme
        const posMarks = q.marks;
        let negMarks = 0;
        if (q.type === 'MCQ') {
            negMarks = posMarks === 1 ? '0.33' : '0.67';
        }
        document.getElementById('q-marks-info').innerHTML = `Marks: <strong>+${posMarks}</strong> | Negative Marks: <span class="neg-mark">-${negMarks}</span>`;

        // Render question stem
        const stemContainer = document.getElementById('q-stem-content');
        stemContainer.innerHTML = GateFormatter.render(q.stem);

        // Render input/options based on type
        const answerContainer = document.getElementById('q-options-container');
        answerContainer.innerHTML = '';

        const currentAns = this.responses[qNum];

        if (q.type === 'MCQ') {
            const letters = ['A', 'B', 'C', 'D'];
            const opts = q.options || [];
            let html = '<div class="options-container">';
            opts.forEach((optText, optIdx) => {
                const letter = letters[optIdx];
                const isSelected = currentAns === letter;
                html += `
                    <div class="option-card ${isSelected ? 'selected' : ''}" data-letter="${letter}">
                        <div class="option-letter-badge">${letter}</div>
                        <div class="option-text">${GateFormatter.render(optText)}</div>
                    </div>
                `;
            });
            html += '</div>';
            answerContainer.innerHTML = html;

            answerContainer.querySelectorAll('.option-card').forEach(card => {
                card.addEventListener('click', () => {
                    const letter = card.dataset.letter;
                    this.responses[qNum] = letter;
                    answerContainer.querySelectorAll('.option-card').forEach(c => c.classList.remove('selected'));
                    card.classList.add('selected');
                });
            });

        } else if (q.type === 'MSQ') {
            const letters = ['A', 'B', 'C', 'D'];
            const opts = q.options || [];
            let selectedLetters = Array.isArray(currentAns) ? [...currentAns] : [];
            let html = '<div class="options-container">';
            opts.forEach((optText, optIdx) => {
                const letter = letters[optIdx];
                const isSelected = selectedLetters.includes(letter);
                html += `
                    <div class="option-card ${isSelected ? 'selected' : ''}" data-letter="${letter}">
                        <div class="option-letter-badge">${letter}</div>
                        <div class="option-text">${GateFormatter.render(optText)}</div>
                    </div>
                `;
            });
            html += '</div>';
            answerContainer.innerHTML = html;

            answerContainer.querySelectorAll('.option-card').forEach(card => {
                card.addEventListener('click', () => {
                    const letter = card.dataset.letter;
                    if (selectedLetters.includes(letter)) {
                        selectedLetters = selectedLetters.filter(l => l !== letter);
                        card.classList.remove('selected');
                    } else {
                        selectedLetters.push(letter);
                        card.classList.add('selected');
                    }
                    this.responses[qNum] = selectedLetters.length > 0 ? selectedLetters : null;
                });
            });

        } else if (q.type === 'NAT') {
            const val = currentAns !== undefined && currentAns !== null ? currentAns : '';
            const precisionNote = q.nat_precision !== null ? `(Allowed precision: ${q.nat_precision} decimal places)` : '';
            answerContainer.innerHTML = `
                <div class="nat-input-container">
                    <label class="nat-label">Enter Numerical Answer ${precisionNote}:</label>
                    <input type="text" id="nat-input-display" class="nat-display-input" value="${val}" placeholder="Enter value using keypad or keyboard" />
                    <div class="nat-keypad-grid">
                        <button class="nat-btn" data-key="7">7</button>
                        <button class="nat-btn" data-key="8">8</button>
                        <button class="nat-btn" data-key="9">9</button>
                        <button class="nat-btn" data-key="4">4</button>
                        <button class="nat-btn" data-key="5">5</button>
                        <button class="nat-btn" data-key="6">6</button>
                        <button class="nat-btn" data-key="1">1</button>
                        <button class="nat-btn" data-key="2">2</button>
                        <button class="nat-btn" data-key="3">3</button>
                        <button class="nat-btn" data-key="0">0</button>
                        <button class="nat-btn" data-key=".">.</button>
                        <button class="nat-btn" data-key="-">&minus;</button>
                        <button class="nat-btn nat-btn-action" data-key="backspace" style="grid-column: span 1;">&larr; Del</button>
                        <button class="nat-btn nat-btn-action" data-key="clear" style="grid-column: span 2;">Clear Input</button>
                    </div>
                </div>
            `;

            const inputDisplay = document.getElementById('nat-input-display');
            inputDisplay.addEventListener('input', (e) => {
                this.responses[qNum] = e.target.value.trim();
            });

            answerContainer.querySelectorAll('.nat-btn').forEach(btn => {
                btn.addEventListener('click', () => {
                    const k = btn.dataset.key;
                    let cur = inputDisplay.value;
                    if (k === 'clear') {
                        cur = '';
                    } else if (k === 'backspace') {
                        cur = cur.slice(0, -1);
                    } else if (k === '-') {
                        cur = cur.startsWith('-') ? cur.slice(1) : '-' + cur;
                    } else if (k === '.') {
                        if (!cur.includes('.')) cur += '.';
                    } else {
                        cur += k;
                    }
                    inputDisplay.value = cur;
                    this.responses[qNum] = cur.trim();
                });
            });
        }

        this.updatePaletteButtonState();
        this.updateLegendCounters();
    }

    navigateToQuestion(index) {
        if (index < 0 || index >= this.questions.length) return;
        this.showQuestion(index);
    }

    handleSaveNext() {
        const qNum = this.currentIndex + 1;
        const ans = this.responses[qNum];
        const hasAnswer = this.isResponseGiven(ans);

        if (hasAnswer) {
            this.qStates[this.currentIndex] = 2; // Answered (Green)
        } else {
            if (this.qStates[this.currentIndex] === 0 || this.qStates[this.currentIndex] === 1) {
                this.qStates[this.currentIndex] = 1; // Not Answered (Red)
            }
        }

        this.saveCurrentProgress();
        if (this.currentIndex < this.questions.length - 1) {
            this.showQuestion(this.currentIndex + 1);
        } else {
            GateNotify.show('Reached last question of paper.', 'info');
        }
    }

    handleMarkReviewNext() {
        const qNum = this.currentIndex + 1;
        const ans = this.responses[qNum];
        const hasAnswer = this.isResponseGiven(ans);

        if (hasAnswer) {
            this.qStates[this.currentIndex] = 4; // Answered & Marked for Review (Purple with dot)
        } else {
            this.qStates[this.currentIndex] = 3; // Marked for Review (Purple)
        }

        this.saveCurrentProgress();
        if (this.currentIndex < this.questions.length - 1) {
            this.showQuestion(this.currentIndex + 1);
        } else {
            GateNotify.show('Reached last question of paper.', 'info');
        }
    }

    handleClearResponse() {
        const qNum = this.currentIndex + 1;
        this.responses[qNum] = null;
        this.qStates[this.currentIndex] = 1; // Not Answered

        this.showQuestion(this.currentIndex);
        this.saveCurrentProgress();
        GateNotify.show('Response cleared', 'info');
    }

    handlePrev() {
        if (this.currentIndex > 0) {
            this.showQuestion(this.currentIndex - 1);
        }
    }

    isResponseGiven(ans) {
        if (ans === undefined || ans === null) return false;
        if (typeof ans === 'string' && ans.trim() === '') return false;
        if (Array.isArray(ans) && ans.length === 0) return false;
        return true;
    }

    renderPaletteGrid() {
        const gaGrid = document.getElementById('palette-grid-ga');
        const csGrid = document.getElementById('palette-grid-cs');
        gaGrid.innerHTML = '';
        csGrid.innerHTML = '';

        for (let i = 0; i < 65; i++) {
            const qNum = i + 1;
            const btn = document.createElement('button');
            btn.className = 'palette-q-btn shape-not-visited';
            btn.id = `palette-btn-${i}`;
            btn.innerText = qNum;

            btn.addEventListener('click', () => {
                this.showQuestion(i);
            });

            if (i < 10) {
                gaGrid.appendChild(btn);
            } else {
                csGrid.appendChild(btn);
            }
        }
        this.updatePaletteButtonState();
        this.updateLegendCounters();
    }

    updatePaletteButtonState() {
        for (let i = 0; i < 65; i++) {
            const btn = document.getElementById(`palette-btn-${i}`);
            if (!btn) continue;

            const st = this.qStates[i];
            btn.className = 'palette-q-btn';

            if (i === this.currentIndex) {
                btn.classList.add('current');
            }

            switch (st) {
                case 0: btn.classList.add('shape-not-visited'); break;
                case 1: btn.classList.add('shape-not-answered'); break;
                case 2: btn.classList.add('shape-answered'); break;
                case 3: btn.classList.add('shape-marked'); break;
                case 4: btn.classList.add('shape-ans-marked'); break;
            }
        }
    }

    updateLegendCounters() {
        let notVisited = 0, notAnswered = 0, answered = 0, marked = 0, ansMarked = 0;
        let gaAnswered = 0, csAnswered = 0;

        for (let i = 0; i < 65; i++) {
            const st = this.qStates[i];
            if (st === 0) notVisited++;
            else if (st === 1) notAnswered++;
            else if (st === 2) {
                answered++;
                if (i < 10) gaAnswered++; else csAnswered++;
            }
            else if (st === 3) marked++;
            else if (st === 4) {
                ansMarked++;
                if (i < 10) gaAnswered++; else csAnswered++;
            }
        }

        document.getElementById('legend-count-answered').innerText = answered;
        document.getElementById('legend-count-not-answered').innerText = notAnswered;
        document.getElementById('legend-count-not-visited').innerText = notVisited;
        document.getElementById('legend-count-marked').innerText = marked;
        document.getElementById('legend-count-ans-marked').innerText = ansMarked;

        document.getElementById('section-badge-ga').innerText = `${gaAnswered}/10`;
        document.getElementById('section-badge-cs').innerText = `${csAnswered}/55`;
    }

    saveCurrentProgress() {
        GateStorage.saveProgress(this.paperNum, {
            paper: this.paperNum,
            responses: this.responses,
            qStates: this.qStates,
            timeLeft: this.timeLeft,
            currentIndex: this.currentIndex
        });
    }

    openSubmitSummaryModal() {
        // Calculate breakdown for summary table
        let ga = { total: 10, ans: 0, notAns: 0, marked: 0, ansMarked: 0, notVis: 0 };
        let cs = { total: 55, ans: 0, notAns: 0, marked: 0, ansMarked: 0, notVis: 0 };

        for (let i = 0; i < 65; i++) {
            const target = i < 10 ? ga : cs;
            const st = this.qStates[i];
            if (st === 0) target.notVis++;
            else if (st === 1) target.notAns++;
            else if (st === 2) target.ans++;
            else if (st === 3) target.marked++;
            else if (st === 4) target.ansMarked++;
        }

        const tbody = document.getElementById('submit-summary-tbody');
        tbody.innerHTML = `
            <tr>
                <td style="text-align: left; font-weight: bold;">General Aptitude</td>
                <td>10</td>
                <td style="color: #27ae60; font-weight: bold;">${ga.ans}</td>
                <td style="color: #e74c3c;">${ga.notAns}</td>
                <td style="color: #8e44ad;">${ga.marked}</td>
                <td style="color: #8e44ad; font-weight: bold;">${ga.ansMarked}</td>
                <td style="color: #9e9e9e;">${ga.notVis}</td>
            </tr>
            <tr>
                <td style="text-align: left; font-weight: bold;">Computer Science & IT</td>
                <td>55</td>
                <td style="color: #27ae60; font-weight: bold;">${cs.ans}</td>
                <td style="color: #e74c3c;">${cs.notAns}</td>
                <td style="color: #8e44ad;">${cs.marked}</td>
                <td style="color: #8e44ad; font-weight: bold;">${cs.ansMarked}</td>
                <td style="color: #9e9e9e;">${cs.notVis}</td>
            </tr>
            <tr style="font-weight: bold; background: #eef2f7;">
                <td style="text-align: left;">Total (GATE CS 2027)</td>
                <td>65</td>
                <td style="color: #27ae60;">${ga.ans + cs.ans}</td>
                <td style="color: #e74c3c;">${ga.notAns + cs.notAns}</td>
                <td style="color: #8e44ad;">${ga.marked + cs.marked}</td>
                <td style="color: #8e44ad;">${ga.ansMarked + cs.ansMarked}</td>
                <td style="color: #9e9e9e;">${ga.notVis + cs.notVis}</td>
            </tr>
        `;

        document.getElementById('submit-summary-modal').classList.add('active');
    }

    openQuestionPaperModal() {
        const body = document.getElementById('qp-modal-content');
        let html = '';
        this.questions.forEach((q, idx) => {
            const num = idx + 1;
            if (num === 1) html += '<div class="palette-section-header" style="margin-top: 10px;">Section 1: General Aptitude</div>';
            if (num === 11) html += '<div class="palette-section-header" style="margin-top: 24px;">Section 2: Computer Science & IT</div>';

            html += `
                <div style="border: 1px solid #e2e8f0; border-radius: 4px; padding: 12px; margin-bottom: 12px; background: #fff;">
                    <div style="font-weight: bold; font-size: 13px; color: #1e293b; margin-bottom: 6px;">
                        Q${num}. [${q.marks} Mark] [${q.type}] [${q.subject}]
                    </div>
                    <div style="font-size: 13.5px; margin-bottom: 8px;">${GateFormatter.render(q.stem)}</div>
            `;
            if (q.options && q.options.length > 0) {
                const letters = ['A', 'B', 'C', 'D'];
                html += '<div style="margin-left: 12px; font-size: 13px;">';
                q.options.forEach((opt, oIdx) => {
                    html += `<div><strong>(${letters[oIdx]})</strong> ${opt}</div>`;
                });
                html += '</div>';
            }
            html += '</div>';
        });

        body.innerHTML = html;
        document.getElementById('question-paper-modal').classList.add('active');
    }

    openInstructionsModal() {
        document.getElementById('instructions-modal').classList.add('active');
    }

    async submitExam() {
        clearInterval(this.timerInterval);
        document.getElementById('submit-summary-modal').classList.remove('active');

        // Loading state
        GateNotify.show('Evaluating answers with official GATE negative marking scheme...', 'info', 5000);

        const timeSpent = this.totalDurationSeconds - this.timeLeft;

        try {
            const resp = await fetch(`/api/paper/${this.paperNum}/submit`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    responses: this.responses,
                    time_spent_seconds: timeSpent
                })
            });

            const data = await resp.json();
            if (data.status === 'success') {
                GateStorage.saveResult(this.paperNum, data.result);
                window.location.href = `/result.html?paper=${this.paperNum}`;
            } else {
                GateNotify.show(data.message || 'Submission failed', 'error');
            }
        } catch (e) {
            console.error('Submit failed', e);
            GateNotify.show('Network error during test submission', 'error');
        }
    }
}

// Instantiate simulator on page load
document.addEventListener('DOMContentLoaded', () => {
    window.gateSimulator = new GateExamSimulator();
});

