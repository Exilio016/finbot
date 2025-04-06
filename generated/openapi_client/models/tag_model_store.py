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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TagModelStore(BaseModel):
    """
    TagModelStore
    """ # noqa: E501
    tag: StrictStr = Field(description="The tag")
    var_date: Optional[date] = Field(default=None, description="The date to which the tag is applicable.", alias="date")
    description: Optional[StrictStr] = None
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latitude of the tag's location, if applicable. Can be used to draw a map.")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latitude of the tag's location, if applicable. Can be used to draw a map.")
    zoom_level: Optional[StrictInt] = Field(default=None, description="Zoom level for the map, if drawn. This to set the box right. Unfortunately this is a proprietary value because each map provider has different zoom levels.")
    __properties: ClassVar[List[str]] = ["tag", "date", "description", "latitude", "longitude", "zoom_level"]

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
        """Create an instance of TagModelStore from a JSON string"""
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
        # set to None if var_date (nullable) is None
        # and model_fields_set contains the field
        if self.var_date is None and "var_date" in self.model_fields_set:
            _dict['date'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if zoom_level (nullable) is None
        # and model_fields_set contains the field
        if self.zoom_level is None and "zoom_level" in self.model_fields_set:
            _dict['zoom_level'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TagModelStore from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tag": obj.get("tag"),
            "date": obj.get("date"),
            "description": obj.get("description"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "zoom_level": obj.get("zoom_level")
        })
        return _obj


