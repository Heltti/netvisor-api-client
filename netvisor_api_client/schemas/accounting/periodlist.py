"""
netvisor.schemas.accounting.periodlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from marshmallow import Schema, fields

from ..common import FinnishDateSchema
from ..fields import List


class AccountPeriodSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisor_key")
    name = fields.String()
    begin_date = fields.Nested(FinnishDateSchema, load_from="begin_date")
    end_date = fields.Nested(FinnishDateSchema, load_from="end_date")


class PeriodLockInformationSchema(Schema):
    accounting_period_lock_date = fields.Nested(
        FinnishDateSchema, load_from="accounting_period_lock_date"
    )
    vat_period_lock_date = fields.Nested(FinnishDateSchema)
    purchase_lock_date = fields.Nested(FinnishDateSchema)


class AccountingPeriodListSchema(Schema):
    periods = List(fields.Nested(AccountPeriodSchema), load_from="period")
    period_lock_information = fields.Nested(
        PeriodLockInformationSchema, load_from="period_lock_information"
    )
