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

class CurrencyExchangeRateReadAttributes(BaseModel):
    """
    CurrencyExchangeRateReadAttributes
    """ # noqa: E501
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    from_currency_id: Optional[StrictStr] = Field(default=None, description="Base currency ID for this exchange rate entry.")
    from_currency_code: Optional[StrictStr] = Field(default=None, description="Base currency code for this exchange rate entry.")
    from_currency_symbol: Optional[StrictStr] = Field(default=None, description="Base currency symbol for this exchange rate entry.")
    from_currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Base currency decimal places for this exchange rate entry.")
    to_currency_id: Optional[StrictStr] = Field(default=None, description="Destination currency ID for this exchange rate entry.")
    to_currency_code: Optional[StrictStr] = Field(default=None, description="Destination currency code for this exchange rate entry.")
    to_currency_symbol: Optional[StrictStr] = Field(default=None, description="Destination currency symbol for this exchange rate entry.")
    to_currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Destination currency decimal places for this exchange rate entry.")
    rate: Optional[StrictStr] = Field(default=None, description="The actual exchange rate. How many 'to' currency will you get for 1 'from' currency?")
    var_date: Optional[datetime] = Field(default=None, description="Date and time of the exchange rate.", alias="date")
    __properties: ClassVar[List[str]] = ["created_at", "updated_at", "from_currency_id", "from_currency_code", "from_currency_symbol", "from_currency_decimal_places", "to_currency_id", "to_currency_code", "to_currency_symbol", "to_currency_decimal_places", "rate", "date"]

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
        """Create an instance of CurrencyExchangeRateReadAttributes from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_at",
            "updated_at",
            "from_currency_id",
            "from_currency_code",
            "from_currency_symbol",
            "from_currency_decimal_places",
            "to_currency_id",
            "to_currency_code",
            "to_currency_symbol",
            "to_currency_decimal_places",
            "rate",
            "var_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CurrencyExchangeRateReadAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "from_currency_id": obj.get("from_currency_id"),
            "from_currency_code": obj.get("from_currency_code"),
            "from_currency_symbol": obj.get("from_currency_symbol"),
            "from_currency_decimal_places": obj.get("from_currency_decimal_places"),
            "to_currency_id": obj.get("to_currency_id"),
            "to_currency_code": obj.get("to_currency_code"),
            "to_currency_symbol": obj.get("to_currency_symbol"),
            "to_currency_decimal_places": obj.get("to_currency_decimal_places"),
            "rate": obj.get("rate"),
            "date": obj.get("date")
        })
        return _obj


