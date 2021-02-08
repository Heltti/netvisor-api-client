from .base import Response
from ..schemas.replies import DimensionRepliesSchema
from ..schemas.dimensions import DimensionNameListSchema


class DimensionListResponse(Response):
    schema_cls = DimensionNameListSchema
    tag_name = 'dimension_name_list'


class CreateDimensionResponse(Response):
    '''
    Dimeonsins response does not have element 'replies'
    '''
    schema_cls = DimensionRepliesSchema
    tag_name = 'response_status'