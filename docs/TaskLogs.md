# TaskLogs

Specifies the id of the task log related to this active directory.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_task_id** | **str** | Specifies the id of adding task. | [optional] 
**edit_task_id** | **List[str]** | Specifies the id of editing task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.task_logs import TaskLogs

# TODO update the JSON string below
json = "{}"
# create an instance of TaskLogs from a JSON string
task_logs_instance = TaskLogs.from_json(json)
# print the JSON string representation of the object
print(TaskLogs.to_json())

# convert the object into a dict
task_logs_dict = task_logs_instance.to_dict()
# create an instance of TaskLogs from a dict
task_logs_from_dict = TaskLogs.from_dict(task_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


