from marshmallow import Schema, fields, post_load

from ..common import DateSchema, DecimalSchema, StringSchema
from ..fields import Boolean, Decimal, List


class VatPercentageSchema(Schema):
    percentage = Decimal(required=True, load_from='#text')
    code = fields.String(required=True, load_from='@vatcode')


class PurchaseInvoiceLineSchema(Schema):
    name = fields.String(load_from='product_name')
    identifier = fields.Nested(
        StringSchema,
        load_from='product_code'
    )
    unit_price = Decimal(load_from='unit_price')
    order_amount = Decimal(load_from='order_amount')
    discount_percentage = Decimal(
        load_from='discount_percentage'
    )
    accounting_account_suggestion = fields.String(allow_none=True)
    line_sum = Decimal(load_from='line_sum')
    vat_percentage = fields.Nested(
        VatPercentageSchema,
        load_from='vat_percent'
    )


class InvoiceLineSchema(Schema):
    product_lines = List(
        fields.Nested(PurchaseInvoiceLineSchema),
        load_from='purchase_invoice_line'
    )

    @post_load
    def preprocess_invoice_line(self, input_data):
        if input_data:
            return input_data['product_lines']


class InvoiceLinesSchema(Schema):
    invoice_line = fields.Nested(InvoiceLineSchema)

    @post_load
    def preprocess_invoice_lines(self, input_data):
        if input_data:
            return input_data['invoice_line']


class GetPurchaseInvoice(Schema):
    number = fields.Integer(
        required=True,
        load_from='purchase_invoice_number'
    )
    date = fields.Nested(
        DateSchema,
        required=True,
        load_from='purchase_invoice_date'
    )
    delivery_date = fields.Nested(
        DateSchema,
        required=True,
        load_from='purchase_invoice_delivery_date'
    )
    due_date = fields.Nested(
        DateSchema,
        required=True,
        load_from='purchase_invoice_due_date'
    )
    value_date = fields.Nested(
        DateSchema,
        required=True,
        load_from='purchase_invoice_value_date'
    )
    reference_number = fields.String(
        required=True,
        load_from='purchase_invoice_reference_number'
    )
    amount = fields.Nested(
        DecimalSchema(),
        required=True,
        load_from='purchase_invoice_amount'
    )
    paid_amount = fields.Nested(
        DecimalSchema(),
        required=True,
        load_from='purchase_invoice_paid_amount'
    )
    foreign_currency_amount = fields.Nested(
        DecimalSchema(),
        required=False,
        load_from='foreign_currency_amount'
    )
    currency_name_id = fields.String(
        required=False,
        load_from='foreign_currecy_name_id'
    )
    status = fields.String(
        required=True,
        load_from='invoice_status' # Currently returns always 'Open'
    )
    our_reference = fields.String(
        required=True,
        load_from='purchase_invoice_our_reference'
    )
    your_reference = fields.String(
        required=False, # ?
        load_from='purchase_invoice_your_reference'
    )
    description = fields.String(
        required=False,
        load_from='purchase_invoice_description'
    )
    vendor_name