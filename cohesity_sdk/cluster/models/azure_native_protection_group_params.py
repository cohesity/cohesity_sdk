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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.azure_native_protection_group_object_params import AzureNativeProtectionGroupObjectParams
from cohesity_sdk.cluster.models.cloud_backup_script_params import CloudBackupScriptParams
from cohesity_sdk.cluster.models.data_transfer_info import DataTransferInfo
from cohesity_sdk.cluster.models.indexing_policy import IndexingPolicy
from typing import Optional, Set
from typing_extensions import Self

class AzureNativeProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to Azure related Protection Groups using Azure native snapshot APIs. Objects must be specified.
    """ # noqa: E501
    cloud_migration: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to move the workload to the cloud.", alias="cloudMigration")
    cloud_pre_post_script: Optional[CloudBackupScriptParams] = Field(default=None, alias="cloudPrePostScript")
    data_transfer_info: Optional[DataTransferInfo] = Field(default=None, alias="dataTransferInfo")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    exclude_vm_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of arrays of VM Tag Ids that Specify VMs to Exclude.", alias="excludeVmTagIds")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    objects: Optional[List[AzureNativeProtectionGroupObjectParams]] = Field(default=None, description="Specifies the objects to be included in the Protection Group.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    vm_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of arrays of VM Tag Ids that Specify VMs to Protect.", alias="vmTagIds")
    __properties: ClassVar[List[str]] = ["cloudMigration", "cloudPrePostScript", "dataTransferInfo", "excludeObjectIds", "excludeVmTagIds", "indexingPolicy", "objects", "sourceId", "sourceName", "vmTagIds"]

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
        """Create an instance of AzureNativeProtectionGroupParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "source_id",
            "source_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cloud_pre_post_script
        if self.cloud_pre_post_script:
            _dict['cloudPrePostScript'] = self.cloud_pre_post_script.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_transfer_info
        if self.data_transfer_info:
            _dict['dataTransferInfo'] = self.data_transfer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if cloud_migration (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_migration is None and "cloud_migration" in self.model_fields_set:
            _dict['cloudMigration'] = None

        # set to None if exclude_vm_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_vm_tag_ids is None and "exclude_vm_tag_ids" in self.model_fields_set:
            _dict['excludeVmTagIds'] = None

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        # set to None if vm_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.vm_tag_ids is None and "vm_tag_ids" in self.model_fields_set:
            _dict['vmTagIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AzureNativeProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cloudMigration": obj.get("cloudMigration"),
            "cloudPrePostScript": CloudBackupScriptParams.from_dict(obj["cloudPrePostScript"]) if obj.get("cloudPrePostScript") is not None else None,
            "dataTransferInfo": DataTransferInfo.from_dict(obj["dataTransferInfo"]) if obj.get("dataTransferInfo") is not None else None,
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "excludeVmTagIds": obj.get("excludeVmTagIds"),
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None,
            "objects": [AzureNativeProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "vmTagIds": obj.get("vmTagIds")
        })
        return _obj


