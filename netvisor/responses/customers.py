"""
    netvisor.responses.customers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Response
from ..schemas import CustomerListSchema, GetCustomerSchema, RepliesSchema


class CustomerListResponse(Response):
    schema_cls = CustomerListSchema
    tag_name = 'customerlist'


class GetCustomerResponse(Response):
    schema_cls = GetCustomerSchema
    tag_name = 'customer'


class CreateCustomerResponse(Response):
    schema_cls = RepliesSchema
    tag_name = 'replies'


class UpdateCustomerResponse(Response):
    schema_cls = None
    tag_name = None
