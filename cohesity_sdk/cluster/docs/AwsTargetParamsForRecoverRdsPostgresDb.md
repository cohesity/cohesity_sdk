# AwsTargetParamsForRecoverRdsPostgresDb

Specifies the parameters for an AWS RDS Postgres recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**AwsRdsPostgresDbRecoveryTargetConfig**](AwsRdsPostgresDbRecoveryTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_recover_rds_postgres_db import AwsTargetParamsForRecoverRdsPostgresDb

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverRdsPostgresDb from a JSON string
aws_target_params_for_recover_rds_postgres_db_instance = AwsTargetParamsForRecoverRdsPostgresDb.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverRdsPostgresDb.to_json())

# convert the object into a dict
aws_target_params_for_recover_rds_postgres_db_dict = aws_target_params_for_recover_rds_postgres_db_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverRdsPostgresDb from a dict
aws_target_params_for_recover_rds_postgres_db_from_dict = AwsTargetParamsForRecoverRdsPostgresDb.from_dict(aws_target_params_for_recover_rds_postgres_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


