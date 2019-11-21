from .base import ListRequest
from ..responses.purchase_invoices import (
    PurchaseInvoiceListResponse
)


class PurchaseInvoiceListRequest(ListRequest):
    method = 'GET'
    uri = 'purchaseinvoicelist.nv'
    response_cls = PurchaseInvoiceListResponse