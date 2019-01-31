#!/usr/bin/python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from threading import Thread


PORT = 2222

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Handler on port 2222, path :: {}".format(self.path))

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
  pass

def serve_on_port(port):
  server = ThreadingHTTPServer(("localhost", port), Handler)
  server.serve_forever()

httpd=Thread(target=serve_on_port, args=[PORT]).start()
print('Server start on localhost on port {}'.format(PORT))
