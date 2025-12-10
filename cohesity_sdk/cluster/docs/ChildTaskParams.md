# ChildTaskParams

Details about a child task used as part of a restore.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **int** | The task id of the child task. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.child_task_params import ChildTaskParams

# TODO update the JSON string below
json = "{}"
# create an instance of ChildTaskParams from a JSON string
child_task_params_instance = ChildTaskParams.from_json(json)
# print the JSON string representation of the object
print(ChildTaskParams.to_json())

# convert the object into a dict
child_task_params_dict = child_task_params_instance.to_dict()
# create an instance of ChildTaskParams from a dict
child_task_params_from_dict = ChildTaskParams.from_dict(child_task_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


