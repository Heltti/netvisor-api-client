"""
netvisor.schemas.accounting.ledger
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from marshmallow import Schema, fields, post_load

from ..fields import Decimal, FinnishDate, List


class DimensionSchema(Schema):
    name = fields.String(load_from="dimension_name")
    item = fields.String(load_from="dimension_item", allow_none=True)


class VoucherLineSchema(Schema):
    key = fields.Integer(load_from="netvisor_key")
    line_sum = Decimal()
    description = fields.String(allow_none=True)
    account_number = fields.Integer()
    vat_percent = fields.Integer()
    vat_code = fields.String(allow_none=True)
    dimensions = List(
        fields.Nested(DimensionSchema), load_from="dimension", missing=list
    )


class VoucherNetvisorURISchema(Schema):
    type = fields.String(load_from="@type")
    key = fields.Integer(load_from="#text")


class VoucherSchema(Schema):
    status = fields.String(load_from="@status")
    key = fields.Integer(load_from="netvisor_key")
    date = FinnishDate(load_from="voucher_date")
    number = fields.Integer(load_from="voucher_number")
    description = fields.String(load_from="voucher_description", allow_none=True)
    class_ = fields.String(attribute="class", load_from="voucher_class")
    linked_source = fields.Nested(
        VoucherNetvisorURISchema, load_from="linked_source_netvisor_key"
    )
    uri = fields.String(load_from="voucher_netvisor_uri")
    lines = List(
        fields.Nested(VoucherLineSchema), load_from="voucher_line", missing=list
    )


class AccountingLedgerSchema(Schema):
    vouchers = List(fields.Nested(VoucherSchema), load_from="voucher")

    @post_load
    def preprocess_voucher_list(self, input_data):
        return input_data["vouchers"] if input_data else []
