"""
    netvisor.requests.company
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from ..responses.companies import CompanyListResponse, GetCompanyInformationResponse
from .base import Request


class GetCompanyInformationRequest(Request):
    method = "GET"
    uri = "GetCompanyInformation.nv"
    response_cls = GetCompanyInformationResponse


class CompanyListRequest(Request):
    method = "GET"
    uri = "CompanyList.nv"
    response_cls = CompanyListResponse
