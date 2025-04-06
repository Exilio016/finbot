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

from openapi_client.models.budget_array import BudgetArray

class TestBudgetArray(unittest.TestCase):
    """BudgetArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetArray:
        """Test BudgetArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetArray`
        """
        model = BudgetArray()
        if include_optional:
            return BudgetArray(
                data = [
                    openapi_client.models.budget_read.BudgetRead(
                        type = 'budgets', 
                        id = '2', 
                        attributes = openapi_client.models.budget.Budget(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            name = 'Bills', 
                            active = False, 
                            notes = 'Some notes', 
                            order = 5, 
                            auto_budget_type = 'reset', 
                            currency_id = '12', 
                            currency_code = 'EUR', 
                            currency_symbol = '$', 
                            currency_decimal_places = 2, 
                            native_currency_id = '5', 
                            native_currency_code = 'EUR', 
                            native_currency_symbol = '$', 
                            native_currency_decimal_places = 2, 
                            auto_budget_amount = '-1012.12', 
                            native_auto_budget_amount = '-1012.12', 
                            auto_budget_period = 'monthly', 
                            spent = [
                                openapi_client.models.budget_spent.BudgetSpent(
                                    sum = '123.45', 
                                    currency_id = '5', 
                                    currency_code = 'USD', 
                                    currency_symbol = '$', 
                                    currency_decimal_places = 2, )
                                ], ), )
                    ],
                meta = openapi_client.models.meta.Meta(
                    pagination = openapi_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), )
            )
        else:
            return BudgetArray(
                data = [
                    openapi_client.models.budget_read.BudgetRead(
                        type = 'budgets', 
                        id = '2', 
                        attributes = openapi_client.models.budget.Budget(
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            name = 'Bills', 
                            active = False, 
                            notes = 'Some notes', 
                            order = 5, 
                            auto_budget_type = 'reset', 
                            currency_id = '12', 
                            currency_code = 'EUR', 
                            currency_symbol = '$', 
                            currency_decimal_places = 2, 
                            native_currency_id = '5', 
                            native_currency_code = 'EUR', 
                            native_currency_symbol = '$', 
                            native_currency_decimal_places = 2, 
                            auto_budget_amount = '-1012.12', 
                            native_auto_budget_amount = '-1012.12', 
                            auto_budget_period = 'monthly', 
                            spent = [
                                openapi_client.models.budget_spent.BudgetSpent(
                                    sum = '123.45', 
                                    currency_id = '5', 
                                    currency_code = 'USD', 
                                    currency_symbol = '$', 
                                    currency_decimal_places = 2, )
                                ], ), )
                    ],
                meta = openapi_client.models.meta.Meta(
                    pagination = openapi_client.models.meta_pagination.Meta_pagination(
                        total = 3, 
                        count = 20, 
                        per_page = 100, 
                        current_page = 1, 
                        total_pages = 1, ), ),
        )
        """

    def testBudgetArray(self):
        """Test BudgetArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
