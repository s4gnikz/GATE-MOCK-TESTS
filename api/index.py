"""
Vercel Serverless Function entrypoint for GATE CS 2027 Mock Portal.
Uses Flask to expose the REST APIs and serve portal pages on Vercel.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import portal_server
from flask import Flask, jsonify, request, send_from_directory

# Pre-load question bank
portal_server.load_question_bank()

PORTAL_DIR = ROOT / "portal"
STATIC_DIR = PORTAL_DIR / "static"

app = Flask(__name__, static_folder=str(STATIC_DIR), static_url_path="/static")


@app.route("/")
def index():
    return send_from_directory(str(PORTAL_DIR), "index.html")


@app.route("/exam.html")
@app.route("/exam")
def exam():
    return send_from_directory(str(PORTAL_DIR), "exam.html")


@app.route("/result.html")
@app.route("/result")
def result():
    return send_from_directory(str(PORTAL_DIR), "result.html")


@app.route("/paper_view.html")
@app.route("/paper_view")
def paper_view():
    return send_from_directory(str(PORTAL_DIR), "paper_view.html")


@app.route("/api/papers", methods=["GET"])
def get_papers():
    return jsonify({
        "status": "success",
        "papers": portal_server.PAPER_SUMMARIES,
        "total": len(portal_server.PAPER_SUMMARIES)
    })


@app.route("/api/stats", methods=["GET"])
def get_stats():
    total_qs = sum(len(v) for v in portal_server.QUESTIONS_BY_PAPER.values())
    return jsonify({
        "status": "success",
        "total_papers": len(portal_server.PAPER_SUMMARIES),
        "total_questions": total_qs,
        "exam": "GATE Computer Science & Information Technology (CS) 2027",
        "questions_per_paper": 65,
        "marks_per_paper": 100,
        "duration_minutes": 180,
    })


@app.route("/api/paper/<int:paper_num>", methods=["GET"])
def get_paper(paper_num: int):
    if paper_num not in portal_server.QUESTIONS_BY_PAPER:
        return jsonify({"status": "error", "message": f"Paper {paper_num} not found"}), 404
    qs = portal_server.QUESTIONS_BY_PAPER[paper_num]
    sanitized = [portal_server.sanitize_question_for_exam(q) for q in qs]
    summary = next((s for s in portal_server.PAPER_SUMMARIES if s["paper"] == paper_num), None)
    return jsonify({
        "status": "success",
        "paper": paper_num,
        "title": f"GATE CS 2027 Mock Test {paper_num:03}",
        "summary": summary,
        "questions": sanitized,
    })


@app.route("/api/paper/<int:paper_num>/solutions", methods=["GET"])
def get_paper_solutions(paper_num: int):
    if paper_num not in portal_server.QUESTIONS_BY_PAPER:
        return jsonify({"status": "error", "message": f"Paper {paper_num} not found"}), 404
    qs = portal_server.QUESTIONS_BY_PAPER[paper_num]
    summary = next((s for s in portal_server.PAPER_SUMMARIES if s["paper"] == paper_num), None)
    return jsonify({
        "status": "success",
        "paper": paper_num,
        "title": f"GATE CS 2027 Mock Test {paper_num:03} — Solutions",
        "summary": summary,
        "questions": qs,
    })


@app.route("/api/paper/<int:paper_num>/submit", methods=["POST"])
def submit_paper(paper_num: int):
    if paper_num not in portal_server.QUESTIONS_BY_PAPER:
        return jsonify({"status": "error", "message": f"Paper {paper_num} not found"}), 404

    payload = request.get_json(silent=True) or {}
    user_responses = payload.get("responses", {})
    time_spent = int(payload.get("time_spent_seconds", 0))

    try:
        res = portal_server.evaluate_submission(paper_num, user_responses, time_spent)
        return jsonify({"status": "success", "result": res})
    except Exception as e:
        return jsonify({"status": "error", "message": f"Grading error: {e}"}), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)

