"""
netvisor.requestmodels.accounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..responsemodels.accounting import (
    AccountingLedgerResponse,
    AccountingPeriodListResponse,
    AccountListResponse,
    CreateAccountingResponse,
)
from ..schemas.accounting import CreateAccountingVoucherSchema
from .base import Request


class AccountingLedgerRequest(Request):
    method = "GET"
    uri = "AccountingLedger.nv"
    response_cls = AccountingLedgerResponse


class AccountListRequest(Request):
    method = "GET"
    uri = "accountlist.nv"
    response_cls = AccountListResponse


class CreateAccountingRequest(Request):
    method = "POST"
    uri = "Accounting.nv"
    response_cls = CreateAccountingResponse
    schema_cls = CreateAccountingVoucherSchema
    tag_name = "Voucher"


class AccountingPeriodListRequest(Request):
    method = "GET"
    uri = "accountingperiodlist.nv"
    response_cls = AccountingPeriodListResponse
