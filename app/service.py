from app import http_client


class Service:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port

    @property
    def fetch_url(self):
        return 'http://%s:%s/fetch' % (self.host, self.port)

    @property
    def check_url(self):
        return 'http://%s:%s/check' % (self.host, self.port)

    @property
    def is_available(self):
        # TODO mock HTTP-request to check_url
        # TODO move http client initialization somewhere else
        return http_client.request(self.check_url)
