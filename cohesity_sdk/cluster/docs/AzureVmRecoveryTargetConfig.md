# AzureVmRecoveryTargetConfig

Specifies the target object parameters to recover Azure vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverAzureVmNewSourceConfig**](RecoverAzureVmNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverAzureVmOriginalSourceConfig**](RecoverAzureVmOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.azure_vm_recovery_target_config import AzureVmRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureVmRecoveryTargetConfig from a JSON string
azure_vm_recovery_target_config_instance = AzureVmRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(AzureVmRecoveryTargetConfig.to_json())

# convert the object into a dict
azure_vm_recovery_target_config_dict = azure_vm_recovery_target_config_instance.to_dict()
# create an instance of AzureVmRecoveryTargetConfig from a dict
azure_vm_recovery_target_config_from_dict = AzureVmRecoveryTargetConfig.from_dict(azure_vm_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


