import socketserver
from pathlib import Path

import http.server

PORT = 80
DIRECTORY = Path(__file__).resolve().parent  # folder di samping file ini

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving {DIRECTORY} at http://0.0.0.0:{PORT}")
    httpd.serve_forever()