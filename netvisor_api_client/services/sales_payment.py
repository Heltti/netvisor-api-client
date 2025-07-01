"""
netvisor.services.sales_payment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..requestmodels.sales_payment import (
    SalesPaymentCreateRequest,
    SalesPaymentListRequest,
)
from .base import Service


class SalesPaymentService(Service):
    def list(self, params=None):
        if params is None:
            params = {}
        request = SalesPaymentListRequest(self.client, params=params)
        return request.make_request()

    def create(self, data):
        request = SalesPaymentCreateRequest(self.client, data=data)
        return request.make_request()
