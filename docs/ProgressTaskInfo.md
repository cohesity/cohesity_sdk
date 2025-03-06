# ProgressTaskInfo

Specifies the details about a Progress Task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**List[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**expected_remaining_time_usecs** | **int** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**percentage_completed** | **float** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**status** | **str** | Specifies the current status of the progress task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.progress_task_info import ProgressTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressTaskInfo from a JSON string
progress_task_info_instance = ProgressTaskInfo.from_json(json)
# print the JSON string representation of the object
print(ProgressTaskInfo.to_json())

# convert the object into a dict
progress_task_info_dict = progress_task_info_instance.to_dict()
# create an instance of ProgressTaskInfo from a dict
progress_task_info_from_dict = ProgressTaskInfo.from_dict(progress_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


