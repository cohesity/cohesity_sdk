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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.gcp_recover_files_new_target_config import GcpRecoverFilesNewTargetConfig
from cohesity_sdk.helios.models.gcp_recover_files_original_target_config import GcpRecoverFilesOriginalTargetConfig
from cohesity_sdk.helios.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Optional, Set
from typing_extensions import Self

class GcpTargetParamsForRecoverFileAndFolder(BaseModel):
    """
    Specifies the parameters for a GCP recovery target.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other files if one of files or folders failed to recover. Default value is false.", alias="continueOnError")
    new_target_config: Optional[GcpRecoverFilesNewTargetConfig] = Field(default=None, alias="newTargetConfig")
    original_target_config: Optional[GcpRecoverFilesOriginalTargetConfig] = Field(default=None, alias="originalTargetConfig")
    overwrite_existing: Optional[StrictBool] = Field(default=None, description="Specifies whether to override the existing files. Default is true.", alias="overwriteExisting")
    preserve_attributes: Optional[StrictBool] = Field(default=None, description="Specifies whether to preserve original attributes. Default is true.", alias="preserveAttributes")
    recover_to_original_target: Optional[StrictBool] = Field(description="Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified.", alias="recoverToOriginalTarget")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["continueOnError", "newTargetConfig", "originalTargetConfig", "overwriteExisting", "preserveAttributes", "recoverToOriginalTarget", "vlanConfig"]

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
        """Create an instance of GcpTargetParamsForRecoverFileAndFolder from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of new_target_config
        if self.new_target_config:
            _dict['newTargetConfig'] = self.new_target_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_target_config
        if self.original_target_config:
            _dict['originalTargetConfig'] = self.original_target_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if overwrite_existing (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite_existing is None and "overwrite_existing" in self.model_fields_set:
            _dict['overwriteExisting'] = None

        # set to None if preserve_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.preserve_attributes is None and "preserve_attributes" in self.model_fields_set:
            _dict['preserveAttributes'] = None

        # set to None if recover_to_original_target (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to_original_target is None and "recover_to_original_target" in self.model_fields_set:
            _dict['recoverToOriginalTarget'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GcpTargetParamsForRecoverFileAndFolder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "newTargetConfig": GcpRecoverFilesNewTargetConfig.from_dict(obj["newTargetConfig"]) if obj.get("newTargetConfig") is not None else None,
            "originalTargetConfig": GcpRecoverFilesOriginalTargetConfig.from_dict(obj["originalTargetConfig"]) if obj.get("originalTargetConfig") is not None else None,
            "overwriteExisting": obj.get("overwriteExisting"),
            "preserveAttributes": obj.get("preserveAttributes"),
            "recoverToOriginalTarget": obj.get("recoverToOriginalTarget"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


