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


class DataDestroyObject(str, Enum):
    """
    DataDestroyObject
    """

    """
    allowed enum values
    """
    NOT_ASSETS_LIABILITIES = 'not_assets_liabilities'
    BUDGETS = 'budgets'
    BILLS = 'bills'
    PIGGY_BANKS = 'piggy_banks'
    RULES = 'rules'
    RECURRING = 'recurring'
    CATEGORIES = 'categories'
    TAGS = 'tags'
    OBJECT_GROUPS = 'object_groups'
    ACCOUNTS = 'accounts'
    ASSET_ACCOUNTS = 'asset_accounts'
    EXPENSE_ACCOUNTS = 'expense_accounts'
    REVENUE_ACCOUNTS = 'revenue_accounts'
    LIABILITIES = 'liabilities'
    TRANSACTIONS = 'transactions'
    WITHDRAWALS = 'withdrawals'
    DEPOSITS = 'deposits'
    TRANSFERS = 'transfers'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DataDestroyObject from a JSON string"""
        return cls(json.loads(json_str))


