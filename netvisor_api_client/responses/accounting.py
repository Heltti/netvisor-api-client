"""
netvisor.responses.accounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..schemas import AccountingLedgerSchema, RepliesSchema
from .base import Response


class AccountingLedgerResponse(Response):
    schema_cls = AccountingLedgerSchema
    tag_name = "vouchers"


class CreateAccountingResponse(Response):
    schema_cls = RepliesSchema
    tag_name = "replies"
