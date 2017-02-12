from tornado.web import Application
from tornado.ioloop import IOLoop
from .handlers import ServiceHandler


def main():
    app = Application([
        (r'/fetch', ServiceHandler),
    ])

    app.listen(5000)
    IOLoop.current().start()
