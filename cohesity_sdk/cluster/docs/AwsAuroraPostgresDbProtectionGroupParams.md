# AwsAuroraPostgresDbProtectionGroupParams

Specifies the parameters which are specific to AWS Aurora Postgres DB related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aurora_tag_ids** | **[[int]], none_type** | Array of arrays of Aurora Tag Ids that specify aurora clusters to protect. | [optional] 
**exclude_aurora_tag_ids** | **[[int]], none_type** | Array of arrays of Aurora Tag Ids that specify aurora clusters to exclude. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[AwsPostgresDbProtectionGroupObjectParams]**](AwsPostgresDbProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


