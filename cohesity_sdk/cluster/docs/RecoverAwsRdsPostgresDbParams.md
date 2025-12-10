# RecoverAwsRdsPostgresDbParams

Specifies the parameters to recover RDS Postgres.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRdsPostgresDb**](AwsTargetParamsForRecoverRdsPostgresDb.md) |  | [optional] 
**snapshots** | [**List[RecoverAwsRdsSnapshotParams]**](RecoverAwsRdsSnapshotParams.md) | Specifies the details of the aws rds objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_postgres_db_params import RecoverAwsRdsPostgresDbParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsPostgresDbParams from a JSON string
recover_aws_rds_postgres_db_params_instance = RecoverAwsRdsPostgresDbParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsPostgresDbParams.to_json())

# convert the object into a dict
recover_aws_rds_postgres_db_params_dict = recover_aws_rds_postgres_db_params_instance.to_dict()
# create an instance of RecoverAwsRdsPostgresDbParams from a dict
recover_aws_rds_postgres_db_params_from_dict = RecoverAwsRdsPostgresDbParams.from_dict(recover_aws_rds_postgres_db_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


