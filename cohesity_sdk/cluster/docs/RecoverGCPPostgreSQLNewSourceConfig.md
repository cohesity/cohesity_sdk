# RecoverGCPPostgreSQLNewSourceConfig

Specifies the configuration for recovering GCP PostgreSQL database to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_postgre_sql_new_source_config import RecoverGCPPostgreSQLNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPPostgreSQLNewSourceConfig from a JSON string
recover_gcp_postgre_sql_new_source_config_instance = RecoverGCPPostgreSQLNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPPostgreSQLNewSourceConfig.to_json())

# convert the object into a dict
recover_gcp_postgre_sql_new_source_config_dict = recover_gcp_postgre_sql_new_source_config_instance.to_dict()
# create an instance of RecoverGCPPostgreSQLNewSourceConfig from a dict
recover_gcp_postgre_sql_new_source_config_from_dict = RecoverGCPPostgreSQLNewSourceConfig.from_dict(recover_gcp_postgre_sql_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


