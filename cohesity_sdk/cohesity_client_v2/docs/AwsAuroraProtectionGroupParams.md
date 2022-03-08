# AwsAuroraProtectionGroupParams

Specifies the parameters which are specific to AWS Aurora related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AwsAuroraProtectionGroupObjectParams]**](AwsAuroraProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**aurora_tag_ids** | **[[int]], none_type** | Array of arrays of Aurora Tag Ids that specify aurora clusters to protect. | [optional] 
**exclude_aurora_tag_ids** | **[[int]], none_type** | Array of arrays of RDS Tag Ids that specify aurora clusters to exclude. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


