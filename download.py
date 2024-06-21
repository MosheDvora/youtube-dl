import json
import subprocess
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url = self.path.split('url=')[1] if 'url=' in self.path else None
        if not url:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': 'No URL provided'}).encode())
            return

        try:
            result = subprocess.run(['youtube-dl', '--no-playlist', '-f', 'best', '--get-url', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            download_url = result.stdout.strip()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'downloadUrl': download_url}).encode())
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'success': False, 'error': str(e)}).encode())
