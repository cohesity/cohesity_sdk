# CancelObjectRunsParams

Request to cancel object runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **int, none_type** | Specifies object id | 
**runs_config** | [**[CancelObjectRunParams], none_type**](CancelObjectRunParams.md) | Specifies a list of runs to cancel. If no runs are specified, then all the outstanding runs will be canceled. | [optional] 
**snapshot_backend_types** | **[str], none_type** | Specifies the protections type on which action to be performed. This is used when an object is protected by multiple protection types. If not specified action will be performed on all protection types. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


