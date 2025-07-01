# -*- coding: utf-8 -*-

import decimal

import pytest
from marshmallow import ValidationError

from netvisor_api_client.exc import InvalidData
from tests.utils import get_request_content, get_response_content


class TestCustomerService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetCustomer.nv?id=5",
            body=get_response_content("GetCustomer.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        customer = netvisor.customers.get(5)
        assert customer == {
            "customer_base_information": {
                "internal_identifier": "MM",
                "external_identifier": "1234567-8",
                "customer_group_netvisor_key": 1,
                "customer_group_name": "Asiakasryhm\xe4 1",
                "name": "Maija Mallikas",
                "name_extension": "toimitusjohtaja",
                "street_address": "Pajukuja 2",
                "city": "Lappeenranta",
                "post_number": "53100",
                "country": "FI",
                "netvisor_key": 5,
                "phone_number": "040 12157 988",
                "fax_number": "(015) 123 4567",
                "email": "maija.mallikas@netvisor.fi",
                "email_invoicing_address": "matti.mallikas@netvisor.fi",
                "home_page_uri": "www.netvisor.fi",
                "is_active": True,
            },
            "customer_finvoice_details": {
                "finvoice_address": "FI002316574613249",
                "finvoice_router_code": "PSPBFIHH",
            },
            "customer_delivery_details": {
                "delivery_name": "Matti",
                "delivery_street_address": "Pajukuja 90",
                "delivery_post_number": "53100",
                "delivery_city": "Lappeenranta",
            },
            "customer_contact_details": {
                "contact_person": "Perttu",
                "contact_person_email": "perttu@netvisor.fi",
                "contact_person_phone": "040 21578 999",
            },
            "customer_additional_information": {
                "comment": "Great customer!",
                "reference_number": "1070",
                "balance_limit": decimal.Decimal("200.3"),
                "your_default_reference": "Default reference",
                "default_text_before_invoice_lines": "Default test before invoice lines",
                "default_text_after_invoice_lines": "Default test after invoice lines",
            },
        }

    def test_getlist(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetCustomer.nv?idlist=5,6",
            body=get_response_content("GetCustomerList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        customers = netvisor.customers.detail_list([5, 6])
        assert customers == [
            {
                "customer_base_information": {
                    "internal_identifier": "MM",
                    "external_identifier": "1234567-8",
                    "customer_group_netvisor_key": 1,
                    "customer_group_name": "Asiakasryhm\xe4 1",
                    "name": "Maija Mallikas",
                    "name_extension": "toimitusjohtaja",
                    "netvisor_key": 5,
                    "street_address": "Pajukuja 2",
                    "city": "Lappeenranta",
                    "post_number": "53100",
                    "country": "FI",
                    "phone_number": "040 12157 988",
                    "fax_number": "(015) 123 4567",
                    "email": "maija.mallikas@netvisor.fi",
                    "email_invoicing_address": "matti.mallikas@netvisor.fi",
                    "home_page_uri": "www.netvisor.fi",
                    "is_active": True,
                },
                "customer_finvoice_details": {
                    "finvoice_address": "FI002316574613249",
                    "finvoice_router_code": "PSPBFIHH",
                },
                "customer_delivery_details": {
                    "delivery_name": "Matti",
                    "delivery_street_address": "Pajukuja 90",
                    "delivery_post_number": "53100",
                    "delivery_city": "Lappeenranta",
                },
                "customer_contact_details": {
                    "contact_person": "Perttu",
                    "contact_person_email": "perttu@netvisor.fi",
                    "contact_person_phone": "040 21578 999",
                },
                "customer_additional_information": {
                    "comment": "Great customer!",
                    "reference_number": "1070",
                    "balance_limit": decimal.Decimal("200.3"),
                    "your_default_reference": "Default reference",
                    "default_text_before_invoice_lines": "Default test before invoice lines",
                    "default_text_after_invoice_lines": "Default test after invoice lines",
                },
            },
            {
                "customer_base_information": {
                    "internal_identifier": "MM2",
                    "external_identifier": "2234567-8",
                    "customer_group_netvisor_key": 1,
                    "customer_group_name": "Asiakasryhm\xe4 2",
                    "name": "Maija Mallikas 2",
                    "name_extension": "toimitusjohtaja 2",
                    "netvisor_key": 6,
                    "street_address": "Pajukuja 2",
                    "city": "Lappeenranta",
                    "post_number": "53100",
                    "country": "FI",
                    "phone_number": "040 12157 988",
                    "fax_number": "(015) 123 4567",
                    "email": "maija.mallikas@netvisor.fi",
                    "email_invoicing_address": "matti.mallikas@netvisor.fi",
                    "home_page_uri": "www.netvisor.fi",
                    "is_active": True,
                },
                "customer_finvoice_details": {
                    "finvoice_address": "FI002316574613249",
                    "finvoice_router_code": "PSPBFIHH",
                },
                "customer_delivery_details": {
                    "delivery_name": "Matti",
                    "delivery_street_address": "Pajukuja 90",
                    "delivery_post_number": "53100",
                    "delivery_city": "Lappeenranta",
                },
                "customer_contact_details": {
                    "contact_person": "Perttu",
                    "contact_person_email": "perttu@netvisor.fi",
                    "contact_person_phone": "040 21578 999",
                },
                "customer_additional_information": {
                    "comment": "Great customer!",
                    "reference_number": "1070",
                    "balance_limit": decimal.Decimal("200.3"),
                    "your_default_reference": "Default reference",
                    "default_text_before_invoice_lines": "Default test before invoice lines",
                    "default_text_after_invoice_lines": "Default test after invoice lines",
                },
            },
        ]

    def test_get_with_minimal_customer(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetCustomer.nv?id=5",
            body=get_response_content("GetCustomerMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        customer = netvisor.customers.get(5)
        assert customer == {
            "customer_base_information": {
                "internal_identifier": None,
                "external_identifier": None,
                "customer_group_netvisor_key": 1,
                "customer_group_name": "Asiakasryhm\xe4 1",
                "name": "Maija Mallikas",
                "name_extension": None,
                "street_address": None,
                "city": None,
                "post_number": None,
                "country": "FI",
                "phone_number": None,
                "fax_number": None,
                "email": None,
                "email_invoicing_address": None,
                "home_page_uri": None,
                "is_active": False,
            },
            "customer_finvoice_details": {
                "finvoice_address": None,
                "finvoice_router_code": None,
            },
            "customer_delivery_details": {
                "delivery_name": None,
                "delivery_street_address": None,
                "delivery_post_number": None,
                "delivery_city": None,
            },
            "customer_contact_details": {
                "contact_person": None,
                "contact_person_email": None,
                "contact_person_phone": None,
            },
            "customer_additional_information": {
                "comment": None,
                "reference_number": None,
                "balance_limit": None,
            },
        }

    def test_get_raises_error_if_customer_not_found(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/GetCustomer.nv?id=123",
            body=get_response_content("GetCustomerNotFound.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        with pytest.raises(InvalidData) as excinfo:
            netvisor.customers.get(123)

        assert str(excinfo.value) == (
            "Data form incorrect:. " "Customer not found with Netvisor identifier: 123"
        )

    def test_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/CustomerList.nv",
            body=get_response_content("CustomerList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        customers = netvisor.customers.list()
        assert customers == [
            {
                "netvisor_key": 165,
                "name": "Anni Asiakas",
                "code": "AA",
                "organisation_identifier": "12345678-9",
            },
            {
                "netvisor_key": 166,
                "name": "Matti Mallikas",
                "code": None,
                "organisation_identifier": None,
            },
        ]

    def test_list_with_zero_customers(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/CustomerList.nv",
            body=get_response_content("CustomerListMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        customers = netvisor.customers.list()
        assert customers == []

    def test_list_with_query(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/CustomerList.nv?Keyword=anni",
            body=get_response_content("CustomerList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        customers = netvisor.customers.list(query="anni")
        assert customers == [
            {
                "netvisor_key": 165,
                "name": "Anni Asiakas",
                "code": "AA",
                "organisation_identifier": "12345678-9",
            },
            {
                "netvisor_key": 166,
                "name": "Matti Mallikas",
                "code": None,
                "organisation_identifier": None,
            },
        ]

    def test_create(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/Customer.nv?method=add",
            body=get_response_content("CustomerCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        netvisor_id = netvisor.customers.create(
            {
                "customer_base_information": {
                    "internal_identifier": "MM",
                    "external_identifier": "1967543-8",
                    "name": "Matti Meikäläinen",
                    "name_extension": "Toimitusjohtaja",
                    "street_address": "c/o Yritys Oy",
                    "additional_address_line": "Pajukuja 1",
                    "city": "Lappeenranta",
                    "post_number": "53100",
                    "country": "FI",
                    "customer_group_name": "Alennusasiakkaat",
                    "phone_number": "040 123456",
                    "fax_number": "05 123456",
                    "email": "matti.meikalainen@firma.fi",
                    "email_invoicing_address": "maija.meikalainen@firma.fi",
                    "home_page_uri": "www.firma.fi",
                    "is_active": True,
                },
                "customer_finvoice_details": {
                    "finvoice_address": "FI109700021497",
                    "finvoice_router_code": "NDEAFIHH",
                },
                "customer_delivery_details": {
                    "delivery_name": "Maija Mehiläinen",
                    "delivery_street_address": "Pajukuja 2",
                    "delivery_city": "Lappeenranta",
                    "delivery_post_number": "53900",
                    "delivery_country": "FI",
                },
                "customer_contact_details": {
                    "contact_person": "Matti Meikäläinen",
                    "contact_person_email": "matti.meikalainen@firma.fi",
                    "contact_person_phone": "040 987 254",
                },
                "customer_additional_information": {
                    "comment": "Kommentti",
                    "customer_reference_number": "1070",
                    "invoicing_language": "FI",
                    "invoice_print_channel_format": "1",
                    "your_default_reference": "Default reference",
                    "default_text_before_invoice_lines": "Default text before invoice lines",
                    "default_text_after_invoice_lines": "Default text after invoice lines",
                },
            }
        )
        request = responses.calls[0].request
        assert netvisor_id == 8
        assert request.body == get_request_content("Customer.xml")

    def test_create_with_minimal_data(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/Customer.nv?method=add",
            body=get_response_content("CustomerCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        netvisor_id = netvisor.customers.create(
            {"customer_base_information": {"name": "Matti Meikäläinen"}}
        )
        request = responses.calls[0].request
        assert netvisor_id == 8
        assert request.body == get_request_content("CustomerMinimal.xml")

    @pytest.mark.parametrize(
        "data",
        [
            {"foo": "bar"},
            {"customer_base_information": {"foo": "bar"}},
            {"customer_finvoice_details": {"foo": "bar"}},
            {"customer_delivery_details": {"foo": "bar"}},
            {"customer_contact_details": {"foo": "bar"}},
            {"customer_additional_information": {"foo": "bar"}},
        ],
    )
    def test_create_with_unknown_fields(self, netvisor, responses, data):
        with pytest.raises(ValidationError):
            netvisor.customers.create(data)

    def test_update(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/Customer.nv?method=edit&id=8",
            body=get_response_content("CustomerEdit.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        data = {
            "customer_base_information": {
                "internal_identifier": "MM",
                "external_identifier": "1967543-8",
                "name": "Matti Meikäläinen",
                "name_extension": "Toimitusjohtaja",
                "street_address": "c/o Yritys Oy",
                "additional_address_line": "Pajukuja 1",
                "city": "Lappeenranta",
                "post_number": "53100",
                "country": "FI",
                "customer_group_name": "Alennusasiakkaat",
                "phone_number": "040 123456",
                "fax_number": "05 123456",
                "email": "matti.meikalainen@firma.fi",
                "email_invoicing_address": "maija.meikalainen@firma.fi",
                "home_page_uri": "www.firma.fi",
                "is_active": True,
            },
            "customer_finvoice_details": {
                "finvoice_address": "FI109700021497",
                "finvoice_router_code": "NDEAFIHH",
            },
            "customer_delivery_details": {
                "delivery_name": "Maija Mehiläinen",
                "delivery_street_address": "Pajukuja 2",
                "delivery_city": "Lappeenranta",
                "delivery_post_number": "53900",
                "delivery_country": "FI",
            },
            "customer_contact_details": {
                "contact_person": "Matti Meikäläinen",
                "contact_person_email": "matti.meikalainen@firma.fi",
                "contact_person_phone": "040 987 254",
            },
            "customer_additional_information": {
                "comment": "Kommentti",
                "customer_reference_number": "1070",
                "invoicing_language": "FI",
                "invoice_print_channel_format": "1",
                "your_default_reference": "Default reference",
                "default_text_before_invoice_lines": "Default text before invoice lines",
                "default_text_after_invoice_lines": "Default text after invoice lines",
            },
        }
        assert netvisor.customers.update(id=8, data=data) is None
        request = responses.calls[0].request
        assert request.body == get_request_content("Customer.xml")
