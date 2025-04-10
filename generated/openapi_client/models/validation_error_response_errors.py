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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ValidationErrorResponseErrors(BaseModel):
    """
    ValidationErrorResponseErrors
    """ # noqa: E501
    email: Optional[List[StrictStr]] = None
    force: Optional[List[StrictStr]] = None
    blocked: Optional[List[StrictStr]] = None
    var_field: Optional[List[StrictStr]] = Field(default=None, alias="field")
    role: Optional[List[StrictStr]] = None
    blocked_code: Optional[List[StrictStr]] = None
    name: Optional[List[StrictStr]] = None
    type: Optional[List[StrictStr]] = None
    iban: Optional[List[StrictStr]] = None
    start: Optional[List[StrictStr]] = None
    end: Optional[List[StrictStr]] = None
    var_date: Optional[List[StrictStr]] = Field(default=None, alias="date")
    __properties: ClassVar[List[str]] = ["email", "force", "blocked", "field", "role", "blocked_code", "name", "type", "iban", "start", "end", "date"]

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
        """Create an instance of ValidationErrorResponseErrors from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationErrorResponseErrors from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "email": obj.get("email"),
            "force": obj.get("force"),
            "blocked": obj.get("blocked"),
            "field": obj.get("field"),
            "role": obj.get("role"),
            "blocked_code": obj.get("blocked_code"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "iban": obj.get("iban"),
            "start": obj.get("start"),
            "end": obj.get("end"),
            "date": obj.get("date")
        })
        return _obj


