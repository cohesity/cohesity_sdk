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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.logical_volume_info import LogicalVolumeInfo
from typing import Optional, Set
from typing_extensions import Self

class VolumeInfo(BaseModel):
    """
    Specifies info of logical volume (filesystem).
    """ # noqa: E501
    filesystem_type: Optional[StrictStr] = Field(default=None, description="Specifies the filesystem type.", alias="filesystemType")
    filesystem_uuid: Optional[StrictStr] = Field(default=None, description="Specifies the filesystem uuid.", alias="filesystemUuid")
    is_dedupe: Optional[StrictBool] = Field(default=None, description="Specifies if this is NTFS dedupe volume", alias="isDedupe")
    is_supported: Optional[StrictBool] = Field(default=None, description="Specifies if this volume is supported.", alias="isSupported")
    logical_volume_info: Optional[LogicalVolumeInfo] = Field(default=None, description="Specifies the logical volume info. This fields is for 'LVM' and 'LDM' volume type only.", alias="logicalVolumeInfo")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the volume name.")
    volume_guid: Optional[StrictStr] = Field(default=None, description="Specifies the volume guid.", alias="volumeGuid")
    volume_size_in_bytes: Optional[StrictInt] = Field(default=None, description="Specifies volume size in bytes.", alias="volumeSizeInBytes")
    volume_type: Optional[StrictStr] = Field(default=None, description="Specifies the volume type.", alias="volumeType")
    __properties: ClassVar[List[str]] = ["filesystemType", "filesystemUuid", "isDedupe", "isSupported", "logicalVolumeInfo", "name", "volumeGuid", "volumeSizeInBytes", "volumeType"]

    @field_validator('volume_type')
    def volume_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SimpleVolume', 'LVM', 'LDM']):
            raise ValueError("must be one of enum values ('SimpleVolume', 'LVM', 'LDM')")
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
        """Create an instance of VolumeInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of logical_volume_info
        if self.logical_volume_info:
            _dict['logicalVolumeInfo'] = self.logical_volume_info.to_dict()
        # set to None if filesystem_type (nullable) is None
        # and model_fields_set contains the field
        if self.filesystem_type is None and "filesystem_type" in self.model_fields_set:
            _dict['filesystemType'] = None

        # set to None if filesystem_uuid (nullable) is None
        # and model_fields_set contains the field
        if self.filesystem_uuid is None and "filesystem_uuid" in self.model_fields_set:
            _dict['filesystemUuid'] = None

        # set to None if is_dedupe (nullable) is None
        # and model_fields_set contains the field
        if self.is_dedupe is None and "is_dedupe" in self.model_fields_set:
            _dict['isDedupe'] = None

        # set to None if is_supported (nullable) is None
        # and model_fields_set contains the field
        if self.is_supported is None and "is_supported" in self.model_fields_set:
            _dict['isSupported'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if volume_guid (nullable) is None
        # and model_fields_set contains the field
        if self.volume_guid is None and "volume_guid" in self.model_fields_set:
            _dict['volumeGuid'] = None

        # set to None if volume_size_in_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.volume_size_in_bytes is None and "volume_size_in_bytes" in self.model_fields_set:
            _dict['volumeSizeInBytes'] = None

        # set to None if volume_type (nullable) is None
        # and model_fields_set contains the field
        if self.volume_type is None and "volume_type" in self.model_fields_set:
            _dict['volumeType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VolumeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filesystemType": obj.get("filesystemType"),
            "filesystemUuid": obj.get("filesystemUuid"),
            "isDedupe": obj.get("isDedupe"),
            "isSupported": obj.get("isSupported"),
            "logicalVolumeInfo": LogicalVolumeInfo.from_dict(obj["logicalVolumeInfo"]) if obj.get("logicalVolumeInfo") is not None else None,
            "name": obj.get("name"),
            "volumeGuid": obj.get("volumeGuid"),
            "volumeSizeInBytes": obj.get("volumeSizeInBytes"),
            "volumeType": obj.get("volumeType")
        })
        return _obj


