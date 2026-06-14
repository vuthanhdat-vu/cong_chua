import http.server
import socketserver
import webbrowser

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

class MyHTTPServer(socketserver.TCPServer):
    allow_reuse_address = True

print(f"Starting server on http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")

# Automatically open the browser
webbrowser.open(f"http://localhost:{PORT}")

with MyHTTPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
