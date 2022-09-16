# ProtectdObjectsActionRequest

Specifies the request for performing various actions on protected objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Specifies the action type to be performed on object getting protected. Based on selected action, provide the action params. | 
**pause_params** | [**ProtectedObjectPauseActionParams**](ProtectedObjectPauseActionParams.md) |  | [optional] 
**resume_params** | [**ProtectedObjectResumeActionParams**](ProtectedObjectResumeActionParams.md) |  | [optional] 
**run_now_params** | [**ProtectedObjectRunNowActionParams**](ProtectedObjectRunNowActionParams.md) |  | [optional] 
**un_protect_params** | [**ProtectedObjectUnProtectActionParams**](ProtectedObjectUnProtectActionParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


