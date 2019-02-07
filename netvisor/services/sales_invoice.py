"""
    netvisor.services.sales_invoice
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.sales_invoice import (
    CreateSalesInvoiceRequest,
    GetSalesInvoiceRequest,
    SalesInvoiceListRequest,
    UpdateSalesInvoiceRequest
)


class SalesInvoiceService(Service):
    def get(self, id):
        request = GetSalesInvoiceRequest(
            self.client,
            params={'NetvisorKey': id}
        )
        return request.make_request()

    def list(self, above_id=None, invoice_number=None, start_date=None, end_date=None):
        request = SalesInvoiceListRequest(
            self.client,
            params={
                'InvoicesAboveNetvisorKey': above_id,
                'InvoiceNumber': invoice_number,
                'BeginInvoiceDate': start_date,
                'EndInvoiceDate': end_date,
            }
        )
        return request.make_request()

    def create(self, data):
        request = CreateSalesInvoiceRequest(
            self.client,
            params={'method': 'add'},
            data=data
        )
        return request.make_request()

    def update(self, id, data):
        request = UpdateSalesInvoiceRequest(
            self.client,
            params={'id': id, 'method': 'edit'},
            data=data
        )
        return request.make_request()
