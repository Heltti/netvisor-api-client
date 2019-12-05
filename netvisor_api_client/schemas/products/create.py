from marshmallow import Schema, fields, post_dump
from ..common import RejectUnknownFieldsSchema

from ..fields import Decimal, Boolean


class UnitPriceSchema(Schema):
    amount = Decimal()
    type = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['amount'],
            '@type': data['type']
        }


class ProductBaseInformationSchema(RejectUnknownFieldsSchema):
    product_code = fields.String(allow_none=True)
    product_group = fields.String(allow_none=True)
    name = fields.String()
    description = fields.String(allow_none=True)
    unit_price = fields.Nested(UnitPriceSchema, attribute='unit_price')
    unit = fields.String(allow_none=True)
    purchase_price = fields.Decimal(allow_none=True)
    tariff_heading = fields.String(allow_none=True)
    comission_percentage = fields.Decimal(allow_none=True)
    is_active = Boolean(true='1', false='0')
    is_sales_product = Boolean(allow_none=True, true='1', false='0')
    inventory_enabled = Boolean(allow_none=True, true='1', false='0')
    country_of_origin = fields.String(allow_none=True)

    class Meta:
        ordered = True


class ProductBookKeepingDetailsSchema(Schema):
    default_vat_percentage = Decimal()


class CreateProductSchema(RejectUnknownFieldsSchema):
    product_base_information = fields.Nested(ProductBaseInformationSchema)
    product_book_keeping_details = fields.Nested(
        ProductBookKeepingDetailsSchema
    )

    class Meta:
        ordered = True