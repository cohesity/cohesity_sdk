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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.ms_group_param import MsGroupParam
from typing import Set
from typing_extensions import Self

class RecoverMsGroupParams(BaseModel):
    """
    Specifies the parameters to recover Microsoft 365 Group.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other MS groups if one of MS groups failed to recover. Default value is false.", alias="continueOnError")
    ms_groups: Optional[List[MsGroupParam]] = Field(description="Specifies a list of groups getting restored.", alias="msGroups")
    restore_to_original: Optional[StrictBool] = Field(default=None, description="Specifies whether or not all groups are restored to original location.", alias="restoreToOriginal")
    target_group: Optional[StrictStr] = Field(default=None, description="Specifies target group nickname in case restoreToOriginal is false. This needs to be specifid when restoreToOriginal is false.", alias="targetGroup")
    target_group_name: Optional[StrictStr] = Field(default=None, description="Specifies target group name in case restore_to_original is false. This needs to be specifid when restoreToOriginal is false. However, this will be ignored if restoring to alternate existing group (i.e. to a group the nickname of which is same as the one supplied by the end user).", alias="targetGroupName")
    __properties: ClassVar[List[str]] = ["continueOnError", "msGroups", "restoreToOriginal", "targetGroup", "targetGroupName"]

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
        """Create an instance of RecoverMsGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ms_groups (list)
        _items = []
        if self.ms_groups:
            for _item_ms_groups in self.ms_groups:
                if _item_ms_groups:
                    _items.append(_item_ms_groups.to_dict())
            _dict['msGroups'] = _items
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if ms_groups (nullable) is None
        # and model_fields_set contains the field
        if self.ms_groups is None and "ms_groups" in self.model_fields_set:
            _dict['msGroups'] = None

        # set to None if restore_to_original (nullable) is None
        # and model_fields_set contains the field
        if self.restore_to_original is None and "restore_to_original" in self.model_fields_set:
            _dict['restoreToOriginal'] = None

        # set to None if target_group (nullable) is None
        # and model_fields_set contains the field
        if self.target_group is None and "target_group" in self.model_fields_set:
            _dict['targetGroup'] = None

        # set to None if target_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_group_name is None and "target_group_name" in self.model_fields_set:
            _dict['targetGroupName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverMsGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "msGroups": [MsGroupParam.from_dict(_item) for _item in obj["msGroups"]] if obj.get("msGroups") is not None else None,
            "restoreToOriginal": obj.get("restoreToOriginal"),
            "targetGroup": obj.get("targetGroup"),
            "targetGroupName": obj.get("targetGroupName")
        })
        return _obj


