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
from cohesity_sdk.cluster.models.recovered_or_cloned_vms_rename_config import RecoveredOrClonedVmsRenameConfig
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig
from cohesity_sdk.cluster.models.vmware_vm_recovery_target_config import VmwareVmRecoveryTargetConfig
from typing import Optional, Set
from typing_extensions import Self

class VmwareTargetParamsForRecoverVM(BaseModel):
    """
    Specifies the parameters for a VMware recovery target.
    """ # noqa: E501
    attempt_differential_restore: Optional[StrictBool] = Field(default=None, description="Specifies whether to attempt differential restore.", alias="attemptDifferentialRestore")
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false.", alias="continueOnError")
    disk_provision_type: Optional[StrictStr] = Field(default=None, description="Specifies the Virtual Disk Provisioning Policies for Vmware VM", alias="diskProvisionType")
    enable_nbdssl_fallback: Optional[StrictBool] = Field(default=None, description="If this field is set to true and SAN transport recovery fails, then recovery will fallback to use NBDSSL transport. This field only applies if 'leverageSanTransport' is set to true.", alias="enableNBDSSLFallback")
    is_multi_stage_restore: Optional[StrictBool] = Field(default=None, description="Specifies whether this is a multistage restore which is used for migration/hot-standby purpose.", alias="isMultiStageRestore")
    leverage_san_transport: Optional[StrictBool] = Field(default=None, description="Specifies whether to enable SAN transport for copy recovery or not", alias="leverageSanTransport")
    overwrite_existing_vm: Optional[StrictBool] = Field(default=None, description="Specifies whether to overwrite the VM at the target location. This is a data destructive operation and if this is selected, the original VM may no longer be accessible. This option is only applicable if renameRecoveredVmParams is null and powerOffAndRenameExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false.", alias="overwriteExistingVm")
    power_off_and_rename_existing_vm: Optional[StrictBool] = Field(default=None, description="Specifies whether to power off and mark the VM at the target location as deprecated. As an example, <vm_name> will be renamed to deprecated::<vm_name>, and a new VM with the name <vm_name> in place of the now deprecated VM. Both deprecated::<vm_name> and <vm_name> will exist on the primary, but the corresponding protection job will only backup <vm_name> on its next run. Only applicable if renameRecoveredVmParams is null and overwriteExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false.", alias="powerOffAndRenameExistingVm")
    power_on_vms: Optional[StrictBool] = Field(default=None, description="Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state.", alias="powerOnVms")
    recovery_process_type: Optional[StrictStr] = Field(default=None, description="Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery.", alias="recoveryProcessType")
    recovery_target_config: Optional[VmwareVmRecoveryTargetConfig] = Field(default=None, alias="recoveryTargetConfig")
    rename_recovered_vms_params: Optional[RecoveredOrClonedVmsRenameConfig] = Field(default=None, alias="renameRecoveredVmsParams")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["attemptDifferentialRestore", "continueOnError", "diskProvisionType", "enableNBDSSLFallback", "isMultiStageRestore", "leverageSanTransport", "overwriteExistingVm", "powerOffAndRenameExistingVm", "powerOnVms", "recoveryProcessType", "recoveryTargetConfig", "renameRecoveredVmsParams", "vlanConfig"]

    @field_validator('disk_provision_type')
    def disk_provision_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kThickLazyZeroed', 'kThickEagerZero', 'kThin', 'kBackedUpDiskType', 'originalBackUpDisk']):
            raise ValueError("must be one of enum values ('kThickLazyZeroed', 'kThickEagerZero', 'kThin', 'kBackedUpDiskType', 'originalBackUpDisk')")
        return value

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
        """Create an instance of VmwareTargetParamsForRecoverVM from a JSON string"""
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
        # set to None if attempt_differential_restore (nullable) is None
        # and model_fields_set contains the field
        if self.attempt_differential_restore is None and "attempt_differential_restore" in self.model_fields_set:
            _dict['attemptDifferentialRestore'] = None

        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if disk_provision_type (nullable) is None
        # and model_fields_set contains the field
        if self.disk_provision_type is None and "disk_provision_type" in self.model_fields_set:
            _dict['diskProvisionType'] = None

        # set to None if enable_nbdssl_fallback (nullable) is None
        # and model_fields_set contains the field
        if self.enable_nbdssl_fallback is None and "enable_nbdssl_fallback" in self.model_fields_set:
            _dict['enableNBDSSLFallback'] = None

        # set to None if is_multi_stage_restore (nullable) is None
        # and model_fields_set contains the field
        if self.is_multi_stage_restore is None and "is_multi_stage_restore" in self.model_fields_set:
            _dict['isMultiStageRestore'] = None

        # set to None if leverage_san_transport (nullable) is None
        # and model_fields_set contains the field
        if self.leverage_san_transport is None and "leverage_san_transport" in self.model_fields_set:
            _dict['leverageSanTransport'] = None

        # set to None if overwrite_existing_vm (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite_existing_vm is None and "overwrite_existing_vm" in self.model_fields_set:
            _dict['overwriteExistingVm'] = None

        # set to None if power_off_and_rename_existing_vm (nullable) is None
        # and model_fields_set contains the field
        if self.power_off_and_rename_existing_vm is None and "power_off_and_rename_existing_vm" in self.model_fields_set:
            _dict['powerOffAndRenameExistingVm'] = None

        # set to None if power_on_vms (nullable) is None
        # and model_fields_set contains the field
        if self.power_on_vms is None and "power_on_vms" in self.model_fields_set:
            _dict['powerOnVms'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareTargetParamsForRecoverVM from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "attemptDifferentialRestore": obj.get("attemptDifferentialRestore"),
            "continueOnError": obj.get("continueOnError"),
            "diskProvisionType": obj.get("diskProvisionType"),
            "enableNBDSSLFallback": obj.get("enableNBDSSLFallback"),
            "isMultiStageRestore": obj.get("isMultiStageRestore"),
            "leverageSanTransport": obj.get("leverageSanTransport"),
            "overwriteExistingVm": obj.get("overwriteExistingVm"),
            "powerOffAndRenameExistingVm": obj.get("powerOffAndRenameExistingVm"),
            "powerOnVms": obj.get("powerOnVms"),
            "recoveryProcessType": obj.get("recoveryProcessType"),
            "recoveryTargetConfig": VmwareVmRecoveryTargetConfig.from_dict(obj["recoveryTargetConfig"]) if obj.get("recoveryTargetConfig") is not None else None,
            "renameRecoveredVmsParams": RecoveredOrClonedVmsRenameConfig.from_dict(obj["renameRecoveredVmsParams"]) if obj.get("renameRecoveredVmsParams") is not None else None,
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


