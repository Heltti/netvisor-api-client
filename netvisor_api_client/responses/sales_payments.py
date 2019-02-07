"""
    netvisor.responses.sales_payments
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Response
from ..schemas import SalesPaymentListSchema


class SalesPaymentListResponse(Response):
    schema_cls = SalesPaymentListSchema
    tag_name = 'sales_payment_list'
