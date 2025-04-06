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

from openapi_client.models.recurrence_read import RecurrenceRead

class TestRecurrenceRead(unittest.TestCase):
    """RecurrenceRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceRead:
        """Test RecurrenceRead
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceRead`
        """
        model = RecurrenceRead()
        if include_optional:
            return RecurrenceRead(
                type = 'recurrences',
                id = '2',
                attributes = openapi_client.models.recurrence.Recurrence(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    type = 'withdrawal', 
                    title = 'Rent', 
                    description = 'Recurring transaction for the monthly rent', 
                    first_date = 'Sun Sep 16 21:00:00 BRT 2018', 
                    latest_date = 'Sun Sep 16 21:00:00 BRT 2018', 
                    repeat_until = 'Sun Sep 16 21:00:00 BRT 2018', 
                    nr_of_repetitions = 5, 
                    apply_rules = True, 
                    active = True, 
                    notes = 'Some notes', 
                    repetitions = [
                        openapi_client.models.recurrence_repetition.RecurrenceRepetition(
                            id = '2', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            type = 'weekly', 
                            moment = '3', 
                            skip = 0, 
                            weekend = 1, 
                            description = 'Every week on Friday', 
                            occurrences = [
                                '2018-09-17T12:46:47+01:00'
                                ], )
                        ], 
                    transactions = [
                        openapi_client.models.recurrence_transaction.RecurrenceTransaction(
                            id = 'ID of the recurring transaction. Not to be confused with the ID of the recurrence itself.', 
                            description = 'Rent for the current month', 
                            amount = '123.45', 
                            foreign_amount = '123.45', 
                            currency_id = '3', 
                            currency_code = 'EUR', 
                            currency_symbol = '€', 
                            currency_decimal_places = 2, 
                            foreign_currency_id = '17', 
                            foreign_currency_code = 'GBP', 
                            foreign_currency_symbol = '$', 
                            foreign_currency_decimal_places = 2, 
                            budget_id = '4', 
                            budget_name = 'Groceries', 
                            category_id = '211', 
                            category_name = 'Bills', 
                            source_id = '913', 
                            source_name = 'Checking account', 
                            source_iban = 'NL02ABNA0123456789', 
                            source_type = 'Asset account', 
                            destination_id = '258', 
                            destination_name = 'Buy and Large', 
                            destination_iban = 'NL02ABNA0123456789', 
                            destination_type = 'Asset account', 
                            tags = [
                                'Barbecue preparation'
                                ], 
                            piggy_bank_id = '123', 
                            piggy_bank_name = '', 
                            bill_id = '123', 
                            bill_name = '', )
                        ], ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), )
            )
        else:
            return RecurrenceRead(
                type = 'recurrences',
                id = '2',
                attributes = openapi_client.models.recurrence.Recurrence(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    type = 'withdrawal', 
                    title = 'Rent', 
                    description = 'Recurring transaction for the monthly rent', 
                    first_date = 'Sun Sep 16 21:00:00 BRT 2018', 
                    latest_date = 'Sun Sep 16 21:00:00 BRT 2018', 
                    repeat_until = 'Sun Sep 16 21:00:00 BRT 2018', 
                    nr_of_repetitions = 5, 
                    apply_rules = True, 
                    active = True, 
                    notes = 'Some notes', 
                    repetitions = [
                        openapi_client.models.recurrence_repetition.RecurrenceRepetition(
                            id = '2', 
                            created_at = '2018-09-17T12:46:47+01:00', 
                            updated_at = '2018-09-17T12:46:47+01:00', 
                            type = 'weekly', 
                            moment = '3', 
                            skip = 0, 
                            weekend = 1, 
                            description = 'Every week on Friday', 
                            occurrences = [
                                '2018-09-17T12:46:47+01:00'
                                ], )
                        ], 
                    transactions = [
                        openapi_client.models.recurrence_transaction.RecurrenceTransaction(
                            id = 'ID of the recurring transaction. Not to be confused with the ID of the recurrence itself.', 
                            description = 'Rent for the current month', 
                            amount = '123.45', 
                            foreign_amount = '123.45', 
                            currency_id = '3', 
                            currency_code = 'EUR', 
                            currency_symbol = '€', 
                            currency_decimal_places = 2, 
                            foreign_currency_id = '17', 
                            foreign_currency_code = 'GBP', 
                            foreign_currency_symbol = '$', 
                            foreign_currency_decimal_places = 2, 
                            budget_id = '4', 
                            budget_name = 'Groceries', 
                            category_id = '211', 
                            category_name = 'Bills', 
                            source_id = '913', 
                            source_name = 'Checking account', 
                            source_iban = 'NL02ABNA0123456789', 
                            source_type = 'Asset account', 
                            destination_id = '258', 
                            destination_name = 'Buy and Large', 
                            destination_iban = 'NL02ABNA0123456789', 
                            destination_type = 'Asset account', 
                            tags = [
                                'Barbecue preparation'
                                ], 
                            piggy_bank_id = '123', 
                            piggy_bank_name = '', 
                            bill_id = '123', 
                            bill_name = '', )
                        ], ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), ),
        )
        """

    def testRecurrenceRead(self):
        """Test RecurrenceRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
