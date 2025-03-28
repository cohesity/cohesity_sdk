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

class ReplicatedViewNameConfig(BaseModel):
    """
    Specifies an object protected by a View Protection Group.
    """ # noqa: E501
    source_view_id: Optional[StrictInt] = Field(description="Specifies the ID of the protected view.", alias="sourceViewId")
    use_same_view_name: Optional[StrictBool] = Field(default=None, description="Specifies if the remote view name to be kept is same as the source view name. If this field is true, viewName field will be ignored.", alias="useSameViewName")
    view_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the remote view. This field is only used when useSameViewName is false. If useSameViewName is true, this field is not used.", alias="viewName")
    __properties: ClassVar[List[str]] = ["sourceViewId", "useSameViewName", "viewName"]

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
        """Create an instance of ReplicatedViewNameConfig from a JSON string"""
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
        # set to None if source_view_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_view_id is None and "source_view_id" in self.model_fields_set:
            _dict['sourceViewId'] = None

        # set to None if use_same_view_name (nullable) is None
        # and model_fields_set contains the field
        if self.use_same_view_name is None and "use_same_view_name" in self.model_fields_set:
            _dict['useSameViewName'] = None

        # set to None if view_name (nullable) is None
        # and model_fields_set contains the field
        if self.view_name is None and "view_name" in self.model_fields_set:
            _dict['viewName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReplicatedViewNameConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sourceViewId": obj.get("sourceViewId"),
            "useSameViewName": obj.get("useSameViewName"),
            "viewName": obj.get("viewName")
        })
        return _obj


