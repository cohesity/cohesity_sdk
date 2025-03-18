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
from cohesity_sdk.helios.models.recover_acropolis_vm_target_config import RecoverAcropolisVmTargetConfig
from cohesity_sdk.helios.models.recovered_or_cloned_vms_rename_config import RecoveredOrClonedVmsRenameConfig
from cohesity_sdk.helios.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Set
from typing_extensions import Self

class AcropolisTargetParamsForRecoverVm(BaseModel):
    """
    Specifies the parameters for an Acropolis recovery target.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false.", alias="continueOnError")
    power_on_vms: Optional[StrictBool] = Field(default=None, description="Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state.", alias="powerOnVms")
    recover_excluded_disk: Optional[StrictBool] = Field(default=None, description="Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false.", alias="recoverExcludedDisk")
    recovery_process_type: Optional[StrictStr] = Field(default=None, description="Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery.", alias="recoveryProcessType")
    recovery_target_config: Optional[RecoverAcropolisVmTargetConfig] = Field(default=None, description="Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source or to original Source with different configuration. If not specified, then the recovery of the vms will be performed to original location with all configuration parameters retained.", alias="recoveryTargetConfig")
    rename_recovered_vms_params: Optional[RecoveredOrClonedVmsRenameConfig] = Field(default=None, description="Specifies params to rename the VMs that are recovered. If not specified, the original names of the VMs are preserved.", alias="renameRecoveredVmsParams")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, description="Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client's (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery.", alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["continueOnError", "powerOnVms", "recoverExcludedDisk", "recoveryProcessType", "recoveryTargetConfig", "renameRecoveredVmsParams", "vlanConfig"]

    @field_validator('recovery_process_type')
    def recovery_process_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InstantRecovery', 'CopyRecovery']):
            raise ValueError("must be one of enum values ('InstantRecovery', 'CopyRecovery')")
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
        """Create an instance of AcropolisTargetParamsForRecoverVm from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of recovery_target_config
        if self.recovery_target_config:
            _dict['recoveryTargetConfig'] = self.recovery_target_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rename_recovered_vms_params
        if self.rename_recovered_vms_params:
            _dict['renameRecoveredVmsParams'] = self.rename_recovered_vms_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if power_on_vms (nullable) is None
        # and model_fields_set contains the field
        if self.power_on_vms is None and "power_on_vms" in self.model_fields_set:
            _dict['powerOnVms'] = None

        # set to None if recover_excluded_disk (nullable) is None
        # and model_fields_set contains the field
        if self.recover_excluded_disk is None and "recover_excluded_disk" in self.model_fields_set:
            _dict['recoverExcludedDisk'] = None

        # set to None if recovery_target_config (nullable) is None
        # and model_fields_set contains the field
        if self.recovery_target_config is None and "recovery_target_config" in self.model_fields_set:
            _dict['recoveryTargetConfig'] = None

        # set to None if rename_recovered_vms_params (nullable) is None
        # and model_fields_set contains the field
        if self.rename_recovered_vms_params is None and "rename_recovered_vms_params" in self.model_fields_set:
            _dict['renameRecoveredVmsParams'] = None

        # set to None if vlan_config (nullable) is None
        # and model_fields_set contains the field
        if self.vlan_config is None and "vlan_config" in self.model_fields_set:
            _dict['vlanConfig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AcropolisTargetParamsForRecoverVm from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "powerOnVms": obj.get("powerOnVms"),
            "recoverExcludedDisk": obj.get("recoverExcludedDisk"),
            "recoveryProcessType": obj.get("recoveryProcessType"),
            "recoveryTargetConfig": RecoverAcropolisVmTargetConfig.from_dict(obj["recoveryTargetConfig"]) if obj.get("recoveryTargetConfig") is not None else None,
            "renameRecoveredVmsParams": RecoveredOrClonedVmsRenameConfig.from_dict(obj["renameRecoveredVmsParams"]) if obj.get("renameRecoveredVmsParams") is not None else None,
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


