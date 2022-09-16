# PatchOperationStatus

Specifies the status of the current or the last patch operation.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **bool, none_type** | Specifies whether a operation is in progress now. | [optional] 
**operation** | **str, none_type** | Specifies the patch operation. It is either apply or revert patch operation. | [optional] 
**percentage** | **int, none_type** | Specifies the percentage of completion of the current patch operation in progress or the last patch operation completed. | [optional] 
**time_remaining_seconds** | **int, none_type** | Specifies the time remaining to complete the patch operation. | [optional] 
**time_taken_seconds** | **int, none_type** | Specifies the time taken so far to complete the patch operation. | [optional] 
**services_progress** | [**[ServiceUnitProgress], none_type**](ServiceUnitProgress.md) | Specifies the details of patch operation services at each patch level. | [optional] 
**operation_message** | **str, none_type** | Specifies a message about the patch operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


