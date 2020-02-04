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
            url='http://koulutus.netvisor.fi/GetPurchaseInvoice.nv?NetvisorKey=11110',
            body=get_response_content('GetPurchaseInvoice.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )

        purchase_invoice = netvisor.purchase_invoices.get(11110)
        assert purchase_invoice == {
            "PurchaseInvoiceNetvisorKey": 1025,
            "PurchaseInvoiceNumber": 152212,
            "PurchaseInvoiceDate": date(2018, 1, 2),
            "PurchaseInvoiceDeliveryDate": date(2014, 10, 2),
            "PurchaseInvoiceDueDate": date(2018, 1, 31),
            "PurchaseInvoiceValueDate": date(2018, 1, 15),
            "PurchaseInvoiceReferencenumber": "011234",
            "PurchaseInvoiceVendorBankAccountNumber": "FI000111234567",
            "IsPurchaseInvoiceVendorBankAccountDeleted": False,
            "IsPurchaseInvoiceVendorBankAccountFromSEPARegion": True,
            "PurchaseInvoiceAmount": Decimal(100.00),
            "PurchaseInvoicePaidAmount": Decimal(0,00),
            "ForeignCurrencyAmount": Decimal(100),
            "ForeignCurrencyNameID": "EUR",
            "InvoiceStatus": "Avoin",
            "ApprovalStatus": "open",
            "PurchaseInvoiceOurReference": "111234",
            "PurchaseInvoiceYourReference": "21134",
            "PurchaseInvoiceDescription": "Comment text",
            "VendorName": "Vendor Oy Ab",
            "VendorAddressline": "Pajukuja 5",
            "VendorPostnumber": "53100",
            "VendorTown": "Lappeenranta",
            "VendorCountry": "FI",
            "IsAccounted": False,
            "InvoiceLines": {
              "PurchaseInvoiceLine": {
                "NetvisorKey": 1051,
                "LineSum": Decimal(125.25),
                "LineNetSum": Decimal(102.6639),
                "UnitPrice": Decimal(5.480000000000),
                "VatPercent": Decimal(22),
                "VatCode": "KOOS",
                "Description": "Description text",
                "Unit": "kpl",
                "OrderedAmount": Decimal(15),
                "DeliveredAmount": "10",
                "ProductCode": "15243",
                "DiscountPercentage": "1,5",
                "ProductName": "Test Product",
                "AccountingSuggestionBookkeepingAccountNetvisorKey": "643",
                "AccountingSuggestionBookkeepingAccount": "4000 Ostot"
              },
              "PurchaseInvoiceLineDimensions": {
                "Dimension": {
                  "DimensionName": "Projects",
                  "DimensionNameNetvisorKey": "3",
                  "DimensionDetailName": "Project 1",
                  "DimensionDetailNetvisorKey": "3"
                }
              }
            }
        }