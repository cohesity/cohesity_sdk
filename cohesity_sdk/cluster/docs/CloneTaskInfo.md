# CloneTaskInfo

Parameters for a clone op.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Clone task. | [optional] 
**task_id** | **str** | Id of the Clone task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.clone_task_info import CloneTaskInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CloneTaskInfo from a JSON string
clone_task_info_instance = CloneTaskInfo.from_json(json)
# print the JSON string representation of the object
print(CloneTaskInfo.to_json())

# convert the object into a dict
clone_task_info_dict = clone_task_info_instance.to_dict()
# create an instance of CloneTaskInfo from a dict
clone_task_info_from_dict = CloneTaskInfo.from_dict(clone_task_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


