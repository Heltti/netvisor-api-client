"""
netvisor.responsemodels.accounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..schemas import (
    AccountingLedgerSchema,
    AccountingPeriodListSchema,
    AccountListSchema,
    RepliesSchema,
)
from .base import Response


class AccountingLedgerResponse(Response):
    schema_cls = AccountingLedgerSchema
    tag_name = "vouchers"


class AccountListResponse(Response):
    schema_cls = AccountListSchema
    tag_name = "account_list"


class CreateAccountingResponse(Response):
    schema_cls = RepliesSchema
    tag_name = "replies"


class AccountingPeriodListResponse(Response):
    schema_cls = AccountingPeriodListSchema
    tag_name = "accounting_period_list"
