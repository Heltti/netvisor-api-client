# -*- coding: utf-8 -*-

import decimal
from datetime import date

import xmltodict

from tests.utils import get_request_content, get_response_content


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

    def test_create_minimal(self, netvisor, responses):
        responses.add(
            method="POST",
            url="http://koulutus.netvisor.fi/SalesPayment.nv",
            body=get_response_content("SalesInvoiceCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        netvisor_id = netvisor.sales_payments.create(
            {
                "sum": dict(value=decimal.Decimal("10.15"), currency="EUR"),
                "payment_date": date(2014, 2, 7),
                "target_identifier": dict(
                    type="netvisor", targettype="invoice", target="1070"
                ),
                "source_name": "Matti Mallikas",
                "payment_method": dict(method="pankkikortti"),
            }
        )

        request = responses.calls[0].request
        assert netvisor_id == 8
        assert xmltodict.parse(request.body) == xmltodict.parse(
            get_request_content("SalesPayment.xml")
        )
