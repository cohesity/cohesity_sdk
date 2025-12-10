# AwsRdsMySqlRecoveryTargetConfig

Specifies the target object parameters to recover AWS RDS MySQL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAwsRdsMySqlNewSourceConfig**](RecoverAwsRdsMySqlNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_rds_my_sql_recovery_target_config import AwsRdsMySqlRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRdsMySqlRecoveryTargetConfig from a JSON string
aws_rds_my_sql_recovery_target_config_instance = AwsRdsMySqlRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsRdsMySqlRecoveryTargetConfig.to_json())

# convert the object into a dict
aws_rds_my_sql_recovery_target_config_dict = aws_rds_my_sql_recovery_target_config_instance.to_dict()
# create an instance of AwsRdsMySqlRecoveryTargetConfig from a dict
aws_rds_my_sql_recovery_target_config_from_dict = AwsRdsMySqlRecoveryTargetConfig.from_dict(aws_rds_my_sql_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


