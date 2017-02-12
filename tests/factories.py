import factory
from app.service import Service


class ServiceFactory(factory.Factory):
    class Meta:
        model = Service

    host = 'localhost'
    port = '1234'
    name = 'Sample service'
