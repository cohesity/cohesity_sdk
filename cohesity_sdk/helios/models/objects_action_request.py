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
from cohesity_sdk.helios.models.object_linking_params import ObjectLinkingParams
from cohesity_sdk.helios.models.object_un_linking_params import ObjectUnLinkingParams
from typing import Set
from typing_extensions import Self

class ObjectsActionRequest(BaseModel):
    """
    Specifies the type of the action need to be performed on given set of objects.
    """ # noqa: E501
    action: Optional[StrictStr] = Field(default=None, description="Specifies the action type that need to be performed.")
    link_params: Optional[ObjectLinkingParams] = Field(default=None, alias="linkParams")
    link_type: Optional[StrictStr] = Field(default=None, description="Specifies the link type for the link/unlink action.", alias="linkType")
    un_link_params: Optional[ObjectUnLinkingParams] = Field(default=None, alias="unLinkParams")
    __properties: ClassVar[List[str]] = ["action", "linkParams", "linkType", "unLinkParams"]

    @field_validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Link', 'UnLink']):
            raise ValueError("must be one of enum values ('Link', 'UnLink')")
        return value

    @field_validator('link_type')
    def link_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Replication', 'FailoverRestore', 'VmMigration']):
            raise ValueError("must be one of enum values ('Replication', 'FailoverRestore', 'VmMigration')")
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
        """Create an instance of ObjectsActionRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of link_params
        if self.link_params:
            _dict['linkParams'] = self.link_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of un_link_params
        if self.un_link_params:
            _dict['unLinkParams'] = self.un_link_params.to_dict()
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if link_type (nullable) is None
        # and model_fields_set contains the field
        if self.link_type is None and "link_type" in self.model_fields_set:
            _dict['linkType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectsActionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "action": obj.get("action"),
            "linkParams": ObjectLinkingParams.from_dict(obj["linkParams"]) if obj.get("linkParams") is not None else None,
            "linkType": obj.get("linkType"),
            "unLinkParams": ObjectUnLinkingParams.from_dict(obj["unLinkParams"]) if obj.get("unLinkParams") is not None else None
        })
        return _obj


