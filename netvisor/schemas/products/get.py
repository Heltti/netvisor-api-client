"""
    netvisor.schemas.products.get
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..fields import Decimal


class UnitPriceSchema(Schema):
    amount = Decimal(load_from='#text')
    type = fields.String(load_from='@type')


class ProductBaseInformationSchema(Schema):
    netvisor_key = fields.Integer()
    name = fields.String()
    product_code = fields.String(allow_none=True)
    product_group = fields.String(allow_none=True)
    description = fields.String(allow_none=True)
    tariff_heading = fields.String(allow_none=True)
    is_active = fields.Boolean()
    is_sales_product = fields.Boolean(allow_none=True)
    comission_percentage = Decimal(allow_none=True)
    purchase_price = Decimal(allow_none=True)
    unit_price = fields.Nested(UnitPriceSchema)
    unit = fields.String(allow_none=True)
    unit_weight = Decimal(allow_none=True)


class ProductInventoryDetailsSchema(Schema):
    inventory_amount = Decimal()
    inventory_mid_price = Decimal()
    inventory_value = Decimal()
    inventory_reserved_amount = Decimal()
    inventory_ordered_amount = Decimal()


class ProductBookKeepingDetailsSchema(Schema):
    default_domestic_account_number = fields.String()
    default_eu_account_number = fields.String()
    default_outside_eu_account_number = fields.String()
    default_vat_percent = Decimal()


class GetProductSchema(Schema):
    product_base_information = fields.Nested(ProductBaseInformationSchema)
    product_book_keeping_details = fields.Nested(
        ProductBookKeepingDetailsSchema
    )
    product_inventory_details = fields.Nested(ProductInventoryDetailsSchema)
