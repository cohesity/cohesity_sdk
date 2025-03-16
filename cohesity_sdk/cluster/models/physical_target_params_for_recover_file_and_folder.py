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
from cohesity_sdk.cluster.models.recover_target import RecoverTarget
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Optional, Set
from typing_extensions import Self

class PhysicalTargetParamsForRecoverFileAndFolder(BaseModel):
    """
    Specifies the parameters for a Physical recovery target.
    """ # noqa: E501
    alternate_restore_directory: Optional[StrictStr] = Field(default=None, description="Specifies the directory path where restore should happen if restore_to_original_paths is set to false.", alias="alternateRestoreDirectory")
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other volumes if one of the volumes fails to recover. Default value is false.", alias="continueOnError")
    overwrite_existing: Optional[StrictBool] = Field(default=None, description="Specifies whether to overwrite existing file/folder during recovery.", alias="overwriteExisting")
    preserve_acls: Optional[StrictBool] = Field(default=None, description="Whether to preserve the ACLs of the original file.", alias="preserveAcls")
    preserve_attributes: Optional[StrictBool] = Field(default=None, description="Specifies whether to preserve file/folder attributes during recovery.", alias="preserveAttributes")
    preserve_timestamps: Optional[StrictBool] = Field(default=None, description="Whether to preserve the original time stamps.", alias="preserveTimestamps")
    recover_target: RecoverTarget = Field(alias="recoverTarget")
    restore_entity_type: Optional[StrictStr] = Field(default=None, description="Specifies the restore type (restore everything or ACLs only) when restoring or downloading files or folders from a Physical file based or block based backup snapshot.", alias="restoreEntityType")
    restore_to_original_paths: Optional[StrictBool] = Field(default=None, description="If this is true, then files will be restored to original paths.", alias="restoreToOriginalPaths")
    save_success_files: Optional[StrictBool] = Field(default=None, description="Specifies whether to save success files or not. Default value is false", alias="saveSuccessFiles")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["alternateRestoreDirectory", "continueOnError", "overwriteExisting", "preserveAcls", "preserveAttributes", "preserveTimestamps", "recoverTarget", "restoreEntityType", "restoreToOriginalPaths", "saveSuccessFiles", "vlanConfig"]

    @field_validator('restore_entity_type')
    def restore_entity_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kRegular', 'kACLOnly']):
            raise ValueError("must be one of enum values ('kRegular', 'kACLOnly')")
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
        """Create an instance of PhysicalTargetParamsForRecoverFileAndFolder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recover_target
        if self.recover_target:
            _dict['recoverTarget'] = self.recover_target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # set to None if alternate_restore_directory (nullable) is None
        # and model_fields_set contains the field
        if self.alternate_restore_directory is None and "alternate_restore_directory" in self.model_fields_set:
            _dict['alternateRestoreDirectory'] = None

        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if overwrite_existing (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite_existing is None and "overwrite_existing" in self.model_fields_set:
            _dict['overwriteExisting'] = None

        # set to None if preserve_acls (nullable) is None
        # and model_fields_set contains the field
        if self.preserve_acls is None and "preserve_acls" in self.model_fields_set:
            _dict['preserveAcls'] = None

        # set to None if preserve_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.preserve_attributes is None and "preserve_attributes" in self.model_fields_set:
            _dict['preserveAttributes'] = None

        # set to None if preserve_timestamps (nullable) is None
        # and model_fields_set contains the field
        if self.preserve_timestamps is None and "preserve_timestamps" in self.model_fields_set:
            _dict['preserveTimestamps'] = None

        # set to None if restore_entity_type (nullable) is None
        # and model_fields_set contains the field
        if self.restore_entity_type is None and "restore_entity_type" in self.model_fields_set:
            _dict['restoreEntityType'] = None

        # set to None if restore_to_original_paths (nullable) is None
        # and model_fields_set contains the field
        if self.restore_to_original_paths is None and "restore_to_original_paths" in self.model_fields_set:
            _dict['restoreToOriginalPaths'] = None

        # set to None if save_success_files (nullable) is None
        # and model_fields_set contains the field
        if self.save_success_files is None and "save_success_files" in self.model_fields_set:
            _dict['saveSuccessFiles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalTargetParamsForRecoverFileAndFolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alternateRestoreDirectory": obj.get("alternateRestoreDirectory"),
            "continueOnError": obj.get("continueOnError"),
            "overwriteExisting": obj.get("overwriteExisting"),
            "preserveAcls": obj.get("preserveAcls"),
            "preserveAttributes": obj.get("preserveAttributes"),
            "preserveTimestamps": obj.get("preserveTimestamps"),
            "recoverTarget": RecoverTarget.from_dict(obj["recoverTarget"]) if obj.get("recoverTarget") is not None else None,
            "restoreEntityType": obj.get("restoreEntityType"),
            "restoreToOriginalPaths": obj.get("restoreToOriginalPaths"),
            "saveSuccessFiles": obj.get("saveSuccessFiles"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


