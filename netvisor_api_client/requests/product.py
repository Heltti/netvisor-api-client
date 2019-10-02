"""
    netvisor.requests.product
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import ValidationError

from .base import Request, ListRequest
from ..exc import InvalidData
from ..responses.products import GetProductResponse, ProductListResponse


class GetProductRequest(Request):
    method = 'GET'
    uri = 'GetProduct.nv'
    response_cls = GetProductResponse

    def _raise_validation_error(self):
        raise InvalidData(
            'Data form incorrect:. '
            'Product not found with Netvisor identifier: {0}'.format(
                self.params['id']
            )
        )

    def parse_response(self, response):
        try:
            result = super(GetProductRequest, self).parse_response(response)

            if not result:
                self._raise_validation_error()

            return result

        except ValidationError:
            self._raise_validation_error()


class ProductListRequest(ListRequest):
    method = 'GET'
    uri = 'ProductList.nv'
    response_cls = ProductListResponse
