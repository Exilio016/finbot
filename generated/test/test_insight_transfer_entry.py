# coding: utf-8

"""
    Firefly III API v6.2.9

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2025-03-05T19:12:52+00:00 Please keep in mind that the demo site does not accept requests from curl, colly, wget, etc. You must use a browser or a tool like Postman to make requests. Too many script kiddies out there, sorry about that. 

    The version of the OpenAPI document: v6.2.9
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.insight_transfer_entry import InsightTransferEntry

class TestInsightTransferEntry(unittest.TestCase):
    """InsightTransferEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InsightTransferEntry:
        """Test InsightTransferEntry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InsightTransferEntry`
        """
        model = InsightTransferEntry()
        if include_optional:
            return InsightTransferEntry(
                id = '123',
                name = 'Land lord',
                difference = '-123.45',
                difference_float = -123.45,
                var_in = '123.45',
                in_float = 123.45,
                out = '123.45',
                out_float = 123.45,
                currency_id = '5',
                currency_code = 'EUR'
            )
        else:
            return InsightTransferEntry(
        )
        """

    def testInsightTransferEntry(self):
        """Test InsightTransferEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
