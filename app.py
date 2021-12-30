import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import path as os_path

from Controller import Controller

DIRECTORY = os_path.abspath(__file__)[:-6]
HOST_NAME = 'localhost'
SERVER_PORT = 5000


class AppServer(BaseHTTPRequestHandler):

    # noinspection PyPep8Naming
    def do_GET(self):
        controller = Controller(self.path, DIRECTORY)
        if controller.type == Controller.PATH_TO_STATIC:
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
            f = open(f'{DIRECTORY}{path}')
            text = f.read()
            for line in text:
                self.wfile.write(bytes(line, "utf-8"))
            f.close()
        except Exception as e:
            print('send_file', e)
            return


def init():
    web_server = HTTPServer((HOST_NAME, SERVER_PORT), AppServer)
    print(f'Server started http://{HOST_NAME}:{SERVER_PORT}')
    try:
        web_server.serve_forever()
    except Exception as e:
        print(e)

    web_server.server_close()
    print('init', "Server stopped.")


def load_ip_address() -> 'str':
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    except Exception as e:
        print('load_ip_address', e)
        return HOST_NAME


# noinspection PyRedeclaration
HOST_NAME = load_ip_address()
if __name__ == "__main__":
    init()
