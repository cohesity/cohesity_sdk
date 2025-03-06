# AwsTargetParamsForRecoverRds

Specifies the parameters for an AWS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rds_config** | [**RdsConfig**](RdsConfig.md) |  | [optional] 
**recovery_target_config** | [**AwsRdsRecoveryTargetConfig**](AwsRdsRecoveryTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_recover_rds import AwsTargetParamsForRecoverRds

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverRds from a JSON string
aws_target_params_for_recover_rds_instance = AwsTargetParamsForRecoverRds.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverRds.to_json())

# convert the object into a dict
aws_target_params_for_recover_rds_dict = aws_target_params_for_recover_rds_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverRds from a dict
aws_target_params_for_recover_rds_from_dict = AwsTargetParamsForRecoverRds.from_dict(aws_target_params_for_recover_rds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


