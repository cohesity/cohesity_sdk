# NodeStatusResult

Specifies the current status of a Node in the cluster.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_operation** | **str** | Specifies the active operation on the Node if there is one. | [optional] 
**cluster_id** | **int** | Specifies the Cluster ID if the Node is part of a Cluster. | [optional] 
**id** | **int** | Specifies the ID of the Node. | [optional] 
**in_cluster** | **bool** | Specifies whether or not the Node is part of a Cluster. | [optional] 
**in_maintenance_mode** | **bool** | InMaintenanceMode is used to mark a node in maintenance mode. | [optional] 
**incarnation_id** | **int** | Specifies the Incarnation ID if the Node is part of a Cluster. | [optional] 
**ip** | **str** | Specifies the IP address of the Node. | [optional] 
**is_app_node** | **bool** | Whether the node is an app node. | [optional] 
**last_upgrade_time_secs** | **int** | Specifies the time of the last upgrade in seconds since the epoch. | [optional] 
**marked_for_removal** | **bool** | Specifies whether or not this node is marked for removal. | [optional] 
**message** | **str** | Specifies an optional message describing the current state of the Node. | [optional] 
**removal_progress_list** | [**List[ComponentRemovalProgress]**](ComponentRemovalProgress.md) | Removal progress for various components which are not acked yet. | [optional] 
**removal_reason** | **str** | Specifies the reason for the removal operation if there is a removal operation going on. | [optional] 
**services** | [**List[ServiceProcessEntry]**](ServiceProcessEntry.md) | Specifies the list of services running on the cluster and their process IDs. | [optional] 
**services_acked_list** | **List[str]** | Services already acked for removal of this entity. | [optional] 
**services_not_acked** | **str** | ServicesNotAcked specifies services that have not ACKed yet in string format after the node is marked for removal. | [optional] 
**services_not_acked_list** | **List[str]** | Services not acked yet for removal of this entity. | [optional] 
**software_version** | **str** | Specifies the version of the software running on the Node. | [optional] 
**uptime** | **str** | Uptime of node. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.node_status_result import NodeStatusResult

# TODO update the JSON string below
json = "{}"
# create an instance of NodeStatusResult from a JSON string
node_status_result_instance = NodeStatusResult.from_json(json)
# print the JSON string representation of the object
print(NodeStatusResult.to_json())

# convert the object into a dict
node_status_result_dict = node_status_result_instance.to_dict()
# create an instance of NodeStatusResult from a dict
node_status_result_from_dict = NodeStatusResult.from_dict(node_status_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


