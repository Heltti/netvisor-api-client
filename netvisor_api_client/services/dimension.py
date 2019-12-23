from .base import Service
from ..requests.dimension import CreateDimensionsRequest, ListDimensionsRequest


class DimensionService(Service):
    def create(self, data):
        request = CreateDimensionsRequest(
            self.client,
            params={'method': 'add'},
            data=data
        )

        return request.make_request()

    def list(self, query=None):
        request = ListDimensionsRequest(self.client, params={'Keyword': query})

        return request.make_request()