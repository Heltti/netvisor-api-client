from .base import Response
from ..schemas import (
    PurchaseInvoiceListSchema,
    GetPurchaseInvoiceSchema
)


class PurchaseInvoiceListResponse(Response):
    schema_cls = PurchaseInvoiceListSchema
    tag_name = 'purchase_invoice_list'


class GetPurchaseInvoiceResponse(Response):
    schema_cls = GetPurchaseInvoiceSchema
    tag_name = 'purchase_invoice'