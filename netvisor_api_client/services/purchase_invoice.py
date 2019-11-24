from .base import Service
from ..requests.purchase_invoice import (
    PurchaseInvoiceListRequest,
    GetPurchaseInvoiceRequest
)


class PurchaseInvoiceService(Service):
    def get(self, id):
        request = GetPurchaseInvoiceRequest(
            self.client,
            params={'NetvisorKey': id}
        )
        return request.make_request()

    def list(self, status=None, invoice_number=None, start_date=None, end_date=None):
        request = PurchaseInvoiceListRequest(
            self.client,
            params={
                'invoicestatus': status,
                'invoicenumber': invoice_number,
                'begininvoicedate': start_date,
                'endinvoicedate': end_date,
            }
        )
        return request.make_request()
