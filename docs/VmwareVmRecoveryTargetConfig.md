# VmwareVmRecoveryTargetConfig

Specifies the target object parameters to recover VMware vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverVmwareVmNewSourceConfig**](RecoverVmwareVmNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverVmwareVmOriginalSourceConfig**](RecoverVmwareVmOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.models.vmware_vm_recovery_target_config import VmwareVmRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareVmRecoveryTargetConfig from a JSON string
vmware_vm_recovery_target_config_instance = VmwareVmRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(VmwareVmRecoveryTargetConfig.to_json())

# convert the object into a dict
vmware_vm_recovery_target_config_dict = vmware_vm_recovery_target_config_instance.to_dict()
# create an instance of VmwareVmRecoveryTargetConfig from a dict
vmware_vm_recovery_target_config_from_dict = VmwareVmRecoveryTargetConfig.from_dict(vmware_vm_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


