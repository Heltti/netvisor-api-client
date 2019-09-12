"""
    netvisor.schemas.customers.get
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields

from ..common import StringSchema
from ..fields import Decimal


class CustomerBaseInformationSchema(Schema):
    internal_identifier = fields.String(allow_none=True)
    external_identifier = fields.String(allow_none=True)
    name = fields.String()
    name_extension = fields.String(allow_none=True)
    customer_group_netvisor_key = fields.Integer()
    customer_group_name = fields.String()
    email = fields.String(allow_none=True)
    email_invoicing_address = fields.String(allow_none=True)
    phone_number = fields.String(allow_none=True)
    fax_number = fields.String(allow_none=True)
    home_page_uri = fields.String(allow_none=True)
    is_active = fields.Boolean()
    street_address = fields.String(allow_none=True)
    city = fields.String(allow_none=True)
    post_number = fields.String(allow_none=True)
    country = fields.Nested(StringSchema, allow_none=True)


class CustomerFinvoiceDetailsSchema(Schema):
    finvoice_address = fields.String(allow_none=True)
    finvoice_router_code = fields.String(allow_none=True)


class CustomerAdditionalInformationSchema(Schema):
    balance_limit = Decimal(allow_none=True)
    comment = fields.String(allow_none=True)
    reference_number = fields.String(allow_none=True)
    your_default_reference = fields.String(allow_none=True)
    default_text_before_invoice_lines = fields.String(allow_none=True)
    default_text_after_invoice_lines = fields.String(allow_none=True)


class CustomerContactDetailsSchema(Schema):
    contact_person = fields.String(allow_none=True)
    contact_person_email = fields.String(allow_none=True)
    contact_person_phone = fields.String(allow_none=True)


class CustomerDeliveryDetailsSchema(Schema):
    delivery_name = fields.String(allow_none=True)
    delivery_street_address = fields.String(allow_none=True)
    delivery_post_number = fields.String(allow_none=True)
    delivery_city = fields.String(allow_none=True)


class GetCustomerSchema(Schema):
    customer_base_information = fields.Nested(CustomerBaseInformationSchema)
    customer_additional_information = fields.Nested(
        CustomerAdditionalInformationSchema
    )
    customer_contact_details = fields.Nested(CustomerContactDetailsSchema)
    customer_finvoice_details = fields.Nested(CustomerFinvoiceDetailsSchema)
    customer_delivery_details = fields.Nested(CustomerDeliveryDetailsSchema)
