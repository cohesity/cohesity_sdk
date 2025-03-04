# ArchivalTargetProgressInfo

Specifies the progress of an archival run target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_task_id** | **str** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**ownership_context** | **str** | Specifies the ownership context for the target. | [optional] 
**target_id** | **int** | Specifies the archival target ID. | [optional] 
**target_name** | **str** | Specifies the archival target name. | [optional] 
**target_type** | **str** | Specifies the archival target type. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**usage_type** | **str** | Specifies the usage type for the target. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**List[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**expected_remaining_time_usecs** | **int** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**percentage_completed** | **float** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**status** | **str** | Specifies the current status of the progress task. | [optional] 
**objects** | [**List[ObjectProgressInfo]**](ObjectProgressInfo.md) | Specifies progress for objects. | [optional] 

## Example

```python
from cohesity_sdk.models.archival_target_progress_info import ArchivalTargetProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalTargetProgressInfo from a JSON string
archival_target_progress_info_instance = ArchivalTargetProgressInfo.from_json(json)
# print the JSON string representation of the object
print(ArchivalTargetProgressInfo.to_json())

# convert the object into a dict
archival_target_progress_info_dict = archival_target_progress_info_instance.to_dict()
# create an instance of ArchivalTargetProgressInfo from a dict
archival_target_progress_info_from_dict = ArchivalTargetProgressInfo.from_dict(archival_target_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


