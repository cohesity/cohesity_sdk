# UsageAndPerformanceStats

Provides usage and performance statistics for entities such as a disks, Nodes or Clusters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_in_bytes** | **int** | Specifies the data read from the protected objects by the Cohesity Cluster before any data reduction using deduplication and compression. | [optional] 
**data_in_bytes_after_reduction** | **int** | Morphed Usage before data is replicated to other nodes as per RF or Erasure Coding policy. | [optional] 
**min_usable_physical_capacity_bytes** | **int** | Specifies the minimum usable capacity available after erasure coding or RF. This will only be populated for cluster. If a cluster has multiple Domains (View Boxes) with different RF or erasure coding, this metric will be computed using the scheme that will provide least saving. | [optional] 
**num_bytes_read** | **int** | Provides the total number of bytes read in the last 30 seconds. | [optional] 
**num_bytes_written** | **int** | Provides the total number of bytes written in the last 30 second. | [optional] 
**physical_capacity_bytes** | **int** | Provides the total physical capacity in bytes of all the storage devices, after subtracting space reserved for cluster services | [optional] 
**read_ios** | **int** | Provides the number of Read IOs that occurred in the last 30 seconds. | [optional] 
**read_latency_msecs** | **float** | Provides the Read latency in milliseconds for the Read IOs that occurred during the last 30 seconds. | [optional] 
**system_capacity_bytes** | **int** | Provides the total available capacity as computed by the Linux &#39;statfs&#39; command. | [optional] 
**system_usage_bytes** | **int** | Provides the usage of bytes, as computed by the Linux &#39;statfs&#39; command, after the size of the data is reduced by change-block tracking, compression and deduplication. | [optional] 
**total_physical_raw_usage_bytes** | **int** | Provides the usage of bytes, as computed by the Cohesity Cluster, before the size of the data is reduced by change-block tracking, compression and deduplication. | [optional] 
**total_physical_usage_bytes** | **int** | Provides the data stored locally, after the data has been reduced by deduplication and compression, including the space required for honoring the resiliency settings (EC/RF). | [optional] 
**write_ios** | **int** | Provides the number of Write IOs that occurred in the last 30 seconds. | [optional] 
**write_latency_msecs** | **float** | Provides the Write latency in milliseconds for the Write IOs that occurred during the last 30 seconds. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.usage_and_performance_stats import UsageAndPerformanceStats

# TODO update the JSON string below
json = "{}"
# create an instance of UsageAndPerformanceStats from a JSON string
usage_and_performance_stats_instance = UsageAndPerformanceStats.from_json(json)
# print the JSON string representation of the object
print(UsageAndPerformanceStats.to_json())

# convert the object into a dict
usage_and_performance_stats_dict = usage_and_performance_stats_instance.to_dict()
# create an instance of UsageAndPerformanceStats from a dict
usage_and_performance_stats_from_dict = UsageAndPerformanceStats.from_dict(usage_and_performance_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


