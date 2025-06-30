"""
netvisor.services.customer
~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..requestmodels.customer import (
    CreateCustomerRequest,
    CustomerListRequest,
    GetCustomerListRequest,
    GetCustomerRequest,
    UpdateCustomerRequest,
)
from .base import Service


class CustomerService(Service):
    def get(self, id: int):
        request = GetCustomerRequest(self.client, params={"id": id})

        return request.make_request()

    def detail_list(self, id_list: list[int]):
        request = GetCustomerListRequest(
            self.client, params={"idlist": ",".join(str(id) for id in id_list)}
        )
        return request.make_request()

    def list(self, query=None):
        request = CustomerListRequest(self.client, params={"Keyword": query})

        return request.make_request()

    def create(self, data):
        request = CreateCustomerRequest(
            self.client, params={"method": "add"}, data=data
        )

        return request.make_request()

    def update(self, id: int, data):
        request = UpdateCustomerRequest(
            self.client, params={"id": id, "method": "edit"}, data=data
        )

        return request.make_request()
