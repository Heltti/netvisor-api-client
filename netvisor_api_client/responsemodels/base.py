"""
netvisor.responsemodels.base
~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
:license: MIT, see LICENSE for more details.
"""

import inflection
import xmltodict

from ..exc import NetvisorError


class Response(object):
    tag_name = None
    raw_data = None
    data = None
    schema_cls = None

    def __init__(self, response):
        self.response = response
        self.parse()
        self.raise_for_failure()
        self.deserialize()

    def parse(self):
        self.raw_data = xmltodict.parse(
            self.response.text, postprocessor=self.postprocess, dict_constructor=dict
        )

    def postprocess(self, _path, key, data):
        return inflection.underscore(key), data

    def deserialize(self):
        if self.schema_cls is not None:
            root_tag_data = self.raw_data["root"][self.tag_name]

            if root_tag_data is not None:
                result = self.schema_cls(strict=True).load(root_tag_data)

                self.data = result.data

    def raise_for_failure(self):
        if not self.is_ok:
            raise NetvisorError.from_status(self.statuses[1])

    @property
    def statuses(self):
        return self.raw_data["root"]["response_status"]["status"]

    @property
    def is_ok(self):
        return self.statuses == "OK"
