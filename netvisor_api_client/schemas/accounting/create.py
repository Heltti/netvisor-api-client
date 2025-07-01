from marshmallow import fields, post_dump

from ..common import RejectUnknownFieldsSchema
from ..fields import Decimal, FinnishDate, List


class VatPercentageSchema(RejectUnknownFieldsSchema):
    percentage = Decimal()
    code = fields.String()

    @post_dump
    def post_dump(self, data):
        return {"#text": data["percentage"], "@vatcode": data["code"]}


class AccountingDimensionSchema(RejectUnknownFieldsSchema):
    dimension = fields.String()
    type = fields.String()

    @post_dump()
    def post_dump(self, data):
        return {"#text": data["dimension"], "@type": data["type"]}


class LineSumSchema(RejectUnknownFieldsSchema):
    sum = Decimal()
    type = fields.String()

    @post_dump
    def post_dump(self, data):
        return {"#text": data["sum"], "@type": data["type"]}


class DimensionSchema(RejectUnknownFieldsSchema):
    dimension_name = fields.String(attribute="name")
    dimension_item = fields.String(attribute="item")


class VoucherLineSchema(RejectUnknownFieldsSchema):
    line_sum = fields.Nested(LineSumSchema)
    description = fields.String(allow_none=True)
    account_number = fields.Integer()
    vat_percent = fields.Nested(VatPercentageSchema)
    account_dimension = fields.Nested(AccountingDimensionSchema)
    dimension = fields.Nested(DimensionSchema)

    class Meta:
        ordered = True

    def __setattr__(self, attr, value):
        if attr == "ordered":
            value = True
        super(VoucherLineSchema, self).__setattr__(attr, value)


class AccountingAttachmentLineSchema(RejectUnknownFieldsSchema):
    mime_type = fields.String()
    attachment_description = fields.String(attribute="description")
    filename = fields.String(attribute="filename")
    document_data = fields.String(attribute="data")

    class Meta:
        ordered = True

    def __setattr__(self, attr, value):
        if attr == "ordered":
            value = True
        super(AccountingAttachmentLineSchema, self).__setattr__(attr, value)


class CreateAccountingVoucherSchema(RejectUnknownFieldsSchema):
    calculation_mode = fields.String(attribute="mode")
    voucher_date = FinnishDate(attribute="date")
    voucher_number = fields.Integer(attribute="number")
    description = fields.String(allow_none=True)
    voucher_class = fields.String(attribute="class")
    voucher_line = List(fields.Nested(VoucherLineSchema), default=list)
    voucher_attachments = List(
        fields.Nested(AccountingAttachmentLineSchema),
        default=list,
        attribute="attachments",
    )

    class Meta:
        ordered = True

    @post_dump
    def post_dump(self, data):
        if "voucher_attachments" in data and data["voucher_attachments"]:
            data["voucher_attachments"] = [
                {"voucher_attachment": data["voucher_attachments"]}
            ]
