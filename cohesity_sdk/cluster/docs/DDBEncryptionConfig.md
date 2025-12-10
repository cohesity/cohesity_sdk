# DDBEncryptionConfig

Specifies the encryption configuration for dynamo DB tables. Restored tables will be encryptred based on this configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_kms_key_arn** | **str** | Specifies custom KMS key arn to be set when encryption type is CustomKMS. It will be of form arn:aws:kms:&lt;region&gt;:&lt;account_id&gt;:key/&lt;key_id&gt; | [optional] 
**enable_encrypt** | **bool** | Specifies whether to use encrypt recovered volumes or not. When set to true, supports either AWS/self managed encryption. | 
**kms_key** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ddb_encryption_config import DDBEncryptionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DDBEncryptionConfig from a JSON string
ddb_encryption_config_instance = DDBEncryptionConfig.from_json(json)
# print the JSON string representation of the object
print(DDBEncryptionConfig.to_json())

# convert the object into a dict
ddb_encryption_config_dict = ddb_encryption_config_instance.to_dict()
# create an instance of DDBEncryptionConfig from a dict
ddb_encryption_config_from_dict = DDBEncryptionConfig.from_dict(ddb_encryption_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


