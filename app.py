'''
Api ei handlaa nyt substatusta osto- ja myyntilaskuissa
'''

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

data = {'Myyntilaskut': {},
        'Ostolaskut': {}}


def current_month():
    # Hakee kuukauden alusta vain
    return datetime.now().strftime('%Y-%m') + '-1'

def data_handler():
    pass

def main():
    ### Myyntlaskut
    # Erääntyneet, hakee seuraavat substatusalaiset OVERDUE, REMINDED, REQUESTED, COLLECTED
    overdue_sales_list = client.sales_invoices.list(status='overdue')
    data['Myyntilaskut']['Erääntyneiden myyntilaskujen määrä'] = len(overdue_sales_list)

    invoice_sum = 0
    for invoice in overdue_sales_list:
        invoice_sum += invoice['sum']
    data['Myyntilaskut']['Erääntyneiden summa'] = invoice_sum

    # Avoimet, OPEN, OVERDUE, REMINDED, REQUESTED, COLLECTED
    open_sales_list = client.sales_invoices.list(status='open')
    data['Myyntilaskut']['Avoimien määrä'] = len(open_sales_list)

    # Hylätyt
    rejected_sales_list = client.sales_invoices.list(status='rejected')
    data['Myyntilaskut']['Hylättyjen määrä'] = len(rejected_sales_list)

    ### Ostolaskut
    '''
    Hakee Kuukauden alusta hyväksytyt ostolaskut 
    '''
    id_list = client.purchase_invoices.list(status='Accepted', start_date=current_month())
    for company in id_list:
        data['Ostolaskut']['Avointen määrä'] = len(open_purchase_list)

    print(data)


if __name__ == '__main__':
    main()
