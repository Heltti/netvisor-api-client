# -*- coding: utf-8 -*-

from datetime import date

from tests.utils import get_response_content


class TestCompanyService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method="GET",
            url=(
                "https://koulutus.netvisor.fi/GetCompanyInformation.nv?"
                "OrganizationIdentifier=1234567-8"
            ),
            body=get_response_content("GetCompanyInformation.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        company = netvisor.companies.get("1234567-8")
        assert company == {
            "name": "General Motors Finland",
            "finnish_organization_identifier": "1234567-8",
            "type": "Osakeyhtiö",
            "responsible_person_authorization_rule": (
                "Yhteisösääntöjen mukaan toiminimen kirjoittavat hallituksen "
                "puheenjohtaja, toimitusjohtaja ja toimitusjohtajan sijainen "
                "kukin yksin."
            ),
            "established_date": date(2009, 12, 31),
            "terminated_date": date(2009, 12, 31),
            "most_recent_change_date": date(2009, 12, 31),
            "current_activity_status": "active",
            "current_special_status": None,
            "domicile": "Helsinki",
            "activity_description": "Kebab",
            "street_address": {
                "street": "Esimerkkikatu 123",
                "postal_code": "00100",
                "postal_office": "Helsinki",
            },
            "postal_address": {
                "street": None,
                "postal_code": "00002",
                "postal_office": "Helsinki",
            },
            "email": "info@generalmotors.fi",
            "phone": "020 1234567",
            "fax": "(09) 5551234",
            "registered_person_roles": [
                {
                    "type": "Yhtiön muu johto",
                    "identifier": "Toimitusjohtaja",
                    "established_date": date(2009, 12, 31),
                    "name": "Gunnar Peterson",
                    "nationality": "FI",
                }
            ],
            "registered_names": [
                {
                    "type": "Päätoiminimi",
                    "name": "Pekan yritys Oy",
                    "current_activity_status": "active",
                    "established_date": date(2009, 12, 31),
                    "terminated_date": date(2009, 12, 31),
                }
            ],
            "stat_employer_register_status": "never_registered",
            "stat_revenue_size": "100-200",
            "stat_staff_size": "4-9",
            "stat_vat_register_status": "currently_registered",
            "stat_standard_industrial_classification2008": "Kaivostoiminta",
            "stat_tax_prepayment_register_status": "previously_registered",
        }

    def test_list_with_query(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/CompanyList.nv?QueryTerm=acme",
            body=get_response_content("CompanyList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        companies = netvisor.companies.list(query="acme")
        assert companies == [
            {
                "id": 125,
                "is_active": True,
                "name": "ACME",
                "finnish_organization_identifier": "1234567-8",
            }
        ]
