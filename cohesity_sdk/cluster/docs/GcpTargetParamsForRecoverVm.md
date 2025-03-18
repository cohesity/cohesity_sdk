# GcpTargetParamsForRecoverVm

Specifies the parameters for a GCP recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_target_config** | [**GcpVmRecoveryTargetConfig**](GcpVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_vm import GcpTargetParamsForRecoverVm

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


