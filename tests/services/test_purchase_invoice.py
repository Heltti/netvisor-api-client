from decimal import Decimal
from datetime import date

import pytest
import xmltodict
from marshmallow import ValidationError

from netvisor_api_client.exc import InvalidData
from tests.utils import get_request_content, get_response_content

class TestPurchaseInvoiceService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/GetPurchaseInvoice.nv?NetvisorKey=1025',
            body=get_response_content('GetPurchaseInvoice.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )

        purchase_invoice = netvisor.purchase_invoices.get(1025)
        from pprint import pprint
        pprint(purchase_invoice)
        assert purchase_invoice == {
            "netvisor_key": 1025,
            "number": 152212,
            "date": date(2018, 1, 2),
            "delivery_date": date(2014, 10, 2),
            "due_date": date(2018, 1, 31),
            "value_date": date(2018, 1, 15),
            "reference_number": "011234",
            "vendor_bank_account_number": "FI000111234567",
            "amount": Decimal('100.00'),
            "paid_amount": Decimal('0.00'),
            "foreign_currency_amount": Decimal('100'),
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
            'vendor_bank_account_number': 'FI000111234567',
            "voucher_id": None,
            "accounted": False,
            "invoice_lines": [{
                "netvisor_key": 1051,
                "line_sum": Decimal('125.25'),
                "line_net_sum": Decimal('102.6639'),
                "unit_price": Decimal('5.480000000000'),
                "vat_percentage": {
                    "percentage": Decimal('22'),
                    "code": "KOOS"
                },
                "description": "Description text",
                "unit": "kpl",
                "order_amount": Decimal('15'),
                "delivered_amount": Decimal('10'),
                "product_code": "15243",
                "discount_percentage": Decimal('1.5'),
                "product_name": "Test Product",
                "bookkeeping_account_netvisor_key": "643",
                "bookkeeping_account": "4000 Ostot"
              }],
                "dimension": [{
                  "name": "Projects",
                  "detail_name": "Project 1",
                }]
            }