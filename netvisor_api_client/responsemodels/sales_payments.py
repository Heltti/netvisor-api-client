"""
netvisor.responsemodels.sales_payments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..schemas import RepliesSchema, SalesPaymentListSchema
from .base import Response


class SalesPaymentListResponse(Response):
    schema_cls = SalesPaymentListSchema
    tag_name = "sales_payment_list"


class SalesPaymentCreateResponse(Response):
    schema_cls = RepliesSchema
    tag_name = 'replies'
