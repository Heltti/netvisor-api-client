from ..requestmodels.dimension import CreateDimensionsRequest, DimensionsListRequest
from .base import Service


class DimensionService(Service):
    def create(self, data):
        request = CreateDimensionsRequest(
            self.client, params={"method": "add"}, data=data
        )

        return request.make_request()

    def list(self, showhidden=None):
        request = DimensionsListRequest(self.client, params={"showhidden": showhidden})

        return request.make_request()
