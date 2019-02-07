"""
    netvisor.schemas.companies.get
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load

from ..common import DateSchema, StringSchema
from ..fields import List


class Address(Schema):
    street = fields.String(allow_none=True)
    postal_code = fields.String()
    postal_office = fields.String()


class RegisteredName(Schema):
    type = fields.String()
    name = fields.String()
    current_activity_status = fields.String()
    established_date = fields.Nested(DateSchema)
    terminated_date = fields.Nested(DateSchema)


class RegisteredNames(Schema):
    registered_name = List(fields.Nested(RegisteredName))

    @post_load
    def preprocess_registered_names(self, input_data):
        return input_data['registered_name'] if input_data else []


class RegisteredPersonRole(Schema):
    type = fields.String()
    identifier = fields.String()
    established_date = fields.Nested(DateSchema)
    name = fields.String()
    nationality = fields.Nested(StringSchema)


class RegisteredPersonRoles(Schema):
    role = List(fields.Nested(RegisteredPersonRole))

    @post_load
    def preprocess_registered_person_roles(self, input_data):
        return input_data['role'] if input_data else []


class CompanySchema(Schema):
    name = fields.String()
    finnish_organization_identifier = fields.String()
    type = fields.String()
    responsible_person_authorization_rule = fields.String()
    established_date = fields.Nested(DateSchema)
    terminated_date = fields.Nested(DateSchema)
    most_recent_change_date = fields.Nested(DateSchema)
    current_activity_status = fields.String()
    current_special_status = fields.String(allow_none=True)
    domicile = fields.String()
    activity_description = fields.String()
    street_address = fields.Nested(Address)
    postal_address = fields.Nested(Address)
    email = fields.String()
    phone = fields.String()
    fax = fields.String()
    registered_person_roles = fields.Nested(RegisteredPersonRoles)
    registered_names = fields.Nested(RegisteredNames)
    stat_employer_register_status = fields.String()
    stat_revenue_size = fields.String()
    stat_staff_size = fields.String()
    stat_vat_register_status = fields.String()
    stat_standard_industrial_classification2008 = fields.String()
    stat_tax_prepayment_register_status = fields.String()


class GetCompanyInformationSchema(Schema):
    company = fields.Nested(CompanySchema)

    @post_load
    def preprocess_customer(self, input_data):
        return input_data['company']
