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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.account_type_property import AccountTypeProperty
from typing import Optional, Set
from typing_extensions import Self

class RecurrenceTransaction(BaseModel):
    """
    RecurrenceTransaction
    """ # noqa: E501
    id: Optional[StrictStr] = None
    description: StrictStr
    amount: StrictStr = Field(description="Amount of the transaction.")
    foreign_amount: Optional[StrictStr] = Field(default=None, description="Foreign amount of the transaction.")
    currency_id: Optional[StrictStr] = Field(default=None, description="Submit either a currency_id or a currency_code.")
    currency_code: Optional[StrictStr] = Field(default=None, description="Submit either a currency_id or a currency_code.")
    currency_symbol: Optional[StrictStr] = None
    currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Number of decimals in the currency")
    foreign_currency_id: Optional[StrictStr] = Field(default=None, description="Submit either a foreign_currency_id or a foreign_currency_code, or neither.")
    foreign_currency_code: Optional[StrictStr] = Field(default=None, description="Submit either a foreign_currency_id or a foreign_currency_code, or neither.")
    foreign_currency_symbol: Optional[StrictStr] = None
    foreign_currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Number of decimals in the currency")
    budget_id: Optional[StrictStr] = Field(default=None, description="The budget ID for this transaction.")
    budget_name: Optional[StrictStr] = Field(default=None, description="The name of the budget to be used. If the budget name is unknown, the ID will be used or the value will be ignored.")
    category_id: Optional[StrictStr] = Field(default=None, description="Category ID for this transaction.")
    category_name: Optional[StrictStr] = Field(default=None, description="Category name for this transaction.")
    source_id: Optional[StrictStr] = Field(default=None, description="ID of the source account. Submit either this or source_name.")
    source_name: Optional[StrictStr] = Field(default=None, description="Name of the source account. Submit either this or source_id.")
    source_iban: Optional[StrictStr] = None
    source_type: Optional[AccountTypeProperty] = None
    destination_id: Optional[StrictStr] = Field(default=None, description="ID of the destination account. Submit either this or destination_name.")
    destination_name: Optional[StrictStr] = Field(default=None, description="Name of the destination account. Submit either this or destination_id.")
    destination_iban: Optional[StrictStr] = None
    destination_type: Optional[AccountTypeProperty] = None
    tags: Optional[List[StrictStr]] = Field(default=None, description="Array of tags.")
    piggy_bank_id: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the piggy_bank_name")
    piggy_bank_name: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the piggy_bank_id")
    bill_id: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the bill_name")
    bill_name: Optional[StrictStr] = Field(default=None, description="Optional. Use either this or the bill_id")
    __properties: ClassVar[List[str]] = ["id", "description", "amount", "foreign_amount", "currency_id", "currency_code", "currency_symbol", "currency_decimal_places", "foreign_currency_id", "foreign_currency_code", "foreign_currency_symbol", "foreign_currency_decimal_places", "budget_id", "budget_name", "category_id", "category_name", "source_id", "source_name", "source_iban", "source_type", "destination_id", "destination_name", "destination_iban", "destination_type", "tags", "piggy_bank_id", "piggy_bank_name", "bill_id", "bill_name"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RecurrenceTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "currency_symbol",
            "currency_decimal_places",
            "foreign_currency_symbol",
            "foreign_currency_decimal_places",
            "budget_name",
            "source_iban",
            "destination_iban",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if foreign_amount (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_amount is None and "foreign_amount" in self.model_fields_set:
            _dict['foreign_amount'] = None

        # set to None if foreign_currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_id is None and "foreign_currency_id" in self.model_fields_set:
            _dict['foreign_currency_id'] = None

        # set to None if foreign_currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_code is None and "foreign_currency_code" in self.model_fields_set:
            _dict['foreign_currency_code'] = None

        # set to None if foreign_currency_symbol (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_symbol is None and "foreign_currency_symbol" in self.model_fields_set:
            _dict['foreign_currency_symbol'] = None

        # set to None if foreign_currency_decimal_places (nullable) is None
        # and model_fields_set contains the field
        if self.foreign_currency_decimal_places is None and "foreign_currency_decimal_places" in self.model_fields_set:
            _dict['foreign_currency_decimal_places'] = None

        # set to None if budget_name (nullable) is None
        # and model_fields_set contains the field
        if self.budget_name is None and "budget_name" in self.model_fields_set:
            _dict['budget_name'] = None

        # set to None if source_iban (nullable) is None
        # and model_fields_set contains the field
        if self.source_iban is None and "source_iban" in self.model_fields_set:
            _dict['source_iban'] = None

        # set to None if destination_iban (nullable) is None
        # and model_fields_set contains the field
        if self.destination_iban is None and "destination_iban" in self.model_fields_set:
            _dict['destination_iban'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if piggy_bank_id (nullable) is None
        # and model_fields_set contains the field
        if self.piggy_bank_id is None and "piggy_bank_id" in self.model_fields_set:
            _dict['piggy_bank_id'] = None

        # set to None if piggy_bank_name (nullable) is None
        # and model_fields_set contains the field
        if self.piggy_bank_name is None and "piggy_bank_name" in self.model_fields_set:
            _dict['piggy_bank_name'] = None

        # set to None if bill_id (nullable) is None
        # and model_fields_set contains the field
        if self.bill_id is None and "bill_id" in self.model_fields_set:
            _dict['bill_id'] = None

        # set to None if bill_name (nullable) is None
        # and model_fields_set contains the field
        if self.bill_name is None and "bill_name" in self.model_fields_set:
            _dict['bill_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecurrenceTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "description": obj.get("description"),
            "amount": obj.get("amount"),
            "foreign_amount": obj.get("foreign_amount"),
            "currency_id": obj.get("currency_id"),
            "currency_code": obj.get("currency_code"),
            "currency_symbol": obj.get("currency_symbol"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "foreign_currency_id": obj.get("foreign_currency_id"),
            "foreign_currency_code": obj.get("foreign_currency_code"),
            "foreign_currency_symbol": obj.get("foreign_currency_symbol"),
            "foreign_currency_decimal_places": obj.get("foreign_currency_decimal_places"),
            "budget_id": obj.get("budget_id"),
            "budget_name": obj.get("budget_name"),
            "category_id": obj.get("category_id"),
            "category_name": obj.get("category_name"),
            "source_id": obj.get("source_id"),
            "source_name": obj.get("source_name"),
            "source_iban": obj.get("source_iban"),
            "source_type": obj.get("source_type"),
            "destination_id": obj.get("destination_id"),
            "destination_name": obj.get("destination_name"),
            "destination_iban": obj.get("destination_iban"),
            "destination_type": obj.get("destination_type"),
            "tags": obj.get("tags"),
            "piggy_bank_id": obj.get("piggy_bank_id"),
            "piggy_bank_name": obj.get("piggy_bank_name"),
            "bill_id": obj.get("bill_id"),
            "bill_name": obj.get("bill_name")
        })
        return _obj


