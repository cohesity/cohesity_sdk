# RecoverAzureSQLMINewSourceConfig

Specifies the configuration for recovering Azure SQL MI instance to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_azure_sqlmi_new_source_config import RecoverAzureSQLMINewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAzureSQLMINewSourceConfig from a JSON string
recover_azure_sqlmi_new_source_config_instance = RecoverAzureSQLMINewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAzureSQLMINewSourceConfig.to_json())

# convert the object into a dict
recover_azure_sqlmi_new_source_config_dict = recover_azure_sqlmi_new_source_config_instance.to_dict()
# create an instance of RecoverAzureSQLMINewSourceConfig from a dict
recover_azure_sqlmi_new_source_config_from_dict = RecoverAzureSQLMINewSourceConfig.from_dict(recover_azure_sqlmi_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


