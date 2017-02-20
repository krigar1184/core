from tornado.web import RequestHandler


class FetchHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('fetch')


class CheckHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('check')
