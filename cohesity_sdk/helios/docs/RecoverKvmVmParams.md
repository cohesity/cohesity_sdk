# RecoverKvmVmParams

Specifies the parameters to recover VMs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kvm_target_params** | [**KvmTargetParamsForRecoverVm**](KvmTargetParamsForRecoverVm.md) | Specifies the params for recovering to a KVM target. | [optional] 
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.helios.models.recover_kvm_vm_params import RecoverKvmVmParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverKvmVmParams from a JSON string
recover_kvm_vm_params_instance = RecoverKvmVmParams.from_json(json)
# print the JSON string representation of the object
print(RecoverKvmVmParams.to_json())

# convert the object into a dict
recover_kvm_vm_params_dict = recover_kvm_vm_params_instance.to_dict()
# create an instance of RecoverKvmVmParams from a dict
recover_kvm_vm_params_from_dict = RecoverKvmVmParams.from_dict(recover_kvm_vm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


