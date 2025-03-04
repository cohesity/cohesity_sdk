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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.failed_protection_group_details import FailedProtectionGroupDetails
from typing import Optional, Set
from typing_extensions import Self

class UpdateProtectionGroupsState(BaseModel):
    """
    UpdateProtectionGroupsState
    """ # noqa: E501
    failed_protection_groups: Optional[List[FailedProtectionGroupDetails]] = Field(default=None, description="Specifies a list of Protection Group ids along with details for which updation of state was failed.", alias="failedProtectionGroups")
    successful_protection_group_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of Protection Group ids for which updation of state was successful.", alias="successfulProtectionGroupIds")
    __properties: ClassVar[List[str]] = ["failedProtectionGroups", "successfulProtectionGroupIds"]

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
        """Create an instance of UpdateProtectionGroupsState from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failed_protection_groups (list)
        _items = []
        if self.failed_protection_groups:
            for _item_failed_protection_groups in self.failed_protection_groups:
                if _item_failed_protection_groups:
                    _items.append(_item_failed_protection_groups.to_dict())
            _dict['failedProtectionGroups'] = _items
        # set to None if failed_protection_groups (nullable) is None
        # and model_fields_set contains the field
        if self.failed_protection_groups is None and "failed_protection_groups" in self.model_fields_set:
            _dict['failedProtectionGroups'] = None

        # set to None if successful_protection_group_ids (nullable) is None
        # and model_fields_set contains the field
        if self.successful_protection_group_ids is None and "successful_protection_group_ids" in self.model_fields_set:
            _dict['successfulProtectionGroupIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateProtectionGroupsState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "failedProtectionGroups": [FailedProtectionGroupDetails.from_dict(_item) for _item in obj["failedProtectionGroups"]] if obj.get("failedProtectionGroups") is not None else None,
            "successfulProtectionGroupIds": obj.get("successfulProtectionGroupIds")
        })
        return _obj


