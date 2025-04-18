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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BudgetLimit(BaseModel):
    """
    BudgetLimit
    """ # noqa: E501
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    start: datetime = Field(description="Start date of the budget limit.")
    end: datetime = Field(description="End date of the budget limit.")
    currency_id: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    currency_code: Optional[StrictStr] = Field(default=None, description="Use either currency_id or currency_code. Defaults to the user's default currency.")
    currency_name: Optional[StrictStr] = None
    currency_symbol: Optional[StrictStr] = None
    currency_decimal_places: Optional[StrictInt] = None
    native_currency_id: Optional[StrictStr] = Field(default=None, description="The administration's native currency ID.")
    native_currency_code: Optional[StrictStr] = Field(default=None, description="The administration's native currency code.")
    native_currency_symbol: Optional[StrictStr] = Field(default=None, description="The administration's native currency symbol.")
    native_currency_decimal_places: Optional[StrictInt] = Field(default=None, description="The administration's native currency decimal places.")
    budget_id: StrictStr = Field(description="The budget ID of the associated budget.")
    period: Optional[StrictStr] = Field(default=None, description="Period of the budget limit. Only used when auto-generated by auto-budget.")
    amount: StrictStr
    native_amount: Optional[StrictStr] = Field(default=None, description="The amount of this budget limit in the user's native currency, if the original amount is in a different currency.")
    spent: Optional[StrictStr] = Field(default=None, description="Will be in the native currency if this is turned on by the user.")
    notes: Optional[StrictStr] = Field(default=None, description="Some notes for this specific budget limit.")
    __properties: ClassVar[List[str]] = ["created_at", "updated_at", "start", "end", "currency_id", "currency_code", "currency_name", "currency_symbol", "currency_decimal_places", "native_currency_id", "native_currency_code", "native_currency_symbol", "native_currency_decimal_places", "budget_id", "period", "amount", "native_amount", "spent", "notes"]

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
        """Create an instance of BudgetLimit from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
            "currency_name",
            "currency_symbol",
            "currency_decimal_places",
            "native_currency_id",
            "native_currency_code",
            "native_currency_symbol",
            "native_currency_decimal_places",
            "budget_id",
            "period",
            "native_amount",
            "spent",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if period (nullable) is None
        # and model_fields_set contains the field
        if self.period is None and "period" in self.model_fields_set:
            _dict['period'] = None

        # set to None if native_amount (nullable) is None
        # and model_fields_set contains the field
        if self.native_amount is None and "native_amount" in self.model_fields_set:
            _dict['native_amount'] = None

        # set to None if spent (nullable) is None
        # and model_fields_set contains the field
        if self.spent is None and "spent" in self.model_fields_set:
            _dict['spent'] = None

        # set to None if notes (nullable) is None
        # and model_fields_set contains the field
        if self.notes is None and "notes" in self.model_fields_set:
            _dict['notes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BudgetLimit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "currency_id": obj.get("currency_id"),
            "currency_code": obj.get("currency_code"),
            "currency_name": obj.get("currency_name"),
            "currency_symbol": obj.get("currency_symbol"),
            "currency_decimal_places": obj.get("currency_decimal_places"),
            "native_currency_id": obj.get("native_currency_id"),
            "native_currency_code": obj.get("native_currency_code"),
            "native_currency_symbol": obj.get("native_currency_symbol"),
            "native_currency_decimal_places": obj.get("native_currency_decimal_places"),
            "budget_id": obj.get("budget_id"),
            "period": obj.get("period"),
            "amount": obj.get("amount"),
            "native_amount": obj.get("native_amount"),
            "spent": obj.get("spent"),
            "notes": obj.get("notes")
        })
        return _obj


