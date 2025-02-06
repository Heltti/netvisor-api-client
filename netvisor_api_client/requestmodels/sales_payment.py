"""
netvisor.requestmodels.sales_payment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..responsemodels.sales_payments import (
    SalesPaymentCreateResponse,
    SalesPaymentListResponse,
)
from ..schemas import SalesPaymentCreateSchema
from .base import Request


class SalesPaymentListRequest(Request):
    method = "GET"
    uri = "SalesPaymentList.nv"
    response_cls = SalesPaymentListResponse


class SalesPaymentCreateRequest(Request):
    method = "POST"
    uri = "SalesPayment.nv"
    response_cls = SalesPaymentCreateResponse
    schema_cls = SalesPaymentCreateSchema
    tag_name = "salespayment"
