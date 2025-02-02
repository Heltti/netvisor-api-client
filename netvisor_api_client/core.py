"""
netvisor.core
~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from .auth import NetvisorAuth
from .client import Client
from .services.accounting import AccountingService
from .services.company import CompanyService
from .services.customer import CustomerService
from .services.dimension import DimensionService
from .services.product import ProductService
from .services.purchase_invoice import PurchaseInvoiceService
from .services.sales_invoice import SalesInvoiceService
from .services.sales_payment import SalesPaymentService


class Netvisor(object):
    def __init__(self, host, **kwargs):
        self._client = self._make_client(host, **kwargs)
        self._init_services()

    def _make_client(self, host, **kwargs):
        auth = NetvisorAuth(**kwargs)
        return Client(host, auth)

    def _init_services(self):
        self.companies = CompanyService(self._client)
        self.customers = CustomerService(self._client)
        self.products = ProductService(self._client)
        self.purchase_invoices = PurchaseInvoiceService(self._client)
        self.sales_invoices = SalesInvoiceService(self._client)
        self.sales_payments = SalesPaymentService(self._client)
        self.accounting = AccountingService(self._client)
        self.dimensions = DimensionService(self._client)
