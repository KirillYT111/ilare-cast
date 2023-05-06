import yaml
from http.server import HTTPServer, BaseHTTPRequestHandler
print("[IMPORT] Импортирование конфигурации...")
with open('config.yml') as file:
        prime_service = yaml.safe_load(file)
        country = prime_service["country"]
        streamport = prime_service["port"]
        maxclients = prime_service["clients"]
        maxsources = prime_service["sources"]
        streampass = prime_service["password"]
        adminpass = prime_service["admin"]

print("[LOAD] Запуск сервера в регеоне", country, "\n[INFO] Порт сервера", streamport)

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    #
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'html')
        self.end_headers()
        self.send_error(403)
#
httpd = HTTPServer(('localhost', streamport), SimpleHTTPRequestHandler)
print("[SERVER] Сервер запущен")
httpd.serve_forever()
