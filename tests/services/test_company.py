from datetime import date

from tests.utils import get_response_content


class TestCompanyService(object):
    def test_get(self, netvisor, responses):
        responses.add(
            method='GET',
            url=(
                'http://koulutus.netvisor.fi/GetCompanyInformation.nv?'
                'OrganizationIdentifier=1234567-8'
            ),
            body=get_response_content('GetCompanyInformation.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        company = netvisor.companies.get('1234567-8')
        assert company == {
            'name': u'General Motors Finland',
            'finnish_organization_identifier': u'1234567-8',
            'type': u'Osakeyhtiö',
            'responsible_person_authorization_rule': (
                u'Yhteisösääntöjen mukaan toiminimen kirjoittavat hallituksen '
                u'puheenjohtaja, toimitusjohtaja ja toimitusjohtajan sijainen '
                u'kukin yksin.'
            ),
            'established_date': date(2009, 12, 31),
            'terminated_date': date(2009, 12, 31),
            'most_recent_change_date': date(2009, 12, 31),
            'current_activity_status': u'active',
            'current_special_status': None,
            'domicile': u'Helsinki',
            'activity_description': u'Kebab',
            'street_address': {
                'street': u'Esimerkkikatu 123',
                'postal_code': u'00100',
                'postal_office': u'Helsinki',
            },
            'postal_address': {
                'street': None,
                'postal_code': u'00002',
                'postal_office': u'Helsinki',
            },
            'email': u'info@generalmotors.fi',
            'phone': u'020 1234567',
            'fax': u'(09) 5551234',
            'registered_person_roles': [
                {
                    'type': u'Yhtiön muu johto',
                    'identifier': u'Toimitusjohtaja',
                    'established_date': date(2009, 12, 31),
                    'name': u'Gunnar Peterson',
                    'nationality': u'FI',
                }
            ],
            'registered_names': [
                {
                    'type': u'Päätoiminimi',
                    'name': u'Pekan yritys Oy',
                    'current_activity_status': u'active',
                    'established_date': date(2009, 12, 31),
                    'terminated_date': date(2009, 12, 31),
                }
            ],
            'stat_employer_register_status': u'never_registered',
            'stat_revenue_size': u'100-200',
            'stat_staff_size': u'4-9',
            'stat_vat_register_status': u'currently_registered',
            'stat_standard_industrial_classification2008': u'Kaivostoiminta',
            'stat_tax_prepayment_register_status': u'previously_registered',
        }

    def test_list_with_query(self, netvisor, responses):
        responses.add(
            method='GET',
            url='http://koulutus.netvisor.fi/CompanyList.nv?QueryTerm=acme',
            body=get_response_content('CompanyList.xml'),
            content_type='text/html; charset=utf-8',
            match_querystring=True
        )
        companies = netvisor.companies.list(query=u'acme')
        assert companies == [
            {
                'id': 125,
                'is_active': True,
                'name': u'ACME',
                'finnish_organization_identifier': u'1234567-8'
            }
        ]
