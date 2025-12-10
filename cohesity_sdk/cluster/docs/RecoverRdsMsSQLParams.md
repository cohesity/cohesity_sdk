# RecoverRdsMsSQLParams

Specifies the parameters to recover AWS RDS MS SQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_target_params** | [**AwsTargetParamsForRecoverRdsMsSQL**](AwsTargetParamsForRecoverRdsMsSQL.md) |  | [optional] 
**snapshots** | [**List[RecoverRdsMsSQLSnapshotParams]**](RecoverRdsMsSQLSnapshotParams.md) | Specifies the details of the AWS RDS MS SQL objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_rds_ms_sql_params import RecoverRdsMsSQLParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverRdsMsSQLParams from a JSON string
recover_rds_ms_sql_params_instance = RecoverRdsMsSQLParams.from_json(json)
# print the JSON string representation of the object
print(RecoverRdsMsSQLParams.to_json())

# convert the object into a dict
recover_rds_ms_sql_params_dict = recover_rds_ms_sql_params_instance.to_dict()
# create an instance of RecoverRdsMsSQLParams from a dict
recover_rds_ms_sql_params_from_dict = RecoverRdsMsSQLParams.from_dict(recover_rds_ms_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


