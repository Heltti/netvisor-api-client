from netvisor_api_client import Netvisor
from decimal import Decimal

client = Netvisor(
            host='https://isvapi.netvisor.fi',
            sender='Demokayttaja Tilitoimisto Likvidi Oy',
            partner_id='Til_29717',
            partner_key='E511E2AC07B2F398D2274CFB9F307312',
            customer_id='TD_102739_40763',
            customer_key='A2316508C2440FA61E4E5367B6531043',
            organization_id="0937054-2",
            language='FI'
        )


product = {
    "product_code": "cc",
    "name": 'Puuta',
    "description": "Paaaljon puuuta",
    "unit_price": {
        "amount": Decimal(30.23),
        "type": "M3"
    },
    "is_active": 1,
    "default_vat_percentage": Decimal(24.00),
}
print(client.purchase_invoices.list())
client.products.create(product)

