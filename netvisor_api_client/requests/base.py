"""
    netvisor.requests.base
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013-2016 by Fast Monkeys Oy | 2019- by Heltti Oy
    :license: MIT, see LICENSE for more details.
"""
import inflection
import xmltodict


class Request(object):
    method = None
    uri = None
    schema_cls = None
    response_cls = None
    tag_name = None

    raw_data = None

    def __init__(self, client, params=None, data=None):
        self.client = client
        self.params = params
        self.data = data
        self.serialize()

    def make_request(self):
        response = self.client.request(
            method=self.method,
            path=self.uri,
            params=self.params,
            headers={'content-type': 'text/xml; charset=utf-8'},
            data=self.unparse()
        )

        return self.parse_response(response)

    def serialize(self):
        if self.schema_cls:
            schema = self.schema_cls(strict=True)

            result = schema.dump(self.data)

            self.raw_data = {
                'root': {
                    self.tag_name: result.data
                }
            }

        else:
            self.raw_data = None

    def unparse(self):
        if self.raw_data is not None:
            xml = xmltodict.unparse(
                self.raw_data,
                preprocessor=self.preprocess,
                pretty=True,
                indent='  '
            )
            return self._remove_xml_declaration(xml).encode('utf-8')

    def _remove_xml_declaration(self, xml):
        return xml.replace('<?xml version="1.0" encoding="utf-8"?>\n', '', 1)

    def preprocess(self, key, value):
        return inflection.camelize(key), value

    def parse_response(self, response):
        response = self.response_cls(response)

        return response.data


class ListRequest(Request):
    def parse_response(self, response):
        response = super(ListRequest, self).parse_response(response=response)

        return response if response is not None else []
