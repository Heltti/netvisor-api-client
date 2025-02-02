"""
netvisor.requestmodels.product
~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from marshmallow import ValidationError

from ..exc import InvalidData
from ..responsemodels.products import (
    CreateProductResponse,
    GetProductResponse,
    ProductListResponse,
    UpdateProductResponse,
)
from ..schemas.products import CreateProductSchema
from .base import ListRequest, Request


class GetProductRequest(Request):
    method = "GET"
    uri = "GetProduct.nv"
    response_cls = GetProductResponse

    def _raise_validation_error(self):
        raise InvalidData(
            "Data form incorrect:. "
            "Product not found with Netvisor identifier: {0}".format(self.params["id"])
        )

    def parse_response(self, response):
        try:
            result = super(GetProductRequest, self).parse_response(response)

            if not result:
                self._raise_validation_error()

            return result

        except ValidationError:
            self._raise_validation_error()


class CreateProductRequest(Request):
    method = "POST"
    uri = "Product.nv"
    response_cls = CreateProductResponse
    schema_cls = CreateProductSchema
    tag_name = "product"


class ProductListRequest(ListRequest):
    method = "GET"
    uri = "ProductList.nv"
    response_cls = ProductListResponse


class UpdateProductRequest(Request):
    method = "POST"
    uri = "Product.nv"
    response_cls = UpdateProductResponse
    schema_cls = CreateProductSchema
    tag_name = "product"
