# ProgressTaskEvent

Specifies the details about the various events which are created during the execution of Progress Task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Specifies the log message describing the current event. | [optional] 
**occured_at_usecs** | **int** | Specifies the time of the event occurance in Unix epoch Timestamp(in microseconds). | [optional] 

## Example

```python
from cohesity_sdk.models.progress_task_event import ProgressTaskEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ProgressTaskEvent from a JSON string
progress_task_event_instance = ProgressTaskEvent.from_json(json)
# print the JSON string representation of the object
print(ProgressTaskEvent.to_json())

# convert the object into a dict
progress_task_event_dict = progress_task_event_instance.to_dict()
# create an instance of ProgressTaskEvent from a dict
progress_task_event_from_dict = ProgressTaskEvent.from_dict(progress_task_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


