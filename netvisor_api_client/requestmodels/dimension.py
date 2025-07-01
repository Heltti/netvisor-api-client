from ..responsemodels.dimensions import CreateDimensionResponse, DimensionListResponse
from ..schemas.dimensions import CreateDimensionItemSchema
from .base import ListRequest, Request


class DimensionsListRequest(ListRequest):
    method = "GET"
    uri = "DimensionList.nv"
    response_cls = DimensionListResponse


class CreateDimensionsRequest(Request):
    method = "POST"
    uri = "DimensionItem.nv"
    response_cls = CreateDimensionResponse
    schema_cls = CreateDimensionItemSchema
    tag_name = "dimensionitem"
