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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.user_group_read_members import UserGroupReadMembers
from typing import Optional, Set
from typing_extensions import Self

class UserGroupReadAttributes(BaseModel):
    """
    UserGroupReadAttributes
    """ # noqa: E501
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    in_use: Optional[StrictBool] = Field(default=None, description="Is this user group ('financial administration') currently the active administration?")
    can_see_members: Optional[StrictBool] = Field(default=None, description="Can the current user see the members of this user group?")
    title: Optional[StrictStr] = Field(default=None, description="Title of the user group. By default, it is the same as the user's email address.")
    native_currency_id: Optional[StrictStr] = Field(default=None, description="Returns the native currency ID of the user group.")
    native_currency_code: Optional[StrictStr] = Field(default=None, description="Returns the native currency code of the user group.")
    native_currency_symbol: Optional[StrictStr] = Field(default=None, description="Returns the native currency symbol of the user group.")
    native_currency_decimal_places: Optional[StrictInt] = Field(default=None, description="Returns the native currency decimal places of the user group.")
    members: Optional[List[UserGroupReadMembers]] = None
    __properties: ClassVar[List[str]] = ["created_at", "updated_at", "in_use", "can_see_members", "title", "native_currency_id", "native_currency_code", "native_currency_symbol", "native_currency_decimal_places", "members"]

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
        """Create an instance of UserGroupReadAttributes from a JSON string"""
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
            "created_at",
            "updated_at",
            "in_use",
            "can_see_members",
            "native_currency_id",
            "native_currency_symbol",
            "native_currency_decimal_places",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in members (list)
        _items = []
        if self.members:
            for _item_members in self.members:
                if _item_members:
                    _items.append(_item_members.to_dict())
            _dict['members'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserGroupReadAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "in_use": obj.get("in_use"),
            "can_see_members": obj.get("can_see_members"),
            "title": obj.get("title"),
            "native_currency_id": obj.get("native_currency_id"),
            "native_currency_code": obj.get("native_currency_code"),
            "native_currency_symbol": obj.get("native_currency_symbol"),
            "native_currency_decimal_places": obj.get("native_currency_decimal_places"),
            "members": [UserGroupReadMembers.from_dict(_item) for _item in obj["members"]] if obj.get("members") is not None else None
        })
        return _obj


