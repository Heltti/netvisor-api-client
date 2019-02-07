"""
    netvisor.schemas.products.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load

from ..fields import Decimal, List


class ProductSchema(Schema):
    netvisor_key = fields.Integer()
    name = fields.String()
    product_code = fields.String(allow_none=True)
    unit_price = Decimal()


class ProductListSchema(Schema):
    products = List(fields.Nested(ProductSchema), load_from='product')

    @post_load
    def preprocess_product_list(self, input_data):
        return input_data['products'] if input_data else []
