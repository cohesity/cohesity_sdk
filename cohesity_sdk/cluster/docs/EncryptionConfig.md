# EncryptionConfig

Specifies the encryption configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_encrypt** | **bool, none_type** | Specifies whether to encrypt recovered volumes or not. Default value is true. | 
**custom_kms_key_arn** | **str, none_type** | Specifies custom KMS key arn. It will be of form arn:aws:kms:&lt;region&gt;:&lt;account_id&gt;:key/&lt;key_id&gt; | [optional] 
**kms_key** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


