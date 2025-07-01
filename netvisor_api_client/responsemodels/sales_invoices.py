"""
netvisor.responsemodels.sales_invoices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..schemas import (
    GetSalesInvoiceListSchema,
    GetSalesInvoiceSchema,
    RepliesSchema,
    SalesInvoiceListSchema,
)
from .base import Response


class SalesInvoiceListResponse(Response):
    schema_cls = SalesInvoiceListSchema
    tag_name = "sales_invoice_list"


class GetSalesInvoiceResponse(Response):
    schema_cls = GetSalesInvoiceSchema
    tag_name = "sales_invoice"


class GetSalesInvoiceListResponse(Response):
    schema_cls = GetSalesInvoiceListSchema
    tag_name = "sales_invoices"


class CreateSalesInvoiceResponse(Response):
    schema_cls = RepliesSchema
    tag_name = "replies"


class UpdateSalesInvoiceResponse(Response):
    schema_cls = None
    tag_name = None


class UpdateSalesInvoiceStatusResponse(Response):
    schema_cls = None
    tag_name = None


class MatchCreditNoteResponse(Response):
    schema_cls = None
    tag_name = None


class SalesInvoiceMatchCreditNoteSchema(Response):
    schema_cls = None
    tag_name = None
