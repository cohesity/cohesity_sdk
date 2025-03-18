# ProtectedObjectUnProtectActionParams

Specifies the request parameters for Unprotect action on Protected objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[UnprotectActionObjectLevelParams]**](UnprotectActionObjectLevelParams.md) | Specifies the list of objects to perform an action. If provided object id is not explicitly protected by object protection, then given action will not be performed on that. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protected_object_un_protect_action_params import ProtectedObjectUnProtectActionParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectedObjectUnProtectActionParams from a JSON string
protected_object_un_protect_action_params_instance = ProtectedObjectUnProtectActionParams.from_json(json)
# print the JSON string representation of the object
print(ProtectedObjectUnProtectActionParams.to_json())

# convert the object into a dict
protected_object_un_protect_action_params_dict = protected_object_un_protect_action_params_instance.to_dict()
# create an instance of ProtectedObjectUnProtectActionParams from a dict
protected_object_un_protect_action_params_from_dict = ProtectedObjectUnProtectActionParams.from_dict(protected_object_un_protect_action_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


