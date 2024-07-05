#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from socketserver import ThreadingMixIn
import threading

hostName = "0.0.0.0"
serverPort = 80

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # curl http://<ServerIP>/index.html
        if self.path == "/":
            # Respond with the file contents.
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            content = open('ncsi.txt', 'rb').read()
            self.wfile.write(content)
            
            return
        
        if self.path == "/generate_204":
            self.send_response(204)
            self.end_headers()

            return
        
        self.send_response(404)
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  """Handle requests in a separate thread."""

if __name__ == "__main__":
  webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
  print("Server started http://%s:%s" % (hostName, serverPort))

  try:
      webServer.serve_forever()
  except KeyboardInterrupt:
      pass

  webServer.server_close()
  print("Server stopped.")