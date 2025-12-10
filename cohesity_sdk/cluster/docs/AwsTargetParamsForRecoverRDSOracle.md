# AwsTargetParamsForRecoverRDSOracle

Specifies the parameters for an AWS RDS Oracle recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**AwsRDSOracleRecoveryTargetConfig**](AwsRDSOracleRecoveryTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_recover_rds_oracle import AwsTargetParamsForRecoverRDSOracle

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverRDSOracle from a JSON string
aws_target_params_for_recover_rds_oracle_instance = AwsTargetParamsForRecoverRDSOracle.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverRDSOracle.to_json())

# convert the object into a dict
aws_target_params_for_recover_rds_oracle_dict = aws_target_params_for_recover_rds_oracle_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverRDSOracle from a dict
aws_target_params_for_recover_rds_oracle_from_dict = AwsTargetParamsForRecoverRDSOracle.from_dict(aws_target_params_for_recover_rds_oracle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


