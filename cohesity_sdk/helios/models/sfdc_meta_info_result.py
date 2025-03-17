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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.sfdc_dependent_object import SfdcDependentObject
from typing import Set
from typing_extensions import Self

class SfdcMetaInfoResult(BaseModel):
    """
    Specifies the meta info params for salesforce object.
    """ # noqa: E501
    child_objects: Optional[List[SfdcDependentObject]] = Field(default=None, description="Specifies the list of child objects.", alias="childObjects")
    parent_objects: Optional[List[SfdcDependentObject]] = Field(default=None, description="Specifies the list of parent objects.", alias="parentObjects")
    __properties: ClassVar[List[str]] = ["childObjects", "parentObjects"]

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
        """Create an instance of SfdcMetaInfoResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in child_objects (list)
        _items = []
        if self.child_objects:
            for _item_child_objects in self.child_objects:
                if _item_child_objects:
                    _items.append(_item_child_objects.to_dict())
            _dict['childObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parent_objects (list)
        _items = []
        if self.parent_objects:
            for _item_parent_objects in self.parent_objects:
                if _item_parent_objects:
                    _items.append(_item_parent_objects.to_dict())
            _dict['parentObjects'] = _items
        # set to None if child_objects (nullable) is None
        # and model_fields_set contains the field
        if self.child_objects is None and "child_objects" in self.model_fields_set:
            _dict['childObjects'] = None

        # set to None if parent_objects (nullable) is None
        # and model_fields_set contains the field
        if self.parent_objects is None and "parent_objects" in self.model_fields_set:
            _dict['parentObjects'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SfdcMetaInfoResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "childObjects": [SfdcDependentObject.from_dict(_item) for _item in obj["childObjects"]] if obj.get("childObjects") is not None else None,
            "parentObjects": [SfdcDependentObject.from_dict(_item) for _item in obj["parentObjects"]] if obj.get("parentObjects") is not None else None
        })
        return _obj


