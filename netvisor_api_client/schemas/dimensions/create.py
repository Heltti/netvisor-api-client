from marshmallow import fields

from ..common import RejectUnknownFieldsSchema


class DimensionItemSchema(RejectUnknownFieldsSchema):
    name = fields.String(required=True)
    item = fields.String(required=True)
    old_item = fields.String()
    father_id = fields.Integer()
    father_name = fields.String()
    is_hidden = fields.Boolean(true='1', false='0')


class CreateDimensionItemSchema(RejectUnknownFieldsSchema):
    dimension_item = fields.Nested(DimensionItemSchema)

    class Meta:
        ordered = True