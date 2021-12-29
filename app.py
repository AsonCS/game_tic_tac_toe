# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from Controller import Controller

hostName = "192.168.0.118"
serverPort = 5000

class AppServer(BaseHTTPRequestHandler):

	def do_GET(self):
		controller = Controller(self.path)
		if (controller.type == Controller.PATH_TO_STATIC):
			self.send_file(controller.path)
			return
		
		code, html = controller.load_game()

		self.send_response(code)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		for line in html:
			self.wfile.write(bytes(line, "utf-8"))
	

	def send_file(self, path: 'str'):
		try:
			path = path[1:]
			self.send_response(200)
			# self.send_header("", "")
			self.end_headers()
			f = open(path)
			text = f.read()
			for line in text:
				self.wfile.write(bytes(line, "utf-8"))
			f.close()
		except:
			return


if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), AppServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
