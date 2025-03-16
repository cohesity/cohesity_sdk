# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class HeliosTier(BaseModel):
    """
    Specifies the Helios Tier details.
    """ # noqa: E501
    is_default_tier: Optional[StrictBool] = Field(default=None, description="Specifies whether the current tier will be the default tier for primary retention.", alias="isDefaultTier")
    move_after: Optional[StrictInt] = Field(default=None, description="Specifies the duration after which the backup will be moved to next tier.", alias="moveAfter")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the tier type.")
    unit: Optional[StrictStr] = Field(default=None, description="Specificies the time unit after which backup will be moved to next tier.")
    __properties: ClassVar[List[str]] = ["isDefaultTier", "moveAfter", "type", "unit"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAmazonS3Standard', 'kAmazonS3Glacier']):
            raise ValueError("must be one of enum values ('kAmazonS3Standard', 'kAmazonS3Glacier')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Days', 'Weeks', 'Months', 'Years']):
            raise ValueError("must be one of enum values ('Days', 'Weeks', 'Months', 'Years')")
        return value

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
        """Create an instance of HeliosTier from a JSON string"""
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
        # set to None if is_default_tier (nullable) is None
        # and model_fields_set contains the field
        if self.is_default_tier is None and "is_default_tier" in self.model_fields_set:
            _dict['isDefaultTier'] = None

        # set to None if move_after (nullable) is None
        # and model_fields_set contains the field
        if self.move_after is None and "move_after" in self.model_fields_set:
            _dict['moveAfter'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isDefaultTier": obj.get("isDefaultTier"),
            "moveAfter": obj.get("moveAfter"),
            "type": obj.get("type"),
            "unit": obj.get("unit")
        })
        return _obj


