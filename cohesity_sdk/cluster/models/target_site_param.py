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
from typing import Optional, Set
from typing_extensions import Self

class TargetSiteParam(BaseModel):
    """
    Specifies the target Site to recover to.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(description="Specifies the id of the object.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    target_doc_lib_name: Optional[StrictStr] = Field(default=None, description="Specifies the name for the target doc lib.", alias="targetDocLibName")
    target_doc_lib_prefix: Optional[StrictStr] = Field(default=None, description="Specifies the prefix for the target doc lib.", alias="targetDocLibPrefix")
    __properties: ClassVar[List[str]] = ["id", "name", "targetDocLibName", "targetDocLibPrefix"]

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
        """Create an instance of TargetSiteParam from a JSON string"""
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
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if target_doc_lib_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_doc_lib_name is None and "target_doc_lib_name" in self.model_fields_set:
            _dict['targetDocLibName'] = None

        # set to None if target_doc_lib_prefix (nullable) is None
        # and model_fields_set contains the field
        if self.target_doc_lib_prefix is None and "target_doc_lib_prefix" in self.model_fields_set:
            _dict['targetDocLibPrefix'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TargetSiteParam from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "targetDocLibName": obj.get("targetDocLibName"),
            "targetDocLibPrefix": obj.get("targetDocLibPrefix")
        })
        return _obj


