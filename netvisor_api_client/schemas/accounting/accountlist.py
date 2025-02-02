"""
netvisor.schemas.accounting.accountlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from marshmallow import Schema, fields, post_load

from ..fields import List


class AccountSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisor_key")
    number = fields.Integer(allow_none=True)
    name = fields.String(allow_none=True)
    account_type = fields.String(allow_none=True)
    father_netvisor_key = fields.Integer(allow_none=True)
    is_active = fields.Integer(allow_none=True)
    is_cumulative = fields.Integer(allow_none=True)
    sort = fields.Integer(allow_none=True)
    end_sort = fields.Integer(allow_none=True)
    is_natural_negative = fields.Integer(allow_none=True)


class AccountListSchema(Schema):
    account = List(fields.Nested(AccountSchema), load_from="account")

    @post_load
    def preprocess_account_list(self, input_data):
        return input_data["account"] if input_data else []
