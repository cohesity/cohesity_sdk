# CloudRetrieveTask

Specifies cloud retrieve task info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the task end time in microseconds. | [optional] 
**message** | **str** | Message about the cloud retrieve task. | [optional] 
**percentage_finished** | **int** | Specifies the percentage of the task. | [optional] 
**pulse_task_id** | **int** | Specifies the pulse task id. | [optional] 
**start_time_usecs** | **int** | Specifies the task start time in microseconds. | [optional] 
**status** | **str** | Specifies the status of the retrieve task. | [optional] 
**time_remaining_seconds** | **int** | Specifies the time remaining to complete the retrieve task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cloud_retrieve_task import CloudRetrieveTask

# TODO update the JSON string below
json = "{}"
# create an instance of CloudRetrieveTask from a JSON string
cloud_retrieve_task_instance = CloudRetrieveTask.from_json(json)
# print the JSON string representation of the object
print(CloudRetrieveTask.to_json())

# convert the object into a dict
cloud_retrieve_task_dict = cloud_retrieve_task_instance.to_dict()
# create an instance of CloudRetrieveTask from a dict
cloud_retrieve_task_from_dict = CloudRetrieveTask.from_dict(cloud_retrieve_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


