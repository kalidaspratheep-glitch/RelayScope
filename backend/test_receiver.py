from http.server import BaseHTTPRequestHandler, HTTPServer


class WebhookReceiver(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        print("\n--- Webhook received ---")
        print("Method:", self.command)
        print("Path:", self.path)
        print("Headers:", dict(self.headers))
        print("Body:", body.decode("utf-8", errors="replace"))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Webhook received successfully"}')


server = HTTPServer(("127.0.0.1", 9000), WebhookReceiver)

print("Test receiver running on http://127.0.0.1:9000")
server.serve_forever()