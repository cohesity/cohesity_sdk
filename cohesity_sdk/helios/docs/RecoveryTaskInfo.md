# RecoveryTaskInfo

Specifies the info about a recovery task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**progress_task_id** | **str** | Specifies the progress monitor path. | [optional] [readonly] 
**start_time_usecs** | **int** | Specifies the start time in Unix timestamp epoch in microseconds. | [optional] [readonly] 
**status** | **str** | Specifies the status of the recovery. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.recovery_task_info import RecoveryTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryTaskInfo from a JSON string
recovery_task_info_instance = RecoveryTaskInfo.from_json(json)
# print the JSON string representation of the object
print(RecoveryTaskInfo.to_json())

# convert the object into a dict
recovery_task_info_dict = recovery_task_info_instance.to_dict()
# create an instance of RecoveryTaskInfo from a dict
recovery_task_info_from_dict = RecoveryTaskInfo.from_dict(recovery_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


