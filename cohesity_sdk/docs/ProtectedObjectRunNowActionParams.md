# ProtectedObjectRunNowActionParams

Specifies the request parameters for RunNow action on Protected objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**run_label** | **str, none_type** | Specifies a label with which this run is created. Only applicable for user triggered protect now action. | [optional] 
**objects** | [**[RunNowActionObjectLevelParams]**](RunNowActionObjectLevelParams.md) | Specifies the list of objects to perform an action. If provided object id is not explicitly protected by object protection, then given action will not be performed on that. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


