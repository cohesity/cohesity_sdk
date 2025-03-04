# HyperVTargetParamsForRecoverVm

Specifies the parameters for a HyperV recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**instant_recovery** | **bool** | Specifies whether to perform an instant recovery. By instant recovery, the recovered VM is available before files are completely copied to the recovered VM. Default is true. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**preserve_uuids** | **bool** | Specifies whether to preserve uuids of recovered VMs. Default is false. | [optional] 
**recover_excluded_disk** | **bool** | Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false. | [optional] 
**recovery_target_config** | [**HyperVVmRecoveryTargetConfig**](HyperVVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**use_smb_service** | **bool** | Specifies if the HyperV recovery is using the SMB service to perform the restore. On-prem, this is the case by default. However, as of today, DMaaS does not support SMB, and HyperV VM VM restores will employ an alternative restore method in this case. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.hyper_v_target_params_for_recover_vm import HyperVTargetParamsForRecoverVm

# TODO update the JSON string below
json = "{}"
# create an instance of HyperVTargetParamsForRecoverVm from a JSON string
hyper_v_target_params_for_recover_vm_instance = HyperVTargetParamsForRecoverVm.from_json(json)
# print the JSON string representation of the object
print(HyperVTargetParamsForRecoverVm.to_json())

# convert the object into a dict
hyper_v_target_params_for_recover_vm_dict = hyper_v_target_params_for_recover_vm_instance.to_dict()
# create an instance of HyperVTargetParamsForRecoverVm from a dict
hyper_v_target_params_for_recover_vm_from_dict = HyperVTargetParamsForRecoverVm.from_dict(hyper_v_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


