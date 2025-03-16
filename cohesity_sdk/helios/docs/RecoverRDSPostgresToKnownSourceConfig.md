# RecoverRDSPostgresToKnownSourceConfig

Specifies the configuration for recovering RDS Postgres instance to the known target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the instance in which to deploy the Rds instance. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new target. | [optional] 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the AWS region in which to deploy the Rds instance. | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) | Specifies the target source details where RDS Postgres database will be recovered. This source id should be a RDS Postgres target instance id were databases could be restored. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_rds_postgres_to_known_source_config import RecoverRDSPostgresToKnownSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverRDSPostgresToKnownSourceConfig from a JSON string
recover_rds_postgres_to_known_source_config_instance = RecoverRDSPostgresToKnownSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverRDSPostgresToKnownSourceConfig.to_json())

# convert the object into a dict
recover_rds_postgres_to_known_source_config_dict = recover_rds_postgres_to_known_source_config_instance.to_dict()
# create an instance of RecoverRDSPostgresToKnownSourceConfig from a dict
recover_rds_postgres_to_known_source_config_from_dict = RecoverRDSPostgresToKnownSourceConfig.from_dict(recover_rds_postgres_to_known_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


