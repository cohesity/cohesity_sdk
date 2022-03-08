# ProtectdObjectsActionRequest

Specifies the request for performing various actions on protected objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params. | 
**object_action_key** | **str, none_type** | Specifies the object action key for any action on the given object. | [optional] 
**pause_params** | [**ProtectedObjectPauseActionParams**](ProtectedObjectPauseActionParams.md) |  | [optional] 
**resume_params** | [**ProtectedObjectResumeActionParams**](ProtectedObjectResumeActionParams.md) |  | [optional] 
**run_now_params** | [**ProtectedObjectRunNowActionParams**](ProtectedObjectRunNowActionParams.md) |  | [optional] 
**un_protect_params** | [**ProtectedObjectUnProtectActionParams**](ProtectedObjectUnProtectActionParams.md) |  | [optional] 
**snapshot_backend_types** | **[str], none_type** | Specifies the protections type on which action to be performed. This is used when an object is protected by multiple protection types. If not specified action will be performed on all protection types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


