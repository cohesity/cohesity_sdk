# ProtectdObjectsActionRequest

Specifies the request for performing various actions on protected objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params. | 
**object_action_key** | **str** | Specifies the object action key for any action on the given object. | [optional] 
**pause_params** | [**ProtectedObjectPauseActionParams**](ProtectedObjectPauseActionParams.md) |  | [optional] 
**resume_params** | [**ProtectedObjectResumeActionParams**](ProtectedObjectResumeActionParams.md) |  | [optional] 
**run_now_params** | [**ProtectedObjectRunNowActionParams**](ProtectedObjectRunNowActionParams.md) |  | [optional] 
**snapshot_backend_types** | **List[str]** | Specifies the protections type on which action to be performed. This is used when an object is protected by multiple protection types. If not specified action will be performed on all protection types. | [optional] 
**un_protect_params** | [**ProtectedObjectUnProtectActionParams**](ProtectedObjectUnProtectActionParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.protectd_objects_action_request import ProtectdObjectsActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectdObjectsActionRequest from a JSON string
protectd_objects_action_request_instance = ProtectdObjectsActionRequest.from_json(json)
# print the JSON string representation of the object
print(ProtectdObjectsActionRequest.to_json())

# convert the object into a dict
protectd_objects_action_request_dict = protectd_objects_action_request_instance.to_dict()
# create an instance of ProtectdObjectsActionRequest from a dict
protectd_objects_action_request_from_dict = ProtectdObjectsActionRequest.from_dict(protectd_objects_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


