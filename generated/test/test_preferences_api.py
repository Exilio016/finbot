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

from openapi_client.api.preferences_api import PreferencesApi


class TestPreferencesApi(unittest.TestCase):
    """PreferencesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PreferencesApi()

    def tearDown(self) -> None:
        pass

    def test_get_preference(self) -> None:
        """Test case for get_preference

        Return a single preference.
        """
        pass

    def test_list_preference(self) -> None:
        """Test case for list_preference

        List all users preferences.
        """
        pass

    def test_store_preference(self) -> None:
        """Test case for store_preference

        Store a new preference for this user.
        """
        pass

    def test_update_preference(self) -> None:
        """Test case for update_preference

        Update preference
        """
        pass


if __name__ == '__main__':
    unittest.main()
