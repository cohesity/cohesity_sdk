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
from cohesity_sdk.helios.models.recovery_vlan_config import RecoveryVlanConfig
from cohesity_sdk.helios.models.vmware_recover_disks_original_source_config import VmwareRecoverDisksOriginalSourceConfig
from cohesity_sdk.helios.models.vmware_recover_disks_target_source_config import VmwareRecoverDisksTargetSourceConfig
from typing import Set
from typing_extensions import Self

class VmwareTargetParamsForRecoverDisk(BaseModel):
    """
    Specifies the parameters for a VMware recovery target.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to continue performing the recovery in the event that an error is encountered.", alias="continueOnError")
    original_source_config: Optional[VmwareRecoverDisksOriginalSourceConfig] = Field(default=None, alias="originalSourceConfig")
    power_off_vms: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to power off VMs before performing the recovery.", alias="powerOffVms")
    power_on_vms: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to power on VMs after performing the recovery.", alias="powerOnVms")
    target_source_config: Optional[VmwareRecoverDisksTargetSourceConfig] = Field(default=None, alias="targetSourceConfig")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, description="Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client's (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery.", alias="vlanConfig")
    __properties: ClassVar[List[str]] = ["continueOnError", "originalSourceConfig", "powerOffVms", "powerOnVms", "targetSourceConfig", "vlanConfig"]

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
        """Create an instance of VmwareTargetParamsForRecoverDisk from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of original_source_config
        if self.original_source_config:
            _dict['originalSourceConfig'] = self.original_source_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_source_config
        if self.target_source_config:
            _dict['targetSourceConfig'] = self.target_source_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if power_off_vms (nullable) is None
        # and model_fields_set contains the field
        if self.power_off_vms is None and "power_off_vms" in self.model_fields_set:
            _dict['powerOffVms'] = None

        # set to None if power_on_vms (nullable) is None
        # and model_fields_set contains the field
        if self.power_on_vms is None and "power_on_vms" in self.model_fields_set:
            _dict['powerOnVms'] = None

        # set to None if vlan_config (nullable) is None
        # and model_fields_set contains the field
        if self.vlan_config is None and "vlan_config" in self.model_fields_set:
            _dict['vlanConfig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareTargetParamsForRecoverDisk from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "originalSourceConfig": VmwareRecoverDisksOriginalSourceConfig.from_dict(obj["originalSourceConfig"]) if obj.get("originalSourceConfig") is not None else None,
            "powerOffVms": obj.get("powerOffVms"),
            "powerOnVms": obj.get("powerOnVms"),
            "targetSourceConfig": VmwareRecoverDisksTargetSourceConfig.from_dict(obj["targetSourceConfig"]) if obj.get("targetSourceConfig") is not None else None,
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None
        })
        return _obj


