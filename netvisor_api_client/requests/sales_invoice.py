"""
    netvisor.requests.sales_invoice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import ValidationError

from .base import Request, ListRequest
from ..exc import InvalidData
from ..responses.sales_invoices import (
    CreateSalesInvoiceResponse,
    GetSalesInvoiceResponse,
    SalesInvoiceListResponse,
    UpdateSalesInvoiceResponse
)
from ..schemas import CreateSalesInvoiceSchema


class GetSalesInvoiceRequest(Request):
    method = 'GET'
    uri = 'GetSalesInvoice.nv'
    response_cls = GetSalesInvoiceResponse

    def _raise_exception(self):
        raise InvalidData(
            'Data form incorrect:. '
            'Sales invoice not found with Netvisor identifier: {0}'.format(
                self.params['NetvisorKey']
            )
        )

    def parse_response(self, response):
        try:
            result = super(GetSalesInvoiceRequest, self).parse_response(response=response)

            if not result:
                self._raise_exception()

            return result

        except ValidationError:
            self._raise_exception()


class SalesInvoiceListRequest(ListRequest):
    method = 'GET'
    uri = 'SalesInvoiceList.nv'
    response_cls = SalesInvoiceListResponse


class CreateSalesInvoiceRequest(Request):
    method = 'POST'
    uri = 'salesinvoice.nv'
    response_cls = CreateSalesInvoiceResponse
    schema_cls = CreateSalesInvoiceSchema
    tag_name = 'sales_invoice'


class UpdateSalesInvoiceRequest(Request):
    method = 'POST'
    uri = 'salesinvoice.nv'
    response_cls = UpdateSalesInvoiceResponse
    schema_cls = CreateSalesInvoiceSchema
    tag_name = 'sales_invoice'
