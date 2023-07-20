"""
    netvisor.responses.accounting
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from ..schemas import AccountingListSchema, RepliesSchema
from .base import Response


class AccountingListResponse(Response):
    schema_cls = AccountingListSchema
    tag_name = "vouchers"


class CreateAccountingResponse(Response):
    schema_cls = RepliesSchema
    tag_name = "replies"
