"""
    netvisor.responses.accounting
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from .base import Response
from ..schemas import AccountingListSchema


class AccountingListResponse(Response):
    schema_cls = AccountingListSchema
    tag_name = 'vouchers'
