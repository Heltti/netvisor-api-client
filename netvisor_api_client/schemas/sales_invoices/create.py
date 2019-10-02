"""
    netvisor.schemas.sales_invoices.create
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import fields, post_dump

from ..common import RejectUnknownFieldsSchema
from ..fields import Decimal, List


class ProductIdentifierSchema(RejectUnknownFieldsSchema):
    identifier = fields.String()
    type = fields.String(default='netvisor')

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['identifier'],
            '@type': data['type']
        }


class VatPercentageSchema(RejectUnknownFieldsSchema):
    percentage = Decimal()
    code = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['percentage'],
            '@vatcode': data['code']
        }


class UnitPriceSchema(RejectUnknownFieldsSchema):
    amount = Decimal()
    type = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            '#text': data['amount'],
            '@type': data['type']
        }


class SalesInvoiceAttachmentLineSchema(RejectUnknownFieldsSchema):
    mime_type = fields.String()
    attachment_description = fields.String(attribute='description')
    filename = fields.String(attribute='filename')
    document_data = fields.String(attribute='data')
    document_type = fields.String(attribute='type')

    class Meta:
        ordered = True

    def __setattr__(self, attr, value):
        if attr == 'ordered':
            value = True

        super().__setattr__(attr, value)

    @post_dump
    def post_dump(self, data):
        document_data = data['document_data']
        document_type = data["document_type"]

        data['document_data'] = {
            '#text': document_data,
            '@type': document_type
        }

        del data["document_type"]

        return data


class SalesInvoiceProductLineSchema(RejectUnknownFieldsSchema):
    product_identifier = fields.Nested(ProductIdentifierSchema, attribute='identifier', default=dict(identifier=''))
    product_name = fields.String(attribute='name')
    product_unit_price = fields.Nested(UnitPriceSchema, attribute='unit_price')
    product_vat_percentage = fields.Nested(VatPercentageSchema, attribute='vat_percentage')

    sales_invoice_product_line_quantity = Decimal(attribute='quantity')
    sales_invoice_product_line_discount_percentage = Decimal(attribute='discount_percentage')
    sales_invoice_product_line_free_text = fields.String(attribute='free_text')

    accounting_account_suggestion = fields.String()

    class Meta:
        ordered = True

    def __setattr__(self, attr, value):
        if attr == 'ordered':
            value = True
        super(SalesInvoiceProductLineSchema, self).__setattr__(attr, value)


class CreateSalesInvoiceSchema(RejectUnknownFieldsSchema):
    sales_invoice_number = fields.Integer(attribute='number')
    sales_invoice_date = fields.Date(attribute='date')
    sales_invoice_value_date = fields.Date(attribute='value_date')
    sales_invoice_delivery_date = fields.Date(attribute='delivery_date')
    sales_invoice_reference_number = fields.String(attribute='reference_number')
    sales_invoice_amount = Decimal(attribute='amount')
    sales_invoice_amount_currency = fields.String(attribute='currency')

    seller_identifier = fields.String()
    seller_name = fields.String()

    invoice_type = fields.String()

    sales_invoice_status = fields.String(attribute='status')
    sales_invoice_free_text_before_lines = fields.String(attribute='free_text_before_lines')
    sales_invoice_free_text_after_lines = fields.String(attribute='free_text_after_lines')

    sales_invoice_our_reference = fields.String(attribute='our_reference')
    sales_invoice_your_reference = fields.String(attribute='your_reference')
    sales_invoice_private_comment = fields.String(attribute='private_comment')

    invoicing_customer_identifier = fields.String()
    invoicing_customer_name = fields.String()
    invoicing_customer_name_extension = fields.String()
    invoicing_customer_address_line = fields.String()
    invoicing_customer_additional_address_line = fields.String()
    invoicing_customer_post_number = fields.String()
    invoicing_customer_town = fields.String()
    invoicing_customer_country_code = fields.String()

    delivery_address_name = fields.String()
    delivery_address_name_extension = fields.String()
    delivery_address_line = fields.String()
    delivery_address_post_number = fields.String()
    delivery_address_town = fields.String()
    delivery_address_country_code = fields.String()
    delivery_method = fields.String()
    delivery_term = fields.String()

    payment_term_net_days = fields.Integer()
    payment_term_cash_discount_days = fields.Integer()
    payment_term_cash_discount = Decimal()

    invoice_lines = List(fields.Nested(SalesInvoiceProductLineSchema), default=list)

    sales_invoice_attachments = List(fields.Nested(SalesInvoiceAttachmentLineSchema), default=list, attribute="attachments")

    class Meta:
        ordered = True

    @post_dump
    def post_dump(self, data):
        if 'seller_identifier' in data:
            data['seller_identifier'] = {
                '#text': data['seller_identifier'],
                '@type': 'netvisor'
            }

        if 'sales_invoice_status' in data:
            data['sales_invoice_status'] = {
                '#text': data['sales_invoice_status'],
                '@type': 'netvisor'
            }

        if 'sales_invoice_amount_currency' in data:
            data['sales_invoice_amount'] = {
                '#text': data['sales_invoice_amount'],
                '@iso4217currencycode': data['sales_invoice_amount_currency']
            }
            del data['sales_invoice_amount_currency']

        # Only add to data if there are attachments, Netvisor API doesn't like empty lists
        if 'sales_invoice_attachments' in data and data['sales_invoice_attachments']:
            data['sales_invoice_attachments'] = [
                {'sales_invoice_attachment': data['sales_invoice_attachments']}
            ]

        if 'invoicing_customer_identifier' in data:
            data['invoicing_customer_identifier'] = {
                '#text': data['invoicing_customer_identifier'],
                '@type': 'netvisor'
            }

        if 'payment_term_cash_discount' in data:
            data['payment_term_cash_discount'] = {
                '#text': data['payment_term_cash_discount'],
                '@type': 'percentage'
            }

        data['invoice_lines'] = {
            'invoice_line': [
                {'sales_invoice_product_line': line} for line in data['invoice_lines']
            ]
        }

        return data
