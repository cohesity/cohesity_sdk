# RecoverAzureDbNewSourceConfig

Specifies the source and instance configuration for Azure database recovery.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_db_new_source_config import RecoverAzureDbNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureDbNewSourceConfig from a JSON string
recover_azure_db_new_source_config_instance = RecoverAzureDbNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureDbNewSourceConfig.to_json())

# convert the object into a dict
recover_azure_db_new_source_config_dict = recover_azure_db_new_source_config_instance.to_dict()
# create an instance of RecoverAzureDbNewSourceConfig from a dict
recover_azure_db_new_source_config_from_dict = RecoverAzureDbNewSourceConfig.from_dict(recover_azure_db_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


