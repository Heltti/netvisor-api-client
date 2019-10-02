"""
    netvisor.requests.customer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Request, ListRequest
from ..responses.customers import (
    CreateCustomerResponse,
    CustomerListResponse,
    GetCustomerResponse,
    UpdateCustomerResponse
)
from ..schemas import CreateCustomerSchema


class GetCustomerRequest(Request):
    method = 'GET'
    uri = 'GetCustomer.nv'
    response_cls = GetCustomerResponse


class CustomerListRequest(ListRequest):
    method = 'GET'
    uri = 'CustomerList.nv'
    response_cls = CustomerListResponse


class CreateCustomerRequest(Request):
    method = 'POST'
    uri = 'Customer.nv'
    response_cls = CreateCustomerResponse
    schema_cls = CreateCustomerSchema
    tag_name = 'customer'


class UpdateCustomerRequest(Request):
    method = 'POST'
    uri = 'Customer.nv'
    response_cls = UpdateCustomerResponse
    schema_cls = CreateCustomerSchema
    tag_name = 'customer'
