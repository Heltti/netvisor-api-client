from marshmallow import Schema, fields, post_dump
from ..common import RejectUnknownFieldsSchema

from ..fields import Decimal, Boolean


class UnitPriceSchema(RejectUnknownFieldsSchema):
    amount = Decimal()
    type = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['amount'],
            '@type': data['type']
        }


class ProductBaseInformationSchema(RejectUnknownFieldsSchema):
    product_code = fields.String()
    product_group = fields.String()
    name = fields.String()
    description = fields.String()
    unit_price = fields.Nested(UnitPriceSchema)
    unit = fields.String()
    purchase_price = Decimal()
    tariff_heading = fields.String()
    comission_percentage = fields.Decimal()
    is_active = Boolean(true='1', false='0')
    is_sales_product = Boolean(true='1', false='0')
    inventory_enabled = Boolean(true='yes', false='no')
    country_of_origin = fields.String()

    class Meta:
        ordered = True


class ProductBookKeepingDetailsSchema(RejectUnknownFieldsSchema):
    default_vat_percentage = Decimal()

    class Meta:
        ordered = True


class ProductAdditionalInformationSchema(RejectUnknownFieldsSchema):
    product_net_weight = Decimal()
    product_gross_weight = Decimal()
    product_weight_unit = fields.String()


class ProductPackageInformation(RejectUnknownFieldsSchema):
    package_width = Decimal()
    package_height = Decimal()
    package_length = Decimal()


class CreateProductSchema(RejectUnknownFieldsSchema):
    product_base_information = fields.Nested(ProductBaseInformationSchema)
    product_book_keeping_details = fields.Nested(
        ProductBookKeepingDetailsSchema
    )
    product_additional_information = fields.Nested(ProductAdditionalInformationSchema)
    product_package_information = fields.Nested(ProductPackageInformation)

    class Meta:
        ordered = True

    @post_dump
    def post_dump(self, data):
        if 'country_of_origin' in data['product_base_information']:
            data['product_base_information']['country_of_origin'] = {
                '#text': data['product_base_information']['country_of_origin'],
                '@type': 'ISO-3166'
            }
        return data
