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
# Erääntyneet
overdue_list = client.sales_invoices.list(status='overdue')
print(len(overdue_list))
sum = 0
for invoice in overdue_list:
    sum = sum + invoice['sum']

print(sum)