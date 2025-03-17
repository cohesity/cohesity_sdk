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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recover_vmware_vm_new_source_network_config import RecoverVmwareVmNewSourceNetworkConfig
from cohesity_sdk.cluster.models.recovered_or_cloned_vms_rename_config import RecoveredOrClonedVmsRenameConfig
from typing import Set
from typing_extensions import Self

class VmwareProtectionGroupStandbyResourceParams(BaseModel):
    """
    VMware protection group standby resource params which will be used to create standby VM entity for backup entity.
    """ # noqa: E501
    recovery_point_objective_secs: Optional[StrictInt] = Field(default=None, description="Specifies the recovery point objective time user expects for this standby resource.", alias="recoveryPointObjectiveSecs")
    datastore_object_ids: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Specifies the list of IDs of the datastore objects where this standby resource should be created.", alias="datastoreObjectIds")
    network_config: Optional[RecoverVmwareVmNewSourceNetworkConfig] = Field(default=None, alias="networkConfig")
    parent_object_id: Optional[StrictInt] = Field(default=None, description="Specifies the object id for parent vCenter source where this standby resource should be created.", alias="parentObjectId")
    rename_restored_object_params: Optional[RecoveredOrClonedVmsRenameConfig] = Field(default=None, alias="renameRestoredObjectParams")
    resource_pool_object_id: Optional[StrictInt] = Field(default=None, description="Specifies the object id for resource pool where this standby resource should be created.", alias="resourcePoolObjectId")
    target_datastore_folder_object_id: Optional[StrictInt] = Field(default=None, description="Specifies the object id for target datastore folder where disks for this standby resource should be placed.", alias="targetDatastoreFolderObjectId")
    target_folder_object_id: Optional[StrictInt] = Field(default=None, description="Specifies the object id for target vm folder where this standby resource should be created.", alias="targetFolderObjectId")
    __properties: ClassVar[List[str]] = ["recoveryPointObjectiveSecs", "datastoreObjectIds", "networkConfig", "parentObjectId", "renameRestoredObjectParams", "resourcePoolObjectId", "targetDatastoreFolderObjectId", "targetFolderObjectId"]

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
        """Create an instance of VmwareProtectionGroupStandbyResourceParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of network_config
        if self.network_config:
            _dict['networkConfig'] = self.network_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rename_restored_object_params
        if self.rename_restored_object_params:
            _dict['renameRestoredObjectParams'] = self.rename_restored_object_params.to_dict()
        # set to None if recovery_point_objective_secs (nullable) is None
        # and model_fields_set contains the field
        if self.recovery_point_objective_secs is None and "recovery_point_objective_secs" in self.model_fields_set:
            _dict['recoveryPointObjectiveSecs'] = None

        # set to None if parent_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_object_id is None and "parent_object_id" in self.model_fields_set:
            _dict['parentObjectId'] = None

        # set to None if resource_pool_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.resource_pool_object_id is None and "resource_pool_object_id" in self.model_fields_set:
            _dict['resourcePoolObjectId'] = None

        # set to None if target_datastore_folder_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_datastore_folder_object_id is None and "target_datastore_folder_object_id" in self.model_fields_set:
            _dict['targetDatastoreFolderObjectId'] = None

        # set to None if target_folder_object_id (nullable) is None
        # and model_fields_set contains the field
        if self.target_folder_object_id is None and "target_folder_object_id" in self.model_fields_set:
            _dict['targetFolderObjectId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VmwareProtectionGroupStandbyResourceParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "recoveryPointObjectiveSecs": obj.get("recoveryPointObjectiveSecs"),
            "datastoreObjectIds": obj.get("datastoreObjectIds"),
            "networkConfig": RecoverVmwareVmNewSourceNetworkConfig.from_dict(obj["networkConfig"]) if obj.get("networkConfig") is not None else None,
            "parentObjectId": obj.get("parentObjectId"),
            "renameRestoredObjectParams": RecoveredOrClonedVmsRenameConfig.from_dict(obj["renameRestoredObjectParams"]) if obj.get("renameRestoredObjectParams") is not None else None,
            "resourcePoolObjectId": obj.get("resourcePoolObjectId"),
            "targetDatastoreFolderObjectId": obj.get("targetDatastoreFolderObjectId"),
            "targetFolderObjectId": obj.get("targetFolderObjectId")
        })
        return _obj


