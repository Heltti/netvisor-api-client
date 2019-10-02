"""
    netvisor.services.product
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.product import GetProductRequest, ProductListRequest


class ProductService(Service):
    def get(self, id):
        request = GetProductRequest(self.client, params={'id': id})

        return request.make_request()

    def list(self):
        request = ProductListRequest(self.client)
        return request.make_request()
