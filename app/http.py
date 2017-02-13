from tornado.httpclient import HTTPError
from contextlib import contextmanager


class WebClient:
    def __init__(self, client_class):
        self._client_class = client_class

    def request(self, url):
        return self._make_async_request(url)

    def _handle_response(response):
        if response.error:
            print('Error', response.error)
        else:
            print(response.body)

    def _make_async_request(self, url):
        with self._create_client_instance() as c:
            import ipdb;ipdb.set_trace(context=5)
            c.fetch(url, self._handle_response)

    def _make_request(self, url):
        with self._create_client_instance() as c:
            response = c.fetch(url)
            self._handle_response(response)

    @contextmanager
    def _create_client_instance(self):
        http_client = self._client_class()
        try:
            yield http_client
        except HTTPError as e:
            print('HTTP error: %s' % str(e))
        except Exception as e:
            print('Unknown error: %s' % str(e))
        finally:
            http_client.close()
