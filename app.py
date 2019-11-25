"""
Esimerkki tuloste:

{'Myyntilaskut': {'Avoimien määrä': 11,
                  'Erääntyneiden myyntilaskujen määrä': 0,
                  'Erääntyneiden summa': 0,
                  'Hylättyjen määrä': 0},
 'Ostolaskut': {'Hyväksytyt ei tiliöidyt': 3}}
"""

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
    language='FI'
)

data = {'Myyntilaskut': {},
        'Ostolaskut': {}}


def current_month():
    # Hakee kuukauden alusta vain
    return datetime.now().strftime('%Y-%m') + '-1'


def main():
    ### Myyntlaskut
    # Erääntyneet, hakee seuraavat substatusalaiset OVERDUE, REMINDED, REQUESTED, COLLECTED
    overdue_sales_list = client.sales_invoices.list(status='overdue', start_date=current_month())
    data['Myyntilaskut']['Erääntyneiden myyntilaskujen määrä'] = len(overdue_sales_list)

    # TÄTÄ EI TAIDA TARVITA
    invoice_sum = 0
    for invoice in overdue_sales_list:
        invoice_sum += invoice['sum']
    data['Myyntilaskut']['Erääntyneiden summa'] = invoice_sum

    # Avoimet
    open_sales_list = client.sales_invoices.list(status='open', start_date=current_month())
    data['Myyntilaskut']['Avoimien määrä'] = len(open_sales_list)

    # Hylätyt
    rejected_sales_list = client.sales_invoices.list(status='rejected', start_date=current_month())
    data['Myyntilaskut']['Hylättyjen määrä'] = len(rejected_sales_list)

    ### Ostolaskut
    '''
    Tarkista Nonen ja Falsen erot
    '''
    accepted_purchase_list = []
    invoices = client.purchase_invoices.list(status='Accepted', start_date=current_month())
    for invoice in invoices:
        invoice_data = client.purchase_invoices.get(id=invoice['netvisor_key'])
        if invoice_data['accounted'] is False:
            accepted_purchase_list.append(invoice_data)
    data['Ostolaskut']['Hyväksytyt ei tiliöidyt'] = len(accepted_purchase_list)

    return data


if __name__ == '__main__':
    main()
