"""
    netvisor.services.sales_payment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from ..requests.sales_payment import SalesPaymentListRequest
from .base import Service


class SalesPaymentService(Service):
    def list(self):
        request = SalesPaymentListRequest(self.client)
        return request.make_request()
