# ObjectProgressInfo

Specifies the progress of an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **int** | Specifies object id. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**source_id** | **int** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str** | Specifies registered source name to which object belongs. | [optional] 
**end_time_usecs** | **int** | Specifies the end time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**events** | [**List[ProgressTaskEvent]**](ProgressTaskEvent.md) | Specifies the event log created for progress Task. | [optional] 
**expected_remaining_time_usecs** | **int** | Specifies the expected remaining time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**percentage_completed** | **float** | Specifies the current completed percentage of the progress task. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of the progress task in Unix epoch Timestamp(in microseconds). | [optional] 
**stats** | [**ProgressStats**](ProgressStats.md) |  | [optional] 
**status** | **str** | Specifies the current status of the progress task. | [optional] 
**failed_attempts** | [**List[ProgressTaskInfo]**](ProgressTaskInfo.md) | Specifies progress for failed attempts of this object. | [optional] 

## Example

```python
from cohesity_sdk.models.object_progress_info import ObjectProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectProgressInfo from a JSON string
object_progress_info_instance = ObjectProgressInfo.from_json(json)
# print the JSON string representation of the object
print(ObjectProgressInfo.to_json())

# convert the object into a dict
object_progress_info_dict = object_progress_info_instance.to_dict()
# create an instance of ObjectProgressInfo from a dict
object_progress_info_from_dict = ObjectProgressInfo.from_dict(object_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


