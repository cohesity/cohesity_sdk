# RecoverAzureSQLDBNewSourceConfig

Specifies the configuration for recovering Azure SQL DB instance to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_sqldb_new_source_config import RecoverAzureSQLDBNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSQLDBNewSourceConfig from a JSON string
recover_azure_sqldb_new_source_config_instance = RecoverAzureSQLDBNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSQLDBNewSourceConfig.to_json())

# convert the object into a dict
recover_azure_sqldb_new_source_config_dict = recover_azure_sqldb_new_source_config_instance.to_dict()
# create an instance of RecoverAzureSQLDBNewSourceConfig from a dict
recover_azure_sqldb_new_source_config_from_dict = RecoverAzureSQLDBNewSourceConfig.from_dict(recover_azure_sqldb_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


