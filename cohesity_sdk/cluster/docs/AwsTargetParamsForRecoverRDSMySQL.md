# AwsTargetParamsForRecoverRDSMySQL

Specifies the parameters for an AWS RDS MySQL recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**AwsRdsMySqlRecoveryTargetConfig**](AwsRdsMySqlRecoveryTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_recover_rdsmy_sql import AwsTargetParamsForRecoverRDSMySQL

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverRDSMySQL from a JSON string
aws_target_params_for_recover_rdsmy_sql_instance = AwsTargetParamsForRecoverRDSMySQL.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverRDSMySQL.to_json())

# convert the object into a dict
aws_target_params_for_recover_rdsmy_sql_dict = aws_target_params_for_recover_rdsmy_sql_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverRDSMySQL from a dict
aws_target_params_for_recover_rdsmy_sql_from_dict = AwsTargetParamsForRecoverRDSMySQL.from_dict(aws_target_params_for_recover_rdsmy_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


