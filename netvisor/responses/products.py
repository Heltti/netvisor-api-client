"""
    netvisor.responses.products
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Response
from ..schemas import GetProductSchema, ProductListSchema


class ProductListResponse(Response):
    schema_cls = ProductListSchema
    tag_name = 'product_list'


class GetProductResponse(Response):
    schema_cls = GetProductSchema
    tag_name = 'product'
