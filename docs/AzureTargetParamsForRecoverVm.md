# AzureTargetParamsForRecoverVm

Specifies the parameters for an Azure recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_target_config** | [**AzureVmRecoveryTargetConfig**](AzureVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.azure_target_params_for_recover_vm import AzureTargetParamsForRecoverVm

# TODO update the JSON string below
json = "{}"
# create an instance of AzureTargetParamsForRecoverVm from a JSON string
azure_target_params_for_recover_vm_instance = AzureTargetParamsForRecoverVm.from_json(json)
# print the JSON string representation of the object
print(AzureTargetParamsForRecoverVm.to_json())

# convert the object into a dict
azure_target_params_for_recover_vm_dict = azure_target_params_for_recover_vm_instance.to_dict()
# create an instance of AzureTargetParamsForRecoverVm from a dict
azure_target_params_for_recover_vm_from_dict = AzureTargetParamsForRecoverVm.from_dict(azure_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


