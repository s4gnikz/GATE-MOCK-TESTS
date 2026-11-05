#!/usr/bin/env python3
"""
GATE CS 2027 Mock Test Portal Server
A high-performance, standard-library-only web server providing REST APIs
and an authentic GATE 3-Hour Online Examination Simulation Portal for candidates.
"""
from __future__ import annotations

import http.server
import json
import os
import re
import socketserver
import sys
import threading
import time
import urllib.parse
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "questions.jsonl"
PORTAL_DIR = ROOT / "portal"

# In-memory stores
QUESTIONS_BY_PAPER: dict[int, list[dict]] = defaultdict(list)
PAPER_SUMMARIES: list[dict] = []
BANK_LOADED = False
LOAD_LOCK = threading.Lock()


def load_question_bank():
    """Load questions.jsonl into memory and build fast index for all 100 papers."""
    global BANK_LOADED, PAPER_SUMMARIES
    with LOAD_LOCK:
        if BANK_LOADED:
            return
        t0 = time.time()
        print(f"[*] Loading question bank from {DATA_PATH}...")
        if not DATA_PATH.exists():
            raise FileNotFoundError(f"Questions database not found at {DATA_PATH}")

        with open(DATA_PATH, "r", encoding="utf-8-sig") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                q = json.loads(line)
                paper_num = int(q.get("paper", 0))
                QUESTIONS_BY_PAPER[paper_num].append(q)

        # Ensure questions in each paper are sorted 1..65
        for p in QUESTIONS_BY_PAPER:
            QUESTIONS_BY_PAPER[p].sort(key=lambda q: int(q.get("number", 0)))

        # Build summaries for papers 1 to 100
        summaries = []
        for p in range(1, 101):
            qs = QUESTIONS_BY_PAPER.get(p, [])
            types = Counter(q.get("type", "MCQ") for q in qs)
            diffs = Counter(q.get("difficulty", "Medium") for q in qs)
            subjects = Counter(q.get("subject", "Unknown") for q in qs)
            total_marks = sum(int(q.get("marks", 1)) for q in qs)

            summaries.append({
                "paper": p,
                "id": f"Mock_{p:03}",
                "title": f"GATE CS 2027 Mock Test {p:03}",
                "questions_count": len(qs),
                "total_marks": total_marks,
                "duration_minutes": 180,
                "types": dict(types),
                "difficulties": dict(diffs),
                "subjects": dict(subjects),
                "section_a_count": sum(1 for q in qs if q.get("number", 0) <= 10),
                "section_b_count": sum(1 for q in qs if q.get("number", 0) > 10),
            })
        PAPER_SUMMARIES = summaries
        BANK_LOADED = True
        t1 = time.time()
        print(f"[+] Loaded {sum(len(v) for v in QUESTIONS_BY_PAPER.values())} questions across {len(PAPER_SUMMARIES)} papers in {t1 - t0:.2f}s")


def sanitize_question_for_exam(q: dict) -> dict:
    """Return question metadata needed for the live examination (answers hidden)."""
    return {
        "id": q.get("id"),
        "paper": q.get("paper"),
        "number": q.get("number"),
        "subject": q.get("subject"),
        "subtopic": q.get("subtopic"),
        "type": q.get("type"),
        "marks": q.get("marks"),
        "difficulty": q.get("difficulty"),
        "stem": q.get("stem"),
        "options": q.get("options", []),
        "nat_precision": (q.get("nat") or {}).get("precision") if q.get("type") == "NAT" else None,
    }


def evaluate_submission(paper_num: int, user_responses: dict, time_spent_seconds: int = 0) -> dict:
    """
    Evaluate user responses against official answers following official GATE rules:
    - MCQ 1 Mark: +1 if correct, -1/3 (-0.3333) if incorrect, 0 if unattempted.
    - MCQ 2 Mark: +2 if correct, -2/3 (-0.6667) if incorrect, 0 if unattempted.
    - MSQ 1/2 Mark: Full marks if all correct options selected and no incorrect selected; 0 otherwise (no negative).
    - NAT 1/2 Mark: Full marks if numeric value within [min, max] range; 0 otherwise (no negative).
    - Answered & Marked for Review are evaluated!
    """
    questions = QUESTIONS_BY_PAPER.get(paper_num, [])
    if not questions:
        raise ValueError(f"Paper {paper_num} not found")

    total_score = 0.0
    positive_marks = 0.0
    negative_marks = 0.0
    correct_count = 0
    incorrect_count = 0
    unattempted_count = 0

    section_a_score = 0.0
    section_b_score = 0.0
    subject_stats = defaultdict(lambda: {"total": 0, "attempted": 0, "correct": 0, "incorrect": 0, "score": 0.0, "marks_possible": 0})
    question_results = []

    for q in questions:
        num = int(q.get("number", 0))
        num_str = str(num)
        typ = q.get("type", "MCQ")
        marks = int(q.get("marks", 1))
        subject = q.get("subject", "General Aptitude")
        user_ans = user_responses.get(num_str) if num_str in user_responses else user_responses.get(num)

        # Status tracking
        subject_stats[subject]["total"] += 1
        subject_stats[subject]["marks_possible"] += marks

        is_attempted = False
        if user_ans is not None:
            if isinstance(user_ans, str) and user_ans.strip() != "":
                is_attempted = True
            elif isinstance(user_ans, list) and len(user_ans) > 0:
                is_attempted = True
            elif isinstance(user_ans, (int, float)):
                is_attempted = True

        status = "UNATTEMPTED"
        q_score = 0.0

        if not is_attempted:
            unattempted_count += 1
            status = "UNATTEMPTED"
            q_score = 0.0
        else:
            subject_stats[subject]["attempted"] += 1
            if typ == "MCQ":
                # User answer is letter string 'A', 'B', 'C', 'D'
                correct_letter = q.get("answer", [""])[0] if isinstance(q.get("answer"), list) and q.get("answer") else str(q.get("answer", ""))
                selected = str(user_ans).strip().upper()
                if selected == correct_letter.upper():
                    status = "CORRECT"
                    q_score = float(marks)
                    correct_count += 1
                    positive_marks += q_score
                    subject_stats[subject]["correct"] += 1
                else:
                    status = "INCORRECT"
                    deduction = round(marks / 3.0, 4)
                    q_score = -deduction
                    incorrect_count += 1
                    negative_marks += deduction
                    subject_stats[subject]["incorrect"] += 1

            elif typ == "MSQ":
                # Multiple select: answer is list of letters
                correct_set = set(q.get("answer", []))
                if isinstance(user_ans, list):
                    user_set = set(str(x).strip().upper() for x in user_ans)
                elif isinstance(user_ans, str):
                    user_set = set(re.findall(r"[A-D]", user_ans.upper()))
                else:
                    user_set = set()

                if user_set == correct_set:
                    status = "CORRECT"
                    q_score = float(marks)
                    correct_count += 1
                    positive_marks += q_score
                    subject_stats[subject]["correct"] += 1
                else:
                    status = "INCORRECT"
                    q_score = 0.0  # In GATE, no negative marks for MSQ
                    incorrect_count += 1
                    subject_stats[subject]["incorrect"] += 1

            elif typ == "NAT":
                # Numerical Answer Type: check tolerance
                nat_info = q.get("nat") or {}
                min_val = nat_info.get("min")
                max_val = nat_info.get("max")
                exact_ans = q.get("answer")

                parsed_val = None
                try:
                    parsed_val = float(str(user_ans).strip())
                except (ValueError, TypeError):
                    parsed_val = None

                if parsed_val is not None:
                    is_correct = False
                    if min_val is not None and max_val is not None:
                        is_correct = (min_val - 1e-5) <= parsed_val <= (max_val + 1e-5)
                    elif exact_ans is not None:
                        try:
                            is_correct = abs(parsed_val - float(exact_ans)) < 1e-5
                        except Exception:
                            is_correct = False

                    if is_correct:
                        status = "CORRECT"
                        q_score = float(marks)
                        correct_count += 1
                        positive_marks += q_score
                        subject_stats[subject]["correct"] += 1
                    else:
                        status = "INCORRECT"
                        q_score = 0.0  # In GATE, no negative marks for NAT
                        incorrect_count += 1
                        subject_stats[subject]["incorrect"] += 1
                else:
                    status = "INCORRECT"
                    q_score = 0.0
                    incorrect_count += 1
                    subject_stats[subject]["incorrect"] += 1

        total_score += q_score
        subject_stats[subject]["score"] += q_score
        if num <= 10:
            section_a_score += q_score
        else:
            section_b_score += q_score

        question_results.append({
            "number": num,
            "id": q.get("id"),
            "subject": subject,
            "subtopic": q.get("subtopic"),
            "type": typ,
            "marks": marks,
            "difficulty": q.get("difficulty"),
            "stem": q.get("stem"),
            "options": q.get("options", []),
            "user_answer": user_ans,
            "correct_answer": q.get("answer"),
            "nat_range": q.get("nat"),
            "status": status,
            "score_awarded": round(q_score, 2),
            "solution": q.get("solution", ""),
            "option_explanations": q.get("option_explanations", []),
            "misconception": q.get("misconception", ""),
            "reasoning_steps": q.get("reasoning_steps"),
        })

    # Total score calculation & GATE Score estimation
    final_score = round(total_score, 2)
    # GATE qualifying marks for CS typically ~27.5
    qualifying_marks = 27.5
    is_qualified = final_score >= qualifying_marks

    # Estimated GATE Score out of 1000
    if final_score <= 0:
        estimated_gate_score = 0
        estimated_air = "N/A"
    elif final_score < qualifying_marks:
        estimated_gate_score = int((final_score / qualifying_marks) * 350)
        estimated_air = "15,000+"
    else:
        # Scale between qualifying (350) and 75 marks (~900)
        norm = (final_score - qualifying_marks) / (75.0 - qualifying_marks)
        norm = max(0.0, min(1.2, norm))
        estimated_gate_score = min(1000, int(350 + norm * 550))
        if final_score >= 75:
            estimated_air = "Top 100 (AIR 1 - 100)"
        elif final_score >= 65:
            estimated_air = "AIR 100 - 500"
        elif final_score >= 55:
            estimated_air = "AIR 500 - 1,500"
        elif final_score >= 45:
            estimated_air = "AIR 1,500 - 4,000"
        elif final_score >= 35:
            estimated_air = "AIR 4,000 - 8,000"
        else:
            estimated_air = "AIR 8,000 - 15,000"

    accuracy = round((correct_count / (correct_count + incorrect_count) * 100), 1) if (correct_count + incorrect_count) > 0 else 0.0

    # Format subject summary
    subject_summary = []
    for subj, data in subject_stats.items():
        subj_acc = round((data["correct"] / data["attempted"] * 100), 1) if data["attempted"] > 0 else 0.0
        subject_summary.append({
            "subject": subj,
            "total_questions": data["total"],
            "attempted": data["attempted"],
            "correct": data["correct"],
            "incorrect": data["incorrect"],
            "score": round(data["score"], 2),
            "marks_possible": data["marks_possible"],
            "accuracy": subj_acc,
        })
    subject_summary.sort(key=lambda s: s["score"], reverse=True)

    return {
        "paper": paper_num,
        "title": f"GATE CS 2027 Mock Test {paper_num:03}",
        "time_spent_seconds": time_spent_seconds,
        "total_score": final_score,
        "max_marks": 100,
        "positive_marks": round(positive_marks, 2),
        "negative_marks": round(negative_marks, 2),
        "correct_count": correct_count,
        "incorrect_count": incorrect_count,
        "unattempted_count": unattempted_count,
        "total_questions": len(questions),
        "accuracy_percentage": accuracy,
        "is_qualified": is_qualified,
        "qualifying_marks": qualifying_marks,
        "estimated_gate_score": estimated_gate_score,
        "estimated_air": estimated_air,
        "section_a_score": round(section_a_score, 2),
        "section_b_score": round(section_b_score, 2),
        "subject_breakdown": subject_summary,
        "questions": question_results,
    }


class GatePortalRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handles REST APIs and serves static portal web pages."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PORTAL_DIR), **kwargs)

    def end_headers(self):
        # Enable CORS for convenience
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def send_json(self, data: any, status: int = 200):
        payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # Ensure question bank is loaded
        load_question_bank()

        # API: Get list of all papers
        if path == "/api/papers":
            return self.send_json({"status": "success", "papers": PAPER_SUMMARIES, "total": len(PAPER_SUMMARIES)})

        # API: Overall Stats
        if path == "/api/stats":
            total_qs = sum(len(v) for v in QUESTIONS_BY_PAPER.values())
            return self.send_json({
                "status": "success",
                "total_papers": len(PAPER_SUMMARIES),
                "total_questions": total_qs,
                "exam": "GATE Computer Science & Information Technology (CS) 2027",
                "questions_per_paper": 65,
                "marks_per_paper": 100,
                "duration_minutes": 180,
            })

        # API: Get questions for specific mock paper (test mode: answers hidden)
        match_paper = re.match(r"^/api/paper/(\d+)$", path)
        if match_paper:
            paper_num = int(match_paper.group(1))
            if paper_num not in QUESTIONS_BY_PAPER:
                return self.send_json({"status": "error", "message": f"Paper {paper_num} not found"}, 404)
            qs = QUESTIONS_BY_PAPER[paper_num]
            sanitized = [sanitize_question_for_exam(q) for q in qs]
            summary = next((s for s in PAPER_SUMMARIES if s["paper"] == paper_num), None)
            return self.send_json({
                "status": "success",
                "paper": paper_num,
                "title": f"GATE CS 2027 Mock Test {paper_num:03}",
                "summary": summary,
                "questions": sanitized,
            })

        # API: Get full question details including solutions (study mode)
        match_full = re.match(r"^/api/paper/(\d+)/solutions$", path)
        if match_full:
            paper_num = int(match_full.group(1))
            if paper_num not in QUESTIONS_BY_PAPER:
                return self.send_json({"status": "error", "message": f"Paper {paper_num} not found"}, 404)
            qs = QUESTIONS_BY_PAPER[paper_num]
            summary = next((s for s in PAPER_SUMMARIES if s["paper"] == paper_num), None)
            return self.send_json({
                "status": "success",
                "paper": paper_num,
                "title": f"GATE CS 2027 Mock Test {paper_num:03} — Solutions",
                "summary": summary,
                "questions": qs,
            })

        # HTML routing conveniences
        if path in ("/", "/index", "/index.html"):
            self.path = "/index.html"
            return super().do_GET()
        elif path in ("/exam", "/exam.html"):
            self.path = "/exam.html"
            return super().do_GET()
        elif path in ("/result", "/result.html"):
            self.path = "/result.html"
            return super().do_GET()
        elif path in ("/paper", "/paper_view", "/paper_view.html"):
            self.path = "/paper_view.html"
            return super().do_GET()

        return super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        load_question_bank()

        # API: Submit Paper for evaluation
        match_submit = re.match(r"^/api/paper/(\d+)/submit$", path)
        if match_submit:
            paper_num = int(match_submit.group(1))
            if paper_num not in QUESTIONS_BY_PAPER:
                return self.send_json({"status": "error", "message": f"Paper {paper_num} not found"}, 404)

            content_length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(content_length)
            try:
                payload = json.loads(post_data.decode("utf-8")) if post_data else {}
            except Exception as e:
                return self.send_json({"status": "error", "message": f"Invalid JSON payload: {e}"}, 400)

            user_responses = payload.get("responses", {})
            time_spent = int(payload.get("time_spent_seconds", 0))

            try:
                result = evaluate_submission(paper_num, user_responses, time_spent)
                return self.send_json({"status": "success", "result": result})
            except Exception as e:
                return self.send_json({"status": "error", "message": f"Grading error: {e}"}, 500)

        self.send_json({"status": "error", "message": "Endpoint not found"}, 404)


class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def run_server(port: int = 8000, host: str = "0.0.0.0"):
    """Run the threaded portal HTTP server."""
    load_question_bank()
    server_address = (host, port)
    httpd = ThreadedHTTPServer(server_address, GatePortalRequestHandler)
    print(f"\n" + "=" * 65)
    print(f" GATE CS 2027 MOCK EXAMINATION PORTAL IS LIVE!")
    print(f"=" * 65)
    print(f" * Portal URL      : http://localhost:{port}")
    print(f" * Exam Simulator  : http://localhost:{port}/exam.html?paper=1")
    print(f" * Question Papers : http://localhost:{port}/paper_view.html?paper=1")
    print(f" * Total Mock Tests: {len(PAPER_SUMMARIES)} Full-Length Tests")
    print(f" * Total Questions : {sum(len(v) for v in QUESTIONS_BY_PAPER.values())}")
    print(f" * Press Ctrl+C to stop the server.")
    print("=" * 65 + "\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down portal server...")
        httpd.server_close()


if __name__ == "__main__":
    port_arg = int(os.environ.get("PORT", 8000))
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port_arg = int(sys.argv[1])
    host_arg = os.environ.get("HOST", "0.0.0.0")
    run_server(port=port_arg, host=host_arg)

