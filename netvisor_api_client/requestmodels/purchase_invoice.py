from marshmallow import ValidationError

from ..exc import InvalidData
from ..responsemodels.purchase_invoices import (
    GetPurchaseInvoiceResponse,
    PurchaseInvoiceListResponse,
)
from .base import ListRequest, Request


class GetPurchaseInvoiceRequest(Request):
    method = "GET"
    uri = "GetPurchaseInvoice.nv"
    response_cls = GetPurchaseInvoiceResponse

    def _raise_exception(self):
        raise InvalidData(
            "Data form incorrect:. "
            "Purchase invoice not found with Netvisor identifier: {0}".format(
                self.params["NetvisorKey"]
            )
        )

    def parse_response(self, response):
        try:
            result = super(GetPurchaseInvoiceRequest, self).parse_response(
                response=response
            )

            if not result:
                self._raise_exception()

            return result

        except ValidationError:
            self._raise_exception()


class PurchaseInvoiceListRequest(ListRequest):
    method = "GET"
    uri = "PurchaseInvoiceList.nv"
    response_cls = PurchaseInvoiceListResponse
