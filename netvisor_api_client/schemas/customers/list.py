"""
    netvisor.schemas.customers.list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import Schema, fields, post_load

from ..fields import List


class CustomerSchema(Schema):
    netvisor_key = fields.Integer(load_from='netvisorkey', required=True)
    name = fields.String(required=True)
    code = fields.String(allow_none=True, required=True)
    organisation_identifier = fields.String(allow_none=True, required=True)


class CustomerListSchema(Schema):
    customers = List(
        fields.Nested(CustomerSchema),
        load_from='customer'
    )

    @post_load
    def preprocess_customer_list(self, input_data):
        return input_data['customers'] if input_data else []
