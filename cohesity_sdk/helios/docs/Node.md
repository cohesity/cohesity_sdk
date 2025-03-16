# Node

Node information of a cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_by_tier** | [**List[CapacityByTier]**](CapacityByTier.md) | CapacityByTier describes the capacity of each storage tier. | [optional] 
**chassis_info** | [**ChassisInfo**](ChassisInfo.md) |  | [optional] 
**cluster_partition_id** | **int** | ClusterPartitionId is the Id of the cluster partition to which the Node belongs. | [optional] 
**cluster_partition_name** | **str** | ClusterPartitionName is the name of the cluster to which the Node belongs. | [optional] 
**cohesity_node_serial** | **str** | Cohesity Node Serial Number of the Node. | [optional] 
**disk_count_by_tier** | [**List[CountByTier]**](CountByTier.md) | DiskCountByTier describes the disk number of each storage tier. | [optional] 
**hardware_model** | **str** | Specifies the hardware model of the node. | [optional] 
**host_name** | **str** | Specifies the hostname of the node. | [optional] 
**id** | **int** | Id is the Id of the Node. | [optional] 
**ip** | **str** | Ip is the IP address of the Node. | [optional] 
**is_app_node** | **bool** | Whether node is app node. | [optional] 
**is_marked_for_removal** | **bool** | IsMarkedForRemoval specifies whether the node has been marked for removal. | [optional] 
**max_physical_capacity_bytes** | **int** | MaxPhysicalCapacityBytes specifies the maximum physical capacity of the node in bytes. | [optional] 
**node_hardware_info** | [**NodeHardwareInfo**](NodeHardwareInfo.md) |  | [optional] 
**node_incarnation_id** | **int** | NodeIncarnationId is the incarnation id  of this node. The incarnation id is changed every time the data is wiped from the node. Various services on a node is only run if incarnation id of the node matches the incarnation id of the cluster. Whenever a mismatch is detected, Nexus will stop all services and clean the data from the node. After clean operation is completed, Nexus will set the node incarnation id to cluster incarnation id and start the services. | [optional] 
**node_software_version** | **str** | NodeSoftwareVersion is the current version of Cohesity software installed on a node. | [optional] 
**node_type** | **str** | Node type: StorageNode, AllFlashNode, RoboNode, AppNode, etc. | [optional] 
**offline_disk_count** | **int** | OfflineDiskCount is the number of offline disks in a node. | [optional] 
**offline_mount_paths_of_disks** | **List[str]** | OfflineMountPathsOfDisks provides the corresponding mount paths for direct attached disks that are currently offline - access to these were detected to hang sometime in the past. After these disks have been fixed, their mount paths needs to be removed from the following list before these will be accessed again. | [optional] 
**precheck_timestamp_secs** | **int** | Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds). | [optional] 
**product_model** | **str** | Specifies the product model of the node. | [optional] 
**progress_percentage** | **int** | Specifies the overall progress percentage in removing the Node. | [optional] 
**removal_progress_list** | [**List[ComponentRemovalProgress]**](ComponentRemovalProgress.md) | Specifies the removal progress details for services that are not acked yet. | [optional] 
**removal_reason** | **List[str]** | RemovalReason specifies the removal reason of the node. &#39;kAutoHealthCheck&#39; means the entity health is bad. &#39;kUserGracefulRemoval&#39; means user initiated a graceful removal. &#39;kUserAvoidAccess&#39; means user initiated a mark offline. &#39;kUserGracefulNodeRemoval&#39; mean users initiated graceful node removal. &#39;kUserRemoveDownNode&#39; mean user initiated graceful removal of down node. &#39;kBridgeDataUnavailable&#39; Bridge requested a graceful removal of a disk when it is not available. | [optional] 
**removal_state** | **str** | RemovalState specifies the removal state of the node. &#39;kDontRemove&#39; means the state of object is functional and it is not being removed. &#39;kMarkedForRemoval&#39; means the object is being removed. &#39;kOkToRemove&#39; means the object has been removed on the Cohesity Cluster and if the object is physical, it can be removed from the Cohesity Cluster. | [optional] 
**removal_timestamp_secs** | **int** | Specifies the Unix epoch timestamp (in seconds) when the Node was marked for removal. | [optional] 
**services_acked_list** | **List[str]** | Specifies the services already ACKed for removal of this entity. | [optional] 
**services_not_acked** | **str** | Specifies the services that are not ACKed after node is marked for removal. | [optional] 
**services_not_acked_list** | **List[str]** | Specifies the services not ACKed yet for removal of this entity. | [optional] 
**slot_number** | **int** | Slot number occupied by this node within the chassis. | [optional] 
**stats** | [**NodeStats**](NodeStats.md) |  | [optional] 
**system_disks** | [**List[NodeSystemDiskInfo]**](NodeSystemDiskInfo.md) | SystemDisk describes the node system disks. | [optional] 
**time_remaining** | **int** | Specifies the total duration in seconds left to remove the Node. | [optional] 
**validation_checks** | [**List[PreCheckValidation]**](PreCheckValidation.md) | Specifies the pre-check validations results. | [optional] 
**vendor** | **str** | Specifies the vendor model of the node | [optional] 

## Example

```python
from cohesity_sdk.helios.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


