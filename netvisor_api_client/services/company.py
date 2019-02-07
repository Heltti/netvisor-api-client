"""
    netvisor.services.company
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Service
from ..requests.company import CompanyListRequest, GetCompanyInformationRequest


class CompanyService(Service):
    def get(self, business_code):
        request = GetCompanyInformationRequest(
            self.client,
            params={'OrganizationIdentifier': business_code}
        )
        return request.make_request()

    def list(self, query):
        request = CompanyListRequest(self.client, params={'QueryTerm': query})
        return request.make_request()
