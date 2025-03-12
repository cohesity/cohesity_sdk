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

class DataTieringShareStats(BaseModel):
    """
    Specifies the source shares analysis stats.
    """ # noqa: E501
    access_time_tag: Optional[StrictStr] = Field(default=None, description="Specifies the access time bucket.", alias="accessTimeTag")
    file_count: Optional[StrictInt] = Field(default=None, description="Specifies the file count.", alias="fileCount")
    file_size_tag: Optional[StrictStr] = Field(default=None, description="Specifies the file size bucket.", alias="fileSizeTag")
    file_type_tag: Optional[StrictStr] = Field(default=None, description="Specifies the file type bucket.", alias="fileTypeTag")
    id: Optional[StrictInt] = Field(default=None, description="Specifies the unique identifer for stat.")
    mod_time_tag: Optional[StrictStr] = Field(default=None, description="Specifies the modification time bucket.", alias="modTimeTag")
    total_size: Optional[StrictInt] = Field(default=None, description="Specifies the total count.", alias="totalSize")
    __properties: ClassVar[List[str]] = ["accessTimeTag", "fileCount", "fileSizeTag", "fileTypeTag", "id", "modTimeTag", "totalSize"]

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
        """Create an instance of DataTieringShareStats from a JSON string"""
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
        # set to None if access_time_tag (nullable) is None
        # and model_fields_set contains the field
        if self.access_time_tag is None and "access_time_tag" in self.model_fields_set:
            _dict['accessTimeTag'] = None

        # set to None if file_count (nullable) is None
        # and model_fields_set contains the field
        if self.file_count is None and "file_count" in self.model_fields_set:
            _dict['fileCount'] = None

        # set to None if file_size_tag (nullable) is None
        # and model_fields_set contains the field
        if self.file_size_tag is None and "file_size_tag" in self.model_fields_set:
            _dict['fileSizeTag'] = None

        # set to None if file_type_tag (nullable) is None
        # and model_fields_set contains the field
        if self.file_type_tag is None and "file_type_tag" in self.model_fields_set:
            _dict['fileTypeTag'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if mod_time_tag (nullable) is None
        # and model_fields_set contains the field
        if self.mod_time_tag is None and "mod_time_tag" in self.model_fields_set:
            _dict['modTimeTag'] = None

        # set to None if total_size (nullable) is None
        # and model_fields_set contains the field
        if self.total_size is None and "total_size" in self.model_fields_set:
            _dict['totalSize'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTieringShareStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessTimeTag": obj.get("accessTimeTag"),
            "fileCount": obj.get("fileCount"),
            "fileSizeTag": obj.get("fileSizeTag"),
            "fileTypeTag": obj.get("fileTypeTag"),
            "id": obj.get("id"),
            "modTimeTag": obj.get("modTimeTag"),
            "totalSize": obj.get("totalSize")
        })
        return _obj


