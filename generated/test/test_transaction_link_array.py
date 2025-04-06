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

from openapi_client.models.transaction_link_array import TransactionLinkArray

class TestTransactionLinkArray(unittest.TestCase):
    """TransactionLinkArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionLinkArray:
        """Test TransactionLinkArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionLinkArray`
        """
        model = TransactionLinkArray()
        if include_optional:
            return TransactionLinkArray(
                data = [
                    openapi_client.models.transaction_link_read.TransactionLinkRead(
                        type = 'transactionLinks', 
                        id = '2', 
                        attributes = openapi_client.models.transaction_link.TransactionLink(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            link_type_id = '5', 
                            link_type_name = 'Is paid by', 
                            inward_id = '131', 
                            outward_id = '131', 
                            notes = 'Some example notes', ), 
                        links = openapi_client.models.object_link.ObjectLink(
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                            0 = openapi_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), ), )
                    ],
                meta = openapi_client.models.meta.Meta(
                    pagination = openapi_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), ),
                links = openapi_client.models.page_link.PageLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=4', 
                    first = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=1', 
                    next = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=3', 
                    prev = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=2', 
                    last = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=12', )
            )
        else:
            return TransactionLinkArray(
                data = [
                    openapi_client.models.transaction_link_read.TransactionLinkRead(
                        type = 'transactionLinks', 
                        id = '2', 
                        attributes = openapi_client.models.transaction_link.TransactionLink(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            link_type_id = '5', 
                            link_type_name = 'Is paid by', 
                            inward_id = '131', 
                            outward_id = '131', 
                            notes = 'Some example notes', ), 
                        links = openapi_client.models.object_link.ObjectLink(
                            self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                            0 = openapi_client.models.object_link_0.ObjectLink_0(
                                rel = 'self', 
                                uri = '/OBJECTS/1', ), ), )
                    ],
                meta = openapi_client.models.meta.Meta(
                    pagination = openapi_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), ),
                links = openapi_client.models.page_link.PageLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=4', 
                    first = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=1', 
                    next = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=3', 
                    prev = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=2', 
                    last = 'https://demo.firefly-iii.org/api/v1/OBJECT?&page=12', ),
        )
        """

    def testTransactionLinkArray(self):
        """Test TransactionLinkArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
