"""
netvisor.schemas.replies
~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

from marshmallow import Schema, fields, post_load


class RepliesSchema(Schema):
    inserted_data_identifier = fields.Integer()

    @post_load
    def preprocess_replies(self, input_data):
        return input_data["inserted_data_identifier"]


class DimensionRepliesSchema(Schema):
    pass
