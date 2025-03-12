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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.tier_level_settings import TierLevelSettings
from typing import Optional, Set
from typing_extensions import Self

class PrimaryArchivalTarget(BaseModel):
    """
    Specifies the primary archival settings. Mainly used for cloud direct archive (CAD) policy where primary backup is stored on archival target.
    """ # noqa: E501
    target_id: Optional[StrictInt] = Field(description="Specifies the Archival target id to take primary backup.", alias="targetId")
    target_name: Optional[StrictStr] = Field(default=None, description="Specifies the Archival target name where Snapshots are copied.", alias="targetName")
    tier_settings: Optional[TierLevelSettings] = Field(default=None, alias="tierSettings")
    __properties: ClassVar[List[str]] = ["targetId", "targetName", "tierSettings"]

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
        """Create an instance of PrimaryArchivalTarget from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "target_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tier_settings
        if self.tier_settings:
            _dict['tierSettings'] = self.tier_settings.to_dict()
        # set to None if target_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_id is None and "target_id" in self.model_fields_set:
            _dict['targetId'] = None

        # set to None if target_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_name is None and "target_name" in self.model_fields_set:
            _dict['targetName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PrimaryArchivalTarget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "targetId": obj.get("targetId"),
            "targetName": obj.get("targetName"),
            "tierSettings": TierLevelSettings.from_dict(obj["tierSettings"]) if obj.get("tierSettings") is not None else None
        })
        return _obj


