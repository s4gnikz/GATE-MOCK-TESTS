#!/usr/bin/env python3
"""
Launcher script for the GATE CS 2027 Mock Test Portal.
Starts the portal web server and opens the student portal in your default web browser.
"""
import socket
import sys
import threading
import time
import webbrowser
from pathlib import Path

# Add project root to path
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import portal_server


def find_free_port(start_port: int = 8000) -> int:
    """Find an available TCP port starting from start_port."""
    for port in range(start_port, start_port + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    return start_port


def open_browser_delayed(url: str, delay: float = 1.0):
    """Open user browser after server has started."""
    time.sleep(delay)
    print(f"[*] Opening GATE 2027 Portal in your web browser: {url}")
    webbrowser.open(url)


def main():
    port = find_free_port(8000)
    url = f"http://localhost:{port}"

    # Launch browser in a background thread
    threading.Thread(target=open_browser_delayed, args=(url,), daemon=True).start()

    # Run the portal server
    portal_server.run_server(port=port, host="127.0.0.1")


if __name__ == "__main__":
    main()

