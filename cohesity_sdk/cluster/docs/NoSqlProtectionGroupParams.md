# NoSqlProtectionGroupParams

Specifies the source specific parameters for this Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_scale_concurrency** | **bool, none_type** | Specifies the flag to automatically scale number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**bandwidth_mbps** | **int, none_type** | Specifies the maximum network bandwidth that each concurrent IO Stream can use for exchanging data with the cluster. | [optional] 
**concurrency** | **int, none_type** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. | [optional] 
**custom_source_name** | **str, none_type** | The user specified name for the Source on which this protection was run. | [optional] [readonly] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[NoSqlProtectionGroupObjectParams]**](NoSqlProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Object ID of the Source on which this protection was run . | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the Source on which this protection was run. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


