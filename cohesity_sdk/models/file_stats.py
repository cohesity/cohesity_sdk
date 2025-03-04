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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class FileStats(BaseModel):
    """
    Specifies the file stats.
    """ # noqa: E501
    files_count: Optional[StrictInt] = Field(default=None, description="Specifies the number of files.", alias="filesCount")
    files_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the size of all the files in bytes.", alias="filesSizeBytes")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the file type.")
    __properties: ClassVar[List[str]] = ["filesCount", "filesSizeBytes", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['TextFile', 'AudioFile', 'VideoFile', 'CompressedFile', 'DatabaseFile', 'ImageFile', 'ExecutableFile', 'LogFile', 'OtherFile']):
            raise ValueError("must be one of enum values ('TextFile', 'AudioFile', 'VideoFile', 'CompressedFile', 'DatabaseFile', 'ImageFile', 'ExecutableFile', 'LogFile', 'OtherFile')")
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
        """Create an instance of FileStats from a JSON string"""
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
        # set to None if files_count (nullable) is None
        # and model_fields_set contains the field
        if self.files_count is None and "files_count" in self.model_fields_set:
            _dict['filesCount'] = None

        # set to None if files_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.files_size_bytes is None and "files_size_bytes" in self.model_fields_set:
            _dict['filesSizeBytes'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FileStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filesCount": obj.get("filesCount"),
            "filesSizeBytes": obj.get("filesSizeBytes"),
            "type": obj.get("type")
        })
        return _obj


