# -*- coding: utf-8 -*-

import decimal
from datetime import date

from tests.utils import get_response_content


class TestSalesPaymentService(object):
    def test_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="http://koulutus.netvisor.fi/SalesPaymentList.nv",
            body=get_response_content("SalesPaymentList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        sales_payments = netvisor.sales_payments.list()
        assert sales_payments == [
            {
                "netvisor_key": 165,
                "name": "Matti Mallikas",
                "date": date(2014, 2, 7),
                "sum": decimal.Decimal("249.90"),
                "reference_number": "1094",
                "foreign_currency_amount": None,
                "invoice_number": 1,
                "bank_status": "FAILED",
                "bank_status_error_description": {
                    "code": "ERROR_IN_DUE_DATE",
                    "description": "Eräpäivä virheellinen",
                },
            },
            {
                "netvisor_key": 166,
                "name": "Assi Asiakas",
                "date": date(2014, 3, 10),
                "sum": decimal.Decimal("200"),
                "reference_number": "1106",
                "foreign_currency_amount": None,
                "invoice_number": 2,
                "bank_status": "OK",
            },
        ]
