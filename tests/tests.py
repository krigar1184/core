import unittest
from .factories import ServiceFactory


class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_service(self):
        s = ServiceFactory.create()
        self.assertEqual('http://localhost:1234/check', s.check_url)
        self.assertEqual('http://localhost:1234/fetch', s.fetch_url)

    def test_is_service_available(self):
        s = ServiceFactory.create()
        self.assertFalse(s.is_available)
