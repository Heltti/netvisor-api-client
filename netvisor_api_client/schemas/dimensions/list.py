from marshmallow import Schema, fields, post_load
from ..fields import List


class DimensionDetailSchema(Schema):
    netvisor_key = fields.Integer()
    name = fields.String()
    item = fields.String()
    old_item = fields.String()
    father_id = fields.Integer()
    father_name = fields.String()
    is_hidden = fields.Boolean(true='1', false='0')


class DimensionNameSchema(Schema):
    netvisor_key = fields.Integer()
    name = fields.String()
    is_hidden = fields.Boolean(true='1', false='0')
    link_type = fields.Integer()
    #dimension_details = fields.Nested(DimensionDetailSchema, load_from='dimension_detail', required=False)
    '''
    marshmallow.exceptions.ValidationError: {'dimension_name': {0: {'dimension_details': ['Field may not be null.']}}}
    '''

class DimensionNameListSchema(Schema):
    dimensions = List(
        fields.Nested(DimensionNameSchema),
        load_from='dimension_name'
    )

    @post_load
    def preprocess_dimension_list(self, input_data):
        return input_data['dimensions'] if input_data else []
