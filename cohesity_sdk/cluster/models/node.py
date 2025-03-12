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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.capacity_by_tier import CapacityByTier
from cohesity_sdk.cluster.models.chassis_info import ChassisInfo
from cohesity_sdk.cluster.models.component_removal_progress import ComponentRemovalProgress
from cohesity_sdk.cluster.models.count_by_tier import CountByTier
from cohesity_sdk.cluster.models.node_hardware_info import NodeHardwareInfo
from cohesity_sdk.cluster.models.node_stats import NodeStats
from cohesity_sdk.cluster.models.node_system_disk_info import NodeSystemDiskInfo
from cohesity_sdk.cluster.models.pre_check_validation import PreCheckValidation
from typing import Set
from typing_extensions import Self

class Node(BaseModel):
    """
    Node information of a cluster.
    """ # noqa: E501
    capacity_by_tier: Optional[List[CapacityByTier]] = Field(default=None, description="CapacityByTier describes the capacity of each storage tier.", alias="capacityByTier")
    chassis_info: Optional[ChassisInfo] = Field(default=None, alias="chassisInfo")
    cluster_partition_id: Optional[StrictInt] = Field(default=None, description="ClusterPartitionId is the Id of the cluster partition to which the Node belongs.", alias="clusterPartitionId")
    cluster_partition_name: Optional[StrictStr] = Field(default=None, description="ClusterPartitionName is the name of the cluster to which the Node belongs.", alias="clusterPartitionName")
    cohesity_node_serial: Optional[StrictStr] = Field(default=None, description="Cohesity Node Serial Number of the Node.", alias="cohesityNodeSerial")
    disk_count_by_tier: Optional[List[CountByTier]] = Field(default=None, description="DiskCountByTier describes the disk number of each storage tier.", alias="diskCountByTier")
    hardware_model: Optional[StrictStr] = Field(default=None, description="Specifies the hardware model of the node.", alias="hardwareModel")
    host_name: Optional[StrictStr] = Field(default=None, description="Specifies the hostname of the node.", alias="hostName")
    id: Optional[StrictInt] = Field(default=None, description="Id is the Id of the Node.")
    ip: Optional[StrictStr] = Field(default=None, description="Ip is the IP address of the Node.")
    is_app_node: Optional[StrictBool] = Field(default=None, description="Whether node is app node.", alias="isAppNode")
    is_marked_for_removal: Optional[StrictBool] = Field(default=None, description="IsMarkedForRemoval specifies whether the node has been marked for removal.", alias="isMarkedForRemoval")
    max_physical_capacity_bytes: Optional[StrictInt] = Field(default=None, description="MaxPhysicalCapacityBytes specifies the maximum physical capacity of the node in bytes.", alias="maxPhysicalCapacityBytes")
    node_hardware_info: Optional[NodeHardwareInfo] = Field(default=None, alias="nodeHardwareInfo")
    node_incarnation_id: Optional[StrictInt] = Field(default=None, description="NodeIncarnationId is the incarnation id  of this node. The incarnation id is changed every time the data is wiped from the node. Various services on a node is only run if incarnation id of the node matches the incarnation id of the cluster. Whenever a mismatch is detected, Nexus will stop all services and clean the data from the node. After clean operation is completed, Nexus will set the node incarnation id to cluster incarnation id and start the services.", alias="nodeIncarnationId")
    node_software_version: Optional[StrictStr] = Field(default=None, description="NodeSoftwareVersion is the current version of Cohesity software installed on a node.", alias="nodeSoftwareVersion")
    node_type: Optional[StrictStr] = Field(default=None, description="Node type: StorageNode, AllFlashNode, RoboNode, AppNode, etc.", alias="nodeType")
    offline_disk_count: Optional[StrictInt] = Field(default=None, description="OfflineDiskCount is the number of offline disks in a node.", alias="offlineDiskCount")
    offline_mount_paths_of_disks: Optional[List[StrictStr]] = Field(default=None, description="OfflineMountPathsOfDisks provides the corresponding mount paths for direct attached disks that are currently offline - access to these were detected to hang sometime in the past. After these disks have been fixed, their mount paths needs to be removed from the following list before these will be accessed again.", alias="offlineMountPathsOfDisks")
    precheck_timestamp_secs: Optional[StrictInt] = Field(default=None, description="Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds).", alias="precheckTimestampSecs")
    product_model: Optional[StrictStr] = Field(default=None, description="Specifies the product model of the node.", alias="productModel")
    progress_percentage: Optional[StrictInt] = Field(default=None, description="Specifies the overall progress percentage in removing the Node.", alias="progressPercentage")
    removal_progress_list: Optional[List[ComponentRemovalProgress]] = Field(default=None, description="Specifies the removal progress details for services that are not acked yet.", alias="removalProgressList")
    removal_reason: Optional[List[StrictStr]] = Field(default=None, description="RemovalReason specifies the removal reason of the node. 'kAutoHealthCheck' means the entity health is bad. 'kUserGracefulRemoval' means user initiated a graceful removal. 'kUserAvoidAccess' means user initiated a mark offline. 'kUserGracefulNodeRemoval' mean users initiated graceful node removal. 'kUserRemoveDownNode' mean user initiated graceful removal of down node. 'kBridgeDataUnavailable' Bridge requested a graceful removal of a disk when it is not available.", alias="removalReason")
    removal_state: Optional[StrictStr] = Field(default=None, description="RemovalState specifies the removal state of the node. 'kDontRemove' means the state of object is functional and it is not being removed. 'kMarkedForRemoval' means the object is being removed. 'kOkToRemove' means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster.", alias="removalState")
    removal_timestamp_secs: Optional[StrictInt] = Field(default=None, description="Specifies the Unix epoch timestamp (in seconds) when the Node was marked for removal.", alias="removalTimestampSecs")
    services_acked_list: Optional[List[StrictStr]] = Field(default=None, description="Specifies the services already ACKed for removal of this entity.", alias="servicesAckedList")
    services_not_acked: Optional[StrictStr] = Field(default=None, description="Specifies the services that are not ACKed after node is marked for removal.", alias="servicesNotAcked")
    services_not_acked_list: Optional[List[StrictStr]] = Field(default=None, description="Specifies the services not ACKed yet for removal of this entity.", alias="servicesNotAckedList")
    slot_number: Optional[StrictInt] = Field(default=None, description="Slot number occupied by this node within the chassis.", alias="slotNumber")
    stats: Optional[NodeStats] = None
    system_disks: Optional[List[NodeSystemDiskInfo]] = Field(default=None, description="SystemDisk describes the node system disks.", alias="systemDisks")
    time_remaining: Optional[StrictInt] = Field(default=None, description="Specifies the total duration in seconds left to remove the Node.", alias="timeRemaining")
    validation_checks: Optional[List[PreCheckValidation]] = Field(default=None, description="Specifies the pre-check validations results.", alias="validationChecks")
    vendor: Optional[StrictStr] = Field(default=None, description="Specifies the vendor model of the node")
    __properties: ClassVar[List[str]] = ["capacityByTier", "chassisInfo", "clusterPartitionId", "clusterPartitionName", "cohesityNodeSerial", "diskCountByTier", "hardwareModel", "hostName", "id", "ip", "isAppNode", "isMarkedForRemoval", "maxPhysicalCapacityBytes", "nodeHardwareInfo", "nodeIncarnationId", "nodeSoftwareVersion", "nodeType", "offlineDiskCount", "offlineMountPathsOfDisks", "precheckTimestampSecs", "productModel", "progressPercentage", "removalProgressList", "removalReason", "removalState", "removalTimestampSecs", "servicesAckedList", "servicesNotAcked", "servicesNotAckedList", "slotNumber", "stats", "systemDisks", "timeRemaining", "validationChecks", "vendor"]

    @field_validator('removal_reason')
    def removal_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Unknown', 'AutoHealthCheck', 'UserGracefulRemoval', 'UserAvoidAccess', 'UserGracefulNodeRemoval', 'UserRemoveDownNode', 'BridgeDataUnavailable']):
                raise ValueError("each list item must be one of ('Unknown', 'AutoHealthCheck', 'UserGracefulRemoval', 'UserAvoidAccess', 'UserGracefulNodeRemoval', 'UserRemoveDownNode', 'BridgeDataUnavailable')")
        return value

    @field_validator('removal_state')
    def removal_state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DontRemove', 'MarkedForRemoval', 'OkToRemove']):
            raise ValueError("must be one of enum values ('DontRemove', 'MarkedForRemoval', 'OkToRemove')")
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
        """Create an instance of Node from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in capacity_by_tier (list)
        _items = []
        if self.capacity_by_tier:
            for _item_capacity_by_tier in self.capacity_by_tier:
                if _item_capacity_by_tier:
                    _items.append(_item_capacity_by_tier.to_dict())
            _dict['capacityByTier'] = _items
        # override the default output from pydantic by calling `to_dict()` of chassis_info
        if self.chassis_info:
            _dict['chassisInfo'] = self.chassis_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in disk_count_by_tier (list)
        _items = []
        if self.disk_count_by_tier:
            for _item_disk_count_by_tier in self.disk_count_by_tier:
                if _item_disk_count_by_tier:
                    _items.append(_item_disk_count_by_tier.to_dict())
            _dict['diskCountByTier'] = _items
        # override the default output from pydantic by calling `to_dict()` of node_hardware_info
        if self.node_hardware_info:
            _dict['nodeHardwareInfo'] = self.node_hardware_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in removal_progress_list (list)
        _items = []
        if self.removal_progress_list:
            for _item_removal_progress_list in self.removal_progress_list:
                if _item_removal_progress_list:
                    _items.append(_item_removal_progress_list.to_dict())
            _dict['removalProgressList'] = _items
        # override the default output from pydantic by calling `to_dict()` of stats
        if self.stats:
            _dict['stats'] = self.stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in system_disks (list)
        _items = []
        if self.system_disks:
            for _item_system_disks in self.system_disks:
                if _item_system_disks:
                    _items.append(_item_system_disks.to_dict())
            _dict['systemDisks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in validation_checks (list)
        _items = []
        if self.validation_checks:
            for _item_validation_checks in self.validation_checks:
                if _item_validation_checks:
                    _items.append(_item_validation_checks.to_dict())
            _dict['validationChecks'] = _items
        # set to None if capacity_by_tier (nullable) is None
        # and model_fields_set contains the field
        if self.capacity_by_tier is None and "capacity_by_tier" in self.model_fields_set:
            _dict['capacityByTier'] = None

        # set to None if cluster_partition_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_partition_id is None and "cluster_partition_id" in self.model_fields_set:
            _dict['clusterPartitionId'] = None

        # set to None if cluster_partition_name (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_partition_name is None and "cluster_partition_name" in self.model_fields_set:
            _dict['clusterPartitionName'] = None

        # set to None if cohesity_node_serial (nullable) is None
        # and model_fields_set contains the field
        if self.cohesity_node_serial is None and "cohesity_node_serial" in self.model_fields_set:
            _dict['cohesityNodeSerial'] = None

        # set to None if disk_count_by_tier (nullable) is None
        # and model_fields_set contains the field
        if self.disk_count_by_tier is None and "disk_count_by_tier" in self.model_fields_set:
            _dict['diskCountByTier'] = None

        # set to None if hardware_model (nullable) is None
        # and model_fields_set contains the field
        if self.hardware_model is None and "hardware_model" in self.model_fields_set:
            _dict['hardwareModel'] = None

        # set to None if host_name (nullable) is None
        # and model_fields_set contains the field
        if self.host_name is None and "host_name" in self.model_fields_set:
            _dict['hostName'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if is_app_node (nullable) is None
        # and model_fields_set contains the field
        if self.is_app_node is None and "is_app_node" in self.model_fields_set:
            _dict['isAppNode'] = None

        # set to None if is_marked_for_removal (nullable) is None
        # and model_fields_set contains the field
        if self.is_marked_for_removal is None and "is_marked_for_removal" in self.model_fields_set:
            _dict['isMarkedForRemoval'] = None

        # set to None if max_physical_capacity_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.max_physical_capacity_bytes is None and "max_physical_capacity_bytes" in self.model_fields_set:
            _dict['maxPhysicalCapacityBytes'] = None

        # set to None if node_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_incarnation_id is None and "node_incarnation_id" in self.model_fields_set:
            _dict['nodeIncarnationId'] = None

        # set to None if node_software_version (nullable) is None
        # and model_fields_set contains the field
        if self.node_software_version is None and "node_software_version" in self.model_fields_set:
            _dict['nodeSoftwareVersion'] = None

        # set to None if node_type (nullable) is None
        # and model_fields_set contains the field
        if self.node_type is None and "node_type" in self.model_fields_set:
            _dict['nodeType'] = None

        # set to None if offline_disk_count (nullable) is None
        # and model_fields_set contains the field
        if self.offline_disk_count is None and "offline_disk_count" in self.model_fields_set:
            _dict['offlineDiskCount'] = None

        # set to None if offline_mount_paths_of_disks (nullable) is None
        # and model_fields_set contains the field
        if self.offline_mount_paths_of_disks is None and "offline_mount_paths_of_disks" in self.model_fields_set:
            _dict['offlineMountPathsOfDisks'] = None

        # set to None if precheck_timestamp_secs (nullable) is None
        # and model_fields_set contains the field
        if self.precheck_timestamp_secs is None and "precheck_timestamp_secs" in self.model_fields_set:
            _dict['precheckTimestampSecs'] = None

        # set to None if product_model (nullable) is None
        # and model_fields_set contains the field
        if self.product_model is None and "product_model" in self.model_fields_set:
            _dict['productModel'] = None

        # set to None if progress_percentage (nullable) is None
        # and model_fields_set contains the field
        if self.progress_percentage is None and "progress_percentage" in self.model_fields_set:
            _dict['progressPercentage'] = None

        # set to None if removal_progress_list (nullable) is None
        # and model_fields_set contains the field
        if self.removal_progress_list is None and "removal_progress_list" in self.model_fields_set:
            _dict['removalProgressList'] = None

        # set to None if removal_reason (nullable) is None
        # and model_fields_set contains the field
        if self.removal_reason is None and "removal_reason" in self.model_fields_set:
            _dict['removalReason'] = None

        # set to None if removal_state (nullable) is None
        # and model_fields_set contains the field
        if self.removal_state is None and "removal_state" in self.model_fields_set:
            _dict['removalState'] = None

        # set to None if removal_timestamp_secs (nullable) is None
        # and model_fields_set contains the field
        if self.removal_timestamp_secs is None and "removal_timestamp_secs" in self.model_fields_set:
            _dict['removalTimestampSecs'] = None

        # set to None if services_acked_list (nullable) is None
        # and model_fields_set contains the field
        if self.services_acked_list is None and "services_acked_list" in self.model_fields_set:
            _dict['servicesAckedList'] = None

        # set to None if services_not_acked (nullable) is None
        # and model_fields_set contains the field
        if self.services_not_acked is None and "services_not_acked" in self.model_fields_set:
            _dict['servicesNotAcked'] = None

        # set to None if services_not_acked_list (nullable) is None
        # and model_fields_set contains the field
        if self.services_not_acked_list is None and "services_not_acked_list" in self.model_fields_set:
            _dict['servicesNotAckedList'] = None

        # set to None if slot_number (nullable) is None
        # and model_fields_set contains the field
        if self.slot_number is None and "slot_number" in self.model_fields_set:
            _dict['slotNumber'] = None

        # set to None if system_disks (nullable) is None
        # and model_fields_set contains the field
        if self.system_disks is None and "system_disks" in self.model_fields_set:
            _dict['systemDisks'] = None

        # set to None if time_remaining (nullable) is None
        # and model_fields_set contains the field
        if self.time_remaining is None and "time_remaining" in self.model_fields_set:
            _dict['timeRemaining'] = None

        # set to None if validation_checks (nullable) is None
        # and model_fields_set contains the field
        if self.validation_checks is None and "validation_checks" in self.model_fields_set:
            _dict['validationChecks'] = None

        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capacityByTier": [CapacityByTier.from_dict(_item) for _item in obj["capacityByTier"]] if obj.get("capacityByTier") is not None else None,
            "chassisInfo": ChassisInfo.from_dict(obj["chassisInfo"]) if obj.get("chassisInfo") is not None else None,
            "clusterPartitionId": obj.get("clusterPartitionId"),
            "clusterPartitionName": obj.get("clusterPartitionName"),
            "cohesityNodeSerial": obj.get("cohesityNodeSerial"),
            "diskCountByTier": [CountByTier.from_dict(_item) for _item in obj["diskCountByTier"]] if obj.get("diskCountByTier") is not None else None,
            "hardwareModel": obj.get("hardwareModel"),
            "hostName": obj.get("hostName"),
            "id": obj.get("id"),
            "ip": obj.get("ip"),
            "isAppNode": obj.get("isAppNode"),
            "isMarkedForRemoval": obj.get("isMarkedForRemoval"),
            "maxPhysicalCapacityBytes": obj.get("maxPhysicalCapacityBytes"),
            "nodeHardwareInfo": NodeHardwareInfo.from_dict(obj["nodeHardwareInfo"]) if obj.get("nodeHardwareInfo") is not None else None,
            "nodeIncarnationId": obj.get("nodeIncarnationId"),
            "nodeSoftwareVersion": obj.get("nodeSoftwareVersion"),
            "nodeType": obj.get("nodeType"),
            "offlineDiskCount": obj.get("offlineDiskCount"),
            "offlineMountPathsOfDisks": obj.get("offlineMountPathsOfDisks"),
            "precheckTimestampSecs": obj.get("precheckTimestampSecs"),
            "productModel": obj.get("productModel"),
            "progressPercentage": obj.get("progressPercentage"),
            "removalProgressList": [ComponentRemovalProgress.from_dict(_item) for _item in obj["removalProgressList"]] if obj.get("removalProgressList") is not None else None,
            "removalReason": obj.get("removalReason"),
            "removalState": obj.get("removalState"),
            "removalTimestampSecs": obj.get("removalTimestampSecs"),
            "servicesAckedList": obj.get("servicesAckedList"),
            "servicesNotAcked": obj.get("servicesNotAcked"),
            "servicesNotAckedList": obj.get("servicesNotAckedList"),
            "slotNumber": obj.get("slotNumber"),
            "stats": NodeStats.from_dict(obj["stats"]) if obj.get("stats") is not None else None,
            "systemDisks": [NodeSystemDiskInfo.from_dict(_item) for _item in obj["systemDisks"]] if obj.get("systemDisks") is not None else None,
            "timeRemaining": obj.get("timeRemaining"),
            "validationChecks": [PreCheckValidation.from_dict(_item) for _item in obj["validationChecks"]] if obj.get("validationChecks") is not None else None,
            "vendor": obj.get("vendor")
        })
        return _obj


