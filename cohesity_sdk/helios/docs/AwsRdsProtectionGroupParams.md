# AwsRdsProtectionGroupParams

Specifies the parameters which are specific to AWS RDS related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[AwsRdsProtectionGroupObjectParams]**](AwsRdsProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**rds_tag_ids** | **[[int]], none_type** | Array of arrays of RDS Tag Ids that Specify db instaces to Protect. | [optional] 
**exclude_rds_tag_ids** | **[[int]], none_type** | Array of arrays of RDS Tag Ids that Specify db instaces to Exclude. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str, none_type** | Specifies the name of the parent of the objects. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


