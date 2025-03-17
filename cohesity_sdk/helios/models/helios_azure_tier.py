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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class HeliosAzureTier(BaseModel):
    """
    Specifies the settings for a Azure tier.
    """ # noqa: E501
    move_after: Optional[StrictInt] = Field(default=None, description="Specifies the time period after which the backup will be moved from current tier to next tier.", alias="moveAfter")
    move_after_unit: Optional[StrictStr] = Field(default=None, description="Specifies the unit for moving the data from current tier to next tier. This unit will be a base unit for the 'moveAfter' field specified below.", alias="moveAfterUnit")
    tier_type: Optional[StrictStr] = Field(description="Specifies the Azure tier types.", alias="tierType")
    __properties: ClassVar[List[str]] = ["moveAfter", "moveAfterUnit", "tierType"]

    @field_validator('move_after_unit')
    def move_after_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Days', 'Weeks', 'Months', 'Years']):
            raise ValueError("must be one of enum values ('Days', 'Weeks', 'Months', 'Years')")
        return value

    @field_validator('tier_type')
    def tier_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAzureTierHot', 'kAzureTierCool', 'kAzureTierArchive']):
            raise ValueError("must be one of enum values ('kAzureTierHot', 'kAzureTierCool', 'kAzureTierArchive')")
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
        """Create an instance of HeliosAzureTier from a JSON string"""
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
        # set to None if move_after (nullable) is None
        # and model_fields_set contains the field
        if self.move_after is None and "move_after" in self.model_fields_set:
            _dict['moveAfter'] = None

        # set to None if move_after_unit (nullable) is None
        # and model_fields_set contains the field
        if self.move_after_unit is None and "move_after_unit" in self.model_fields_set:
            _dict['moveAfterUnit'] = None

        # set to None if tier_type (nullable) is None
        # and model_fields_set contains the field
        if self.tier_type is None and "tier_type" in self.model_fields_set:
            _dict['tierType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosAzureTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "moveAfter": obj.get("moveAfter"),
            "moveAfterUnit": obj.get("moveAfterUnit"),
            "tierType": obj.get("tierType")
        })
        return _obj


