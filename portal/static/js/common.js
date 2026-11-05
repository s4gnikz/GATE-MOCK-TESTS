/**
 * GATE CS 2027 Mock Portal — Common Utilities & Storage Engine
 */

const GATE_STORAGE_KEYS = {
    PROGRESS_PREFIX: 'gate_exam_progress_',
    RESULT_PREFIX: 'gate_exam_result_',
    PROFILE: 'gate_candidate_profile',
    RECENT_ATTEMPTS: 'gate_recent_attempts'
};

// Storage Engine
const GateStorage = {
    getProfile() {
        try {
            const raw = localStorage.getItem(GATE_STORAGE_KEYS.PROFILE);
            if (raw) return JSON.parse(raw);
        } catch (e) {
            console.error('Failed to read profile', e);
        }
        return {
            name: 'GATE CS Aspirant',
            rollNumber: 'GATE2027-CS-C001',
            systemId: 'C001',
            targetScore: 75
        };
    },

    saveProfile(profile) {
        try {
            localStorage.setItem(GATE_STORAGE_KEYS.PROFILE, JSON.stringify(profile));
        } catch (e) {
            console.error('Failed to save profile', e);
        }
    },

    getProgress(paperNum) {
        try {
            const key = GATE_STORAGE_KEYS.PROGRESS_PREFIX + String(paperNum).padStart(3, '0');
            const raw = localStorage.getItem(key);
            if (raw) return JSON.parse(raw);
        } catch (e) {
            console.error('Failed to get progress', e);
        }
        return null;
    },

    saveProgress(paperNum, progressData) {
        try {
            const key = GATE_STORAGE_KEYS.PROGRESS_PREFIX + String(paperNum).padStart(3, '0');
            progressData.updatedAt = Date.now();
            localStorage.setItem(key, JSON.stringify(progressData));
            this.updateRecentAttempt(paperNum, 'in_progress');
        } catch (e) {
            console.error('Failed to save progress', e);
        }
    },

    clearProgress(paperNum) {
        try {
            const key = GATE_STORAGE_KEYS.PROGRESS_PREFIX + String(paperNum).padStart(3, '0');
            localStorage.removeItem(key);
        } catch (e) {
            console.error('Failed to clear progress', e);
        }
    },

    getResult(paperNum) {
        try {
            const key = GATE_STORAGE_KEYS.RESULT_PREFIX + String(paperNum).padStart(3, '0');
            const raw = localStorage.getItem(key);
            if (raw) return JSON.parse(raw);
        } catch (e) {
            console.error('Failed to get result', e);
        }
        return null;
    },

    saveResult(paperNum, resultData) {
        try {
            const key = GATE_STORAGE_KEYS.RESULT_PREFIX + String(paperNum).padStart(3, '0');
            resultData.savedAt = Date.now();
            localStorage.setItem(key, JSON.stringify(resultData));
            this.updateRecentAttempt(paperNum, 'completed', resultData.total_score);
            this.clearProgress(paperNum);
        } catch (e) {
            console.error('Failed to save result', e);
        }
    },

    getAllAttemptStates() {
        const states = {};
        try {
            for (let i = 1; i <= 100; i++) {
                const pad = String(i).padStart(3, '0');
                const res = localStorage.getItem(GATE_STORAGE_KEYS.RESULT_PREFIX + pad);
                if (res) {
                    const parsed = JSON.parse(res);
                    states[i] = {
                        status: 'completed',
                        score: parsed.total_score,
                        date: parsed.savedAt
                    };
                    continue;
                }
                const prog = localStorage.getItem(GATE_STORAGE_KEYS.PROGRESS_PREFIX + pad);
                if (prog) {
                    const parsed = JSON.parse(prog);
                    states[i] = {
                        status: 'in_progress',
                        timeLeft: parsed.timeLeft,
                        answeredCount: Object.keys(parsed.responses || {}).length,
                        updatedAt: parsed.updatedAt
                    };
                    continue;
                }
                states[i] = { status: 'not_attempted' };
            }
        } catch (e) {
            console.error('Failed to scan attempts', e);
        }
        return states;
    },

    updateRecentAttempt(paperNum, status, score = null) {
        try {
            let recents = JSON.parse(localStorage.getItem(GATE_STORAGE_KEYS.RECENT_ATTEMPTS) || '[]');
            recents = recents.filter(item => item.paper !== paperNum);
            recents.unshift({
                paper: paperNum,
                status: status,
                score: score,
                timestamp: Date.now()
            });
            if (recents.length > 10) recents = recents.slice(0, 10);
            localStorage.setItem(GATE_STORAGE_KEYS.RECENT_ATTEMPTS, JSON.stringify(recents));
        } catch (e) {
            console.error('Failed to update recent attempts', e);
        }
    }
};

// Markdown & Math Formatter
const GateFormatter = {
    render(text) {
        if (!text) return '';

        // If marked.js is available on window, use it
        if (typeof marked !== 'undefined' && typeof marked.parse === 'function') {
            try {
                let html = marked.parse(text);
                // KaTeX auto-render if available
                return this.renderMath(html);
            } catch (e) {
                console.warn('Marked parse failed, using fallback', e);
            }
        }

        // Lightweight robust Markdown fallback
        let out = text;

        // Escape raw HTML entities
        out = out.replace(/&/g, '&amp;')
                 .replace(/</g, '&lt;')
                 .replace(/>/g, '&gt;');

        // Fenced code blocks with language support
        out = out.replace(/```([a-zA-Z0-9_-]*)\n([\s\S]*?)```/g, (match, lang, code) => {
            const langLabel = lang ? `<span class="code-lang-tag">${lang}</span>` : '';
            return `<div class="code-block-wrapper">${langLabel}<pre class="code-block"><code>${code.trim()}</code></pre></div>`;
        });

        // Inline code
        out = out.replace(/`([^`]+)`/g, '<code class="inline-code">$1</code>');

        // Bold
        out = out.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

        // Italic
        out = out.replace(/\*([^*]+)\*/g, '<em>$1</em>');

        // Tables
        out = out.replace(/((?:\|[^\n]+\|\n?)+)/g, (match) => {
            const lines = match.trim().split('\n');
            if (lines.length < 2) return match;
            let tableHtml = '<div class="table-responsive"><table class="gate-table">';
            lines.forEach((line, idx) => {
                const cells = line.split('|').filter((c, i, a) => i > 0 && i < a.length - 1);
                if (line.includes('---')) return; // Separator line
                const tag = idx === 0 ? 'th' : 'td';
                tableHtml += '<tr>' + cells.map(c => `<${tag}>${c.trim()}</${tag}>`).join('') + '</tr>';
            });
            tableHtml += '</table></div>';
            return tableHtml;
        });

        // Paragraphs & Line Breaks
        out = out.replace(/\n\n+/g, '</p><p>');
        out = '<p>' + out.replace(/\n/g, '<br/>') + '</p>';
        out = out.replace(/<p><\/p>/g, '');

        return this.renderMath(out);
    },

    renderMath(html) {
        if (!html) return '';
        // If KaTeX is loaded
        if (typeof renderMathInElement === 'function') {
            // KaTeX auto render will be triggered on container DOM element
            return html;
        }

        // Fallback for simple math: $...$ and $$...$$
        html = html.replace(/\$\$([^$]+)\$\$/g, '<div class="math-display"><em>$1</em></div>');
        html = html.replace(/\$([^$]+)\$/g, '<span class="math-inline"><em>$1</em></span>');
        return html;
    },

    formatTime(seconds) {
        const h = Math.floor(seconds / 3600);
        const m = Math.floor((seconds % 3600) / 60);
        const s = seconds % 60;
        return [
            h.toString().padStart(2, '0'),
            m.toString().padStart(2, '0'),
            s.toString().padStart(2, '0')
        ].join(':');
    },

    formatMinutesLeft(seconds) {
        const m = Math.floor(seconds / 60);
        const s = seconds % 60;
        return `${m}m ${s.toString().padStart(2, '0')}s`;
    }
};

// UI Notifications
const GateNotify = {
    show(message, type = 'info', duration = 3500) {
        let container = document.getElementById('gate-toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'gate-toast-container';
            container.className = 'gate-toast-container';
            document.body.appendChild(container);
        }

        const toast = document.createElement('div');
        toast.className = `gate-toast gate-toast-${type}`;
        toast.innerHTML = `
            <div class="toast-icon">
                ${type === 'success' ? '✓' : type === 'error' ? '✕' : type === 'warning' ? '⚠' : 'ℹ'}
            </div>
            <div class="toast-body">${message}</div>
        `;
        container.appendChild(toast);

        setTimeout(() => {
            toast.classList.add('fade-out');
            setTimeout(() => toast.remove(), 400);
        }, duration);
    }
};

