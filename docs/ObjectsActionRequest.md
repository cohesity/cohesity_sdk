# ObjectsActionRequest

Specifies the type of the action need to be performed on given set of objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type that need to be performed. | [optional] 
**link_params** | [**CommonObjectsActionParams**](CommonObjectsActionParams.md) |  | [optional] 
**link_type** | **str** | Specifies the link type for the link/unlink action. | [optional] 
**un_link_params** | [**CommonObjectsActionParams**](CommonObjectsActionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.objects_action_request import ObjectsActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectsActionRequest from a JSON string
objects_action_request_instance = ObjectsActionRequest.from_json(json)
# print the JSON string representation of the object
print(ObjectsActionRequest.to_json())

# convert the object into a dict
objects_action_request_dict = objects_action_request_instance.to_dict()
# create an instance of ObjectsActionRequest from a dict
objects_action_request_from_dict = ObjectsActionRequest.from_dict(objects_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


