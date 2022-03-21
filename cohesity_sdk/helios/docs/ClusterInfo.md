# ClusterInfo

Specifies the clusters hardware type, memory used and total memory capacity, health, connected or not, current version, available versions and the upgrade status.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_name** | **str, none_type** | Specifies cluster&#39;s name. | [optional] 
**cluster_id** | **str, none_type** | Specifies cluster&#39;s id. | [optional] 
**cluster_incarnation_id** | **str, none_type** | Specifies cluster&#39;s incarnation id. | [optional] 
**is_connected_to_helios** | **bool, none_type** | Specifies if the cluster is connected to helios. | [optional] 
**current_version** | **str, none_type** | Specifies if the cluster is connected to helios. | [optional] 
**available_versions** | [**[AvailableReleaseVersion], none_type**](AvailableReleaseVersion.md) | Specifies the release versions the cluster can upgrade to. | [optional] 
**used_capacity** | **int, none_type** | Specifies how much of the cluster capacity is consumed. | [optional] 
**total_capacity** | **int, none_type** | Specifies how total memory capacity of the cluster. | [optional] 
**health** | **str, none_type** | Specifies the health of the cluster. | [optional] 
**status** | **str, none_type** | Specifies the upgrade status of the cluster. | [optional] 
**location** | **str, none_type** | Specifies the location of the cluster. | [optional] 
**number_of_nodes** | **int, none_type** | Specifies the number of nodes in the cluster. | [optional] 
**type** | **str, none_type** | Specifies the type of the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


