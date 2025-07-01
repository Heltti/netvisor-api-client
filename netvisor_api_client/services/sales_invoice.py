"""
netvisor.services.sales_invoice
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..requestmodels.sales_invoice import (
    CreateSalesInvoiceRequest,
    GetSalesInvoiceListRequest,
    GetSalesInvoiceRequest,
    MatchCreditNoteRequest,
    SalesInvoiceListRequest,
    UpdateSalesInvoiceRequest,
    UpdateSalesInvoiceStatusRequest,
)
from .base import Service


class SalesInvoiceService(Service):
    def get(self, id: int):
        request = GetSalesInvoiceRequest(self.client, params={"NetvisorKey": id})
        return request.make_request()

    def detail_list(self, id_list: list[int]):
        request = GetSalesInvoiceListRequest(
            self.client, params={"NetvisorKeyList": ",".join(str(id) for id in id_list)}
        )
        return request.make_request()

    def list(
        self,
        status=None,
        above_id=None,
        invoice_number=None,
        start_date=None,
        end_date=None,
    ):
        request = SalesInvoiceListRequest(
            self.client,
            params={
                "InvoicesAboveNetvisorKey": above_id,
                "InvoiceStatus": status,
                "InvoiceNumber": invoice_number,
                "BeginInvoiceDate": start_date,
                "EndInvoiceDate": end_date,
            },
        )
        return request.make_request()

    def create(self, data):
        request = CreateSalesInvoiceRequest(
            self.client, params={"method": "add"}, data=data
        )
        return request.make_request()

    def update(self, id, data):
        request = UpdateSalesInvoiceRequest(
            self.client, params={"id": id, "method": "edit"}, data=data
        )
        return request.make_request()

    def update_status(self, id, netvisor_status):
        request = UpdateSalesInvoiceStatusRequest(
            self.client,
            params={"netvisorkey": id, "status": netvisor_status},
        )
        return request.make_request()

    def match_credit_note(self, data):
        request = MatchCreditNoteRequest(
            self.client,
            data=data,
        )
        return request.make_request()
