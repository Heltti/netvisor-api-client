"""
netvisor.services.sales_payment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..requestmodels.sales_payment import SalesPaymentListRequest
from .base import Service


class SalesPaymentService(Service):
    def list(self, params={}):
        request = SalesPaymentListRequest(self.client, params=params)
        return request.make_request()
