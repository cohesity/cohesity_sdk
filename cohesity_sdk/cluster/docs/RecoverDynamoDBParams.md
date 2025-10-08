# RecoverDynamoDBParams

Specifies the parameters to recover AWS Dynamo DB Tables.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | defaults to "kAWS"
**aws_target_params** | [**AwsTargetParamsForDynamoDB**](AwsTargetParamsForDynamoDB.md) |  | [optional] 
**custom_tags** | [**[SimpleTags], none_type**](SimpleTags.md) | Specifies the custom tags that need to be present on on every entity that this job creates. Only supported for new location recovery. | [optional] 
**prefix** | **str, none_type** | Specifies the prefix to be prepended to the object name after the recovery. | [optional] 
**suffix** | **str, none_type** | Specifies the suffix to be appended to the object name after the recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


