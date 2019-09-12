"""
    netvisor.schemas.customers.create
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import fields, post_dump

from ..common import RejectUnknownFieldsSchema
from ..fields import Boolean


class CustomerBaseInformationSchema(RejectUnknownFieldsSchema):
    internal_identifier = fields.String()
    external_identifier = fields.String()
    name = fields.String()
    name_extension = fields.String()
    street_address = fields.String()
    additional_address_line = fields.String()
    city = fields.String()
    post_number = fields.String()
    country = fields.String()
    customer_group_name = fields.String()
    phone_number = fields.String()
    fax_number = fields.String()
    email = fields.String()
    home_page_uri = fields.String()
    is_active = Boolean(true='1', false='0')
    email_invoicing_address = fields.String()

    class Meta:
        ordered = True


class CustomerFinvoiceDetailsSchema(RejectUnknownFieldsSchema):
    finvoice_address = fields.String()
    finvoice_router_code = fields.String()

    class Meta:
        ordered = True


class CustomerDeliveryDetailsSchema(RejectUnknownFieldsSchema):
    delivery_name = fields.String()
    delivery_street_address = fields.String()
    delivery_city = fields.String()
    delivery_post_number = fields.String()
    delivery_country = fields.String()

    class Meta:
        ordered = True


class CustomerContactDetailsSchema(RejectUnknownFieldsSchema):
    contact_person = fields.String()
    contact_person_email = fields.String()
    contact_person_phone = fields.String()

    class Meta:
        ordered = True


class CustomerAdditionalInformationSchema(RejectUnknownFieldsSchema):
    comment = fields.String()
    customer_reference_number = fields.String()
    invoicing_language = fields.String()
    invoice_print_channel_format = fields.Integer()
    your_default_reference = fields.String()
    default_text_before_invoice_lines = fields.String()
    default_text_after_invoice_lines = fields.String()

    class Meta:
        ordered = True

    @post_dump
    def post_dump(self, data):
        if 'invoice_print_channel_format' in data:
            data['invoice_print_channel_format'] = {
                '#text': str(data['invoice_print_channel_format']),
                '@type': 'netvisor'
            }


class CreateCustomerSchema(RejectUnknownFieldsSchema):
    customer_base_information = fields.Nested(CustomerBaseInformationSchema)
    customer_finvoice_details = fields.Nested(CustomerFinvoiceDetailsSchema)
    customer_delivery_details = fields.Nested(CustomerDeliveryDetailsSchema)
    customer_contact_details = fields.Nested(CustomerContactDetailsSchema)
    customer_additional_information = fields.Nested(
        CustomerAdditionalInformationSchema
    )

    class Meta:
        ordered = True
