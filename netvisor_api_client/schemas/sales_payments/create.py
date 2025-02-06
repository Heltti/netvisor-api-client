"""
netvisor.schemas.sales_payments.create
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:license: MIT, see LICENSE for more details.
"""

from marshmallow import fields, post_dump

from ..common import RejectUnknownFieldsSchema
from ..fields import Decimal


class SalesPaymentSumSchema(RejectUnknownFieldsSchema):
    value = Decimal()
    currency = fields.String()

    @post_dump
    def post_dump(self, data):
        return {"#text": data["value"], "@currency": data["currency"]}


class SalesPaymentTargetIdentifierSchema(RejectUnknownFieldsSchema):
    type = fields.String()
    targettype = fields.String()
    target = fields.String()

    @post_dump
    def post_dump(self, data):
        return {
            "#text": data["target"],
            "@type": data["type"],
            "@targettype": data["targettype"],
        }


class SalesPaymentPaymentMethodSchema(RejectUnknownFieldsSchema):
    type = fields.String(default="alternative")
    override_accounting_account_number = fields.String(allow_none=True)
    override_sales_receivable_account_number = fields.String(allow_none=True)
    method = fields.String()

    @post_dump
    def post_dump(self, data):
        return {"#text": data["method"], "@type": data["type"]}


class SalesPaymentCreateSchema(RejectUnknownFieldsSchema):
    sum = fields.Nested(SalesPaymentSumSchema)
    payment_date = fields.String()
    target_identifier = fields.Nested(SalesPaymentTargetIdentifierSchema)
    source_name = fields.String()
    payment_method = fields.Nested(SalesPaymentPaymentMethodSchema)

    class Meta:
        ordered = True
