# GcpTargetParamsForRecoverVm

Specifies the parameters for a GCP recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_target_config** | [**GcpVmRecoveryTargetConfig**](GcpVmRecoveryTargetConfig.md) | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source or to original Source with different configuration. If not specified, then the recovery of the vms will be performed to original location with all configuration parameters retained. | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) | Specifies params to rename the VMs that are recovered. If not specified, the original names of the VMs are preserved. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.gcp_target_params_for_recover_vm import GcpTargetParamsForRecoverVm

# TODO update the JSON string below
json = "{}"
# create an instance of GcpTargetParamsForRecoverVm from a JSON string
gcp_target_params_for_recover_vm_instance = GcpTargetParamsForRecoverVm.from_json(json)
# print the JSON string representation of the object
print(GcpTargetParamsForRecoverVm.to_json())

# convert the object into a dict
gcp_target_params_for_recover_vm_dict = gcp_target_params_for_recover_vm_instance.to_dict()
# create an instance of GcpTargetParamsForRecoverVm from a dict
gcp_target_params_for_recover_vm_from_dict = GcpTargetParamsForRecoverVm.from_dict(gcp_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


