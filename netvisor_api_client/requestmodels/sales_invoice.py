"""
netvisor.requestmodels.sales_invoice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from marshmallow import ValidationError

from ..exc import InvalidData
from ..responsemodels.sales_invoices import (
    CreateSalesInvoiceResponse,
    GetSalesInvoiceListResponse,
    GetSalesInvoiceResponse,
    MatchCreditNoteResponse,
    SalesInvoiceListResponse,
    SalesInvoiceMatchCreditNoteSchema,
    UpdateSalesInvoiceResponse,
    UpdateSalesInvoiceStatusResponse,
)
from ..schemas import CreateSalesInvoiceSchema
from .base import ListRequest, Request


class GetSalesInvoiceRequest(Request):
    method = "GET"
    uri = "GetSalesInvoice.nv"
    response_cls = GetSalesInvoiceResponse

    def _raise_exception(self):
        raise InvalidData(
            "Data form incorrect:. "
            "Sales invoice not found with Netvisor identifier: {0}".format(
                self.params["NetvisorKey"]
            )
        )

    def parse_response(self, response):
        try:
            result = super(GetSalesInvoiceRequest, self).parse_response(
                response=response
            )

            if not result:
                self._raise_exception()

            return result

        except ValidationError:
            self._raise_exception()


class GetSalesInvoiceListRequest(Request):
    method = "GET"
    uri = "GetSalesInvoice.nv"
    response_cls = GetSalesInvoiceListResponse


class SalesInvoiceListRequest(ListRequest):
    method = "GET"
    uri = "SalesInvoiceList.nv"
    response_cls = SalesInvoiceListResponse


class CreateSalesInvoiceRequest(Request):
    method = "POST"
    uri = "salesinvoice.nv"
    response_cls = CreateSalesInvoiceResponse
    schema_cls = CreateSalesInvoiceSchema
    tag_name = "sales_invoice"


class UpdateSalesInvoiceRequest(Request):
    method = "POST"
    uri = "salesinvoice.nv"
    response_cls = UpdateSalesInvoiceResponse
    schema_cls = CreateSalesInvoiceSchema
    tag_name = "sales_invoice"


class UpdateSalesInvoiceStatusRequest(Request):
    method = "POST"
    uri = "updatesalesinvoicestatus.nv"
    response_cls = UpdateSalesInvoiceStatusResponse


class MatchCreditNoteRequest(Request):
    method = "POST"
    uri = "matchcreditnote.nv"
    response_cls = MatchCreditNoteResponse
    schema_cls = SalesInvoiceMatchCreditNoteSchema
    tag_name = "match_credit_note"
