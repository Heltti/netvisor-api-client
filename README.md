Netvisor: Python API client
============================

This is a Python client for the Netvisor API.

Installation
------------

You can install netvisor with pip::

    $ pip install netvisor-api-client

Usage
-----

Creating a Netvisor client::

    >>> netvisor = Netvisor(
    ...     host='https://isvapi.netvisor.fi'
    ...     sender='Test client',
    ...     partner_id='xxx_yyy',
    ...     partner_key='E2CEBB1966C7016730C70CA92CBB93DD',
    ...     customer_id='xx_yyyy_zz',
    ...     customer_key='7767899D6F5FB333784A2520771E5871',
    ...     organization_id='1967543-8',
    ...     language='EN'
    ... )


Resources
---------

* Bug Tracker <https://github.com/Heltti/netvisor-api-client/issues>
* Code <https://github.com/Heltti/netvisor-api-client>
