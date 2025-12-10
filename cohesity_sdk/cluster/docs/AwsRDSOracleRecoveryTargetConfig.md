# AwsRDSOracleRecoveryTargetConfig

Specifies the target object parameters to recover AWS RDS Oracle.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAwsRDSOracleNewSourceConfig**](RecoverAwsRDSOracleNewSourceConfig.md) |  | 
**num_channels** | **int** | Number of channels for Oracle restore. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_rds_oracle_recovery_target_config import AwsRDSOracleRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRDSOracleRecoveryTargetConfig from a JSON string
aws_rds_oracle_recovery_target_config_instance = AwsRDSOracleRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsRDSOracleRecoveryTargetConfig.to_json())

# convert the object into a dict
aws_rds_oracle_recovery_target_config_dict = aws_rds_oracle_recovery_target_config_instance.to_dict()
# create an instance of AwsRDSOracleRecoveryTargetConfig from a dict
aws_rds_oracle_recovery_target_config_from_dict = AwsRDSOracleRecoveryTargetConfig.from_dict(aws_rds_oracle_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


