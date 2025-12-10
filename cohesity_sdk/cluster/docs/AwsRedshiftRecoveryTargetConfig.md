# AwsRedshiftRecoveryTargetConfig

Specifies the target object parameters to recover AWS Redshift.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAwsRedshiftNewSourceConfig**](RecoverAwsRedshiftNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_redshift_recovery_target_config import AwsRedshiftRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRedshiftRecoveryTargetConfig from a JSON string
aws_redshift_recovery_target_config_instance = AwsRedshiftRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsRedshiftRecoveryTargetConfig.to_json())

# convert the object into a dict
aws_redshift_recovery_target_config_dict = aws_redshift_recovery_target_config_instance.to_dict()
# create an instance of AwsRedshiftRecoveryTargetConfig from a dict
aws_redshift_recovery_target_config_from_dict = AwsRedshiftRecoveryTargetConfig.from_dict(aws_redshift_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


