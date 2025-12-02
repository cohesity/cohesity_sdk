# KvmVmRecoveryTargetConfig

Specifies the target object parameters to recover KVM vms.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverKvmVmNewSourceConfig**](RecoverKvmVmNewSourceConfig.md) |  | [optional] 
**original_source_config** | [**RecoverKvmVmOriginalSourceConfig**](RecoverKvmVmOriginalSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.kvm_vm_recovery_target_config import KvmVmRecoveryTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of KvmVmRecoveryTargetConfig from a JSON string
kvm_vm_recovery_target_config_instance = KvmVmRecoveryTargetConfig.from_json(json)
# print the JSON string representation of the object
print(KvmVmRecoveryTargetConfig.to_json())

# convert the object into a dict
kvm_vm_recovery_target_config_dict = kvm_vm_recovery_target_config_instance.to_dict()
# create an instance of KvmVmRecoveryTargetConfig from a dict
kvm_vm_recovery_target_config_from_dict = KvmVmRecoveryTargetConfig.from_dict(kvm_vm_recovery_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


