from .base import Response
from ..schemas import (
    PurchaseInvoiceListSchema,
)


class PurchaseInvoiceListResponse(Response):
    schema_cls = PurchaseInvoiceListSchema
    tag_name = 'purchase_invoice_list'
