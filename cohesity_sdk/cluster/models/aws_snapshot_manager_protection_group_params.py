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
from cohesity_sdk.cluster.models.aws_snapshot_manager_protection_group_object_params import AwsSnapshotManagerProtectionGroupObjectParams
from cohesity_sdk.cluster.models.ebs_volume_exclusion_params import EbsVolumeExclusionParams
from typing import Optional, Set
from typing_extensions import Self

class AwsSnapshotManagerProtectionGroupParams(BaseModel):
    """
    Specifies the parameters which are specific to AWS related Protection Groups using AWS native snapshot orchestration with snapshot manager. Atlease one of tags or objects must be specified.
    """ # noqa: E501
    ami_creation_frequency: Optional[StrictInt] = Field(default=None, description="The frequency of AMI creation. This should be set if the option to create AMI is set. A value of n creates an AMI from the snapshots after every n runs. eg. n = 2 implies every alternate backup run starting from the first will create an AMI.", alias="amiCreationFrequency")
    create_ami: Optional[StrictBool] = Field(default=None, description="Specifies whether AMI should be created after taking snapshots of the instance.", alias="createAmi")
    exclude_object_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the objects to be excluded in the Protection Group.", alias="excludeObjectIds")
    exclude_vm_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of Arrays of VM Tag Ids that Specify VMs to Exclude. Optionally specify a list of VMs to exclude from protecting by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to exclude from protecting, which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. For example a Datacenter is selected to be protected but you want to exclude all the 'Former Employees' VMs in the East and West but keep all the VMs for 'Former Employees' in the South which are also stored in this Datacenter, by specifying the following tag id array: [ [1000, 2221], [1000, 3031] ], where 1000 is the 'Former Employee' VM Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag id. The first inner array [1000, 2221] produces a list of VMs that are both tagged with 'Former Employees' and 'East' (an intersection). The second inner array [1000, 3031] produces a list of VMs that are both tagged with 'Former Employees' and 'West' (an intersection). The outer array combines the list of VMs from the two inner arrays. The list of resulting VMs are excluded from being protected this Job.", alias="excludeVmTagIds")
    objects: Optional[List[AwsSnapshotManagerProtectionGroupObjectParams]] = Field(default=None, description="Specifies the objects to be included in the Protection Group.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies the id of the parent of the objects.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the parent of the objects.", alias="sourceName")
    vm_tag_ids: Optional[List[List[StrictInt]]] = Field(default=None, description="Array of Array of VM Tag Ids that Specify VMs to Protect. Optionally specify a list of VMs to protect by listing Protection Source ids of VM Tags in this two dimensional array. Using this two dimensional array of Tag ids, the Cluster generates a list of VMs to protect which are derived from intersections of the inner arrays and union of the outer array, as shown by the following example. To protect only 'Eng' VMs in the East and all the VMs in the West, specify the following tag id array: [ [1101, 2221], [3031] ], where 1101 is the 'Eng' VM Tag id, 2221 is the 'East' VM Tag id and 3031 is the 'West' VM Tag id. The inner array [1101, 2221] produces a list of VMs that are both tagged with 'Eng' and 'East' (an intersection). The outer array combines the list from the inner array with list of VMs tagged with 'West' (a union). The list of resulting VMs are protected by this Protection Group.", alias="vmTagIds")
    volume_exclusion_params: Optional[EbsVolumeExclusionParams] = Field(default=None, alias="volumeExclusionParams")
    __properties: ClassVar[List[str]] = ["amiCreationFrequency", "createAmi", "excludeObjectIds", "excludeVmTagIds", "objects", "sourceId", "sourceName", "vmTagIds", "volumeExclusionParams"]

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
        """Create an instance of AwsSnapshotManagerProtectionGroupParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of volume_exclusion_params
        if self.volume_exclusion_params:
            _dict['volumeExclusionParams'] = self.volume_exclusion_params.to_dict()
        # set to None if ami_creation_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.ami_creation_frequency is None and "ami_creation_frequency" in self.model_fields_set:
            _dict['amiCreationFrequency'] = None

        # set to None if create_ami (nullable) is None
        # and model_fields_set contains the field
        if self.create_ami is None and "create_ami" in self.model_fields_set:
            _dict['createAmi'] = None

        # set to None if exclude_object_ids (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_object_ids is None and "exclude_object_ids" in self.model_fields_set:
            _dict['excludeObjectIds'] = None

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

        # set to None if volume_exclusion_params (nullable) is None
        # and model_fields_set contains the field
        if self.volume_exclusion_params is None and "volume_exclusion_params" in self.model_fields_set:
            _dict['volumeExclusionParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsSnapshotManagerProtectionGroupParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amiCreationFrequency": obj.get("amiCreationFrequency"),
            "createAmi": obj.get("createAmi"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "excludeVmTagIds": obj.get("excludeVmTagIds"),
            "objects": [AwsSnapshotManagerProtectionGroupObjectParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "vmTagIds": obj.get("vmTagIds"),
            "volumeExclusionParams": EbsVolumeExclusionParams.from_dict(obj["volumeExclusionParams"]) if obj.get("volumeExclusionParams") is not None else None
        })
        return _obj


