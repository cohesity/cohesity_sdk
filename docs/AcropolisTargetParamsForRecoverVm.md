# AcropolisTargetParamsForRecoverVm

Specifies the parameters for an Acropolis recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recover_excluded_disk** | **bool** | Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false. | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**recovery_target_config** | [**RecoverAcropolisVmTargetConfig**](RecoverAcropolisVmTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.acropolis_target_params_for_recover_vm import AcropolisTargetParamsForRecoverVm

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


