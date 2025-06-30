from datetime import date
from decimal import Decimal

import pytest

from netvisor_api_client.exc import InvalidData
from tests.utils import get_response_content


class TestPurchaseInvoiceService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetPurchaseInvoice.nv?NetvisorKey=1025&Version=2",
            body=get_response_content("GetPurchaseInvoice.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        purchase_invoice = netvisor.purchase_invoices.get(1025)
        assert purchase_invoice == {
            "netvisor_key": 1025,
            "number": 152212,
            "date": date(2018, 1, 2),
            "delivery_date": date(2014, 10, 2),
            "due_date": date(2018, 1, 31),
            "value_date": date(2018, 1, 15),
            "reference_number": "011234",
            "vendor_bank_account_number": "FI000111234567",
            "amount": Decimal("100.00"),
            "paid_amount": Decimal("0.00"),
            "foreign_currency_amount": Decimal("100"),
            "foreign_currency_name_id": "EUR",
            "status": "Avoin",
            "approval_status": "open",
            "our_reference": "111234",
            "your_reference": "21134",
            "description": "Comment text",
            "vendor_name": "Vendor Oy Ab",
            "vendor_addressline": "Pajukuja 5",
            "vendor_postnumber": "53100",
            "vendor_town": "Lappeenranta",
            "vendor_country": "FI",
            "voucher_id": 1,
            "accounted": False,
            "preview_image": "Text",
            "lines": {
                "items": [
                    {
                        "netvisor_key": 1051,
                        "line_sum": Decimal("125.25"),
                        "line_net_sum": Decimal("102.6639"),
                        "unit_price": Decimal("5.480000000000"),
                        "vat_percent": Decimal("22"),
                        "vat_code": "KOOS",
                        "description": "Description text",
                        "unit": "kpl",
                        "ordered_amount": Decimal("15"),
                        "delivered_amount": Decimal("10"),
                        "product_code": "15243",
                        "discount_percentage": Decimal("1.5"),
                        "product_name": "Test Product",
                        "purchase_price": Decimal("24.00"),
                        "bookkeeping_account_netvisor_key": "643",
                        "bookkeeping_account": "4000 Ostot",
                    },
                    {
                        "netvisor_key": 1052,
                        "line_sum": Decimal("125.25"),
                        "line_net_sum": Decimal("102.6639"),
                        "unit_price": Decimal("5.480000000000"),
                        "vat_percent": Decimal("22"),
                        "vat_code": "KOOS",
                        "description": "Description text",
                        "unit": "kpl",
                        "ordered_amount": Decimal("15"),
                        "delivered_amount": Decimal("10"),
                        "product_code": "15243",
                        "discount_percentage": Decimal("1.5"),
                        "product_name": "Test Product",
                        "purchase_price": Decimal("24.00"),
                        "bookkeeping_account_netvisor_key": "643",
                        "bookkeeping_account": "4000 Ostot",
                    },
                ],
                "dimensions": [
                    {
                        "name": "Projects",
                        "netvisor_key": 3,
                        "detail_name": "Project 1",
                        "detail_netvisor_key": 3,
                    },
                    {
                        "name": "Projects",
                        "netvisor_key": 4,
                        "detail_name": "Project 2",
                        "detail_netvisor_key": 4,
                    },
                ],
            },
            "orders": [
                {
                    "netvisor_key": 123,
                    "number": 1,
                },
                {"netvisor_key": 456, "number": 2},
            ],
        }

    def test_get_minimal(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetPurchaseInvoice.nv?NetvisorKey=1025&Version=2",
            body=get_response_content("GetPurchaseInvoiceMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        purchase_invoice = netvisor.purchase_invoices.get(1025)
        assert purchase_invoice == {
            "netvisor_key": 1025,
            "number": 152212,
            "date": date(2018, 1, 2),
            "delivery_date": date(2014, 10, 2),
            "due_date": date(2018, 1, 31),
            "value_date": date(2018, 1, 15),
            "reference_number": "011234",
            "vendor_bank_account_number": "FI000111234567",
            "amount": Decimal("100.00"),
            "paid_amount": Decimal("0.00"),
            "foreign_currency_amount": Decimal("100"),
            "foreign_currency_name_id": "EUR",
            "status": "Avoin",
            "approval_status": "open",
            "our_reference": "111234",
            "your_reference": "21134",
            "description": "Comment text",
            "vendor_name": "Vendor Oy Ab",
            "vendor_addressline": "Pajukuja 5",
            "vendor_postnumber": "53100",
            "vendor_town": "Lappeenranta",
            "vendor_country": "FI",
            "voucher_id": None,
            "accounted": False,
            "preview_image": None,
            "lines": None,
            "orders": None,
        }

    def test_get_raises_error_if_sales_invoice_not_found(self, netvisor, responses):
        responses.add(
            method="GET",
            url=(
                "https://koulutus.netvisor.fi/GetPurchaseInvoice.nv?NetvisorKey=123&Version=2"
            ),
            body=get_response_content("GetPurchaseInvoiceNotFound.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.purchase_invoices.get(123)

        assert str(excinfo.value) == (
            "Data form incorrect:. "
            "Purchase invoice not found with Netvisor identifier: 123"
        )

    def test_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/PurchaseInvoiceList.nv",
            body=get_response_content("PurchaseInvoiceList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        purchase_invoice_list = netvisor.purchase_invoices.list()
        from pprint import pprint

        pprint(purchase_invoice_list)
        assert purchase_invoice_list == [
            {
                "netvisor_key": 1,
                "number": 123,
                "date": date(2017, 11, 16),
                "vendor": "Simon Supplier",
                "vendor_organization_identifier": "1234567-8",
                "sum": Decimal("25"),
                "payments": Decimal("25"),
                "open_sum": Decimal("0"),
                "uri": "https://*****.*****.**/getpurchaseinvoice.nv?netvisorkey=*",
            },
            {
                "netvisor_key": 2,
                "number": 234,
                "date": date(2017, 11, 23),
                "vendor": "Simon Supplier",
                "vendor_organization_identifier": "1234567-8",
                "sum": Decimal("30"),
                "payments": Decimal("0"),
                "open_sum": Decimal("30"),
                "uri": "https://*****.*****.**/getpurchaseinvoice.nv?netvisorkey=*",
            },
            {
                "netvisor_key": 3,
                "number": 345,
                "date": date(2017, 11, 16),
                "vendor": "Sara Supplier",
                "vendor_organization_identifier": None,
                "sum": Decimal("30"),
                "payments": Decimal("0"),
                "open_sum": Decimal("30"),
                "uri": "https://*****.*****.**/getpurchaseinvoice.nv?netvisorkey=*",
            },
        ]

    def test_empty_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/PurchaseInvoiceList.nv",
            body=get_response_content("PurchaseInvoiceListEmpty.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        purchase_invoice_list = netvisor.purchase_invoices.list()
        assert purchase_invoice_list == []
