# Netvisor: Python API client

[![PyPI version](https://badge.fury.io/py/netvisor_api_client.svg)](https://badge.fury.io/py/netvisor_api_client)
[![License](https://img.shields.io/pypi/l/netvisor_api_client)](https://pypi.org/project/netvisor_api_client)
[![Downloads](https://pepy.tech/badge/netvisor_api_client)](https://pepy.tech/project/netvisor_api_client)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)

---

Python client for the Netvisor API.

---

## Installation

You can install netvisor with pip::

    $ pip install netvisor-api-client

## Usage example

```python
from netvisor_api_client import Netvisor
from datetime import date, timedelta

# Create a client
client = Netvisor(
    host="https://isvapi.netvisor.fi",
    sender="Test client",
    partner_id="x",
    partner_key="x",
    customer_id="x",
    customer_key="x",
    organization_id="1967543-8",
    language="EN"
)

# Get a list of sales invoices for last 14 days
invoices = client.sales_invoices.list(start_date=date.today() - timedelta(days=14), end_date=date.today())

# Get detailed information for the first invoice
invoice_details = client.sales_invoices.get(invoices[0]['netvisor_key'])
```

## Running tests

Run tests locally using pytest or by running docker
`docker run --rm -it $(docker build -f tests.dockerfile -q .)`

## Known issues

### Language

Using language other than `EN` can cause failures when parsing responses containing localised boolean like values.

Example: `"Yes"` and `"No"` parsed to bool `True` and `False` fails when language is FI

```python
from netvisor_api_client.schemas.fields import Boolean

# Current schema
match_partial_payments_by_default = Boolean(true="Yes", false="No")

# i.e. for FI this should be
match_partial_payments_by_default = Boolean(true="Kyllä", false="Ei")
```

## Resources

- Bug Tracker <https://github.com/Heltti/netvisor-api-client/issues>
- Code <https://github.com/Heltti/netvisor-api-client>
