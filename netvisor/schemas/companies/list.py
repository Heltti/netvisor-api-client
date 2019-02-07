"""
    netvisor.schemas.companies.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load

from ..fields import Boolean, List


class CompanySchema(Schema):
    id = fields.Integer()
    name = fields.String()
    finnish_organization_identifier = fields.String(allow_none=True)
    is_active = Boolean(true='1', false='0')


class CompanyListSchema(Schema):
    companies = List(
        fields.Nested(CompanySchema, allow_none=True),
        load_from='company'
    )

    @post_load
    def preprocess_company_list(self, input_data):
        return input_data['companies'] if input_data else []
