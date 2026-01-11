# AwsSourceRegistrationParams

Specifies the paramaters to register an AWS source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_type** | **str, none_type** | Specifies the AWS Subscription type (Commercial/Gov). | 
**dynamo_db_params** | [**DynamoDBSpecificParams**](DynamoDBSpecificParams.md) |  | [optional] 
**s3_params** | [**S3SpecificParams**](S3SpecificParams.md) |  | [optional] 
**standard_params** | [**StandardParams**](StandardParams.md) |  | [optional] 
**use_cases** | **[str], none_type** | The use cases for which the source is to be registered. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


