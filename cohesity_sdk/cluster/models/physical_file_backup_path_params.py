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
from typing import Optional, Set
from typing_extensions import Self

class PhysicalFileBackupPathParams(BaseModel):
    """
    PhysicalFileBackupPathParams
    """ # noqa: E501
    excluded_paths: Optional[List[StrictStr]] = Field(default=None, description="Specifies a set of paths nested under the include path which should be excluded from the Protection Group.", alias="excludedPaths")
    included_path: StrictStr = Field(description="Specifies a path to be included on the source. All paths under this path will be included unless they are specifically mentioned in excluded paths.", alias="includedPath")
    skip_nested_volumes: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip any nested volumes (both local and network) that are mounted under include path. Applicable only for windows sources.", alias="skipNestedVolumes")
    __properties: ClassVar[List[str]] = ["excludedPaths", "includedPath", "skipNestedVolumes"]

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
        """Create an instance of PhysicalFileBackupPathParams from a JSON string"""
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
        # set to None if excluded_paths (nullable) is None
        # and model_fields_set contains the field
        if self.excluded_paths is None and "excluded_paths" in self.model_fields_set:
            _dict['excludedPaths'] = None

        # set to None if skip_nested_volumes (nullable) is None
        # and model_fields_set contains the field
        if self.skip_nested_volumes is None and "skip_nested_volumes" in self.model_fields_set:
            _dict['skipNestedVolumes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalFileBackupPathParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludedPaths": obj.get("excludedPaths"),
            "includedPath": obj.get("includedPath"),
            "skipNestedVolumes": obj.get("skipNestedVolumes")
        })
        return _obj


