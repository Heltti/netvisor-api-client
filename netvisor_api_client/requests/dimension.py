from .base import Request, ListRequest
from ..responses.dimensions import CreateDimensionResponse, DimensionListResponse
from ..schemas.dimensions import CreateDimensionItemSchema


class ListDimensionsRequest(Request):
    method = 'GET'
    uri = 'DimensionList.nv'
    response_cls = DimensionListResponse

# Check namea remove -s ending
class CreateDimensionsRequest(Request):
    method = 'POST'
    uri = 'DimensionItem.nv'
    response_cls = CreateDimensionResponse
    schema_cls = CreateDimensionItemSchema
    tag_name = 'dimensionitem'


