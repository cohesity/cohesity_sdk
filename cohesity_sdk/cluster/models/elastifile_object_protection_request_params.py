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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from cohesity_sdk.cluster.models.file_filtering_policy import FileFilteringPolicy
from cohesity_sdk.cluster.models.file_level_data_lock_config import FileLevelDataLockConfig
from cohesity_sdk.cluster.models.host_based_backup_script_params import HostBasedBackupScriptParams
from cohesity_sdk.cluster.models.indexing_policy import IndexingPolicy
from cohesity_sdk.cluster.models.nas_throttling_config import NasThrottlingConfig
from cohesity_sdk.cluster.models.protection_object_input import ProtectionObjectInput
from typing import Set
from typing_extensions import Self

class ElastifileObjectProtectionRequestParams(BaseModel):
    """
    Specifies the parameters which are specific to Elastifile object protection.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether or not the backup should continue regardless of whether or not an error was encountered.", alias="continueOnError")
    encryption_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether the encryption should be used while backup or not.", alias="encryptionEnabled")
    file_filters: Optional[FileFilteringPolicy] = Field(default=None, alias="fileFilters")
    file_lock_config: Optional[FileLevelDataLockConfig] = Field(default=None, alias="fileLockConfig")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    pre_post_script: Optional[HostBasedBackupScriptParams] = Field(default=None, alias="prePostScript")
    throttling_config: Optional[NasThrottlingConfig] = Field(default=None, alias="throttlingConfig")
    protocol: Optional[StrictStr] = Field(default=None, description="Specifies the protocol of the NAS device being backed up.")
    objects: Annotated[List[ProtectionObjectInput], Field(min_length=1)] = Field(description="Specifies the objects to be protected.")
    __properties: ClassVar[List[str]] = ["continueOnError", "encryptionEnabled", "fileFilters", "fileLockConfig", "indexingPolicy", "prePostScript", "throttlingConfig", "protocol", "objects"]

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3']):
            raise ValueError("must be one of enum values ('kNoProtocol', 'kNfs3', 'kNfs4_1', 'kCifs1', 'kCifs2', 'kCifs3')")
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
        """Create an instance of ElastifileObjectProtectionRequestParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of file_filters
        if self.file_filters:
            _dict['fileFilters'] = self.file_filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_lock_config
        if self.file_lock_config:
            _dict['fileLockConfig'] = self.file_lock_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pre_post_script
        if self.pre_post_script:
            _dict['prePostScript'] = self.pre_post_script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of throttling_config
        if self.throttling_config:
            _dict['throttlingConfig'] = self.throttling_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if encryption_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_enabled is None and "encryption_enabled" in self.model_fields_set:
            _dict['encryptionEnabled'] = None

        # set to None if protocol (nullable) is None
        # and model_fields_set contains the field
        if self.protocol is None and "protocol" in self.model_fields_set:
            _dict['protocol'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ElastifileObjectProtectionRequestParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "encryptionEnabled": obj.get("encryptionEnabled"),
            "fileFilters": FileFilteringPolicy.from_dict(obj["fileFilters"]) if obj.get("fileFilters") is not None else None,
            "fileLockConfig": FileLevelDataLockConfig.from_dict(obj["fileLockConfig"]) if obj.get("fileLockConfig") is not None else None,
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None,
            "prePostScript": HostBasedBackupScriptParams.from_dict(obj["prePostScript"]) if obj.get("prePostScript") is not None else None,
            "throttlingConfig": NasThrottlingConfig.from_dict(obj["throttlingConfig"]) if obj.get("throttlingConfig") is not None else None,
            "protocol": obj.get("protocol"),
            "objects": [ProtectionObjectInput.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None
        })
        return _obj


