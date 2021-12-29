# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from Controller import Controller

hostName = "192.168.0.118"
serverPort = 5000

class AppServer(BaseHTTPRequestHandler):

	def do_GET(self):
		controller = Controller(self.path)
		if (controller.type == Controller.PATH_TO_STATIC):
			self.__handle_static_path(controller.path)
		elif (controller.type == Controller.PATH_TO_API_GAME):
			self.__handle_api_game_path(controller)
		else:
			self.__handle_default_path(controller)
		
		
	def __handle_api_game_path(self, controller: 'Controller'):
		code, json = controller.load_game_json()

		self.send_response(code)
		self.send_header("Content-type", "application/json")
		self.end_headers()

		for line in json:
			self.wfile.write(bytes(line, "utf-8"))
	

	def __handle_default_path(self, controller: 'Controller'):
		code, html = controller.load_game_html()

		self.send_response(code)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		for line in html:
			self.wfile.write(bytes(line, "utf-8"))


	def __handle_static_path(self, path: 'str'):
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
