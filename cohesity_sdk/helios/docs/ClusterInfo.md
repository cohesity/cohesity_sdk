# ClusterInfo

Specifies the clusters hardware type, memory used and total memory capacity, health, connected or not, current version, available versions and the upgrade status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_versions** | [**List[AvailableReleaseVersion]**](AvailableReleaseVersion.md) | Specifies the release versions the cluster can upgrade to. | [optional] 
**cluster_id** | **int** | Specifies cluster id. | [optional] 
**cluster_incarnation_id** | **int** | Specifies cluster incarnation id. | [optional] 
**cluster_name** | **str** | Specifies cluster&#39;s name. | [optional] 
**current_version** | **str** | Specifies if the cluster is connected to helios. | [optional] 
**health** | **str** | Specifies the health of the cluster. | [optional] 
**is_connected_to_helios** | **bool** | Specifies if the cluster is connected to helios. | [optional] 
**location** | **str** | Specifies the location of the cluster. | [optional] 
**node_ips** | **List[str]** | Specifies an array of node ips for the cluster. | [optional] 
**number_of_nodes** | **int** | Specifies the number of nodes in the cluster. | [optional] 
**provider_type** | **str** | Specifies the type of the cluster provider. | [optional] 
**scheduled_timestamp** | **int** | Time at which an upgrade is scheduled. | [optional] 
**status** | **str** | Specifies the upgrade status of the cluster. | [optional] 
**target_version** | **str** | Specifies target version to which clusters are to be upgraded. | [optional] 
**total_capacity** | **int** | Specifies how total memory capacity of the cluster. | [optional] 
**type** | **str** | Specifies the type of the cluster. | [optional] 
**used_capacity** | **int** | Specifies how much of the cluster capacity is consumed. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cluster_info import ClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInfo from a JSON string
cluster_info_instance = ClusterInfo.from_json(json)
# print the JSON string representation of the object
print(ClusterInfo.to_json())

# convert the object into a dict
cluster_info_dict = cluster_info_instance.to_dict()
# create an instance of ClusterInfo from a dict
cluster_info_from_dict = ClusterInfo.from_dict(cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


