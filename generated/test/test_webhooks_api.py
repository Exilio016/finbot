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

from openapi_client.api.webhooks_api import WebhooksApi


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_delete_webhook(self) -> None:
        """Test case for delete_webhook

        Delete a webhook.
        """
        pass

    def test_delete_webhook_message(self) -> None:
        """Test case for delete_webhook_message

        Delete a webhook message.
        """
        pass

    def test_delete_webhook_message_attempt(self) -> None:
        """Test case for delete_webhook_message_attempt

        Delete a webhook attempt.
        """
        pass

    def test_get_single_webhook_message(self) -> None:
        """Test case for get_single_webhook_message

        Get a single message from a webhook.
        """
        pass

    def test_get_single_webhook_message_attempt(self) -> None:
        """Test case for get_single_webhook_message_attempt

        Get a single failed attempt from a single webhook message.
        """
        pass

    def test_get_webhook(self) -> None:
        """Test case for get_webhook

        Get a single webhook.
        """
        pass

    def test_get_webhook_message_attempts(self) -> None:
        """Test case for get_webhook_message_attempts

        Get all the failed attempts of a single webhook message.
        """
        pass

    def test_get_webhook_messages(self) -> None:
        """Test case for get_webhook_messages

        Get all the messages of a single webhook.
        """
        pass

    def test_list_webhook(self) -> None:
        """Test case for list_webhook

        List all webhooks.
        """
        pass

    def test_store_webhook(self) -> None:
        """Test case for store_webhook

        Store a new webhook
        """
        pass

    def test_submit_webook(self) -> None:
        """Test case for submit_webook

        Submit messages for a webhook.
        """
        pass

    def test_trigger_transaction_webhook(self) -> None:
        """Test case for trigger_transaction_webhook

        Trigger webhook for a given transaction.
        """
        pass

    def test_update_webhook(self) -> None:
        """Test case for update_webhook

        Update existing webhook.
        """
        pass


if __name__ == '__main__':
    unittest.main()
