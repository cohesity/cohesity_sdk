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
from cohesity_sdk.cluster.models.physical_file_backup_path_params import PhysicalFileBackupPathParams
from typing import Set
from typing_extensions import Self

class PhysicalFileProtectionGroupObjectParams(BaseModel):
    """
    PhysicalFileProtectionGroupObjectParams
    """ # noqa: E501
    excluded_vss_writers: Optional[List[StrictStr]] = Field(default=None, description="Specifies writer names which should be excluded from physical file based backups.", alias="excludedVssWriters")
    file_paths: Optional[List[PhysicalFileBackupPathParams]] = Field(default=None, description="Specifies a list of file paths to be protected by this Protection Group.", alias="filePaths")
    follow_nas_symlink_target: Optional[StrictBool] = Field(default=None, description="Specifies whether to follow NAS target pointed by symlink for windows sources.", alias="followNasSymlinkTarget")
    id: StrictInt = Field(description="Specifies the ID of the object protected.")
    metadata_file_path: Optional[StrictStr] = Field(default=None, description="Specifies the path of metadatafile on source. This file contains absolute paths of files that needs to be backed up on the same source.", alias="metadataFilePath")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object protected.")
    nested_volume_types_to_skip: Optional[List[StrictStr]] = Field(default=None, description="Specifies mount types of nested volumes to be skipped.", alias="nestedVolumeTypesToSkip")
    uses_path_level_skip_nested_volume_setting: Optional[StrictBool] = Field(default=None, description="Specifies whether path level or object level skip nested volume setting will be used.", alias="usesPathLevelSkipNestedVolumeSetting")
    __properties: ClassVar[List[str]] = ["excludedVssWriters", "filePaths", "followNasSymlinkTarget", "id", "metadataFilePath", "name", "nestedVolumeTypesToSkip", "usesPathLevelSkipNestedVolumeSetting"]

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
        """Create an instance of PhysicalFileProtectionGroupObjectParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in file_paths (list)
        _items = []
        if self.file_paths:
            for _item_file_paths in self.file_paths:
                if _item_file_paths:
                    _items.append(_item_file_paths.to_dict())
            _dict['filePaths'] = _items
        # set to None if excluded_vss_writers (nullable) is None
        # and model_fields_set contains the field
        if self.excluded_vss_writers is None and "excluded_vss_writers" in self.model_fields_set:
            _dict['excludedVssWriters'] = None

        # set to None if follow_nas_symlink_target (nullable) is None
        # and model_fields_set contains the field
        if self.follow_nas_symlink_target is None and "follow_nas_symlink_target" in self.model_fields_set:
            _dict['followNasSymlinkTarget'] = None

        # set to None if metadata_file_path (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_file_path is None and "metadata_file_path" in self.model_fields_set:
            _dict['metadataFilePath'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if uses_path_level_skip_nested_volume_setting (nullable) is None
        # and model_fields_set contains the field
        if self.uses_path_level_skip_nested_volume_setting is None and "uses_path_level_skip_nested_volume_setting" in self.model_fields_set:
            _dict['usesPathLevelSkipNestedVolumeSetting'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalFileProtectionGroupObjectParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "excludedVssWriters": obj.get("excludedVssWriters"),
            "filePaths": [PhysicalFileBackupPathParams.from_dict(_item) for _item in obj["filePaths"]] if obj.get("filePaths") is not None else None,
            "followNasSymlinkTarget": obj.get("followNasSymlinkTarget"),
            "id": obj.get("id"),
            "metadataFilePath": obj.get("metadataFilePath"),
            "name": obj.get("name"),
            "nestedVolumeTypesToSkip": obj.get("nestedVolumeTypesToSkip"),
            "usesPathLevelSkipNestedVolumeSetting": obj.get("usesPathLevelSkipNestedVolumeSetting")
        })
        return _obj


