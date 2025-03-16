# LocalCopy

Details of the local copy of this backup run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Cluster ID of the run. | [optional] 
**cluster_incarnation_id** | **int** | Cluster incarnation ID of the run. | [optional] 
**object_id** | **int** | object ID of the run. | [optional] 
**protection_group_id** | **int** | Protection group ID of the run. | [optional] 
**region_id** | **str** | The region id of the run. | [optional] 
**run_instance_id** | **int** | Run instance id of the run. | [optional] 
**run_start_time_usecs** | **int** | The run start time of the task in microseconds. | [optional] 
**snapshot_id** | **str** | Snapshot id of the snapshot corresponding to the local copy of this backup run. | [optional] 
**status** | **str** | Status of the backup run. | [optional] 
**tenant_ids** | **List[str]** |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.local_copy import LocalCopy

# TODO update the JSON string below
json = "{}"
# create an instance of LocalCopy from a JSON string
local_copy_instance = LocalCopy.from_json(json)
# print the JSON string representation of the object
print(LocalCopy.to_json())

# convert the object into a dict
local_copy_dict = local_copy_instance.to_dict()
# create an instance of LocalCopy from a dict
local_copy_from_dict = LocalCopy.from_dict(local_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


