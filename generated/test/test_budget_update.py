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

from openapi_client.models.budget_update import BudgetUpdate

class TestBudgetUpdate(unittest.TestCase):
    """BudgetUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BudgetUpdate:
        """Test BudgetUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BudgetUpdate`
        """
        model = BudgetUpdate()
        if include_optional:
            return BudgetUpdate(
                name = 'Bills',
                active = False,
                order = 5,
                notes = 'Some notes',
                auto_budget_type = 'reset',
                auto_budget_currency_id = '12',
                auto_budget_currency_code = 'EUR',
                auto_budget_amount = '-1012.12',
                auto_budget_period = 'monthly'
            )
        else:
            return BudgetUpdate(
                name = 'Bills',
        )
        """

    def testBudgetUpdate(self):
        """Test BudgetUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
