# ClusterStorageStats

Specifies the Cluster storage stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_protection_logical_usage_bytes** | **int** | Specifies the logical size of protected objects in bytes. | [optional] 
**data_protection_physical_usage_bytes** | **int** | Specifies the physical size of protected objects in bytes. | [optional] 
**file_services_logical_usage_bytes** | **int** | Specifies the logical size consumed by file services in bytes. | [optional] 
**file_services_physical_usage_bytes** | **int** | Specifies the physical size consumed by file services in bytes. | [optional] 
**local_available_bytes** | **int** | Specifies the local storage currently available on the cluster in bytes. | [optional] 
**local_usage_bytes** | **int** | Specifies the local storage currently in use on the cluster in bytes. | [optional] 
**total_capacity_bytes** | **int** | Specifies the total capacity of the cluster in bytes. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_storage_stats import ClusterStorageStats

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStorageStats from a JSON string
cluster_storage_stats_instance = ClusterStorageStats.from_json(json)
# print the JSON string representation of the object
print(ClusterStorageStats.to_json())

# convert the object into a dict
cluster_storage_stats_dict = cluster_storage_stats_instance.to_dict()
# create an instance of ClusterStorageStats from a dict
cluster_storage_stats_from_dict = ClusterStorageStats.from_dict(cluster_storage_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


