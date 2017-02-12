from tornado.web import RequestHandler


class ServiceHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.get_query_argument('qwe'))
        self.write('')
