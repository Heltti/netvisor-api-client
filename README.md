Netvisor: Python API client
============================

This is a Python client for the Netvisor API.

Installation
------------

You can install netvisor with pip::

    $ pip install netvisor-api-client

Usage example
-------------

    # Create a client
    client = Netvisor(
        host='https://isvapi.netvisor.fi',
        sender='Test client',
        partner_id='xxx_yyy',
        partner_key='E2CEBB1966C7016730C70CA92CBB93DD',
        customer_id='xx_yyyy_zz',
        customer_key='7767899D6F5FB333784A2520771E5871',
        organization_id='1967543-8',
        language='EN'
    )

    # Get a list of sales invoices for last 14 days
    invoices = client.sales_invoices.list(start_date=date.today() - timedelta(days=14), end_date=date.today())

    # Get detailed information for the first invoice
    invoice_details = client.sales_invoices.get(invoices[0]['netvisor_key'])

Known issues
------------


**Language**

Using language other than `EN` can cause failures when parsing responses containing localised boolean like values.

Example: `"Yes"` and `"No"` parsed to bool `True` and `False` fails when language is FI

    # Current schema
    match_partial_payments_by_default = Boolean(true='Yes', false='No')

    # i.e. for FI this should be 
    match_partial_payments_by_default = Boolean(true='Kyllä', false='Ei')

Resources
---------

* Bug Tracker <https://github.com/Heltti/netvisor-api-client/issues>
* Code <https://github.com/Heltti/netvisor-api-client>
