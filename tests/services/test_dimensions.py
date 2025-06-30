import xmltodict

from tests.utils import get_request_content, get_response_content


class TestDimensionService(object):
    def test_list(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/DimensionList.nv",
            body=get_response_content("DimensionList.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        dimensions = netvisor.dimensions.list()

        assert dimensions == [
            {
                "netvisor_key": 14,
                "name": "Hinnastoryhmä",
                "is_hidden": False,
                "link_type": 0,
                "dimension_details": [
                    {
                        "netvisor_key": 17,
                        "name": "Opiskelijat",
                        "is_hidden": False,
                        "level": 1,
                        "sort": 0,
                        "end_sort": 0,
                        "father_id": 0,
                    },
                    {
                        "netvisor_key": 23,
                        "name": "Eläkeläiset",
                        "is_hidden": False,
                        "level": 1,
                        "sort": 1,
                        "end_sort": 1,
                        "father_id": 0,
                    },
                ],
            },
            {
                "netvisor_key": 9,
                "name": "KP1",
                "is_hidden": True,
                "link_type": 0,
                "dimension_details": [
                    {
                        "netvisor_key": 12,
                        "name": "PL100",
                        "is_hidden": True,
                        "level": 1,
                        "sort": 0,
                        "end_sort": 0,
                        "father_id": 0,
                    }
                ],
            },
        ]

    def test_list_with_zero_dimensions(self, netvisor, responses):
        responses.add(
            method="GET",
            url="https://koulutus.netvisor.fi/DimensionList.nv",
            body=get_response_content("DimensionListMinimal.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )
        dimensions = netvisor.dimensions.list()
        assert dimensions == []

    def test_create_dimension(self, netvisor, responses):
        responses.add(
            method="POST",
            url="https://koulutus.netvisor.fi/DimensionItem.nv?method=add",
            body=get_response_content("DimensionCreate.xml"),
            content_type="text/html; charset=utf-8",
            match_querystring=True,
        )

        netvisor.dimensions.create(
            {
                "name": "Example Dimension",
                "item": "Example Dimension Item Sub-Item 1",
                "father_id": "0",
                "father_item": "Example Dimension Item 2",
                "is_hidden": False,
            }
        )

        request = responses.calls[0].request

        assert xmltodict.parse(request.body) == xmltodict.parse(
            get_request_content("Dimension.xml")
        )
