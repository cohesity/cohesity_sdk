# KvmTargetParamsForRecoverVm

Specifies the parameters for a KVM recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_target_config** | [**KvmVmRecoveryTargetConfig**](KvmVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kvm_target_params_for_recover_vm import KvmTargetParamsForRecoverVm

# TODO update the JSON string below
json = "{}"
# create an instance of KvmTargetParamsForRecoverVm from a JSON string
kvm_target_params_for_recover_vm_instance = KvmTargetParamsForRecoverVm.from_json(json)
# print the JSON string representation of the object
print(KvmTargetParamsForRecoverVm.to_json())

# convert the object into a dict
kvm_target_params_for_recover_vm_dict = kvm_target_params_for_recover_vm_instance.to_dict()
# create an instance of KvmTargetParamsForRecoverVm from a dict
kvm_target_params_for_recover_vm_from_dict = KvmTargetParamsForRecoverVm.from_dict(kvm_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


