# ExperimentalAdapterProtectionGroupParams

Specifies parameters related to the Experimental Adapter Protection job.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional]  if omitted the server will use the default value of 1
**excluded_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[ExperimentalAdapaterProtectionGroupObjectParams]**](ExperimentalAdapaterProtectionGroupObjectParams.md) | Specifies a list of fully qualified names of the objects to be protected. | [optional] 
**workflow_params** | **str, none_type** | Specifies the discover source workflow parameters. This is a stringified JSON representation of the parameters. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


