"""
netvisor.services.accounting
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from ..requestmodels.accounting import (
    AccountingLedgerRequest,
    AccountingPeriodListRequest,
    AccountListRequest,
    CreateAccountingRequest,
)
from .base import Service


class AccountingService(Service):
    def ledger(
        self,
        start_date=None,
        end_date=None,
        account_number_start=None,
        account_number_end=None,
        last_modified_start=None,
        last_modified_end=None,
        netvisor_key_list=None,
        voucherstatus=None,
        changed_since=None,
    ):
        query = {}
        if start_date is not None:
            query["StartDate"] = start_date.isoformat()
        if end_date is not None:
            query["EndDate"] = end_date.isoformat()
        if account_number_start is not None:
            query["AccountNumberStart"] = account_number_start
        if account_number_end is not None:
            query["AccountNumberEnd"] = account_number_end
        if last_modified_start is not None:
            query["LastModifiedStart"] = last_modified_start.isoformat()
        if last_modified_end is not None:
            query["LastModifiedEnd"] = last_modified_end.isoformat()
        if netvisor_key_list is not None:
            query["NetvisorKeyList"] = ",".join(str(key) for key in netvisor_key_list)
        if voucherstatus is not None:
            query["Voucherstatus"] = voucherstatus
        if changed_since is not None:
            query["ChangedSince"] = changed_since.isoformat()
        request = AccountingLedgerRequest(self.client, params=query)
        return request.make_request()

    def account_list(self):
        request = AccountListRequest(self.client)
        return request.make_request()

    def create(self, data):
        request = CreateAccountingRequest(self.client, data=data)
        return request.make_request()

    def period_list(self):
        request = AccountingPeriodListRequest(self.client)
        return request.make_request()
