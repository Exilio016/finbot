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

from openapi_client.models.transaction_read import TransactionRead

class TestTransactionRead(unittest.TestCase):
    """TransactionRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionRead:
        """Test TransactionRead
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TransactionRead`
        """
        model = TransactionRead()
        if include_optional:
            return TransactionRead(
                type = 'transactions',
                id = '2',
                attributes = openapi_client.models.transaction.Transaction(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    user = '3', 
                    group_title = 'Split transaction title.', 
                    transactions = [
                        openapi_client.models.transaction_split.TransactionSplit(
                            user = '3', 
                            transaction_journal_id = '10421', 
                            type = 'withdrawal', 
                            date = '2018-09-17T12:46:47+01:00', 
                            order = 0, 
                            currency_id = '12', 
                            currency_code = 'EUR', 
                            currency_symbol = '$', 
                            currency_name = 'Euro', 
                            currency_decimal_places = 2, 
                            foreign_currency_id = '17', 
                            foreign_currency_code = 'USD', 
                            foreign_currency_symbol = '$', 
                            foreign_currency_decimal_places = 2, 
                            amount = '123.45', 
                            foreign_amount = '123.45', 
                            description = 'Vegetables', 
                            source_id = '2', 
                            source_name = 'Checking account', 
                            source_iban = 'NL02ABNA0123456789', 
                            source_type = 'Asset account', 
                            destination_id = '2', 
                            destination_name = 'Buy and Large', 
                            destination_iban = 'NL02ABNA0123456789', 
                            destination_type = 'Asset account', 
                            budget_id = '4', 
                            budget_name = 'Groceries', 
                            category_id = '43', 
                            category_name = 'Groceries', 
                            bill_id = '111', 
                            bill_name = 'Monthly rent', 
                            reconciled = False, 
                            notes = 'Some example notes', 
                            tags = [
                                'Barbecue preparation'
                                ], 
                            internal_reference = '', 
                            external_id = '', 
                            external_url = '', 
                            original_source = '', 
                            recurrence_id = '', 
                            recurrence_total = 0, 
                            recurrence_count = 12, 
                            bunq_payment_id = '', 
                            import_hash_v2 = '', 
                            sepa_cc = '', 
                            sepa_ct_op = '', 
                            sepa_ct_id = '', 
                            sepa_db = '', 
                            sepa_country = '', 
                            sepa_ep = '', 
                            sepa_ci = '', 
                            sepa_batch_id = '', 
                            interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = 51.983333, 
                            longitude = 5.916667, 
                            zoom_level = 6, 
                            has_attachments = False, )
                        ], ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), )
            )
        else:
            return TransactionRead(
                type = 'transactions',
                id = '2',
                attributes = openapi_client.models.transaction.Transaction(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    user = '3', 
                    group_title = 'Split transaction title.', 
                    transactions = [
                        openapi_client.models.transaction_split.TransactionSplit(
                            user = '3', 
                            transaction_journal_id = '10421', 
                            type = 'withdrawal', 
                            date = '2018-09-17T12:46:47+01:00', 
                            order = 0, 
                            currency_id = '12', 
                            currency_code = 'EUR', 
                            currency_symbol = '$', 
                            currency_name = 'Euro', 
                            currency_decimal_places = 2, 
                            foreign_currency_id = '17', 
                            foreign_currency_code = 'USD', 
                            foreign_currency_symbol = '$', 
                            foreign_currency_decimal_places = 2, 
                            amount = '123.45', 
                            foreign_amount = '123.45', 
                            description = 'Vegetables', 
                            source_id = '2', 
                            source_name = 'Checking account', 
                            source_iban = 'NL02ABNA0123456789', 
                            source_type = 'Asset account', 
                            destination_id = '2', 
                            destination_name = 'Buy and Large', 
                            destination_iban = 'NL02ABNA0123456789', 
                            destination_type = 'Asset account', 
                            budget_id = '4', 
                            budget_name = 'Groceries', 
                            category_id = '43', 
                            category_name = 'Groceries', 
                            bill_id = '111', 
                            bill_name = 'Monthly rent', 
                            reconciled = False, 
                            notes = 'Some example notes', 
                            tags = [
                                'Barbecue preparation'
                                ], 
                            internal_reference = '', 
                            external_id = '', 
                            external_url = '', 
                            original_source = '', 
                            recurrence_id = '', 
                            recurrence_total = 0, 
                            recurrence_count = 12, 
                            bunq_payment_id = '', 
                            import_hash_v2 = '', 
                            sepa_cc = '', 
                            sepa_ct_op = '', 
                            sepa_ct_id = '', 
                            sepa_db = '', 
                            sepa_country = '', 
                            sepa_ep = '', 
                            sepa_ci = '', 
                            sepa_batch_id = '', 
                            interest_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            book_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            process_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            payment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            latitude = 51.983333, 
                            longitude = 5.916667, 
                            zoom_level = 6, 
                            has_attachments = False, )
                        ], ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), ),
        )
        """

    def testTransactionRead(self):
        """Test TransactionRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
