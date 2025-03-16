# AcropolisTargetParamsForRecoverVm

Specifies the parameters for an Acropolis recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recover_excluded_disk** | **bool** | Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false. | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**recovery_target_config** | [**RecoverAcropolisVmTargetConfig**](RecoverAcropolisVmTargetConfig.md) | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source or to original Source with different configuration. If not specified, then the recovery of the vms will be performed to original location with all configuration parameters retained. | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) | Specifies params to rename the VMs that are recovered. If not specified, the original names of the VMs are preserved. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.acropolis_target_params_for_recover_vm import AcropolisTargetParamsForRecoverVm

# TODO update the JSON string below
json = "{}"
# create an instance of AcropolisTargetParamsForRecoverVm from a JSON string
acropolis_target_params_for_recover_vm_instance = AcropolisTargetParamsForRecoverVm.from_json(json)
# print the JSON string representation of the object
print(AcropolisTargetParamsForRecoverVm.to_json())

# convert the object into a dict
acropolis_target_params_for_recover_vm_dict = acropolis_target_params_for_recover_vm_instance.to_dict()
# create an instance of AcropolisTargetParamsForRecoverVm from a dict
acropolis_target_params_for_recover_vm_from_dict = AcropolisTargetParamsForRecoverVm.from_dict(acropolis_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


