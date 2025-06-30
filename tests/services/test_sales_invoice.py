# -*- coding: utf-8 -*-

import decimal
from datetime import date

import pytest
import xmltodict
from marshmallow import ValidationError

from netvisor_api_client.exc import InvalidData
from tests.utils import get_request_content, get_response_content


class TestSalesInvoiceService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetSalesInvoice.nv?NetvisorKey=5",
            body=get_response_content("GetSalesInvoice.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        sales_invoice = netvisor.sales_invoices.get(5)

        assert sales_invoice == {
            "number": 3,
            "date": date(2012, 1, 27),
            "delivery_date": date(2012, 1, 27),
            "due_date": date(2023, 6, 6),
            "value_date": date(2008, 12, 1),
            "reference_number": "1070",
            "amount": decimal.Decimal("244.12"),
            "seller_identifier": "Jarmo",
            "invoice_status": "Unsent",
            "free_text_before_lines": None,
            "free_text_after_lines": None,
            "our_reference": None,
            "your_reference": None,
            "private_comment": None,
            "invoicing_customer_name": "Matti Mallikas",
            "invoicing_customer_address_line": "Pajukuja 1",
            "invoicing_customer_post_number": "53100",
            "invoicing_customer_town": "Lappeenranta",
            "invoicing_customer_country_code": "Finland",
            "match_partial_payments_by_default": False,
            "delivery_address_name": "Netvisor Oy",
            "delivery_address_line": "Snelmanninkatu 12",
            "delivery_address_post_number": "53100",
            "delivery_address_town": "LPR",
            "delivery_address_country_code": "FINLAND",
            "delivery_method": None,
            "delivery_term": None,
            "payment_term_net_days": 14,
            "payment_term_cash_discount_days": 5,
            "payment_term_cash_discount": decimal.Decimal("9"),
            "invoice_lines": [
                {
                    "identifier": "OMENA",
                    "name": "Omena",
                    "unit_price": decimal.Decimal("6.9000"),
                    "vat_percentage": {
                        "percentage": decimal.Decimal("22"),
                        "code": "KOMY",
                    },
                    "quantity": decimal.Decimal("2"),
                    "discount_percentage": decimal.Decimal("0"),
                    "free_text": None,
                    "vat_sum": decimal.Decimal("3.04"),
                    "sum": decimal.Decimal("16.84"),
                    "accounting_account_suggestion": "551",
                },
                {
                    "identifier": "BANAANI",
                    "name": "Banaani",
                    "unit_price": decimal.Decimal("2.4900"),
                    "vat_percentage": {
                        "percentage": decimal.Decimal("22"),
                        "code": "KOMY",
                    },
                    "quantity": decimal.Decimal("1"),
                    "discount_percentage": decimal.Decimal("0"),
                    "free_text": None,
                    "vat_sum": decimal.Decimal("0.5478"),
                    "sum": decimal.Decimal("3.0378"),
                    "accounting_account_suggestion": "551",
                },
            ],
        }

    def test_get_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetSalesInvoice.nv?NetvisorKeyList=5,6",
            body=get_response_content("GetSalesInvoiceList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        sales_invoices = netvisor.sales_invoices.detail_list([5, 6])

        assert sales_invoices == [
            {
                "number": 3,
                "date": date(2012, 1, 27),
                "delivery_date": date(2012, 1, 27),
                "due_date": date(2023, 6, 6),
                "value_date": date(2008, 12, 1),
                "reference_number": "1070",
                "amount": decimal.Decimal("244.12"),
                "seller_identifier": "Jarmo",
                "invoice_status": "Unsent",
                "free_text_before_lines": None,
                "free_text_after_lines": None,
                "our_reference": None,
                "your_reference": None,
                "private_comment": None,
                "invoicing_customer_name": "Matti Mallikas",
                "invoicing_customer_address_line": "Pajukuja 1",
                "invoicing_customer_post_number": "53100",
                "invoicing_customer_town": "Lappeenranta",
                "invoicing_customer_country_code": "Finland",
                "match_partial_payments_by_default": False,
                "delivery_address_name": "Netvisor Oy",
                "delivery_address_line": "Snelmanninkatu 12",
                "delivery_address_post_number": "53100",
                "delivery_address_town": "LPR",
                "delivery_address_country_code": "FINLAND",
                "delivery_method": None,
                "delivery_term": None,
                "payment_term_net_days": 14,
                "payment_term_cash_discount_days": 5,
                "payment_term_cash_discount": decimal.Decimal("9"),
                "invoice_lines": [
                    {
                        "identifier": "OMENA",
                        "name": "Omena",
                        "unit_price": decimal.Decimal("6.9000"),
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("2"),
                        "discount_percentage": decimal.Decimal("0"),
                        "free_text": None,
                        "vat_sum": decimal.Decimal("3.04"),
                        "sum": decimal.Decimal("16.84"),
                        "accounting_account_suggestion": "551",
                    },
                    {
                        "identifier": "BANAANI",
                        "name": "Banaani",
                        "unit_price": decimal.Decimal("2.4900"),
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("1"),
                        "discount_percentage": decimal.Decimal("0"),
                        "free_text": None,
                        "vat_sum": decimal.Decimal("0.5478"),
                        "sum": decimal.Decimal("3.0378"),
                        "accounting_account_suggestion": "551",
                    },
                ],
            },
            {
                "number": 4,
                "date": date(2012, 1, 27),
                "delivery_date": date(2012, 1, 27),
                "due_date": date(2023, 6, 6),
                "value_date": date(2008, 12, 1),
                "reference_number": "1070",
                "amount": decimal.Decimal("244.12"),
                "seller_identifier": "Jarmo",
                "invoice_status": "Unsent",
                "free_text_before_lines": None,
                "free_text_after_lines": None,
                "our_reference": None,
                "your_reference": None,
                "private_comment": None,
                "invoicing_customer_name": "Matti Mallikas 2",
                "invoicing_customer_address_line": "Pajukuja 1",
                "invoicing_customer_post_number": "53100",
                "invoicing_customer_town": "Lappeenranta",
                "invoicing_customer_country_code": "Finland",
                "match_partial_payments_by_default": False,
                "delivery_address_name": "Netvisor Oy",
                "delivery_address_line": "Snelmanninkatu 12",
                "delivery_address_post_number": "53100",
                "delivery_address_town": "LPR",
                "delivery_address_country_code": "FINLAND",
                "delivery_method": None,
                "delivery_term": None,
                "payment_term_net_days": 14,
                "payment_term_cash_discount_days": 5,
                "payment_term_cash_discount": decimal.Decimal("9"),
                "invoice_lines": [
                    {
                        "identifier": "OMENA",
                        "name": "Omena",
                        "unit_price": decimal.Decimal("6.9000"),
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("2"),
                        "discount_percentage": decimal.Decimal("0"),
                        "free_text": None,
                        "vat_sum": decimal.Decimal("3.04"),
                        "sum": decimal.Decimal("16.84"),
                        "accounting_account_suggestion": "551",
                    },
                    {
                        "identifier": "BANAANI",
                        "name": "Banaani",
                        "unit_price": decimal.Decimal("2.4900"),
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("1"),
                        "discount_percentage": decimal.Decimal("0"),
                        "free_text": None,
                        "vat_sum": decimal.Decimal("0.5478"),
                        "sum": decimal.Decimal("3.0378"),
                        "accounting_account_suggestion": "551",
                    },
                ],
            },
        ]

    def test_get_minimal(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetSalesInvoice.nv?NetvisorKey=5",
            body=get_response_content("GetSalesInvoiceMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        sales_invoice = netvisor.sales_invoices.get(5)
        assert sales_invoice == {
            "number": 3,
            "date": date(2012, 1, 27),
            "delivery_date": date(2012, 1, 27),
            "due_date": date(2012, 2, 11),
            "reference_number": "1070",
            "amount": decimal.Decimal(244.00),
            "seller_identifier": None,
            "invoice_status": "Unsent",
            "free_text_before_lines": None,
            "free_text_after_lines": None,
            "our_reference": None,
            "your_reference": None,
            "private_comment": None,
            "invoicing_customer_name": "Matti Mallikas",
            "invoicing_customer_address_line": None,
            "invoicing_customer_post_number": None,
            "invoicing_customer_town": None,
            "invoicing_customer_country_code": "Finland",
            "match_partial_payments_by_default": False,
            "delivery_address_name": None,
            "delivery_address_line": None,
            "delivery_address_post_number": None,
            "delivery_address_town": None,
            "delivery_address_country_code": None,
            "delivery_method": None,
            "delivery_term": None,
            "payment_term_net_days": None,
            "payment_term_cash_discount_days": None,
            "payment_term_cash_discount": None,
            "invoice_lines": [
                {
                    "identifier": "OMENA",
                    "name": "Omena",
                    "unit_price": decimal.Decimal("6.9000"),
                    "vat_percentage": {
                        "percentage": decimal.Decimal("22"),
                        "code": "KOMY",
                    },
                    "quantity": decimal.Decimal("2"),
                    "discount_percentage": decimal.Decimal("0"),
                    "free_text": None,
                    "vat_sum": decimal.Decimal("3.04"),
                    "sum": decimal.Decimal("16.84"),
                    "accounting_account_suggestion": None,
                }
            ],
        }

    def test_get_raises_error_if_sales_invoice_not_found(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetSalesInvoice.nv?" "NetvisorKey=123",
            body=get_response_content("GetSalesInvoiceNotFound.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.sales_invoices.get(123)

        assert str(excinfo.value) == (
            "Data form incorrect:. "
            "Sales invoice not found with Netvisor identifier: 123"
        )

    def test_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/SalesInvoiceList.nv",
            body=get_response_content("SalesInvoiceList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        sales_invoices = netvisor.sales_invoices.list()
        assert sales_invoices == [
            {
                "netvisor_key": 165,
                "number": 5,
                "date": date(2013, 11, 9),
                "status": "open",
                "substatus": "overdue",
                "customer_code": "MM",
                "customer_name": "Matti Meikäläinen",
                "reference_number": "1070",
                "sum": decimal.Decimal("123.45"),
                "open_sum": decimal.Decimal("45.67"),
            },
            {
                "netvisor_key": 166,
                "number": 6,
                "date": date(2015, 4, 29),
                "status": "unsent",
                "substatus": None,
                "customer_code": None,
                "customer_name": "Matti Meikäläinen",
                "reference_number": "1070",
                "sum": decimal.Decimal("123.45"),
                "open_sum": decimal.Decimal("45.67"),
            },
        ]

    def test_empty_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/SalesInvoiceList.nv",
            body=get_response_content("SalesInvoiceListEmpty.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        sales_invoices = netvisor.sales_invoices.list()
        assert sales_invoices == []

    def test_list_with_above_id(self, netvisor, responses):
        responses.add(
            method="GET",
            url=(
                "https://koulutus.netvisor.fi/SalesInvoiceList.nv?"
                "InvoicesAboveNetvisorKey=1000"
            ),
            body=get_response_content("SalesInvoiceListEmpty.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        sales_invoices = netvisor.sales_invoices.list(above_id=1000)
        assert sales_invoices == []

    def test_list_with_invoice_number(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/SalesInvoiceList.nv?" "InvoiceNumber=5",
            body=get_response_content("SalesInvoiceList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        netvisor.sales_invoices.list(invoice_number=5)

    def test_create(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/salesinvoice.nv?method=add",
            body=get_response_content("SalesInvoiceCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        netvisor_id = netvisor.sales_invoices.create(
            {
                "number": "107",
                "date": date(2008, 12, 12),
                "value_date": date(2008, 11, 30),
                "delivery_date": date(2008, 7, 25),
                "due_date": date(2023, 6, 6),
                "event_date": date(2008, 12, 1),
                "reference_number": "1070",
                "amount": decimal.Decimal("244.00"),
                "currency": "EUR",
                "seller_identifier": 32,
                "status": "unsent",
                "invoicing_customer_identifier": "1",
                "invoicing_customer_name": "Matti Mallikas",
                "invoicing_customer_name_extension": "Masa",
                "invoicing_customer_address_line": "Pajukuja 1",
                "invoicing_customer_additional_address_line": None,
                "invoicing_customer_post_number": "53100",
                "invoicing_customer_town": "Lappeenranta",
                "invoicing_customer_country_code": "FI",
                "delivery_address_name": "Netvisor Oy",
                "delivery_address_name_extension": "Ohjelmistokehitys ja tuotanto",
                "delivery_address_line": "Snelmanninkatu 12",
                "delivery_address_post_number": "53100",
                "delivery_address_town": "LPR",
                "delivery_address_country_code": "FI",
                "payment_term_net_days": 14,
                "payment_term_cash_discount_days": 5,
                "payment_term_cash_discount": decimal.Decimal("9"),
                "print_channel_format": dict(identifier="2", type="netvisor"),
                "invoice_lines": [
                    {
                        "identifier": dict(identifier="1697", type="netvisor"),
                        "name": "Omena",
                        "unit_price": {
                            "amount": decimal.Decimal("6.90"),
                            "type": "net",
                        },
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("2"),
                        "discount_percentage": decimal.Decimal("0"),
                        "free_text": "Punainen",
                        "accounting_account_suggestion": "3000",
                        "dimension": [
                            {
                                "dimension_item": "Example Dimension Item",
                                "dimension_name": "Example Dimension",
                            },
                            {
                                "dimension_item": "Example Dimension 2 Item",
                                "dimension_name": "Example Dimension 2",
                            },
                        ],
                    },
                    {
                        "identifier": dict(identifier="1697", type="netvisor"),
                        "name": "Banaani",
                        "unit_price": {
                            "amount": decimal.Decimal("100.00"),
                            "type": "net",
                        },
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("1"),
                        "free_text": "Keltainen",
                        "accounting_account_suggestion": "3200",
                    },
                ],
                "attachments": [
                    {
                        "mime_type": "application/pdf",
                        "description": "This is a file",
                        "filename": "invoice-attachment.pdf",
                        "data": "SSdtIG5vdCBtYWRlIGJ5IGRlc2lnbg==",
                        "type": "pdf",
                    }
                ],
            }
        )
        request = responses.calls[0].request
        assert netvisor_id == 8
        assert xmltodict.parse(request.body) == xmltodict.parse(
            get_request_content("SalesInvoice.xml")
        )

    def test_create_minimal(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/salesinvoice.nv?method=add",
            body=get_response_content("SalesInvoiceCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        netvisor_id = netvisor.sales_invoices.create(
            {
                "date": date(2008, 12, 12),
                "amount": decimal.Decimal("244.00"),
                "status": "unsent",
                "invoicing_customer_identifier": "1",
                "payment_term_net_days": 14,
                "payment_term_cash_discount_days": 5,
                "payment_term_cash_discount": decimal.Decimal("9"),
                "invoice_lines": [
                    {
                        "identifier": dict(identifier="1697", type="netvisor"),
                        "name": "Omena",
                        "unit_price": {
                            "amount": decimal.Decimal("6.90"),
                            "type": "net",
                        },
                        "vat_percentage": {
                            "percentage": decimal.Decimal("22"),
                            "code": "KOMY",
                        },
                        "quantity": decimal.Decimal("2"),
                    }
                ],
            }
        )
        request = responses.calls[0].request
        assert netvisor_id == 8
        assert xmltodict.parse(request.body) == xmltodict.parse(
            get_request_content("SalesInvoiceMinimal.xml")
        )

    @pytest.mark.parametrize(
        "data",
        [
            {"foo": "bar"},
            {"invoice_lines": {"foo": "bar"}},
            {"invoice_lines": [{"foo": "bar"}]},
        ],
    )
    def test_create_with_unknown_fields(self, netvisor, responses, data):
        with pytest.raises(ValidationError):
            netvisor.customers.create(data)

    def test_update(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/salesinvoice.nv?method=edit&id=8",
            body=get_response_content("SalesInvoiceEdit.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        data = {
            "number": "107",
            "date": date(2008, 12, 12),
            "value_date": date(2008, 11, 30),
            "delivery_date": date(2008, 7, 25),
            "due_date": date(2023, 6, 6),
            "event_date": date(2008, 12, 1),
            "reference_number": "1070",
            "amount": decimal.Decimal("244.00"),
            "currency": "EUR",
            "seller_identifier": 32,
            "status": "unsent",
            "invoicing_customer_identifier": "1",
            "invoicing_customer_name": "Matti Mallikas",
            "invoicing_customer_name_extension": "Masa",
            "invoicing_customer_address_line": "Pajukuja 1",
            "invoicing_customer_additional_address_line": None,
            "invoicing_customer_post_number": "53100",
            "invoicing_customer_town": "Lappeenranta",
            "invoicing_customer_country_code": "FI",
            "delivery_address_name": "Netvisor Oy",
            "delivery_address_name_extension": "Ohjelmistokehitys ja tuotanto",
            "delivery_address_line": "Snelmanninkatu 12",
            "delivery_address_post_number": "53100",
            "delivery_address_town": "LPR",
            "delivery_address_country_code": "FI",
            "payment_term_net_days": 14,
            "payment_term_cash_discount_days": 5,
            "payment_term_cash_discount": decimal.Decimal("9"),
            "print_channel_format": dict(identifier="2", type="netvisor"),
            "invoice_lines": [
                {
                    "identifier": dict(identifier="1697", type="netvisor"),
                    "name": "Omena",
                    "unit_price": {"amount": decimal.Decimal("6.90"), "type": "net"},
                    "vat_percentage": {
                        "percentage": decimal.Decimal("22"),
                        "code": "KOMY",
                    },
                    "quantity": decimal.Decimal("2"),
                    "discount_percentage": decimal.Decimal("0"),
                    "free_text": "Punainen",
                    "accounting_account_suggestion": "3000",
                    "dimension": [
                        {
                            "dimension_item": "Example Dimension Item",
                            "dimension_name": "Example Dimension",
                        },
                        {
                            "dimension_item": "Example Dimension 2 Item",
                            "dimension_name": "Example Dimension 2",
                        },
                    ],
                },
                {
                    "identifier": dict(identifier="1697", type="netvisor"),
                    "name": "Banaani",
                    "unit_price": {"amount": decimal.Decimal("100.00"), "type": "net"},
                    "vat_percentage": {
                        "percentage": decimal.Decimal("22"),
                        "code": "KOMY",
                    },
                    "quantity": decimal.Decimal("1"),
                    "free_text": "Keltainen",
                    "accounting_account_suggestion": "3200",
                },
            ],
            "attachments": [
                {
                    "mime_type": "application/pdf",
                    "description": "This is a file",
                    "filename": "invoice-attachment.pdf",
                    "data": "SSdtIG5vdCBtYWRlIGJ5IGRlc2lnbg==",
                    "type": "pdf",
                }
            ],
        }
        assert netvisor.sales_invoices.update(id=8, data=data) is None

        request = responses.calls[0].request
        assert request.body == get_request_content("SalesInvoice.xml")
