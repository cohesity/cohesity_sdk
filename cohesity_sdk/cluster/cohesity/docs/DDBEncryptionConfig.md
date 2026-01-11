# DDBEncryptionConfig

Specifies the encryption configuration for dynamo DB tables. Restored tables will be encryptred based on this configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_encrypt** | **bool, none_type** | Specifies whether to use encrypt recovered volumes or not. When set to true, supports either AWS/self managed encryption. | 
**custom_kms_key_arn** | **str, none_type** | Specifies custom KMS key arn to be set when encryption type is CustomKMS. It will be of form arn:aws:kms:&lt;region&gt;:&lt;account_id&gt;:key/&lt;key_id&gt; | [optional] 
**kms_key** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


