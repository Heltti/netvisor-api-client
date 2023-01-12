"""
    netvisor.requests.sales_payment
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from ..responses.sales_payments import SalesPaymentListResponse
from .base import Request


class SalesPaymentListRequest(Request):
    method = "GET"
    uri = "SalesPaymentList.nv"
    response_cls = SalesPaymentListResponse
