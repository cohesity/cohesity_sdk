# ClusterStats

Specifies statistics about the Cohesity cluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_usage_perf_stats** | [**UsageAndPerformanceStats**](UsageAndPerformanceStats.md) |  | [optional] 
**data_reduction_ratio** | **float** | Provides the ratio of Cluster Logical Data (totalLogicalUsageBytes) Managed to Cluster Storage Used (totalPhysicalUsageBytes) | [optional] 
**data_usage_stats** | [**DataUsageStatsDefinition**](DataUsageStatsDefinition.md) |  | [optional] 
**id** | **int** | Specifies the id of the Cohesity Cluster. | [optional] 
**local_usage_perf_stats** | [**UsageAndPerformanceStats**](UsageAndPerformanceStats.md) |  | [optional] 
**logical_stats** | [**LogicalStats**](LogicalStats.md) |  | [optional] 
**usage_perf_stats** | [**UsageAndPerformanceStats**](UsageAndPerformanceStats.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cluster_stats import ClusterStats

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStats from a JSON string
cluster_stats_instance = ClusterStats.from_json(json)
# print the JSON string representation of the object
print(ClusterStats.to_json())

# convert the object into a dict
cluster_stats_dict = cluster_stats_instance.to_dict()
# create an instance of ClusterStats from a dict
cluster_stats_from_dict = ClusterStats.from_dict(cluster_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


