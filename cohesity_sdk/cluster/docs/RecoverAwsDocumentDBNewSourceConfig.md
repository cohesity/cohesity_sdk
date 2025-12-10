# RecoverAwsDocumentDBNewSourceConfig

Specifies the new destination Source configuration where the DocumentDB clusters will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_document_db_new_source_config import RecoverAwsDocumentDBNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsDocumentDBNewSourceConfig from a JSON string
recover_aws_document_db_new_source_config_instance = RecoverAwsDocumentDBNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsDocumentDBNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_document_db_new_source_config_dict = recover_aws_document_db_new_source_config_instance.to_dict()
# create an instance of RecoverAwsDocumentDBNewSourceConfig from a dict
recover_aws_document_db_new_source_config_from_dict = RecoverAwsDocumentDBNewSourceConfig.from_dict(recover_aws_document_db_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


