# RecoverAwsRdsMySqlParams

Specifies the parameters to recover RDS MySQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRDSMySQL**](AwsTargetParamsForRecoverRDSMySQL.md) |  | [optional] 
**snapshots** | [**List[RecoverAwsRdsSnapshotParams]**](RecoverAwsRdsSnapshotParams.md) | Specifies the details of the aws rds objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_my_sql_params import RecoverAwsRdsMySqlParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRdsMySqlParams from a JSON string
recover_aws_rds_my_sql_params_instance = RecoverAwsRdsMySqlParams.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRdsMySqlParams.to_json())

# convert the object into a dict
recover_aws_rds_my_sql_params_dict = recover_aws_rds_my_sql_params_instance.to_dict()
# create an instance of RecoverAwsRdsMySqlParams from a dict
recover_aws_rds_my_sql_params_from_dict = RecoverAwsRdsMySqlParams.from_dict(recover_aws_rds_my_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


