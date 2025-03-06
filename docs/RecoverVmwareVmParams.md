# RecoverVmwareVmParams

Specifies the parameters to recover VMware VM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_protection_group_runs_params** | [**List[RecoverProtectionGroupRunParams]**](RecoverProtectionGroupRunParams.md) | Specifies the Protection Group Runs params to recover. All the VM&#39;s that are successfully backed up by specified Runs will be recovered. This can be specified along with individual snapshots of VMs. User has to make sure that specified Object snapshots and Protection Group Runs should not have any intersection. For example, user cannot specify multiple Runs which has same Object or an Object snapshot and a Run which has same Object&#39;s snapshot. | [optional] 
**restore_object_customizations** | [**List[RestoreObjectCustomization]**](RestoreObjectCustomization.md) | Specifies the customization for the VMs being restored. | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 
**vmware_target_params** | [**VmwareTargetParamsForRecoverVM**](VmwareTargetParamsForRecoverVM.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recover_vmware_vm_params import RecoverVmwareVmParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVmwareVmParams from a JSON string
recover_vmware_vm_params_instance = RecoverVmwareVmParams.from_json(json)
# print the JSON string representation of the object
print(RecoverVmwareVmParams.to_json())

# convert the object into a dict
recover_vmware_vm_params_dict = recover_vmware_vm_params_instance.to_dict()
# create an instance of RecoverVmwareVmParams from a dict
recover_vmware_vm_params_from_dict = RecoverVmwareVmParams.from_dict(recover_vmware_vm_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


