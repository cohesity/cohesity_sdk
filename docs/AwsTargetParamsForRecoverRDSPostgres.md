# AwsTargetParamsForRecoverRDSPostgres

Specifies the recovery target params for RDS Postgres target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_server_config** | [**RecoverRDSPostgresCustomServerConfig**](RecoverRDSPostgresCustomServerConfig.md) |  | [optional] 
**known_source_config** | [**RecoverRDSPostgresToKnownSourceConfig**](RecoverRDSPostgresToKnownSourceConfig.md) |  | [optional] 
**recover_to_known_source** | **bool** | Specifies whether the recovery should be performed to a known or a custom target. | 

## Example

```python
from cohesity_sdk.models.aws_target_params_for_recover_rds_postgres import AwsTargetParamsForRecoverRDSPostgres

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverRDSPostgres from a JSON string
aws_target_params_for_recover_rds_postgres_instance = AwsTargetParamsForRecoverRDSPostgres.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverRDSPostgres.to_json())

# convert the object into a dict
aws_target_params_for_recover_rds_postgres_dict = aws_target_params_for_recover_rds_postgres_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverRDSPostgres from a dict
aws_target_params_for_recover_rds_postgres_from_dict = AwsTargetParamsForRecoverRDSPostgres.from_dict(aws_target_params_for_recover_rds_postgres_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


