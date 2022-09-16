# VmwareThrottlingParams

Specifies throttling params.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_task_latency_threshold_msecs** | **int, none_type** | If the latency of a datastore is above this value, then a new backup task that uses the datastore won&#39;t be started. | [optional] 
**active_task_latency_threshold_msecs** | **int, none_type** | If the latency of a datastore is above this value, then an existing backup task that uses the datastore will start getting throttled. | [optional] 
**max_concurrent_streams** | **int, none_type** | If this value is &gt; 0 and the number of streams concurrently active on a datastore is equal to it, then any further requests to access the datastore would be denied until the number of active streams reduces. This applies for all the datastores in the specified host. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


