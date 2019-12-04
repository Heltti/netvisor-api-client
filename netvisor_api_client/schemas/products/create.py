from marshmallow import Schema, fields
from ..common import RejectUnknownFieldsSchema

from ..fields import Decimal

# Tarkista kaikki fieldit


class UnitPriceSchema(Schema):
    amount = Decimal(load_from='#text')
    type = fields.String(load_from='@type')


class ProductBaseInformationSchema(RejectUnknownFieldsSchema):
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


class ProductBookKeepingDetailsSchema(Schema):
    default_domestic_account_number = fields.String()
    default_eu_account_number = fields.String()
    default_outside_eu_account_number = fields.String()
    default_vat_percent = Decimal()


class CreateProductSchema(RejectUnknownFieldsSchema):
    product_base_information = fields.Nested(ProductBaseInformationSchema)
    product_book_keeping_details = fields.Nested(
        ProductBookKeepingDetailsSchema
    )