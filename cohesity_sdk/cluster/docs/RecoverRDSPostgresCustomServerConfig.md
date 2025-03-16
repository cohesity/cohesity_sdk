# RecoverRDSPostgresCustomServerConfig

Specifies the configuration for recovering RDS Postgres instance to the known target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | Specifies the Ip in which to deploy the Rds instance. | 
**port** | **int** | Specifies the port to use to connect to the server. | 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**standard_credentials** | [**Credentials**](Credentials.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_rds_postgres_custom_server_config import RecoverRDSPostgresCustomServerConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverRDSPostgresCustomServerConfig from a JSON string
recover_rds_postgres_custom_server_config_instance = RecoverRDSPostgresCustomServerConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverRDSPostgresCustomServerConfig.to_json())

# convert the object into a dict
recover_rds_postgres_custom_server_config_dict = recover_rds_postgres_custom_server_config_instance.to_dict()
# create an instance of RecoverRDSPostgresCustomServerConfig from a dict
recover_rds_postgres_custom_server_config_from_dict = RecoverRDSPostgresCustomServerConfig.from_dict(recover_rds_postgres_custom_server_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


