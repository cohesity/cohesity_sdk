# AwsTargetParamsForDynamoDB

Specifies the configuration for recovering Dynamo DB objects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_to_new_source** | **bool, none_type** | Specifies the parameter whether the recovery should be performed to a new target. If true, source and region information needs to be provided. | 
**encryption_config** | [**DDBEncryptionConfig**](DDBEncryptionConfig.md) |  | [optional] 
**new_source_config** | [**RecoverAwsDDBNewSourceConfig**](RecoverAwsDDBNewSourceConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


