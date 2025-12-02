# ProtectedObjectActionResponse

Specifies the response upon performing an action on protected objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params. | [optional] 
**objects** | [**List[ActionObjectLevelResponse]**](ActionObjectLevelResponse.md) | Specifies the list of objects on which the provided action was performed. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protected_object_action_response import ProtectedObjectActionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectActionResponse from a JSON string
protected_object_action_response_instance = ProtectedObjectActionResponse.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectActionResponse.to_json())

# convert the object into a dict
protected_object_action_response_dict = protected_object_action_response_instance.to_dict()
# create an instance of ProtectedObjectActionResponse from a dict
protected_object_action_response_from_dict = ProtectedObjectActionResponse.from_dict(protected_object_action_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


