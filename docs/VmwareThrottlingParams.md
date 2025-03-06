# VmwareThrottlingParams

Specifies throttling params.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_task_latency_threshold_msecs** | **int** | If the latency of a datastore is above this value, then an existing backup task that uses the datastore will start getting throttled. | [optional] 
**max_concurrent_backups** | **int** | Specifies the number of VMs of a vCenter that can be backed up concurrently. | [optional] 
**max_concurrent_streams** | **int** | If this value is &gt; 0 and the number of streams concurrently active on a datastore is equal to it, then any further requests to access the datastore would be denied until the number of active streams reduces. This applies for all the datastores in the specified host. | [optional] 
**new_task_latency_threshold_msecs** | **int** | If the latency of a datastore is above this value, then a new backup task that uses the datastore won&#39;t be started. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vmware_throttling_params import VmwareThrottlingParams

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareThrottlingParams from a JSON string
vmware_throttling_params_instance = VmwareThrottlingParams.from_json(json)
# print the JSON string representation of the object
print(VmwareThrottlingParams.to_json())

# convert the object into a dict
vmware_throttling_params_dict = vmware_throttling_params_instance.to_dict()
# create an instance of VmwareThrottlingParams from a dict
vmware_throttling_params_from_dict = VmwareThrottlingParams.from_dict(vmware_throttling_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


