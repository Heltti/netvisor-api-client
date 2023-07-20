from marshmallow import Schema, fields, post_load

from ..fields import List


class DimensionDetailSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisorkey", required=True)
    name = fields.String(required=True)
    is_hidden = fields.Boolean(required=True)
    level = fields.Integer(required=True)
    sort = fields.Integer(required=True)
    end_sort = fields.Integer(required=True)
    father_id = fields.Integer(required=True)


class DimensionDetailsSchema(Schema):
    dimension_detail = List(fields.Nested(DimensionDetailSchema), allow_none=True)

    @post_load
    def preprocess_details_list(self, input_data):
        return input_data["dimension_detail"] if input_data else []


class DimensionNameSchema(Schema):
    netvisor_key = fields.Integer(load_from="netvisorkey", required=True)
    name = fields.String()
    is_hidden = fields.Boolean(required=True)
    link_type = fields.Integer(required=True)
    dimension_details = fields.Nested(DimensionDetailsSchema, allow_none=True)

    class Meta:
        ordered = True


class DimensionNameListSchema(Schema):
    dimensions = List(fields.Nested(DimensionNameSchema), load_from="dimension_name")

    @post_load
    def preprocess_dimension_list(self, input_data):
        return input_data["dimensions"] if input_data else []
