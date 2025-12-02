# RecoverGCPSqlServerNewSourceConfig

Specifies the configuration for recovering GCP SQL Server database to the new target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_sql_server_new_source_config import RecoverGCPSqlServerNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPSqlServerNewSourceConfig from a JSON string
recover_gcp_sql_server_new_source_config_instance = RecoverGCPSqlServerNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPSqlServerNewSourceConfig.to_json())

# convert the object into a dict
recover_gcp_sql_server_new_source_config_dict = recover_gcp_sql_server_new_source_config_instance.to_dict()
# create an instance of RecoverGCPSqlServerNewSourceConfig from a dict
recover_gcp_sql_server_new_source_config_from_dict = RecoverGCPSqlServerNewSourceConfig.from_dict(recover_gcp_sql_server_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


