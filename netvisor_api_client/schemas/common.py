"""
    netvisor.schemas.common
    ~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
from marshmallow import (
    MarshalResult,
    Schema,
    ValidationError,
    fields,
    pre_dump,
    pre_load
)

from .fields import Decimal


class RejectUnknownFieldsSchema(Schema):
    @pre_dump
    def check_unknown_fields(self, data):
        field_names = set()
        for field_name, field in self.fields.items():
            attribute = getattr(field, 'attribute', None)
            field_names.add(field_name if attribute is None else attribute)
        for k in data:
            if k not in field_names:
                raise ValidationError("Unknown field name: '{}'".format(k))


class FlattenElementSchema(Schema):
    @pre_load
    def pre_load(self, data):
        if isinstance(data, (str,)):
            return {'#text': data}
        return data

    def load(self, *args, **kwargs):
        result = super(FlattenElementSchema, self).load(*args, **kwargs)
        return MarshalResult(result.data.get('text'), result.errors)


class DateSchema(FlattenElementSchema):
    text = fields.Date(load_from='#text')


class StringSchema(FlattenElementSchema):
    text = fields.String(load_from='#text')


class DecimalSchema(FlattenElementSchema):
    text = Decimal(load_from='#text')
