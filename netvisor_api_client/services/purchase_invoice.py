from .base import Service
from ..requests.purchase_invoice import (
    PurchaseInvoiceListRequest
)

class PurchaseInvoiceService():
    def list(self, status=None, invoice_number=None, start_date=None, end_date=None):
        request = PurchaseInvoiceListRequest(
            self.client,
            params={
                'invoicestatus': status,
                'InvoiceNumber': invoice_number,
                'BeginInvoiceDate': start_date,
                'EndInvoiceDate': end_date,
            }
        )