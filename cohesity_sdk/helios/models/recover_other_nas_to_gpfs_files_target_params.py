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
from cohesity_sdk.helios.models.filter_ip_config import FilterIpConfig
from cohesity_sdk.helios.models.recover_other_nas_to_elastifile_files_target_params_parent_source import RecoverOtherNasToElastifileFilesTargetParamsParentSource
from cohesity_sdk.helios.models.recover_target import RecoverTarget
from cohesity_sdk.helios.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Set
from typing_extensions import Self

class RecoverOtherNasToGpfsFilesTargetParams(BaseModel):
    """
    Specifies the params of the GPFS recovery target.
    """ # noqa: E501
    alternate_path: Optional[StrictStr] = Field(description="Specifies the path location to recover files to.", alias="alternatePath")
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false.", alias="continueOnError")
    encryption_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether encryption should be enabled during recovery.", alias="encryptionEnabled")
    filter_ip_config: Optional[FilterIpConfig] = Field(default=None, alias="filterIpConfig")
    overwrite_existing_file: Optional[StrictBool] = Field(default=None, description="Specifies whether to overwrite existing file/folder during recovery.", alias="overwriteExistingFile")
    parent_source: Optional[RecoverOtherNasToElastifileFilesTargetParamsParentSource] = Field(default=None, alias="parentSource")
    preserve_file_attributes: Optional[StrictBool] = Field(default=None, description="Specifies whether to preserve file/folder attributes during recovery.", alias="preserveFileAttributes")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    volume: RecoverTarget = Field(description="Specifies the id and name of the parent NAS to recover to. This volume will be the target of the recovery.")
    __properties: ClassVar[List[str]] = ["alternatePath", "continueOnError", "encryptionEnabled", "filterIpConfig", "overwriteExistingFile", "parentSource", "preserveFileAttributes", "vlanConfig", "volume"]

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
        """Create an instance of RecoverOtherNasToGpfsFilesTargetParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filter_ip_config
        if self.filter_ip_config:
            _dict['filterIpConfig'] = self.filter_ip_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent_source
        if self.parent_source:
            _dict['parentSource'] = self.parent_source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of volume
        if self.volume:
            _dict['volume'] = self.volume.to_dict()
        # set to None if alternate_path (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_path is None and "alternate_path" in self.model_fields_set:
            _dict['alternatePath'] = None

        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if encryption_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.encryption_enabled is None and "encryption_enabled" in self.model_fields_set:
            _dict['encryptionEnabled'] = None

        # set to None if overwrite_existing_file (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite_existing_file is None and "overwrite_existing_file" in self.model_fields_set:
            _dict['overwriteExistingFile'] = None

        # set to None if preserve_file_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.preserve_file_attributes is None and "preserve_file_attributes" in self.model_fields_set:
            _dict['preserveFileAttributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverOtherNasToGpfsFilesTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alternatePath": obj.get("alternatePath"),
            "continueOnError": obj.get("continueOnError"),
            "encryptionEnabled": obj.get("encryptionEnabled"),
            "filterIpConfig": FilterIpConfig.from_dict(obj["filterIpConfig"]) if obj.get("filterIpConfig") is not None else None,
            "overwriteExistingFile": obj.get("overwriteExistingFile"),
            "parentSource": RecoverOtherNasToElastifileFilesTargetParamsParentSource.from_dict(obj["parentSource"]) if obj.get("parentSource") is not None else None,
            "preserveFileAttributes": obj.get("preserveFileAttributes"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None,
            "volume": RecoverTarget.from_dict(obj["volume"]) if obj.get("volume") is not None else None
        })
        return _obj


