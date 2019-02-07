"""
    netvisor.requests.sales_invoice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Request
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

    def parse_response(self, response):
        data = super(GetSalesInvoiceRequest, self).parse_response(response)
        self.ensure_not_empty(data)
        return data

    def ensure_not_empty(self, data):
        if data is None:
            raise InvalidData(
                'Data form incorrect:. '
                'Sales invoice not found with Netvisor identifier: {0}'.format(
                    self.params['NetvisorKey']
                )
            )


class SalesInvoiceListRequest(Request):
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
