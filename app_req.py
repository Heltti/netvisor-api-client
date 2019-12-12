from netvisor_api_client import Netvisor
from decimal import Decimal
from datetime import date

client = Netvisor(
            host='https://isvapi.netvisor.fi',
            sender='Demokayttaja Tilitoimisto Likvidi Oy',
            partner_id='Til_29717',
            partner_key='E511E2AC07B2F398D2274CFB9F307312',
            customer_id='TD_102739_56013',
            customer_key='CFC7FC4B7B96BA6D4A7EA51226C3AE84',
            organization_id="0937054-2",
            language='FI'
        )


product = {
            'product_base_information': {
                'product_code': u'H2Q0103000450S2SXS18',
                'product_group': u'H WW STD 30 x 45 S2S S 18%',
                'name': u'Code Complete',
                'description': u'Puuta',
                'unit_price': {
                    'amount': Decimal('310.00'),
                    'type': 'net'
                },
                'unit': u'M3',
                'is_active': True,
                'is_sales_product': False,
                'inventory_enabled': True,
                'country_of_origin': 'FI'
            }
            }

invoice = {
            'amount': Decimal('10878.52'),
            'currency': 'EUR',
            'date': date(2020, 11, 14),
            'delivery_address_country_code': 'FI',
            'delivery_address_line': 'Tuomikoskentie 2 A',
            'delivery_address_name': 'Toivakka Timber Ltd Oy',
            'delivery_address_post_number': '81720',
            'delivery_address_town': 'Lieksa',
            'invoice_lines': [{'identifier': {'identifier': 'H2Q0103000450S2SXS18',
                                   'type': 'netvisor'},
                    'name': 'H WW STD 30 x 45 S2S S 18%',
                    'quantity': '28.30',
                    'unit_price': {'amount': '310.000', 'type': 'net'},
                    'vat_percentage': {'code': 'KOOS', 'percentage': '24.00'}}],
            'invoice_type': 'invoice',
            'invoicing_customer_address_line': 'Tuomikoskentie 2 A',
            'invoicing_customer_country_code': 'FI',
            'invoicing_customer_identifier': '1006',
            'invoicing_customer_name': 'Toivakka Timber Ltd Oy',
            'invoicing_customer_post_number': '81720',
            'invoicing_customer_town': 'Lieksa',
            'number': '12190516',
            'payment_term_net_days': 14,
            'reference_number': '1006121905168',
            'seller_name': 'Anaika Wood Group Ltd Oy',
            'status': 'unsent'
            }

print(client.products.list())