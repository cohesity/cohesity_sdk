# ServiceUnitProgress

Specifies the progress of one patch operation for one service at one patch level.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str, none_type** | Specifies the service which is patched. | [optional] 
**in_progress** | **bool, none_type** | Specifies whether a operation is in progress for the service. | [optional] 
**percentage** | **int, none_type** | Specifies the percentage of completion of the patch unit operation. | [optional] 
**time_remaining_seconds** | **int, none_type** | Specifies the time remaining to complete the patch operation for the service. | [optional] 
**time_taken_seconds** | **int, none_type** | Specifies the time taken so far in this patch unit operation for the service. | [optional] 
**nodes_progress** | [**[NodeUnitProgress], none_type**](NodeUnitProgress.md) | Specifies the details of patch operation for each service at each patch level. | [optional] 
**service_message** | **str, none_type** | Specifies a message about the patch unit operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


