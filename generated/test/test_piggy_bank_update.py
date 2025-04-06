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

from openapi_client.models.piggy_bank_update import PiggyBankUpdate

class TestPiggyBankUpdate(unittest.TestCase):
    """PiggyBankUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PiggyBankUpdate:
        """Test PiggyBankUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PiggyBankUpdate`
        """
        model = PiggyBankUpdate()
        if include_optional:
            return PiggyBankUpdate(
                name = 'New digital camera',
                accounts = [
                    openapi_client.models.piggy_bank_account_update.PiggyBankAccountUpdate(
                        id = '3', 
                        name = 'Checking account', 
                        current_amount = '123.45', )
                    ],
                currency_id = '5',
                currency_code = 'USD',
                target_amount = '123.45',
                start_date = 'Sun Sep 16 21:00:00 BRT 2018',
                target_date = 'Sun Sep 16 21:00:00 BRT 2018',
                order = 5,
                active = True,
                notes = 'Some notes',
                object_group_id = '5',
                object_group_title = 'Example Group'
            )
        else:
            return PiggyBankUpdate(
        )
        """

    def testPiggyBankUpdate(self):
        """Test PiggyBankUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
