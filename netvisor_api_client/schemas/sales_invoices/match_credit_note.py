from marshmallow import fields

from ..common import RejectUnknownFieldsSchema


class SalesInvoiceMatchCreditNoteSchema(RejectUnknownFieldsSchema):
    credit_note_netvisor_key = fields.Integer()
    invoice_netvisor_key = fields.Integer()

    class Meta:
        ordered = True
