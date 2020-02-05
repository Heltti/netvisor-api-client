from marshmallow import Schema, fields, post_load

from ..common import DateSchema, DecimalSchema
from ..fields import Boolean, Decimal, List


class PurchaseInvoiceLineSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisorkey")
    line_sum = Decimal()
    line_net_sum = Decimal()
    unit_price = Decimal()
    vat_percent = Decimal()
    vat_code = fields.String()
    description = fields.String()
    unit = fields.String()
    ordered_amount = Decimal()
    purchase_price = Decimal(allow_none=True)
    delivered_amount = Decimal()
    product_code = fields.String()
    discount_percentage = Decimal()
    product_name = fields.String()
    bookkeeping_account_netvisor_key = fields.String(load_from='accounting_suggestion_bookkeeping_account_netvisor_key')
    bookkeeping_account = fields.String(load_from='accounting_suggestion_bookkeeping_account')


class PurchaseInvoiceDimensionSchema(Schema):
    """
    Levels 4 -5 -6 when version parameter is2
    In other case levels 3-4-5
    """
    name = fields.String(load_from='dimension_name')
    netvisor_key = fields.Integer(load_from='dimension_name_netvisor_key')  # Not in documentation
    detail_name = fields.String(load_from='dimension_detail_name')
    detail_netvisor_key = fields.Integer(load_from='dimension_detail_netvisor_key') # Not in documentation


class InvoiceDimensionLineSchema(Schema):
    dimensions = List(
        fields.Nested(PurchaseInvoiceDimensionSchema),
        load_from='dimension',
        required=False
    )

    @post_load
    def preprocess_dimension_list(self, input_data):
        if input_data:
            return input_data['dimensions']


class InvoiceLineSchema(Schema):
    items = List(
        fields.Nested(PurchaseInvoiceLineSchema),
        load_from='purchase_invoice_line'
    )

    dimensions = fields.Nested(InvoiceDimensionLineSchema,
                               load_from='purchase_invoice_line_dimensions')


class GetPurchaseInvoiceSchema(Schema):
    netvisor_key = fields.Integer(load_from='purchase_invoice_netvisor_key')
    number = fields.Integer(load_from='purchase_invoice_number')
    date = fields.Nested(DateSchema, load_from='purchase_invoice_date')
    delivery_date = fields.Nested(DateSchema, load_from='purchase_invoice_delivery_date')
    due_date = fields.Nested(DateSchema, load_from='purchase_invoice_due_date')
    value_date = fields.Nested(DateSchema, load_from='purchase_invoice_value_date')
    reference_number = fields.String(load_from='purchase_invoice_referencenumber')
    amount = fields.Nested(DecimalSchema(), load_from='purchase_invoice_amount')
    paid_amount = fields.Nested(DecimalSchema(), load_from='purchase_invoice_paid_amount')
    foreign_currency_amount = fields.Nested(DecimalSchema())
    foreign_currency_name_id = fields.String()
    status = fields.String(load_from='invoice_status')
    approval_status = fields.String()
    our_reference = fields.String(allow_none=True, load_from='purchase_invoice_our_reference')
    your_reference = fields.String(allow_none=True, load_from='purchase_invoice_your_reference')
    description = fields.String(allow_none=True, load_from='purchase_invoice_description')
    vendor_name = fields.String()
    vendor_addressline = fields.String(allow_none=True)
    vendor_postnumber = fields.String(allow_none=True)
    vendor_town = fields.String(allow_none=True)
    vendor_country = fields.String(allow_none=True)
    vendor_bank_account_number = fields.String(allow_none=True)
    voucher_id = fields.Integer(allow_none=True)
    accounted = fields.Boolean(load_from='is_accounted')
    comment = fields.String()
    lines = fields.Nested(InvoiceLineSchema, load_from='invoice_lines')


    @post_load
    def preprocess_lines(self, data):
        if 'lines' in data:
            data['lines'] = data['lines']
