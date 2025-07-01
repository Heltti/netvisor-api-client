"""
netvisor.responsemodels.customers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..schemas import (
    CustomerListSchema,
    GetCustomerListSchema,
    GetCustomerSchema,
    RepliesSchema,
)
from .base import Response


class CustomerListResponse(Response):
    schema_cls = CustomerListSchema
    tag_name = "customerlist"


class GetCustomerResponse(Response):
    schema_cls = GetCustomerSchema
    tag_name = "customer"


class GetCustomerListResponse(Response):
    schema_cls = GetCustomerListSchema
    tag_name = "customers"


class CreateCustomerResponse(Response):
    schema_cls = RepliesSchema
    tag_name = "replies"


class UpdateCustomerResponse(Response):
    schema_cls = None
    tag_name = None
