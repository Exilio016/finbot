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

from openapi_client.models.account import Account

class TestAccount(unittest.TestCase):
    """Account unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Account:
        """Test Account
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Account`
        """
        model = Account()
        if include_optional:
            return Account(
                created_at = '2018-09-17T12:46:47+01:00',
                updated_at = '2018-09-17T12:46:47+01:00',
                active = False,
                order = 1,
                name = 'My checking account',
                type = 'asset',
                account_role = 'defaultAsset',
                currency_id = '12',
                currency_code = 'EUR',
                currency_symbol = '$',
                currency_decimal_places = 2,
                native_currency_id = '12',
                native_currency_code = 'EUR',
                native_currency_symbol = '$',
                native_currency_decimal_places = 2,
                current_balance = '123.45',
                native_current_balance = '123.45',
                current_balance_date = '2018-09-17T12:46:47+01:00',
                notes = 'Some example notes',
                monthly_payment_date = '2018-09-17T12:46:47+01:00',
                credit_card_type = 'monthlyFull',
                account_number = '7009312345678',
                iban = 'GB98MIDL07009312345678',
                bic = 'BOFAUS3N',
                virtual_balance = '123.45',
                native_virtual_balance = '123.45',
                opening_balance = '-1012.12',
                native_opening_balance = '-1012.12',
                opening_balance_date = '2018-09-17T12:46:47+01:00',
                liability_type = 'loan',
                liability_direction = 'credit',
                interest = '5.3',
                interest_period = 'monthly',
                current_debt = '1012.12',
                include_net_worth = True,
                longitude = 5.916667,
                latitude = 51.983333,
                zoom_level = 6
            )
        else:
            return Account(
                name = 'My checking account',
                type = 'asset',
        )
        """

    def testAccount(self):
        """Test Account"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
