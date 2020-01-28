from datetime import date
from decimal import Decimal

import pytest

from tests.utils import get_response_content


class TestAccountingService(object):
    def test_list(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/AccountingLedger.nv',
            body=get_response_content('AccountingList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        accounting = netvisor.accounting.list()
        assert accounting == [
            {
                'status': 'valid',
                'key': 12,
                'date': date(2000, 1, 1),
                'number': 13,
                'description': 'Invoice 14',
                'class': 'PI Purchase Invoice',
                'linked_source': {'type': 'purchaseinvoice', 'key': 15},
                'uri': 'https:/netvisor.com/voucher/16',
                'lines': [
                    {
                        'key': 121,
                        'line_sum': Decimal('-17.18'),
                        'description': 'Invoice 19',
                        'account_number': 100,
                        'vat_percent': 20,
                        'vat_code': '-',
                        'dimensions': []
                    },
                    {
                        'key': 122,
                        'line_sum': Decimal('-21.22'),
                        'description': 'Invoice 23',
                        'account_number': 200,
                        'vat_percent': 24,
                        'vat_code': 'KOMY',
                        'dimensions': []
                    }
                ]
            },
            {
                'status': 'invalidated',
                'key': 25,
                'date': date(2000, 1, 2),
                'number': 26,
                'description': 'Invoice 27',
                'class': 'SA Sales Invoice',
                'linked_source': {'type': 'salesinvoice', 'key': 28},
                'uri': 'https:/netvisor.com/voucher/29',
                'lines': [
                    {
                        'key': 251,
                        'line_sum': Decimal('-30.31'),
                        'description': 'Invoice 32',
                        'account_number': 300,
                        'vat_percent': 33,
                        'vat_code': '-',
                        'dimensions': [
                            {
                                'name': 'Sales',
                                'item': 'Mike'
                            },
                            {
                                'name': 'Purchase',
                                'item': 'Matt'
                            }
                        ]
                    }
                ]
            },
            {
                'key': 36,
                'date': date(2000, 1, 3),
                'number': 37,
                'description': 'Invoice 38',
                'class': 'Placeholder',
                'linked_source': {'type': 'salesinvoice', 'key': 38},
                'uri': 'https:/netvisor.com/voucher/39',
                'lines': []
            }
        ]

    @pytest.mark.parametrize(
        ('parameter', 'key'),
        [
            ('start_date', 'StartDate'),
            ('end_date', 'EndDate'),
            ('last_modified_start', 'LastModifiedStart'),
            ('last_modified_end', 'LastModifiedEnd'),
            ('changed_since', 'ChangedSince'),
        ]
    )
    def test_date_parameters(self, netvisor, responses, parameter, key):
        value = date(2000, 1, 2)
        url = (
                'http://koulutus.netvisor.fi/AccountingLedger.nv?%s=2000-01-02' %
                key
        )
        responses.add(
            method='GET',
            url=url,
            body=get_response_content('AccountingList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        assert netvisor.accounting.list(**{parameter: value}) is not None
        request = responses.calls[0].request
        assert request.url == url

    @pytest.mark.parametrize(
        ('parameter', 'key'),
        [
            ('account_number_start', 'AccountNumberStart'),
            ('account_number_end', 'AccountNumberEnd'),
            ('voucherstatus', 'Voucherstatus'),
        ]
    )
    def test_integer_parameters(self, netvisor, responses, parameter, key):
        value = 1
        url = (
                'http://koulutus.netvisor.fi/AccountingLedger.nv?%s=1' %
                key
        )
        responses.add(
            method='GET',
            url=url,
            body=get_response_content('AccountingList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        assert netvisor.accounting.list(**{parameter: value}) is not None
        request = responses.calls[0].request
        assert request.url == url

    def test_netvisor_key_list_parameter(self, netvisor, responses):
        url = (
            'http://koulutus.netvisor.fi/AccountingLedger.nv?'
            'NetvisorKeyList=1%2C2%2C3'
        )
        responses.add(
            method='GET',
            url=url,
            body=get_response_content('AccountingList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        assert (
                netvisor.accounting.list(netvisor_key_list=[1, 2, 3]) is not None
        )
        request = responses.calls[0].request
        assert request.url == url
