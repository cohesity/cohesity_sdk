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
from cohesity_sdk.cluster.models.mounted_volume_mapping import MountedVolumeMapping
from cohesity_sdk.cluster.models.physical_mount_volumes_new_target_config import PhysicalMountVolumesNewTargetConfig
from cohesity_sdk.cluster.models.physical_mount_volumes_original_target_config import PhysicalMountVolumesOriginalTargetConfig
from cohesity_sdk.cluster.models.recovery_vlan_config import RecoveryVlanConfig
from typing import Set
from typing_extensions import Self

class PhysicalTargetParamsForMountVolume(BaseModel):
    """
    Specifies the parameters for a physical recovery target.
    """ # noqa: E501
    mount_to_original_target: Optional[StrictBool] = Field(description="Specifies whether to mount to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified.", alias="mountToOriginalTarget")
    mounted_volume_mapping: Optional[List[MountedVolumeMapping]] = Field(default=None, description="Specifies the mapping of original volumes and mounted volumes", alias="mountedVolumeMapping")
    new_target_config: Optional[PhysicalMountVolumesNewTargetConfig] = Field(default=None, alias="newTargetConfig")
    original_target_config: Optional[PhysicalMountVolumesOriginalTargetConfig] = Field(default=None, alias="originalTargetConfig")
    read_only_mount: Optional[StrictBool] = Field(default=None, description="Specifies whether to perform a read-only mount. Default is false.", alias="readOnlyMount")
    vlan_config: Optional[RecoveryVlanConfig] = Field(default=None, alias="vlanConfig")
    volume_names: Optional[List[StrictStr]] = Field(default=None, description="Specifies the names of volumes that need to be mounted. If this is not specified then all volumes that are part of the source VM will be mounted on the target VM.", alias="volumeNames")
    __properties: ClassVar[List[str]] = ["mountToOriginalTarget", "mountedVolumeMapping", "newTargetConfig", "originalTargetConfig", "readOnlyMount", "vlanConfig", "volumeNames"]

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
        """Create an instance of PhysicalTargetParamsForMountVolume from a JSON string"""
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
            "mounted_volume_mapping",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in mounted_volume_mapping (list)
        _items = []
        if self.mounted_volume_mapping:
            for _item_mounted_volume_mapping in self.mounted_volume_mapping:
                if _item_mounted_volume_mapping:
                    _items.append(_item_mounted_volume_mapping.to_dict())
            _dict['mountedVolumeMapping'] = _items
        # override the default output from pydantic by calling `to_dict()` of new_target_config
        if self.new_target_config:
            _dict['newTargetConfig'] = self.new_target_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_target_config
        if self.original_target_config:
            _dict['originalTargetConfig'] = self.original_target_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vlan_config
        if self.vlan_config:
            _dict['vlanConfig'] = self.vlan_config.to_dict()
        # set to None if mount_to_original_target (nullable) is None
        # and model_fields_set contains the field
        if self.mount_to_original_target is None and "mount_to_original_target" in self.model_fields_set:
            _dict['mountToOriginalTarget'] = None

        # set to None if mounted_volume_mapping (nullable) is None
        # and model_fields_set contains the field
        if self.mounted_volume_mapping is None and "mounted_volume_mapping" in self.model_fields_set:
            _dict['mountedVolumeMapping'] = None

        # set to None if read_only_mount (nullable) is None
        # and model_fields_set contains the field
        if self.read_only_mount is None and "read_only_mount" in self.model_fields_set:
            _dict['readOnlyMount'] = None

        # set to None if volume_names (nullable) is None
        # and model_fields_set contains the field
        if self.volume_names is None and "volume_names" in self.model_fields_set:
            _dict['volumeNames'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PhysicalTargetParamsForMountVolume from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mountToOriginalTarget": obj.get("mountToOriginalTarget"),
            "mountedVolumeMapping": [MountedVolumeMapping.from_dict(_item) for _item in obj["mountedVolumeMapping"]] if obj.get("mountedVolumeMapping") is not None else None,
            "newTargetConfig": PhysicalMountVolumesNewTargetConfig.from_dict(obj["newTargetConfig"]) if obj.get("newTargetConfig") is not None else None,
            "originalTargetConfig": PhysicalMountVolumesOriginalTargetConfig.from_dict(obj["originalTargetConfig"]) if obj.get("originalTargetConfig") is not None else None,
            "readOnlyMount": obj.get("readOnlyMount"),
            "vlanConfig": RecoveryVlanConfig.from_dict(obj["vlanConfig"]) if obj.get("vlanConfig") is not None else None,
            "volumeNames": obj.get("volumeNames")
        })
        return _obj


