from ..schemas.dimensions import DimensionNameListSchema
from ..schemas.replies import DimensionRepliesSchema
from .base import Response


class DimensionListResponse(Response):
    schema_cls = DimensionNameListSchema
    tag_name = "dimension_name_list"


class CreateDimensionResponse(Response):
    """
    Dimeonsins response does not have element 'replies'
    """

    schema_cls = DimensionRepliesSchema
    tag_name = "response_status"
