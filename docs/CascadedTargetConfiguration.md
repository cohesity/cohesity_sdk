# CascadedTargetConfiguration

Specifies the source of the cascadded replication and list of all remote targets that needs to added. Each source cluster and remote targets are considered as nodes and immediate connections between them are considered as edges.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_targets** | [**TargetsConfiguration**](TargetsConfiguration.md) |  | 
**source_cluster_id** | **int, none_type** | Specifies the source cluster id from where the remote operations will be performed to the next set of remote targets. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


