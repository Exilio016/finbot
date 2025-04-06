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


class ConfigValueFilter(str, Enum):
    """
    Title of the configuration value.
    """

    """
    allowed enum values
    """
    CONFIGURATION_DOT_IS_DEMO_SITE = 'configuration.is_demo_site'
    CONFIGURATION_DOT_PERMISSION_UPDATE_CHECK = 'configuration.permission_update_check'
    CONFIGURATION_DOT_LAST_UPDATE_CHECK = 'configuration.last_update_check'
    CONFIGURATION_DOT_SINGLE_USER_MODE = 'configuration.single_user_mode'
    FIREFLY_DOT_VERSION = 'firefly.version'
    FIREFLY_DOT_DEFAULT_LOCATION = 'firefly.default_location'
    FIREFLY_DOT_ACCOUNT_TO_TRANSACTION = 'firefly.account_to_transaction'
    FIREFLY_DOT_ALLOWED_OPPOSING_TYPES = 'firefly.allowed_opposing_types'
    FIREFLY_DOT_ACCOUNT_ROLES = 'firefly.accountRoles'
    FIREFLY_DOT_VALID_LIABILITIES = 'firefly.valid_liabilities'
    FIREFLY_DOT_INTEREST_PERIODS = 'firefly.interest_periods'
    FIREFLY_DOT_ENABLE_EXTERNAL_MAP = 'firefly.enable_external_map'
    FIREFLY_DOT_EXPECTED_SOURCE_TYPES = 'firefly.expected_source_types'
    APP_DOT_TIMEZONE = 'app.timezone'
    FIREFLY_DOT_BILL_PERIODS = 'firefly.bill_periods'
    FIREFLY_DOT_CREDIT_CARD_TYPES = 'firefly.credit_card_types'
    FIREFLY_DOT_LANGUAGES = 'firefly.languages'
    FIREFLY_DOT_VALID_VIEW_RANGES = 'firefly.valid_view_ranges'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigValueFilter from a JSON string"""
        return cls(json.loads(json_str))


