# NodeStatusResult

Specifies the current status of a Node in the cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_operation** | **str, none_type** | Specifies the active operation on the Node if there is one. | [optional] 
**cluster_id** | **int** | Specifies the Cluster ID if the Node is part of a Cluster. | [optional] 
**id** | **int, none_type** | Specifies the ID of the Node. | [optional] 
**in_cluster** | **bool, none_type** | Specifies whether or not the Node is part of a Cluster. | [optional] 
**in_maintenance_mode** | **bool, none_type** | InMaintenanceMode is used to mark a node in maintenance mode. | [optional] 
**incarnation_id** | **int** | Specifies the Incarnation ID if the Node is part of a Cluster. | [optional] 
**ip** | **str, none_type** | Specifies the IP address of the Node. | [optional] 
**is_app_node** | **bool, none_type** | Whether the node is an app node. | [optional] 
**last_upgrade_time_secs** | **int** | Specifies the time of the last upgrade in seconds since the epoch. | [optional] 
**marked_for_removal** | **bool, none_type** | Specifies whether or not this node is marked for removal. | [optional] 
**message** | **str, none_type** | Specifies an optional message describing the current state of the Node. | [optional] 
**removal_progress_list** | [**[ComponentRemovalProgress], none_type**](ComponentRemovalProgress.md) | Removal progress for various components which are not acked yet. | [optional] 
**removal_reason** | **str, none_type** | Specifies the reason for the removal operation if there is a removal operation going on. | [optional] 
**services** | [**[ServiceProcessEntry]**](ServiceProcessEntry.md) | Specifies the list of services running on the cluster and their process IDs. | [optional] 
**services_acked_list** | **[str], none_type** | Services already acked for removal of this entity. | [optional] 
**services_not_acked** | **str, none_type** | ServicesNotAcked specifies services that have not ACKed yet in string format after the node is marked for removal. | [optional] 
**services_not_acked_list** | **[str], none_type** | Services not acked yet for removal of this entity. | [optional] 
**software_version** | **str** | Specifies the version of the software running on the Node. | [optional] 
**uptime** | **str, none_type** | Uptime of node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


