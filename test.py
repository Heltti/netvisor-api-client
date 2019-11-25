from datetime import datetime
from netvisor_api_client import Netvisor

client = Netvisor(
    host='https://integration.netvisor.fi',
    sender='Likvidi Robotti',
    partner_id='Lik_558',
    partner_key='11608A6225D8D4A601320F55984A586A',
    customer_id='TK_16987_1082',
    customer_key='D2A1A66AB1A26DFA8463B392CB2964DA',
    organization_id='0937054-2',
    language='EN'
)


def current_month():
    # Hakee kuukauden alusta vain
    return datetime.now().strftime('%Y-%m') + '-1'

list = client.purchase_invoices.list(start_date=current_month(), status='Accepted')

from pprint import pprint

# Mitä eroa on None & False
data = []
for invoice in list:
    id = invoice['netvisor_key']
    invoice_data = client.purchase_invoices.get(id=id)
    if invoice_data['accounted'] is None or invoice_data['accounted'] is False:
        data.append(invoice_data)


'''
accounted:
True = Esitiliöity, tiliöity
False = Ei tiliöity
None = Ei tiliöity
'''