"""
    netvisor.services.product
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.product import GetProductRequest, ProductListRequest, CreateProductRequest


class ProductService(Service):
    def get(self, id):
        request = GetProductRequest(self.client, params={'id': id})

        return request.make_request()

    def list(self):
        request = ProductListRequest(self.client)

        return request.make_request()

    def create(self, data):
        request = CreateProductRequest(
            self.client,
            params={'method': 'add'},
            data=data
        )

        return request.make_request()

    def update(self, id, data):
        request = CreateProductRequest(
            self.client,
            params={'id': id, 'method': 'edit'},
            data=data
        )

        return request.make_request()