from .base import Response
from ..schemas import RepliesSchema
from ..schemas.dimensions import DimensionNameListSchema


class DimensionListResponse(Response):
    schema_cls = DimensionNameListSchema
    tag_name = 'dimensionlist'


class CreateDimensionResponse(Response):
    schema_cls = RepliesSchema
    tag_name = 'replies'