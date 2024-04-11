# EncryptionConfig

Specifies the encryption configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_encrypt** | **bool, none_type** | Specifies whether to encrypt recovered volumes or not. Default value is true. | 
**custom_kms_key_arn** | **str, none_type** | Specifies custom KMS key arn. It will be of form arn:aws:kms:&lt;region&gt;:&lt;account_id&gt;:key/&lt;key_id&gt; | [optional] 
**kms_key** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies AWS KMS key to use for encryption of restored volumes. This is only populated for selection from dropdown. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


