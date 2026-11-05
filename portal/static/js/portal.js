/**
 * GATE CS 2027 Mock Test Series Portal — Master Directory Controller
 */

class GatePortalDirectory {
    constructor() {
        this.papers = [];
        this.attemptStates = {};
        this.searchQuery = '';
        this.statusFilter = 'all'; // 'all', 'not_attempted', 'in_progress', 'completed'
        this.diffFilter = 'all';
        this.profile = GateStorage.getProfile();

        this.init();
    }

    async init() {
        this.updateProfileUI();
        this.bindProfileModal();

        try {
            const resp = await fetch('/api/papers');
            const data = await resp.json();
            if (data.status === 'success') {
                this.papers = data.papers;
                this.attemptStates = GateStorage.getAllAttemptStates();
                this.renderStatsRibbon();
                this.renderMocksGrid();
                this.bindFilters();
            } else {
                GateNotify.show('Failed to fetch mock papers list', 'error');
            }
        } catch (e) {
            console.error('Failed to load papers', e);
            GateNotify.show('Network error connecting to portal server', 'error');
        }
    }

    updateProfileUI() {
        const name = this.profile.name || 'GATE CS Aspirant';
        const roll = this.profile.rollNumber || 'GATE2027-CS-C001';
        const initials = name.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase() || 'CS';

        document.getElementById('header-cand-name').innerText = name;
        document.getElementById('header-cand-roll').innerText = roll;
        document.getElementById('header-cand-avatar').innerText = initials;
    }

    bindProfileModal() {
        const badge = document.getElementById('header-profile-badge');
        const modal = document.getElementById('profile-edit-modal');
        const closeBtn = document.getElementById('btn-close-profile-modal');
        const saveBtn = document.getElementById('btn-save-profile');

        const inputName = document.getElementById('input-profile-name');
        const inputRoll = document.getElementById('input-profile-roll');
        const inputTarget = document.getElementById('input-profile-target');

        badge.addEventListener('click', () => {
            inputName.value = this.profile.name || '';
            inputRoll.value = this.profile.rollNumber || '';
            inputTarget.value = this.profile.targetScore || 75;
            modal.classList.add('active');
        });

        closeBtn.addEventListener('click', () => modal.classList.remove('active'));

        saveBtn.addEventListener('click', () => {
            this.profile.name = inputName.value.trim() || 'GATE CS Aspirant';
            this.profile.rollNumber = inputRoll.value.trim() || 'GATE2027-CS-C001';
            this.profile.targetScore = parseInt(inputTarget.value, 10) || 75;
            GateStorage.saveProfile(this.profile);
            this.updateProfileUI();
            modal.classList.remove('active');
            GateNotify.show('Candidate profile updated successfully', 'success');
        });
    }

    renderStatsRibbon() {
        const total = this.papers.length;
        let completedCount = 0;
        let inProgressCount = 0;
        let totalScore = 0;

        Object.values(this.attemptStates).forEach(st => {
            if (st.status === 'completed') {
                completedCount++;
                totalScore += (st.score || 0);
            } else if (st.status === 'in_progress') {
                inProgressCount++;
            }
        });

        const avgScore = completedCount > 0 ? (totalScore / completedCount).toFixed(1) : '--';

        document.getElementById('stat-total-mocks').innerHTML = `${total} <small>Papers</small>`;
        document.getElementById('stat-completed-mocks').innerHTML = `${completedCount} <small>/ ${total}</small>`;
        document.getElementById('stat-in-progress-mocks').innerHTML = `${inProgressCount} <small>Active</small>`;
        document.getElementById('stat-avg-score').innerHTML = `${avgScore} <small>/ 100</small>`;
    }

    renderMocksGrid() {
        const grid = document.getElementById('mocks-grid');
        grid.innerHTML = '';

        let visibleCount = 0;

        this.papers.forEach(p => {
            const pNum = p.paper;
            const state = this.attemptStates[pNum] || { status: 'not_attempted' };

            // Status filter
            if (this.statusFilter !== 'all') {
                if (this.statusFilter === 'not_attempted' && state.status !== 'not_attempted') return;
                if (this.statusFilter === 'in_progress' && state.status !== 'in_progress') return;
                if (this.statusFilter === 'completed' && state.status !== 'completed') return;
            }

            // Search filter
            if (this.searchQuery) {
                const q = this.searchQuery.toLowerCase();
                const titleMatch = p.title.toLowerCase().includes(q);
                const numMatch = String(pNum).includes(q);
                const subjMatch = Object.keys(p.subjects || {}).some(s => s.toLowerCase().includes(q));
                if (!titleMatch && !numMatch && !subjMatch) return;
            }

            visibleCount++;

            // Difficulty pill
            let diffClass = 'diff-medium-hard';
            let diffLabel = 'Medium-Hard';
            const diffs = p.difficulties || {};
            if ((diffs['Hard'] || 0) > 12) {
                diffClass = 'diff-hard';
                diffLabel = 'Hard';
            } else if ((diffs['Medium'] || 0) > 30) {
                diffClass = 'diff-medium';
                diffLabel = 'Medium';
            }

            // Subject chips preview (up to 4)
            const subjectsList = Object.keys(p.subjects || {}).slice(0, 4);

            // Action button based on state
            let actionBtnHtml = '';
            if (state.status === 'completed') {
                actionBtnHtml = `
                    <a href="/result.html?paper=${pNum}" class="btn-launch-mock btn-launch-review">
                        <span>Score: ${state.score} / 100</span>
                        <span>&bull; View Solutions &rarr;</span>
                    </a>
                `;
            } else if (state.status === 'in_progress') {
                actionBtnHtml = `
                    <a href="/exam.html?paper=${pNum}" class="btn-launch-mock btn-launch-resume">
                        <span>Resume Test (${state.answeredCount || 0}/65 Answered) &rarr;</span>
                    </a>
                `;
            } else {
                actionBtnHtml = `
                    <a href="/exam.html?paper=${pNum}" class="btn-launch-mock btn-launch-fresh">
                        <span>Launch 3-Hour Exam &rarr;</span>
                    </a>
                `;
            }

            const card = document.createElement('div');
            card.className = 'mock-card';
            card.innerHTML = `
                <div>
                    <div class="mock-card-header">
                        <span class="mock-id-badge">MOCK ${String(pNum).padStart(3, '0')}</span>
                        <span class="mock-diff-pill ${diffClass}">${diffLabel}</span>
                    </div>

                    <div class="mock-card-title">${p.title}</div>

                    <div class="mock-meta-strip">
                        <span><strong>65</strong> Questions</span>
                        <span>&bull;</span>
                        <span><strong>100</strong> Marks</span>
                        <span>&bull;</span>
                        <span><strong>180</strong> Mins</span>
                    </div>

                    <div class="mock-subjects-tags">
                        ${subjectsList.map(s => `<span class="subj-tag-pill">${s}</span>`).join('')}
                    </div>
                </div>

                <div class="mock-card-footer">
                    ${actionBtnHtml}
                    <div class="mock-secondary-links">
                        <a href="/paper_view.html?paper=${pNum}">Read Paper & Answer Key</a>
                        <button class="btn-reset-mock" data-paper="${pNum}">Reset Attempt</button>
                    </div>
                </div>
            `;

            grid.appendChild(card);
        });

        // Bind reset buttons
        grid.querySelectorAll('.btn-reset-mock').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const paper = parseInt(e.target.dataset.paper, 10);
                if (confirm(`Reset all attempt history and progress for Mock ${String(paper).padStart(3, '0')}?`)) {
                    GateStorage.clearProgress(paper);
                    const key = GATE_STORAGE_KEYS.RESULT_PREFIX + String(paper).padStart(3, '0');
                    localStorage.removeItem(key);
                    this.attemptStates = GateStorage.getAllAttemptStates();
                    this.renderStatsRibbon();
                    this.renderMocksGrid();
                    GateNotify.show(`Mock ${String(paper).padStart(3, '0')} reset successfully.`, 'info');
                }
            });
        });

        if (visibleCount === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; color: #64748b;">
                    <h3>No mock tests found matching "${this.searchQuery}"</h3>
                    <p>Try clearing filters or searching by a different term.</p>
                </div>
            `;
        }
    }

    bindFilters() {
        const searchInput = document.getElementById('portal-search-input');
        searchInput.addEventListener('input', (e) => {
            this.searchQuery = e.target.value.trim();
            this.renderMocksGrid();
        });

        document.querySelectorAll('.status-pill-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.status-pill-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                this.statusFilter = btn.dataset.status;
                this.renderMocksGrid();
            });
        });
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.gatePortalDirectory = new GatePortalDirectory();
});

