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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class UpdateProtectionGroupsStateRequest(BaseModel):
    """
    Specifies the parameters to perform an action of list of Protection Groups.
    """ # noqa: E501
    action: Optional[StrictStr] = Field(description="Specifies the action to be performed on all the specfied Protection Groups. 'kActivate' specifies that Protection Group should be activated. 'kDeactivate' sepcifies that Protection Group should be deactivated. 'kPause' specifies that Protection Group should be paused. 'kResume' specifies that Protection Group should be resumed.")
    ids: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(description="Specifies a list of Protection Group ids for which the state should change.")
    __properties: ClassVar[List[str]] = ["action", "ids"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kPause', 'kResume']):
            raise ValueError("must be one of enum values ('kPause', 'kResume')")
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
        """Create an instance of UpdateProtectionGroupsStateRequest from a JSON string"""
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
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if ids (nullable) is None
        # and model_fields_set contains the field
        if self.ids is None and "ids" in self.model_fields_set:
            _dict['ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateProtectionGroupsStateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "ids": obj.get("ids")
        })
        return _obj


