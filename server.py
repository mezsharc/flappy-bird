#!/usr/bin/env python3
"""
Tiny local server for the Flappy Bird game.

Usage:
    python server.py [port]

Then open the printed URL in your browser (it will also try to
open it automatically). Press Ctrl+C to stop the server.
"""

import http.server
import socketserver
import sys
import webbrowser
import os

DEFAULT_PORT = 8000


def main():
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Ignoring invalid port '{sys.argv[1]}', using {DEFAULT_PORT}")

    # Serve files from the same directory as this script,
    # so it works regardless of the current working directory.
    web_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(web_dir)

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), handler) as httpd:
        url = f"http://localhost:{port}/index.html"
        print(f"Serving Flappy Bird at {url}")
        print("Press Ctrl+C to stop.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopping server.")
            httpd.shutdown()


if __name__ == "__main__":
    main()
