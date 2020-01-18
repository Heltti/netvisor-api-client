from marshmallow import Schema, fields, post_load
from ..fields import Decimal, FinnishDate, List


from marshmallow import Schema, fields, post_load, post_dump
from ..common import RejectUnknownFieldsSchema
from ..fields import Decimal, FinnishDate, List


class VatPercentageSchema(RejectUnknownFieldsSchema):
    percentage = Decimal()
    code = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['percentage'],
            '@vatcode': data['code']
        }


class AccountingDimensionSchema(Schema):
    dimension = fields.String()
    type = fields.String()

    @post_dump()
    def post_dump(self, data):
        return {
            'text': data['dimension'],
            '@type': data['type']
        }


class DimensionSchema(Schema):
    name = fields.String(load_from='dimension_name')
    item = fields.String(load_from='dimension_item')


class VoucherLineSchema(Schema):
    line_sum = Decimal()
    description = fields.String(allow_none=True)
    account_number = fields.Integer()
    vat_percent = fields.Nested(VatPercentageSchema)
    account_dimension = fields.Nested(AccountingDimensionSchema)
    dimensions = List(
        fields.Nested(DimensionSchema),
        load_from='dimension',
        missing=list
    )


class AccountingAttachmentLineSchema(RejectUnknownFieldsSchema):
    mime_type = fields.String()
    attachment_description = fields.String(attribute='description')
    filename = fields.String(attribute='filename')
    document_data = fields.String(attribute='data')


class AccountingVoucherSchema(Schema):
    mode = fields.String(load_from='calculation_mode')
    date = FinnishDate(load_from='voucher_date')
    number = fields.Integer(load_from='voucher_number')
    description = fields.String(
        load_from='voucher_description',
        allow_none=True
    )
    class_ = fields.String(attribute='class', load_from='voucher_class')
    lines = List(
        fields.Nested(VoucherLineSchema),
        load_from='voucher_line',
        missing=list
    )
    attachments = List(
        fields.Nested(AccountingAttachmentLineSchema),
        load_from='voucher_attachments',
        missing=list
    )