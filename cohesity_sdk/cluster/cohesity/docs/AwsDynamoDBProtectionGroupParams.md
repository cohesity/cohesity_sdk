# AwsDynamoDBProtectionGroupParams

Specifies the parameters which are specific to AWS Dynamo DB related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **[int], none_type** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**objects** | [**[AwsDynamoDBProtectionGroupObjectParams]**](AwsDynamoDBProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


