"""
    netvisor.schemas.sales_invoices.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load, pre_load

from ..common import DateSchema
from ..fields import Decimal, List


class StatusSchema(Schema):
    status = fields.String(load_from='#text')
    substatus = fields.String(allow_none=True, load_from='@substatus')

    @pre_load
    def pre_load(self, data):
        if isinstance(data, (str,)):
            return {
                '#text': data,
                '@substatus': None
            }
        else:
            return data


class PurchaseInvoiceSchema(Schema):
    netvisor_key = fields.Integer()
    number = fields.Integer(load_from='invoice_number')
    date = fields.Nested(DateSchema, load_from='invoicedate')
    vendor = fields.String()
    #payments = fields.Integer()
    sum = Decimal(load_from='invoice_sum')
    open_sum = Decimal(load_from='open_sum')

    @post_load
    def preprocess_sales_invoice(self, input_data):
        input_data.update(input_data['status'])
        return input_data


class PurchaseInvoiceListSchema(Schema):
    sales_invoices = List(
        fields.Nested(PurchaseInvoiceSchema),
        load_from='sales_invoice'
    )

    @post_load
    def preprocess_sales_invoice_list(self, input_data):
        return input_data['sales_invoices'] if input_data else []
