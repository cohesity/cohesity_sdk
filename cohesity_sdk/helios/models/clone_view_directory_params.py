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
from typing import Set
from typing_extensions import Self

class CloneViewDirectoryParams(BaseModel):
    """
    Specifies the parameters to clone View directory.
    """ # noqa: E501
    source_directory_path: Optional[StrictStr] = Field(description="Specifies the path of source directory. This is the full path including the Storage Domain name and View name.", alias="sourceDirectoryPath")
    target_directory_name: Optional[StrictStr] = Field(description="Specifies the name of the target directory.", alias="targetDirectoryName")
    target_parent_directory_path: Optional[StrictStr] = Field(description="Specifies the path of parent directory of the target directory. This is the full path including the Storage Domain name and View Name.", alias="targetParentDirectoryPath")
    __properties: ClassVar[List[str]] = ["sourceDirectoryPath", "targetDirectoryName", "targetParentDirectoryPath"]

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
        """Create an instance of CloneViewDirectoryParams from a JSON string"""
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
        # set to None if source_directory_path (nullable) is None
        # and model_fields_set contains the field
        if self.source_directory_path is None and "source_directory_path" in self.model_fields_set:
            _dict['sourceDirectoryPath'] = None

        # set to None if target_directory_name (nullable) is None
        # and model_fields_set contains the field
        if self.target_directory_name is None and "target_directory_name" in self.model_fields_set:
            _dict['targetDirectoryName'] = None

        # set to None if target_parent_directory_path (nullable) is None
        # and model_fields_set contains the field
        if self.target_parent_directory_path is None and "target_parent_directory_path" in self.model_fields_set:
            _dict['targetParentDirectoryPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CloneViewDirectoryParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sourceDirectoryPath": obj.get("sourceDirectoryPath"),
            "targetDirectoryName": obj.get("targetDirectoryName"),
            "targetParentDirectoryPath": obj.get("targetParentDirectoryPath")
        })
        return _obj


