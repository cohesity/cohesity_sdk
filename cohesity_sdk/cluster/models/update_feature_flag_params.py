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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class UpdateFeatureFlagParams(BaseModel):
    """
    Describes update feature flag request params.
    """ # noqa: E501
    clear: Optional[StrictBool] = Field(default=None, description="Clear any override status for the feature flag.")
    is_approved: Optional[StrictBool] = Field(default=None, description="New override status for the feature flag.", alias="isApproved")
    is_ui_feature: Optional[StrictBool] = Field(default=None, description="Bool to specify if it's UI feature flag.", alias="isUiFeature")
    name: Optional[StrictStr] = Field(default=None, description="Name of the feature flag that is to be updated.")
    reason: Optional[StrictStr] = Field(default=None, description="Reason for updating the feature flag override status.")
    timestamp: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp of override operation.")
    __properties: ClassVar[List[str]] = ["clear", "isApproved", "isUiFeature", "name", "reason", "timestamp"]

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
        """Create an instance of UpdateFeatureFlagParams from a JSON string"""
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
        # set to None if clear (nullable) is None
        # and model_fields_set contains the field
        if self.clear is None and "clear" in self.model_fields_set:
            _dict['clear'] = None

        # set to None if is_approved (nullable) is None
        # and model_fields_set contains the field
        if self.is_approved is None and "is_approved" in self.model_fields_set:
            _dict['isApproved'] = None

        # set to None if is_ui_feature (nullable) is None
        # and model_fields_set contains the field
        if self.is_ui_feature is None and "is_ui_feature" in self.model_fields_set:
            _dict['isUiFeature'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateFeatureFlagParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clear": obj.get("clear"),
            "isApproved": obj.get("isApproved"),
            "isUiFeature": obj.get("isUiFeature"),
            "name": obj.get("name"),
            "reason": obj.get("reason"),
            "timestamp": obj.get("timestamp")
        })
        return _obj


