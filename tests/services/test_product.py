import decimal

import pytest
import xmltodict

from netvisor_api_client.exc import InvalidData
from tests.utils import get_request_content, get_response_content


class TestProductService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetProduct.nv?id=5",
            body=get_response_content("GetProduct.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        product = netvisor.products.get(5)
        assert product == {
            "product_base_information": {
                "netvisor_key": 165,
                "product_code": "CC",
                "product_group": "Kirjat",
                "name": "Code Complete",
                "description": "Toinen painos",
                "unit_price": {"amount": decimal.Decimal("42.5"), "type": "brutto"},
                "unit": "kpl",
                "unit_weight": decimal.Decimal("0.2"),
                "purchase_price": decimal.Decimal("25"),
                "tariff_heading": "Code Complete",
                "comission_percentage": decimal.Decimal("11"),
                "is_active": True,
                "is_sales_product": False,
            },
            "product_bookkeeping_details": {
                "default_vat_percent": decimal.Decimal("22"),
                "default_domestic_account_number": "3000",
                "default_eu_account_number": "3360",
                "default_outside_eu_account_number": "3380",
            },
            "product_inventory_details": {
                "inventory_amount": decimal.Decimal("2.00"),
                "inventory_mid_price": decimal.Decimal("5.00"),
                "inventory_value": decimal.Decimal("10.0000"),
                "inventory_reserved_amount": decimal.Decimal("1.00"),
                "inventory_ordered_amount": decimal.Decimal("0.00"),
            },
        }

    def test_get_with_minimal_product(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetProduct.nv?id=165",
            body=get_response_content("GetProductMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        product = netvisor.products.get(165)
        assert product == {
            "product_base_information": {
                "netvisor_key": 165,
                "product_code": None,
                "product_group": None,
                "name": "Code Complete",
                "description": None,
                "unit_price": {"amount": decimal.Decimal("0.0000"), "type": "brutto"},
                "unit": None,
                "unit_weight": None,
                "purchase_price": None,
                "tariff_heading": None,
                "comission_percentage": None,
                "is_active": False,
                "is_sales_product": None,
            },
            "product_bookkeeping_details": {
                "default_vat_percent": decimal.Decimal("0"),
                "default_domestic_account_number": "3000",
                "default_eu_account_number": "3360",
                "default_outside_eu_account_number": "3380",
            },
            "product_inventory_details": {
                "inventory_amount": decimal.Decimal("0.00"),
                "inventory_mid_price": decimal.Decimal("0.0000"),
                "inventory_value": decimal.Decimal("0.00"),
                "inventory_reserved_amount": decimal.Decimal("0.00"),
                "inventory_ordered_amount": decimal.Decimal("0.00"),
            },
        }

    def test_get_raises_error_if_product_not_found(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetProduct.nv?id=123",
            body=get_response_content("GetProductNotFound.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.products.get(123)

        assert str(excinfo.value) == (
            "Data form incorrect:. " "Product not found with Netvisor identifier: 123"
        )

    def test_empty_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/ProductList.nv",
            body=get_response_content("ProductListEmpty.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        products = netvisor.products.list()

        assert products == []

    def test_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/ProductList.nv",
            body=get_response_content("ProductList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        products = netvisor.products.list()
        assert products == [
            {
                "netvisor_key": 165,
                "product_code": "TT",
                "name": "Testituote",
                "unit_price": decimal.Decimal("1.96"),
            }
        ]

    def test_list_with_minimal_product(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/ProductList.nv",
            body=get_response_content("ProductListMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        products = netvisor.products.list()
        assert products == [
            {
                "netvisor_key": 165,
                "product_code": None,
                "name": "Testituote",
                "unit_price": decimal.Decimal("1.96"),
            }
        ]

    def test_create_product(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/Product.nv?method=add",
            body=get_response_content("ProductCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        netvisor_id = netvisor.products.create(
            {
                "product_base_information": {
                    "product_code": "CC",
                    "product_group": "Kirjat",
                    "name": "Code Complete",
                    "description": "Toinen painos",
                    "unit_price": {"amount": decimal.Decimal("42.5"), "type": "gross"},
                    "unit": "kpl",
                    "unit_weight": 1,
                    "purchase_price": decimal.Decimal("25.00"),
                    "tariff_heading": "Code Complete",
                    "comission_percentage": decimal.Decimal("11"),
                    "is_active": True,
                    "is_sales_product": False,
                    "inventory_enabled": False,
                    "country_of_origin": "FI",
                },
                "product_bookkeeping_details": {
                    "default_vat_percentage": decimal.Decimal("24"),
                },
                "product_additional_information": {
                    "product_net_weight": dict(
                        amount=decimal.Decimal("11.2"), weightunit="kg"
                    ),
                    "product_gross_weight": dict(
                        amount=decimal.Decimal("12.6"), weightunit="kg"
                    ),
                    "product_package_information": {
                        "package_width": dict(amount=decimal.Decimal("7.3"), unit="cm"),
                        "package_height": dict(
                            amount=decimal.Decimal("15.0"), unit="cm"
                        ),
                        "package_length": dict(
                            amount=decimal.Decimal("36.1"), unit="cm"
                        ),
                    },
                },
            }
        )

        request = responses.calls[0].request

        assert netvisor_id == 8
        assert xmltodict.parse(request.body) == xmltodict.parse(
            get_request_content("Product.xml")
        )

    def test_create_minimal_product(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/Product.nv?method=add",
            body=get_response_content("ProductCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        netvisor_id = netvisor.products.create(
            {
                "product_base_information": {
                    "product_group": "Kirjat",
                    "name": "Code Complete",
                    "unit_price": {"amount": decimal.Decimal("42.5"), "type": "gross"},
                    "is_active": True,
                    "is_sales_product": False,
                }
            }
        )

        request = responses.calls[0].request

        assert netvisor_id == 8
        assert request.body == get_request_content("ProductMinimal.xml")
