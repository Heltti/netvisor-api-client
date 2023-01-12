from ..schemas import GetPurchaseInvoiceSchema, PurchaseInvoiceListSchema
from .base import Response


class PurchaseInvoiceListResponse(Response):
    schema_cls = PurchaseInvoiceListSchema
    tag_name = "purchase_invoice_list"


class GetPurchaseInvoiceResponse(Response):
    schema_cls = GetPurchaseInvoiceSchema
    tag_name = "purchase_invoice"
