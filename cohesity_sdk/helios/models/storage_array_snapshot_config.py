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
from cohesity_sdk.helios.models.storage_array_snapshot_max_snapshot_config import StorageArraySnapshotMaxSnapshotConfig
from cohesity_sdk.helios.models.storage_array_snapshot_max_space_config import StorageArraySnapshotMaxSpaceConfig
from cohesity_sdk.helios.models.storage_array_snapshot_throttling_policy import StorageArraySnapshotThrottlingPolicy
from typing import Set
from typing_extensions import Self

class StorageArraySnapshotConfig(BaseModel):
    """
    Specifies the storage array snapshot config for individual volume/lun.
    """ # noqa: E501
    max_snapshot_config: Optional[StorageArraySnapshotMaxSnapshotConfig] = Field(default=None, alias="maxSnapshotConfig")
    max_snapshots_config_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether we will use storage snapshot managmement max snapshots config to all volumes/luns that are part of the registered entity.", alias="maxSnapshotsConfigEnabled")
    max_space_config: Optional[StorageArraySnapshotMaxSpaceConfig] = Field(default=None, alias="maxSpaceConfig")
    max_space_config_enabled: Optional[StrictBool] = Field(default=None, description="Specifies whether we will use storage snapshot managmement max space config to all volumes/luns that are part of the registered entity.", alias="maxSpaceConfigEnabled")
    storage_array_snapshot_throttling_policies: Optional[List[StorageArraySnapshotThrottlingPolicy]] = Field(default=None, description="Specifies the list of storage array snapshot management throttling policies for individual volume/lun.", alias="storageArraySnapshotThrottlingPolicies")
    __properties: ClassVar[List[str]] = ["maxSnapshotConfig", "maxSnapshotsConfigEnabled", "maxSpaceConfig", "maxSpaceConfigEnabled", "storageArraySnapshotThrottlingPolicies"]

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
        """Create an instance of StorageArraySnapshotConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of max_snapshot_config
        if self.max_snapshot_config:
            _dict['maxSnapshotConfig'] = self.max_snapshot_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max_space_config
        if self.max_space_config:
            _dict['maxSpaceConfig'] = self.max_space_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in storage_array_snapshot_throttling_policies (list)
        _items = []
        if self.storage_array_snapshot_throttling_policies:
            for _item_storage_array_snapshot_throttling_policies in self.storage_array_snapshot_throttling_policies:
                if _item_storage_array_snapshot_throttling_policies:
                    _items.append(_item_storage_array_snapshot_throttling_policies.to_dict())
            _dict['storageArraySnapshotThrottlingPolicies'] = _items
        # set to None if max_snapshots_config_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.max_snapshots_config_enabled is None and "max_snapshots_config_enabled" in self.model_fields_set:
            _dict['maxSnapshotsConfigEnabled'] = None

        # set to None if max_space_config_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.max_space_config_enabled is None and "max_space_config_enabled" in self.model_fields_set:
            _dict['maxSpaceConfigEnabled'] = None

        # set to None if storage_array_snapshot_throttling_policies (nullable) is None
        # and model_fields_set contains the field
        if self.storage_array_snapshot_throttling_policies is None and "storage_array_snapshot_throttling_policies" in self.model_fields_set:
            _dict['storageArraySnapshotThrottlingPolicies'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StorageArraySnapshotConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxSnapshotConfig": StorageArraySnapshotMaxSnapshotConfig.from_dict(obj["maxSnapshotConfig"]) if obj.get("maxSnapshotConfig") is not None else None,
            "maxSnapshotsConfigEnabled": obj.get("maxSnapshotsConfigEnabled"),
            "maxSpaceConfig": StorageArraySnapshotMaxSpaceConfig.from_dict(obj["maxSpaceConfig"]) if obj.get("maxSpaceConfig") is not None else None,
            "maxSpaceConfigEnabled": obj.get("maxSpaceConfigEnabled"),
            "storageArraySnapshotThrottlingPolicies": [StorageArraySnapshotThrottlingPolicy.from_dict(_item) for _item in obj["storageArraySnapshotThrottlingPolicies"]] if obj.get("storageArraySnapshotThrottlingPolicies") is not None else None
        })
        return _obj


