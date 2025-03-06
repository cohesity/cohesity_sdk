# AwsVmRecoveryTargetConfig

Specifies the target object parameters to recover AWS vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAwsVmNewSourceConfig**](RecoverAwsVmNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.aws_vm_recovery_target_config import AwsVmRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsVmRecoveryTargetConfig from a JSON string
aws_vm_recovery_target_config_instance = AwsVmRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AwsVmRecoveryTargetConfig.to_json())

# convert the object into a dict
aws_vm_recovery_target_config_dict = aws_vm_recovery_target_config_instance.to_dict()
# create an instance of AwsVmRecoveryTargetConfig from a dict
aws_vm_recovery_target_config_from_dict = AwsVmRecoveryTargetConfig.from_dict(aws_vm_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


