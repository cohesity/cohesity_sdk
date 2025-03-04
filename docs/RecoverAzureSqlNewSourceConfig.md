# RecoverAzureSqlNewSourceConfig

Specifies the configuration for recovering Azure SQL instance to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.models.recover_azure_sql_new_source_config import RecoverAzureSqlNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSqlNewSourceConfig from a JSON string
recover_azure_sql_new_source_config_instance = RecoverAzureSqlNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSqlNewSourceConfig.to_json())

# convert the object into a dict
recover_azure_sql_new_source_config_dict = recover_azure_sql_new_source_config_instance.to_dict()
# create an instance of RecoverAzureSqlNewSourceConfig from a dict
recover_azure_sql_new_source_config_from_dict = RecoverAzureSqlNewSourceConfig.from_dict(recover_azure_sql_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


