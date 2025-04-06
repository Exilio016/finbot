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

from openapi_client.models.recurrence_store import RecurrenceStore

class TestRecurrenceStore(unittest.TestCase):
    """RecurrenceStore unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceStore:
        """Test RecurrenceStore
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceStore`
        """
        model = RecurrenceStore()
        if include_optional:
            return RecurrenceStore(
                type = 'withdrawal',
                title = 'Rent',
                description = 'Recurring transaction for the monthly rent',
                first_date = 'Sun Sep 16 21:00:00 BRT 2018',
                repeat_until = 'Sun Sep 16 21:00:00 BRT 2018',
                nr_of_repetitions = 5,
                apply_rules = True,
                active = True,
                notes = 'Some notes',
                repetitions = [
                    openapi_client.models.recurrence_repetition_store.RecurrenceRepetitionStore(
                        type = 'weekly', 
                        moment = '3', 
                        skip = 0, 
                        weekend = 1, )
                    ],
                transactions = [
                    openapi_client.models.recurrence_transaction_store.RecurrenceTransactionStore(
                        description = 'Rent for the current month', 
                        amount = '123.45', 
                        foreign_amount = '123.45', 
                        currency_id = '3', 
                        currency_code = 'EUR', 
                        foreign_currency_id = '17', 
                        foreign_currency_code = 'GBP', 
                        budget_id = '4', 
                        category_id = '211', 
                        source_id = '913', 
                        destination_id = '258', 
                        tags = [
                            'Barbecue preparation'
                            ], 
                        piggy_bank_id = '123', 
                        bill_id = '123', )
                    ]
            )
        else:
            return RecurrenceStore(
                type = 'withdrawal',
                title = 'Rent',
                first_date = 'Sun Sep 16 21:00:00 BRT 2018',
                repeat_until = 'Sun Sep 16 21:00:00 BRT 2018',
                repetitions = [
                    openapi_client.models.recurrence_repetition_store.RecurrenceRepetitionStore(
                        type = 'weekly', 
                        moment = '3', 
                        skip = 0, 
                        weekend = 1, )
                    ],
                transactions = [
                    openapi_client.models.recurrence_transaction_store.RecurrenceTransactionStore(
                        description = 'Rent for the current month', 
                        amount = '123.45', 
                        foreign_amount = '123.45', 
                        currency_id = '3', 
                        currency_code = 'EUR', 
                        foreign_currency_id = '17', 
                        foreign_currency_code = 'GBP', 
                        budget_id = '4', 
                        category_id = '211', 
                        source_id = '913', 
                        destination_id = '258', 
                        tags = [
                            'Barbecue preparation'
                            ], 
                        piggy_bank_id = '123', 
                        bill_id = '123', )
                    ],
        )
        """

    def testRecurrenceStore(self):
        """Test RecurrenceStore"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
