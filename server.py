"""
Server lokal untuk Berita ke Video.
Menjalankan halaman aplikasi dan mengambil isi link berita langsung dari komputer kamu
(tanpa proxy pihak ketiga, jadi tidak diblokir oleh CORS).

Cara pakai:
  1. Pastikan Python 3 sudah terpasang.
  2. Simpan server.py dan berita-ke-video.html di folder yang sama.
  3. Jalankan:  python server.py
  4. Buka di browser: http://127.0.0.1:8000
"""
import http.server
import os
import socketserver
import urllib.parse
import urllib.request

PORT = 8000
HERE = os.path.dirname(os.path.abspath(__file__))
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/124.0 Safari/537.36')


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = urllib.parse.urlparse(self.path)
        if p.path == '/fetch':
            target = urllib.parse.parse_qs(p.query).get('url', [''])[0]
            if not target.startswith(('http://', 'https://')):
                return self._send(400, b'url tidak valid', 'text/plain; charset=utf-8')
            try:
                req = urllib.request.Request(target, headers={
                    'User-Agent': UA,
                    'Accept': 'text/html,application/xhtml+xml',
                    'Accept-Language': 'id,en;q=0.8',
                })
                with urllib.request.urlopen(req, timeout=20) as r:
                    data = r.read()
                    ctype = r.headers.get('Content-Type', 'text/html; charset=utf-8')
                self._send(200, data, ctype)
            except Exception as e:
                self._send(502, ('gagal mengambil: ' + str(e)).encode('utf-8'),
                           'text/plain; charset=utf-8')
        elif p.path in ('/', '/index.html', '/berita-ke-video.html'):
            with open(os.path.join(HERE, 'berita-ke-video.html'), 'rb') as f:
                self._send(200, f.read(), 'text/html; charset=utf-8')
        else:
            self._send(404, b'tidak ditemukan', 'text/plain; charset=utf-8')

    def log_message(self, *args):
        pass


if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(('127.0.0.1', PORT), Handler) as srv:
        print(f'Berita ke Video berjalan di http://127.0.0.1:{PORT}  (Ctrl+C untuk berhenti)')
        srv.serve_forever()
