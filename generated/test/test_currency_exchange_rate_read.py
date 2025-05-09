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

from openapi_client.models.currency_exchange_rate_read import CurrencyExchangeRateRead

class TestCurrencyExchangeRateRead(unittest.TestCase):
    """CurrencyExchangeRateRead unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CurrencyExchangeRateRead:
        """Test CurrencyExchangeRateRead
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CurrencyExchangeRateRead`
        """
        model = CurrencyExchangeRateRead()
        if include_optional:
            return CurrencyExchangeRateRead(
                type = 'currency_exchange_rates',
                id = '2',
                attributes = openapi_client.models.currency_exchange_rate_read_attributes.CurrencyExchangeRateReadAttributes(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    from_currency_id = '12', 
                    from_currency_code = 'EUR', 
                    from_currency_symbol = '$', 
                    from_currency_decimal_places = 2, 
                    to_currency_id = '12', 
                    to_currency_code = 'EUR', 
                    to_currency_symbol = '$', 
                    to_currency_decimal_places = 2, 
                    rate = '1.10340', 
                    date = '2018-09-17T12:46:47+01:00', ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), )
            )
        else:
            return CurrencyExchangeRateRead(
                type = 'currency_exchange_rates',
                id = '2',
                attributes = openapi_client.models.currency_exchange_rate_read_attributes.CurrencyExchangeRateReadAttributes(
                    created_at = '2018-09-17T12:46:47+01:00', 
                    updated_at = '2018-09-17T12:46:47+01:00', 
                    from_currency_id = '12', 
                    from_currency_code = 'EUR', 
                    from_currency_symbol = '$', 
                    from_currency_decimal_places = 2, 
                    to_currency_id = '12', 
                    to_currency_code = 'EUR', 
                    to_currency_symbol = '$', 
                    to_currency_decimal_places = 2, 
                    rate = '1.10340', 
                    date = '2018-09-17T12:46:47+01:00', ),
                links = openapi_client.models.object_link.ObjectLink(
                    self = 'https://demo.firefly-iii.org/api/v1/OBJECTS/1', 
                    0 = openapi_client.models.object_link_0.ObjectLink_0(
                        rel = 'self', 
                        uri = '/OBJECTS/1', ), ),
        )
        """

    def testCurrencyExchangeRateRead(self):
        """Test CurrencyExchangeRateRead"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
