"""
netvisor.schemas.accounting.accountlist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from marshmallow import Schema, fields, post_load

from ..fields import List


class AccountSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisor_key")
    number = fields.Integer(allow_none=True)
    name = fields.String(allow_none=True)
    account_type = fields.String(allow_none=True)
    father_netvisor_key = fields.Integer(allow_none=True)
    is_active = fields.Integer(allow_none=True)
    is_cumulative = fields.Integer(allow_none=True)
    sort = fields.Integer(allow_none=True)
    end_sort = fields.Integer(allow_none=True)
    is_natural_negative = fields.Integer(allow_none=True)


class AccountsSchema(Schema):
    accounts = List(fields.Nested(AccountSchema), load_from="account")

    @post_load
    def preprocess_account_list(self, input_data):
        return input_data["accounts"] if input_data else []


class DefaultAccounts(Schema):
    trade_payables = fields.Integer()
    purchase_vat_receivable = fields.Integer()
    rounding_off_difference = fields.Integer()
    vat_payable = fields.Integer()
    tax_account = fields.Integer()
    advance_payments = fields.Integer()
    sales_receivables = fields.Integer()
    sales_vat_debt = fields.Integer()
    inventory = fields.Integer()
    sales_discount = fields.Integer()
    sales_exchange_rate_differences = fields.Integer()
    collection = fields.Integer()
    purchases_discounts = fields.Integer()
    purchases_exchange_rate_differences = fields.Integer()
    purchase_invoice_accrual = fields.Integer()
    sales_invoice_accrual = fields.Integer()
    purchase_domestic_default = fields.Integer()
    purchase_eu_default = fields.Integer()
    purchase_outside_eu_default = fields.Integer()
    sales_domestic_default = fields.Integer()
    sales_eu_default = fields.Integer()
    sales_outside_eu_default = fields.Integer()


class AccountListSchema(Schema):
    company_default_accounts = fields.Nested(DefaultAccounts)
    accounts = fields.Nested(AccountsSchema)
