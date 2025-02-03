"""
netvisor.schemas.accounting.periodlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from marshmallow import Schema, fields, post_load

from ..common import FinnishDateSchema
from ..fields import List


class AccountPeriodSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisor_key")
    name = fields.String()
    begin_date = fields.Nested(FinnishDateSchema, load_from="begin_date")
    end_date = fields.Nested(FinnishDateSchema, load_from="end_date")


class AccountingPeriodListSchema(Schema):
    periods = List(fields.Nested(AccountPeriodSchema), load_from="period")

    @post_load
    def preprocess_accounting_period_list(self, input_data):
        return input_data["periods"] if input_data else []
