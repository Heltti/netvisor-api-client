"""
    netvisor.responses.companies
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Response
from ..schemas import CompanyListSchema, GetCompanyInformationSchema


class CompanyListResponse(Response):
    schema_cls = CompanyListSchema
    tag_name = 'company_list'


class GetCompanyInformationResponse(Response):
    schema_cls = GetCompanyInformationSchema
    tag_name = 'company_information'
