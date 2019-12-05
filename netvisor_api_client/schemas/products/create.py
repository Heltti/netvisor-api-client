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
    unit_price = fields.Nested(UnitPriceSchema, attribute='unit_price')
    unit = fields.String()
    purchase_price = fields.Decimal()
    tariff_heading = fields.String()
    comission_percentage = fields.Decimal()
    is_active = Boolean(true='1', false='0')
    is_sales_product = Boolean(true='1', false='0')
    inventory_enabled = Boolean(true='1', false='0')
    country_of_origin = fields.String()

    class Meta:
        ordered = True


class ProductBookKeepingDetailsSchema(RejectUnknownFieldsSchema):
    default_vat_percentage = Decimal()

    class Meta:
        ordered = True


class ProductAdditionalInformationSchema(RejectUnknownFieldsSchema):
    product_net_weight = fields.Decimal()
    product_gross_weight = fields.Decimal()
    product_weight_unit = fields.Decimal()


class ProductPackageInformation(RejectUnknownFieldsSchema):
    package_width = fields.Decimal()
    package_height = fields.Decimal()
    package_length = fields.Decimal()


class CreateProductSchema(RejectUnknownFieldsSchema):
    product_base_information = fields.Nested(ProductBaseInformationSchema)
    product_book_keeping_details = fields.Nested(
        ProductBookKeepingDetailsSchema
    )
    product_additional_information = fields.Nested(ProductAdditionalInformationSchema)
    product_package_information = fields.Nested(ProductPackageInformation)

    class Meta:
        ordered = True