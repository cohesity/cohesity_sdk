# RecoverAwsRdsPostgresDbNewSourceConfig

Specifies the new destination Source configuration where the RDS Postgres instances will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | [optional] 
**region** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_postgres_db_new_source_config import RecoverAwsRdsPostgresDbNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsPostgresDbNewSourceConfig from a JSON string
recover_aws_rds_postgres_db_new_source_config_instance = RecoverAwsRdsPostgresDbNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsPostgresDbNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_rds_postgres_db_new_source_config_dict = recover_aws_rds_postgres_db_new_source_config_instance.to_dict()
# create an instance of RecoverAwsRdsPostgresDbNewSourceConfig from a dict
recover_aws_rds_postgres_db_new_source_config_from_dict = RecoverAwsRdsPostgresDbNewSourceConfig.from_dict(recover_aws_rds_postgres_db_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


