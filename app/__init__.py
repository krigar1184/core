from tornado.web import Application
from tornado.ioloop import IOLoop
from config import HTTP_CLIENT_USED
from .handlers import ServiceHandler
from .http import WebClient


http_client = WebClient(HTTP_CLIENT_USED)


def main():
    app = Application([
        (r'/fetch', ServiceHandler),
    ])

    app.listen(5000)
    IOLoop.current().start()
