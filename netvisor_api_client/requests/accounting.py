"""
    netvisor.requests.accounting
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from ..responses.accounting import AccountingListResponse
from .base import Request


class AccountingListRequest(Request):
    method = "GET"
    uri = "AccountingLedger.nv"
    response_cls = AccountingListResponse
