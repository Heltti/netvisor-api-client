from marshmallow import Schema, fields, post_load
from ..fields import List


class DimensionDetailSchema(Schema):
    netvisor_key = fields.Integer(required=True)
    name = fields.String(required=True)
    item = fields.String(required=True)
    old_item = fields.String(required=True)
    father_id = fields.Integer(required=True)
    father_name = fields.String(required=True)
    is_hidden = fields.Boolean(true='1', false='0')


class DimensionNameSchema(Schema):
    netvisor_key = fields.Integer(required=True)
    name = fields.String(required=True)
    is_hidden = fields.Boolean(true='1', false='0')
    link_type = fields.Integer(required=True)
    dimension_details = fields.Nested(DimensionDetailSchema, load_from='dimension_detail')


class DimensionNameListSchema(Schema):
    dimensions = List(
        fields.Nested(DimensionNameSchema),
        load_from='dimension_name'
    )

    @post_load
    def preprocess_dimension_list(self, input_data):
        return input_data['dimensions'] if input_data else []
