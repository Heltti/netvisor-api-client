from netvisor_api_client import Netvisor
import decimal

client = Netvisor(
            host='https://isvapi.netvisor.fi',
            sender='Demokayttaja Tilitoimisto Likvidi Oy',
            partner_id='Til_29717',
            partner_key='E511E2AC07B2F398D2274CFB9F307312',
            customer_id='TD_102739_40763',
            customer_key='A2316508C2440FA61E4E5367B6531043',
            organization_id="0937054-2",
            language='EN'
        )


product = {
            'product_base_information': {
                'product_code': u'CC',
                'product_group': u'Kirjat',
                'name': u'Code Complete',
                'description': u'Toinen painos',
                'unit_price': {
                    'amount': decimal.Decimal('42.5'),
                    'type': 'net'
                },
                'unit': u'kpl',
                'comission_percentage': decimal.Decimal('11'),
                'is_active': True,
                'is_sales_product': False,
            },
            'product_book_keeping_details': {
                'default_vat_percentage': decimal.Decimal('24')
                }
            }

client.products.create(product)

