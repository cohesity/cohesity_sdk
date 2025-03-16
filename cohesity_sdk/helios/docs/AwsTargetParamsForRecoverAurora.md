# AwsTargetParamsForRecoverAurora

Specifies the parameters for an AWS recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aurora_config** | [**AuroraConfig**](AuroraConfig.md) | Specifies the Aurora params. | [optional] 
**recovery_target_config** | [**AwsAuroraRecoveryTargetConfig**](AwsAuroraRecoveryTargetConfig.md) | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source or to original Source with different configuration. If not specified, then the recovery of the vms will be performed to original location with all configuration parameters retained. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.aws_target_params_for_recover_aurora import AwsTargetParamsForRecoverAurora

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTargetParamsForRecoverAurora from a JSON string
aws_target_params_for_recover_aurora_instance = AwsTargetParamsForRecoverAurora.from_json(json)
# print the JSON string representation of the object
print(AwsTargetParamsForRecoverAurora.to_json())

# convert the object into a dict
aws_target_params_for_recover_aurora_dict = aws_target_params_for_recover_aurora_instance.to_dict()
# create an instance of AwsTargetParamsForRecoverAurora from a dict
aws_target_params_for_recover_aurora_from_dict = AwsTargetParamsForRecoverAurora.from_dict(aws_target_params_for_recover_aurora_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


