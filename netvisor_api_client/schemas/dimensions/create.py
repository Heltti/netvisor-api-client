from marshmallow import fields

from ..common import RejectUnknownFieldsSchema


class CreateDimensionItemSchema(RejectUnknownFieldsSchema):
    name = fields.String(required=True)
    item = fields.String(required=True)
    old_item = fields.String()
    father_id = fields.Integer()
    father_item = fields.String()
    is_hidden = fields.Boolean()

    class Meta:
        ordered = True
