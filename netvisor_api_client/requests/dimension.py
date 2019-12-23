from .base import Request, ListRequest
from ..responses.dimensions import CreateDimensionResponse, DimensionListResponse
from ..schemas.dimensions import CreateDimensionItemSchema


class ListDimensionsRequest(Request):
    method = 'GET'
    uri = 'dimensionlist.nv'
    response_cls = DimensionListResponse


class CreateDimensionsRequest(Request):
    method = 'POST'
    uri = 'dimensionitem.nv'
    response_cls = CreateDimensionResponse
    schema_cls = CreateDimensionItemSchema
    tag_name = 'dimension'


