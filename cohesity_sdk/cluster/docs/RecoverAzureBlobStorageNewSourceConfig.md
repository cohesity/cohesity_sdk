# RecoverAzureBlobStorageNewSourceConfig

Specifies the configuration for recovering Azure Blob Storage instance to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_blob_storage_new_source_config import RecoverAzureBlobStorageNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureBlobStorageNewSourceConfig from a JSON string
recover_azure_blob_storage_new_source_config_instance = RecoverAzureBlobStorageNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureBlobStorageNewSourceConfig.to_json())

# convert the object into a dict
recover_azure_blob_storage_new_source_config_dict = recover_azure_blob_storage_new_source_config_instance.to_dict()
# create an instance of RecoverAzureBlobStorageNewSourceConfig from a dict
recover_azure_blob_storage_new_source_config_from_dict = RecoverAzureBlobStorageNewSourceConfig.from_dict(recover_azure_blob_storage_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


