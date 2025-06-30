from marshmallow import Schema, fields, post_load

from ..common import DateSchema, DecimalSchema
from ..fields import Decimal, List


class PurchaseInvoiceLineSchema(Schema):
    netvisor_key = fields.Integer(required=True, load_from="netvisorkey")
    line_sum = Decimal(required=True, allow_none=True)
    line_net_sum = Decimal(required=True, allow_none=True)
    unit_price = Decimal(required=True, allow_none=True)
    vat_percent = Decimal(required=True, allow_none=True)
    vat_code = fields.String(required=True, allow_none=True)
    description = fields.String(required=True, allow_none=True)
    unit = fields.String(required=True, allow_none=True)
    ordered_amount = Decimal(required=True, allow_none=True)
    purchase_price = Decimal(allow_none=True)
    delivered_amount = Decimal(required=True, allow_none=True)
    product_code = fields.String(required=True, allow_none=True)
    discount_percentage = Decimal(required=True, allow_none=True)
    product_name = fields.String(required=True, allow_none=True)
    bookkeeping_account_netvisor_key = fields.String(
        required=True,
        allow_none=True,
        load_from="accounting_suggestion_bookkeeping_account_netvisor_key",
    )
    bookkeeping_account = fields.String(
        required=True,
        allow_none=True,
        load_from="accounting_suggestion_bookkeeping_account",
    )


class PurchaseInvoiceDimensionSchema(Schema):
    """
    Levels 4 -5 -6 when version parameter is2
    In other case levels 3-4-5
    """

    name = fields.String(required=True, allow_none=True, load_from="dimension_name")
    netvisor_key = fields.Integer(
        required=True, allow_none=True, load_from="dimension_name_netvisor_key"
    )  # Not in documentation
    detail_name = fields.String(
        required=True, allow_none=True, load_from="dimension_detail_name"
    )
    detail_netvisor_key = fields.Integer(
        required=True, allow_none=True, load_from="dimension_detail_netvisor_key"
    )  # Not in documentation


class InvoiceDimensionLineSchema(Schema):
    dimensions = List(
        fields.Nested(PurchaseInvoiceDimensionSchema),
        load_from="dimension",
        required=False,
    )

    @post_load
    def preprocess_dimension_list(self, input_data):
        if input_data:
            return input_data["dimensions"]
        return None


class InvoiceLineSchema(Schema):
    items = List(
        fields.Nested(PurchaseInvoiceLineSchema), load_from="purchase_invoice_line"
    )

    dimensions = fields.Nested(
        InvoiceDimensionLineSchema, load_from="purchase_invoice_line_dimensions"
    )


class PurchaseOrderSchema(Schema):
    number = fields.Integer(required=True, load_from="order_number")
    netvisor_key = fields.Integer(required=True)


class LinkedPurchaseOrdersSchema(Schema):
    purchase_orders = List(
        fields.Nested(PurchaseOrderSchema), load_from="purchase_order"
    )

    @post_load
    def preprocess_order_list(self, input_data):
        if input_data:
            return input_data["purchase_orders"]
        return None


class GetPurchaseInvoiceSchema(Schema):
    netvisor_key = fields.Integer(
        required=True, load_from="purchase_invoice_netvisor_key"
    )
    number = fields.Integer(
        required=True, allow_none=True, load_from="purchase_invoice_number"
    )
    date = fields.Nested(DateSchema, required=True, load_from="purchase_invoice_date")
    delivery_date = fields.Nested(
        DateSchema, required=True, load_from="purchase_invoice_delivery_date"
    )
    due_date = fields.Nested(
        DateSchema, required=True, load_from="purchase_invoice_due_date"
    )
    value_date = fields.Nested(
        DateSchema, required=True, load_from="purchase_invoice_value_date"
    )
    reference_number = fields.String(
        required=True, load_from="purchase_invoice_referencenumber"
    )
    amount = fields.Nested(
        DecimalSchema(), required=True, load_from="purchase_invoice_amount"
    )
    paid_amount = fields.Nested(
        DecimalSchema(),
        required=True,
        allow_none=True,
        load_from="purchase_invoice_paid_amount",
    )
    foreign_currency_amount = fields.Nested(DecimalSchema(), required=True)
    foreign_currency_name_id = fields.String(required=True)
    status = fields.String(required=True, load_from="invoice_status")
    approval_status = fields.String(required=True)
    our_reference = fields.String(
        required=True, allow_none=True, load_from="purchase_invoice_our_reference"
    )
    your_reference = fields.String(
        required=True, allow_none=True, load_from="purchase_invoice_your_reference"
    )
    description = fields.String(
        required=True, allow_none=True, load_from="purchase_invoice_description"
    )
    vendor_name = fields.String(required=True)
    vendor_addressline = fields.String(required=True, allow_none=True)
    vendor_postnumber = fields.String(required=True, allow_none=True)
    vendor_town = fields.String(required=True, allow_none=True)
    vendor_country = fields.String(required=True, allow_none=True)
    vendor_bank_account_number = fields.String(allow_none=True)
    voucher_id = fields.Integer(allow_none=True)
    accounted = fields.Boolean(required=True, allow_none=True, load_from="is_accounted")
    preview_image = fields.String(allow_none=True)
    lines = fields.Nested(InvoiceLineSchema, allow_none=True, load_from="invoice_lines")
    orders = fields.Nested(
        LinkedPurchaseOrdersSchema, allow_none=True, load_from="linked_purchase_orders"
    )

    @post_load
    def preprocess_lines(self, data):
        if "lines" in data:
            data["lines"] = data["lines"]
