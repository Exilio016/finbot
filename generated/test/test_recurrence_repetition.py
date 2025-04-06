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

from openapi_client.models.recurrence_repetition import RecurrenceRepetition

class TestRecurrenceRepetition(unittest.TestCase):
    """RecurrenceRepetition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RecurrenceRepetition:
        """Test RecurrenceRepetition
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RecurrenceRepetition`
        """
        model = RecurrenceRepetition()
        if include_optional:
            return RecurrenceRepetition(
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
                    ]
            )
        else:
            return RecurrenceRepetition(
                type = 'weekly',
                moment = '3',
        )
        """

    def testRecurrenceRepetition(self):
        """Test RecurrenceRepetition"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
