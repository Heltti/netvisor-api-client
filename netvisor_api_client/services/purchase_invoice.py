from ..requestmodels.purchase_invoice import (
    GetPurchaseInvoiceRequest,
    PurchaseInvoiceListRequest,
)
from .base import Service


class PurchaseInvoiceService(Service):
    def get(self, id, version=2, include=None, omit_attachments=None):
        request = GetPurchaseInvoiceRequest(
            self.client,
            params={
                "NetvisorKey": id,
                "Version": version,
                "Include": include,
                "Omitattachments": omit_attachments,
            },
        )
        return request.make_request()

    def list(self, status=None, invoice_number=None, start_date=None, end_date=None):
        request = PurchaseInvoiceListRequest(
            self.client,
            params={
                "invoicestatus": status,
                "invoicenumber": invoice_number,
                "begininvoicedate": start_date,
                "endinvoicedate": end_date,
            },
        )
        return request.make_request()
