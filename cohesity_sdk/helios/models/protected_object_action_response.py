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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.action_object_level_response import ActionObjectLevelResponse
from typing import Set
from typing_extensions import Self

class ProtectedObjectActionResponse(BaseModel):
    """
    Specifies the response upon performing an action on protected objects.
    """ # noqa: E501
    action: Optional[StrictStr] = Field(default=None, description="Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params.")
    objects: Optional[List[ActionObjectLevelResponse]] = Field(default=None, description="Specifies the list of objects on which the provided action was performed.")
    __properties: ClassVar[List[str]] = ["action", "objects"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Pause', 'Resume', 'UnProtect', 'ProtectNow']):
            raise ValueError("must be one of enum values ('Pause', 'Resume', 'UnProtect', 'ProtectNow')")
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
        """Create an instance of ProtectedObjectActionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProtectedObjectActionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "objects": [ActionObjectLevelResponse.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None
        })
        return _obj


