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
'''
Api ei handlaa nyt substatusta osto- ja myyntilaskuissa
'''
data = {'Myyntilaskut': {},
        'Ostolaskut': {}}
### Myyntlaskut
# Erääntyneet, hakee seuraavat substatusalaiset OVERDUE, REMINDED, REQUESTED, COLLECTED
overdue_sales_list = client.sales_invoices.list(status='overdue')
data['Myyntilaskut']['Erääntyneiden myyntilaskujen määrä'] = len(overdue_sales_list)

sum = 0
for invoice in overdue_sales_list:
    sum = sum + invoice['sum']
data['Myyntilaskut']['Erääntyneiden summa'] = sum

# Avoimet, OPEN, OVERDUE, REMINDED, REQUESTED, COLLECTED
open_sales_list = client.sales_invoices.list(status='open')
data['Myyntilaskut']['Avoimien määrä'] = len(open_sales_list)

# Hylätyt
rejected_sales_list = client.sales_invoices.list(status='rejected')
data['Myyntilaskut']['Hylättyjen määrä'] = len(rejected_sales_list)

### Ostolaskut
open_purchase_list = client.purchase_invoices.list(status='Open')
data['Ostolaskut']['Avointen määrä'] = len(open_purchase_list)

print(data)