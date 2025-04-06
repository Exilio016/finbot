# coding: utf-8

"""
    Firefly III API v6.2.9

    This is the documentation of the Firefly III API. You can find accompanying documentation on the website of Firefly III itself (see below). Please report any bugs or issues. You may use the \"Authorize\" button to try the API below. This file was last generated on 2025-03-05T19:12:52+00:00 Please keep in mind that the demo site does not accept requests from curl, colly, wget, etc. You must use a browser or a tool like Postman to make requests. Too many script kiddies out there, sorry about that. 

    The version of the OpenAPI document: v6.2.9
    Contact: james@firefly-iii.org
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RuleActionKeyword(str, Enum):
    """
    The type of thing this action will do. A limited set is possible.
    """

    """
    allowed enum values
    """
    USER_ACTION = 'user_action'
    SET_CATEGORY = 'set_category'
    CLEAR_CATEGORY = 'clear_category'
    SET_BUDGET = 'set_budget'
    CLEAR_BUDGET = 'clear_budget'
    ADD_TAG = 'add_tag'
    REMOVE_TAG = 'remove_tag'
    REMOVE_ALL_TAGS = 'remove_all_tags'
    SET_DESCRIPTION = 'set_description'
    APPEND_DESCRIPTION = 'append_description'
    PREPEND_DESCRIPTION = 'prepend_description'
    SET_SOURCE_ACCOUNT = 'set_source_account'
    SET_DESTINATION_ACCOUNT = 'set_destination_account'
    SET_NOTES = 'set_notes'
    APPEND_NOTES = 'append_notes'
    PREPEND_NOTES = 'prepend_notes'
    CLEAR_NOTES = 'clear_notes'
    LINK_TO_BILL = 'link_to_bill'
    CONVERT_WITHDRAWAL = 'convert_withdrawal'
    CONVERT_DEPOSIT = 'convert_deposit'
    CONVERT_TRANSFER = 'convert_transfer'
    DELETE_TRANSACTION = 'delete_transaction'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RuleActionKeyword from a JSON string"""
        return cls(json.loads(json_str))


