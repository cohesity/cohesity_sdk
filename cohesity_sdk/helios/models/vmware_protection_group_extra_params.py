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
from cohesity_sdk.helios.models.vm_filter import VMFilter
from typing import Optional, Set
from typing_extensions import Self

class VmwareProtectionGroupExtraParams(BaseModel):
    """
    Specifies the extra parameters which are specific to VMware object protection Group.
    """ # noqa: E501
    allow_parallel_runs: Optional[StrictBool] = Field(default=None, description="Specifies whether or not this job can have parallel runs.", alias="allowParallelRuns")
    cloud_migration: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to move the workload to the cloud.", alias="cloudMigration")
    exclude_filters: Optional[List[VMFilter]] = Field(default=None, description="Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying these filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters.", alias="excludeFilters")
    exclude_object_ids: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Specifies the list of IDs of the objects to not be protected in this backup. This field only applies if provided object id is non leaf entity such as Tag or a folder. This can be used to ignore specific objects under a parent object which has been included for protection.", alias="excludeObjectIds")
    exclude_vm_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of Arrays of VM Tag Ids that Specify VMs to Exclude. Optionally specify a list of VMs to exclude from protecting by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. For example a Datacenter is selected to be protected but you want to exclude all the 'Former Employees' VMs in the East and West but keep all the VMs for 'Former Employees' in the South which are also stored in this Datacenter, by specifying the following tag id array: [ [1000, 2221], [1000, 3031] ], where 1000 is the 'Former Employee' VM Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag id. The first inner array [1000, 2221] produces a list of VMs that are both tagged with 'Former Employees' and 'East' (an intersection). The second inner array [1000, 3031] produces a list of VMs that are both tagged with 'Former Employees' and 'West' (an intersection). The outer array combines the list of VMs from the two inner arrays. The list of resulting VMs are excluded from being protected this Job.", alias="excludeVmTagIds")
    leverage_hyperflex_snapshots: Optional[StrictBool] = Field(default=None, description="Whether to leverage the hyperflex based snapshots for this backup. To leverage hyperflex snapshots, it has to first be registered. If hyperflex based snapshots cannot be taken, backup will fallback to the default backup method.", alias="leverageHyperflexSnapshots")
    leverage_nutanix_snapshots: Optional[StrictBool] = Field(default=None, description="Whether to leverage the nutanix based snapshots for this backup. To leverage nutanix snapshots, it has to first be registered. If nutanix based snapshots cannot be taken, backup will fallback to the default backup method.", alias="leverageNutanixSnapshots")
    leverage_storage_snapshots: Optional[StrictBool] = Field(default=None, description="Whether to leverage the storage array based snapshots for this backup. To leverage storage snapshots, the storage array has to be registered as a source. If storage based snapshots can not be taken, backup will fallback to the default backup method.", alias="leverageStorageSnapshots")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    vm_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of Array of VM Tag Ids that Specify VMs to Protect. Optionally specify a list of VMs to protect by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to protect which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. To protect only 'Eng' VMs in the East and all the VMs in the West, specify the following tag id array: [ [1101, 2221], [3031] ], where 1101 is the 'Eng' VM Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag id. The inner array [1101, 2221] produces a list of VMs that are both tagged with 'Eng' and 'East' (an intersection). The outer array combines the list from the inner array with list of VMs tagged with 'West' (a union). The list of resulting VMs are protected by this Protection Group.", alias="vmTagIds")
    __properties: ClassVar[List[str]] = ["allowParallelRuns", "cloudMigration", "excludeFilters", "excludeObjectIds", "excludeVmTagIds", "leverageHyperflexSnapshots", "leverageNutanixSnapshots", "leverageStorageSnapshots", "sourceId", "sourceName", "vmTagIds"]

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
        """Create an instance of VmwareProtectionGroupExtraParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in exclude_filters (list)
        _items = []
        if self.exclude_filters:
            for _item_exclude_filters in self.exclude_filters:
                if _item_exclude_filters:
                    _items.append(_item_exclude_filters.to_dict())
            _dict['excludeFilters'] = _items
        # set to None if allow_parallel_runs (nullable) is None
        # and model_fields_set contains the field
        if self.allow_parallel_runs is None and "allow_parallel_runs" in self.model_fields_set:
            _dict['allowParallelRuns'] = None

        # set to None if cloud_migration (nullable) is None
        # and model_fields_set contains the field
        if self.cloud_migration is None and "cloud_migration" in self.model_fields_set:
            _dict['cloudMigration'] = None

        # set to None if exclude_filters (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_filters is None and "exclude_filters" in self.model_fields_set:
            _dict['excludeFilters'] = None

        # set to None if leverage_hyperflex_snapshots (nullable) is None
        # and model_fields_set contains the field
        if self.leverage_hyperflex_snapshots is None and "leverage_hyperflex_snapshots" in self.model_fields_set:
            _dict['leverageHyperflexSnapshots'] = None

        # set to None if leverage_nutanix_snapshots (nullable) is None
        # and model_fields_set contains the field
        if self.leverage_nutanix_snapshots is None and "leverage_nutanix_snapshots" in self.model_fields_set:
            _dict['leverageNutanixSnapshots'] = None

        # set to None if leverage_storage_snapshots (nullable) is None
        # and model_fields_set contains the field
        if self.leverage_storage_snapshots is None and "leverage_storage_snapshots" in self.model_fields_set:
            _dict['leverageStorageSnapshots'] = None

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
        """Create an instance of VmwareProtectionGroupExtraParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowParallelRuns": obj.get("allowParallelRuns"),
            "cloudMigration": obj.get("cloudMigration"),
            "excludeFilters": [VMFilter.from_dict(_item) for _item in obj["excludeFilters"]] if obj.get("excludeFilters") is not None else None,
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "excludeVmTagIds": obj.get("excludeVmTagIds"),
            "leverageHyperflexSnapshots": obj.get("leverageHyperflexSnapshots"),
            "leverageNutanixSnapshots": obj.get("leverageNutanixSnapshots"),
            "leverageStorageSnapshots": obj.get("leverageStorageSnapshots"),
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "vmTagIds": obj.get("vmTagIds")
        })
        return _obj


