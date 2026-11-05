/**
 * GATE 2027 Post-Exam Scorecard & Solution Viewer Engine
 */

class GateResultViewer {
    constructor() {
        this.paperNum = this.getPaperNumberFromUrl();
        this.resultData = null;
        this.currentFilter = 'all'; // 'all', 'correct', 'incorrect', 'unattempted'
        this.selectedSubject = 'all';

        this.init();
    }

    getPaperNumberFromUrl() {
        const params = new URLSearchParams(window.location.search);
        const p = parseInt(params.get('paper'), 10);
        return (!isNaN(p) && p >= 1 && p <= 100) ? p : 1;
    }

    async init() {
        // Try reading stored result first
        this.resultData = GateStorage.getResult(this.paperNum);

        // If not in storage (e.g. direct solution viewing), fetch solutions from backend API
        if (!this.resultData) {
            try {
                const resp = await fetch(`/api/paper/${this.paperNum}/solutions`);
                const data = await resp.json();
                if (data.status === 'success') {
                    this.buildStudyModeResult(data.questions, data.summary);
                } else {
                    GateNotify.show('Failed to load solutions for this mock.', 'error');
                }
            } catch (e) {
                console.error(e);
                GateNotify.show('Network error loading test solutions', 'error');
            }
        }

        if (this.resultData) {
            this.renderScorecard();
            this.renderSubjectTable();
            this.populateSubjectFilter();
            this.renderQuestions();
            this.bindEvents();
        }
    }

    buildStudyModeResult(questions, summary) {
        // Mock result representation for direct solutions viewer
        const subjects = {};
        const qResults = questions.map((q) => {
            const subj = q.subject || 'General Aptitude';
            if (!subjects[subj]) subjects[subj] = { total: 0, attempted: 0, correct: 0, incorrect: 0, score: 0, marks_possible: 0 };
            subjects[subj].total++;
            subjects[subj].marks_possible += q.marks;

            return {
                number: q.number,
                id: q.id,
                subject: subj,
                subtopic: q.subtopic,
                type: q.type,
                marks: q.marks,
                difficulty: q.difficulty,
                stem: q.stem,
                options: q.options,
                user_answer: null,
                correct_answer: q.answer,
                nat_range: q.nat,
                status: 'UNATTEMPTED',
                score_awarded: 0,
                solution: q.solution,
                option_explanations: q.option_explanations,
                misconception: q.misconception
            };
        });

        const subjectSummary = Object.keys(subjects).map(s => ({
            subject: s,
            total_questions: subjects[s].total,
            attempted: 0,
            correct: 0,
            incorrect: 0,
            score: 0,
            marks_possible: subjects[s].marks_possible,
            accuracy: 0
        }));

        this.resultData = {
            paper: this.paperNum,
            title: `GATE CS 2027 Mock Test ${String(this.paperNum).padStart(3, '0')} — Official Solutions`,
            time_spent_seconds: 0,
            total_score: 0,
            max_marks: 100,
            positive_marks: 0,
            negative_marks: 0,
            correct_count: 0,
            incorrect_count: 0,
            unattempted_count: questions.length,
            total_questions: questions.length,
            accuracy_percentage: 0,
            is_qualified: false,
            qualifying_marks: 27.5,
            estimated_gate_score: 0,
            estimated_air: 'Study Mode',
            section_a_score: 0,
            section_b_score: 0,
            subject_breakdown: subjectSummary,
            questions: qResults,
            isStudyMode: true
        };
    }

    renderScorecard() {
        const d = this.resultData;
        document.getElementById('result-paper-title').innerText = d.title || `GATE CS 2027 Mock Test ${String(this.paperNum).padStart(3, '0')}`;
        document.getElementById('result-time-taken').innerText = d.time_spent_seconds ? GateFormatter.formatTime(d.time_spent_seconds) : 'N/A';

        // Qualification status
        const qualBox = document.getElementById('result-qual-status');
        if (d.isStudyMode) {
            qualBox.className = 'badge-qualified';
            qualBox.innerHTML = `<span>📖 Solution Study Mode</span>`;
        } else if (d.is_qualified) {
            qualBox.className = 'badge-qualified';
            qualBox.innerHTML = `<span>✓ QUALIFIED (GATE CS Cutoff: ${d.qualifying_marks})</span>`;
        } else {
            qualBox.className = 'badge-not-qualified';
            qualBox.innerHTML = `<span>Below Cutoff (${d.qualifying_marks})</span>`;
        }

        // Metrics
        document.getElementById('metric-total-score').innerHTML = `${d.total_score} <small>/ 100</small>`;
        document.getElementById('metric-gate-score').innerText = d.estimated_gate_score || 0;
        document.getElementById('metric-estimated-air').innerText = d.estimated_air || 'N/A';
        document.getElementById('metric-accuracy').innerText = `${d.accuracy_percentage}%`;
        document.getElementById('metric-attempted').innerText = `${d.correct_count + d.incorrect_count} / ${d.total_questions}`;

        // Marks breakdown
        document.getElementById('metric-correct').innerText = `${d.correct_count} (+${d.positive_marks})`;
        document.getElementById('metric-incorrect').innerText = `${d.incorrect_count} (-${d.negative_marks})`;
        document.getElementById('metric-unattempted').innerText = `${d.unattempted_count}`;

        // Section Cards
        document.getElementById('sec-a-score').innerText = `${d.section_a_score} / 15`;
        document.getElementById('sec-b-score').innerText = `${d.section_b_score} / 85`;
    }

    renderSubjectTable() {
        const tbody = document.getElementById('subject-table-tbody');
        tbody.innerHTML = '';

        (this.resultData.subject_breakdown || []).forEach(sub => {
            const acc = sub.accuracy || 0;
            const barColor = acc >= 70 ? '#16a34a' : acc >= 40 ? '#d97706' : '#dc2626';

            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td style="font-weight: 600; color: #1e293b;">${sub.subject}</td>
                <td>${sub.total_questions}</td>
                <td>${sub.attempted}</td>
                <td style="color: #16a34a; font-weight: bold;">${sub.correct}</td>
                <td style="color: #dc2626;">${sub.incorrect}</td>
                <td style="font-weight: bold; color: #0284c7;">${sub.score} / ${sub.marks_possible}</td>
                <td>
                    <div class="accuracy-bar-track">
                        <div class="accuracy-bar-fill" style="width: ${acc}%; background: ${barColor};"></div>
                    </div>
                    <span>${acc}%</span>
                </td>
            `;
            tbody.appendChild(tr);
        });
    }

    populateSubjectFilter() {
        const select = document.getElementById('filter-subject-select');
        select.innerHTML = '<option value="all">All Subjects (11)</option>';

        (this.resultData.subject_breakdown || []).forEach(sub => {
            const opt = document.createElement('option');
            opt.value = sub.subject;
            opt.innerText = `${sub.subject} (${sub.total_questions})`;
            select.appendChild(opt);
        });
    }

    renderQuestions() {
        const container = document.getElementById('solution-questions-list');
        container.innerHTML = '';

        const qs = this.resultData.questions || [];
        let countVisible = 0;

        qs.forEach(q => {
            // Apply status filter
            if (this.currentFilter === 'correct' && q.status !== 'CORRECT') return;
            if (this.currentFilter === 'incorrect' && q.status !== 'INCORRECT') return;
            if (this.currentFilter === 'unattempted' && q.status !== 'UNATTEMPTED') return;

            // Apply subject filter
            if (this.selectedSubject !== 'all' && q.subject !== this.selectedSubject) return;

            countVisible++;

            let statusClass = 'sol-status-unattempted';
            let statusText = 'Not Attempted (0 Marks)';
            if (q.status === 'CORRECT') {
                statusClass = 'sol-status-correct';
                statusText = `Correct (+${q.score_awarded} Marks)`;
            } else if (q.status === 'INCORRECT') {
                statusClass = 'sol-status-incorrect';
                statusText = `Incorrect (${q.score_awarded} Marks)`;
            }

            // User answer string formatting
            let userAnsDisplay = 'Not Attempted';
            if (q.user_answer !== null && q.user_answer !== undefined && q.user_answer !== '') {
                userAnsDisplay = Array.isArray(q.user_answer) ? q.user_answer.join(', ') : String(q.user_answer);
            }

            // Official answer string formatting
            let officialAnsDisplay = '';
            if (q.type === 'MCQ' || q.type === 'MSQ') {
                officialAnsDisplay = Array.isArray(q.correct_answer) ? q.correct_answer.join(', ') : String(q.correct_answer);
            } else if (q.type === 'NAT') {
                const nat = q.nat_range || {};
                if (nat.min !== undefined && nat.max !== undefined) {
                    officialAnsDisplay = nat.min === nat.max ? `${nat.min}` : `${nat.min} to ${nat.max}`;
                } else {
                    officialAnsDisplay = String(q.correct_answer);
                }
            }

            const card = document.createElement('div');
            card.className = 'solution-item-card';
            card.innerHTML = `
                <div class="solution-item-header">
                    <div>
                        <span class="sol-q-title">Question ${q.number}</span>
                        <span style="font-size: 12px; color: #64748b; margin-left: 10px;">[${q.marks} Mark] [${q.type}] [${q.subject} &bull; ${q.subtopic || ''}]</span>
                    </div>
                    <div class="sol-status-pill ${statusClass}">${statusText}</div>
                </div>

                <div class="sol-stem">${GateFormatter.render(q.stem)}</div>

                <!-- Answer Comparison -->
                <div class="sol-answers-grid">
                    <div>
                        <div class="answer-label">Your Response:</div>
                        <div class="answer-value ${q.status === 'CORRECT' ? 'user-correct' : q.status === 'INCORRECT' ? 'user-wrong' : ''}">
                            ${userAnsDisplay}
                        </div>
                    </div>
                    <div>
                        <div class="answer-label">Official Correct Answer:</div>
                        <div class="answer-value official">${officialAnsDisplay}</div>
                    </div>
                </div>

                <!-- Worked Step-by-Step Solution -->
                <div class="sol-worked-box">
                    <div class="sol-worked-title">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>
                        <span>Step-by-Step Worked Solution</span>
                    </div>
                    <div class="sol-worked-text">${GateFormatter.render(q.solution || 'Detailed derivation available in official reference solution.')}</div>
                </div>

                <!-- Option Explanations (if present) -->
                ${q.option_explanations && q.option_explanations.length > 0 ? `
                    <div class="sol-opt-explanations">
                        <div style="font-weight: bold; margin-bottom: 6px;">Option-by-Option Breakdown:</div>
                        ${q.option_explanations.map((exp, idx) => `
                            <div class="sol-opt-item"><strong>(${String.fromCharCode(65 + idx)}):</strong> ${exp}</div>
                        `).join('')}
                    </div>
                ` : ''}

                <!-- Misconception / Trap Alert -->
                ${q.misconception ? `
                    <div class="sol-misconception-box">
                        <strong>Exam Trap / Key Misconception:</strong> ${q.misconception}
                    </div>
                ` : ''}
            `;
            container.appendChild(card);
        });

        if (countVisible === 0) {
            container.innerHTML = `
                <div style="text-align: center; padding: 40px; color: #64748b;">
                    No questions match the selected filter criteria.
                </div>
            `;
        }
    }

    bindEvents() {
        // Status filter tabs
        document.querySelectorAll('.filter-tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.filter-tab-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.currentFilter = btn.dataset.filter;
                this.renderQuestions();
            });
        });

        // Subject dropdown
        document.getElementById('filter-subject-select').addEventListener('change', (e) => {
            this.selectedSubject = e.target.value;
            this.renderQuestions();
        });

        // Retake test button
        document.getElementById('btn-retake-mock').addEventListener('click', () => {
            if (confirm(`Do you want to retake GATE Mock Test ${String(this.paperNum).padStart(3, '0')}? This will clear your current attempt.`)) {
                GateStorage.clearProgress(this.paperNum);
                window.location.href = `/exam.html?paper=${this.paperNum}`;
            }
        });

        // Print scorecard
        document.getElementById('btn-print-scorecard').addEventListener('click', () => {
            window.print();
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.gateResultViewer = new GateResultViewer();
});

