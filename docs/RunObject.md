# RunObject

Specifies the object details to create a protection run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_ids** | **List[int]** | Specifies a list of ids of applications. | [optional] 
**id** | **int** | Specifies the id of object. | 
**physical_params** | [**RunObjectPhysicalParams**](RunObjectPhysicalParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.run_object import RunObject

# TODO update the JSON string below
json = "{}"
# create an instance of RunObject from a JSON string
run_object_instance = RunObject.from_json(json)
# print the JSON string representation of the object
print(RunObject.to_json())

# convert the object into a dict
run_object_dict = run_object_instance.to_dict()
# create an instance of RunObject from a dict
run_object_from_dict = RunObject.from_dict(run_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


