"""
netvisor.schemas.fields
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from datetime import datetime

from marshmallow import ValidationError, fields, missing
from marshmallow.utils import is_collection


class Boolean(fields.Boolean):
    def __init__(self, true, false, **kwargs):
        super(Boolean, self).__init__(**kwargs)
        self.truthy = [true]
        self.falsy = [false]

    def _serialize(self, value, attr, obj):
        if value:
            return self.truthy[0]
        else:
            return self.falsy[0]


class Decimal(fields.Decimal):
    def _deserialize(self, value, attr, data):
        return super(Decimal, self)._deserialize(value.replace(",", "."), attr, data)

    def serialize(self, attr, obj, accessor=None):
        value = super(Decimal, self).serialize(attr, obj, accessor)
        if value is missing:
            return value
        return str(value).replace(".", ",")


class FinnishDate(fields.Field):
    def _deserialize(self, value, attr, data):
        msg = "Could not deserialize {0!r} to a date object.".format(value)
        err = ValidationError(getattr(self, "error", None) or msg)
        if not value:  # falsy values are invalid
            raise err
        try:
            return datetime.strptime(value, "%d.%m.%Y").date()
        except (AttributeError, TypeError, ValueError):
            raise err


class List(fields.List):
    def _deserialize(self, value, attr, data):
        if not is_collection(value) and value is not None:
            value = [value]
        return super(List, self)._deserialize(value, attr, data)
