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

from openapi_client.api.budgets_api import BudgetsApi


class TestBudgetsApi(unittest.TestCase):
    """BudgetsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BudgetsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_budget(self) -> None:
        """Test case for delete_budget

        Delete a budget.
        """
        pass

    def test_delete_budget_limit(self) -> None:
        """Test case for delete_budget_limit

        Delete a budget limit.
        """
        pass

    def test_get_budget(self) -> None:
        """Test case for get_budget

        Get a single budget.
        """
        pass

    def test_get_budget_limit(self) -> None:
        """Test case for get_budget_limit

        Get single budget limit.
        """
        pass

    def test_list_attachment_by_budget(self) -> None:
        """Test case for list_attachment_by_budget

        Lists all attachments of a budget.
        """
        pass

    def test_list_budget(self) -> None:
        """Test case for list_budget

        List all budgets.
        """
        pass

    def test_list_budget_limit(self) -> None:
        """Test case for list_budget_limit

        Get list of budget limits by date
        """
        pass

    def test_list_budget_limit_by_budget(self) -> None:
        """Test case for list_budget_limit_by_budget

        Get all limits for a budget.
        """
        pass

    def test_list_transaction_by_budget(self) -> None:
        """Test case for list_transaction_by_budget

        All transactions to a budget.
        """
        pass

    def test_list_transaction_by_budget_limit(self) -> None:
        """Test case for list_transaction_by_budget_limit

        List all transactions by a budget limit ID.
        """
        pass

    def test_list_transaction_without_budget(self) -> None:
        """Test case for list_transaction_without_budget

        All transactions without a budget.
        """
        pass

    def test_store_budget(self) -> None:
        """Test case for store_budget

        Store a new budget
        """
        pass

    def test_store_budget_limit(self) -> None:
        """Test case for store_budget_limit

        Store new budget limit.
        """
        pass

    def test_update_budget(self) -> None:
        """Test case for update_budget

        Update existing budget.
        """
        pass

    def test_update_budget_limit(self) -> None:
        """Test case for update_budget_limit

        Update existing budget limit.
        """
        pass


if __name__ == '__main__':
    unittest.main()
