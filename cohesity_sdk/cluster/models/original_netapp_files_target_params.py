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
from cohesity_sdk.cluster.models.filter_ip_config import FilterIpConfig
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Set
from typing_extensions import Self

class OriginalNetappFilesTargetParams(BaseModel):
    """
    Specifies the params of the original Netapp recovery target.
    """ # noqa: E501
    alternate_path: Optional[StrictStr] = Field(default=None, description="Specifies the alternate path location to recover files to.", alias="alternatePath")
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other files if one of the files fails to recover. Default value is false.", alias="continueOnError")
    encryption_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether encryption should be enabled during recovery.", alias="encryptionEnabled")
    filter_ip_config: Optional[FilterIpConfig] = Field(default=None, alias="filterIpConfig")
    overwrite_existing_file: Optional[StrictBool] = Field(default=None, description="Specifies whether to overwrite existing file/folder during recovery.", alias="overwriteExistingFile")
    preserve_file_attributes: Optional[StrictBool] = Field(default=None, description="Specifies whether to preserve file/folder attributes during recovery.", alias="preserveFileAttributes")
    recover_to_original_path: Optional[StrictBool] = Field(description="Specifies whether to recover files and folders to the original path location. If false, alternatePath must be specified.", alias="recoverToOriginalPath")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["alternatePath", "continueOnError", "encryptionEnabled", "filterIpConfig", "overwriteExistingFile", "preserveFileAttributes", "recoverToOriginalPath", "vlanConfig"]

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
        """Create an instance of OriginalNetappFilesTargetParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
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

        # set to None if recover_to_original_path (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to_original_path is None and "recover_to_original_path" in self.model_fields_set:
            _dict['recoverToOriginalPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OriginalNetappFilesTargetParams from a dict"""
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
            "preserveFileAttributes": obj.get("preserveFileAttributes"),
            "recoverToOriginalPath": obj.get("recoverToOriginalPath"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


