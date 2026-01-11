# ProtectedObjectRunNowActionParams

Specifies the request parameters for RunNow action on Protected objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[RunNowActionObjectLevelParams]**](RunNowActionObjectLevelParams.md) | Specifies the list of objects to perform an action. If provided object id is not explicitly protected by object protection, then given action will not be performed on that. | [optional] 
**run_label** | **str, none_type** | Specifies a label with which this run is created. Only applicable for user triggered protect now action. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


