# CancelProtectionGroupRunRequest

Specifies the request to cancel a protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_task_id** | **List[str]** | Specifies the task id of the archival run. | [optional] 
**cloud_spin_task_id** | **List[str]** | Specifies the task id of the cloudSpin run. | [optional] 
**local_task_id** | **str** | Specifies the task id of the local run. | [optional] 
**object_ids** | **List[int]** | List of entity ids for which we need to cancel the backup tasks. If this is provided it will not cancel the complete run but will cancel only subset of backup tasks (if backup tasks are cancelled correspoding copy task will also get cancelled). If the backup tasks are completed successfully it will not cancel those backup tasks. | [optional] 
**replication_task_id** | **List[str]** | Specifies the task id of the replication run. | [optional] 
**run_id** | **str** | Specifies a unique run id of the Protection Group run. | 

## Example

```python
from cohesity_sdk.models.cancel_protection_group_run_request import CancelProtectionGroupRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CancelProtectionGroupRunRequest from a JSON string
cancel_protection_group_run_request_instance = CancelProtectionGroupRunRequest.from_json(json)
# print the JSON string representation of the object
print(CancelProtectionGroupRunRequest.to_json())

# convert the object into a dict
cancel_protection_group_run_request_dict = cancel_protection_group_run_request_instance.to_dict()
# create an instance of CancelProtectionGroupRunRequest from a dict
cancel_protection_group_run_request_from_dict = CancelProtectionGroupRunRequest.from_dict(cancel_protection_group_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


