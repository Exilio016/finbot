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

from openapi_client.api.recurrences_api import RecurrencesApi


class TestRecurrencesApi(unittest.TestCase):
    """RecurrencesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RecurrencesApi()

    def tearDown(self) -> None:
        pass

    def test_delete_recurrence(self) -> None:
        """Test case for delete_recurrence

        Delete a recurring transaction.
        """
        pass

    def test_get_recurrence(self) -> None:
        """Test case for get_recurrence

        Get a single recurring transaction.
        """
        pass

    def test_list_recurrence(self) -> None:
        """Test case for list_recurrence

        List all recurring transactions.
        """
        pass

    def test_list_transaction_by_recurrence(self) -> None:
        """Test case for list_transaction_by_recurrence

        List all transactions created by a recurring transaction.
        """
        pass

    def test_store_recurrence(self) -> None:
        """Test case for store_recurrence

        Store a new recurring transaction
        """
        pass

    def test_update_recurrence(self) -> None:
        """Test case for update_recurrence

        Update existing recurring transaction.
        """
        pass


if __name__ == '__main__':
    unittest.main()
