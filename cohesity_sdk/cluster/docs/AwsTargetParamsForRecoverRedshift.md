# AwsTargetParamsForRecoverRedshift

Specifies the parameters for an AWS Redshift recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recovery_target_config** | [**AwsRedshiftRecoveryTargetConfig**](AwsRedshiftRecoveryTargetConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_target_params_for_recover_redshift import AwsTargetParamsForRecoverRedshift

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverRedshift from a JSON string
aws_target_params_for_recover_redshift_instance = AwsTargetParamsForRecoverRedshift.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverRedshift.to_json())

# convert the object into a dict
aws_target_params_for_recover_redshift_dict = aws_target_params_for_recover_redshift_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverRedshift from a dict
aws_target_params_for_recover_redshift_from_dict = AwsTargetParamsForRecoverRedshift.from_dict(aws_target_params_for_recover_redshift_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


