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

from openapi_client.models.user_group_read import UserGroupRead

class TestUserGroupRead(unittest.TestCase):
    """UserGroupRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserGroupRead:
        """Test UserGroupRead
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserGroupRead`
        """
        model = UserGroupRead()
        if include_optional:
            return UserGroupRead(
                type = 'user_groups',
                id = '2',
                attributes = openapi_client.models.user_group_read_attributes.UserGroupReadAttributes(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    in_use = False, 
                    can_see_members = True, 
                    title = 'demo@firefly', 
                    native_currency_id = '12', 
                    native_currency_code = 'EUR', 
                    native_currency_symbol = '$', 
                    native_currency_decimal_places = 2, 
                    members = [
                        openapi_client.models.user_group_read_members.UserGroupReadMembers(
                            user_id = '5', 
                            user_email = 'james@firefly-iii.org', 
                            you = False, 
                            roles = [
                                'owner'
                                ], )
                        ], ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), )
            )
        else:
            return UserGroupRead(
                type = 'user_groups',
                id = '2',
                attributes = openapi_client.models.user_group_read_attributes.UserGroupReadAttributes(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    in_use = False, 
                    can_see_members = True, 
                    title = 'demo@firefly', 
                    native_currency_id = '12', 
                    native_currency_code = 'EUR', 
                    native_currency_symbol = '$', 
                    native_currency_decimal_places = 2, 
                    members = [
                        openapi_client.models.user_group_read_members.UserGroupReadMembers(
                            user_id = '5', 
                            user_email = 'james@firefly-iii.org', 
                            you = False, 
                            roles = [
                                'owner'
                                ], )
                        ], ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), ),
        )
        """

    def testUserGroupRead(self):
        """Test UserGroupRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
