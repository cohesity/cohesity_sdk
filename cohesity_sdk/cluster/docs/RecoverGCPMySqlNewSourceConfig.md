# RecoverGCPMySqlNewSourceConfig

Specifies the configuration for recovering GCP MySQL database to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcpmy_sql_new_source_config import RecoverGCPMySqlNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPMySqlNewSourceConfig from a JSON string
recover_gcpmy_sql_new_source_config_instance = RecoverGCPMySqlNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPMySqlNewSourceConfig.to_json())

# convert the object into a dict
recover_gcpmy_sql_new_source_config_dict = recover_gcpmy_sql_new_source_config_instance.to_dict()
# create an instance of RecoverGCPMySqlNewSourceConfig from a dict
recover_gcpmy_sql_new_source_config_from_dict = RecoverGCPMySqlNewSourceConfig.from_dict(recover_gcpmy_sql_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


