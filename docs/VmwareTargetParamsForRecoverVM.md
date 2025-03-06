# VmwareTargetParamsForRecoverVM

Specifies the parameters for a VMware recovery target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_differential_restore** | **bool** | Specifies whether to attempt differential restore. | [optional] 
**continue_on_error** | **bool** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**disk_provision_type** | **str** | Specifies the Virtual Disk Provisioning Policies for Vmware VM | [optional] 
**enable_nbdssl_fallback** | **bool** | If this field is set to true and SAN transport recovery fails, then recovery will fallback to use NBDSSL transport. This field only applies if &#39;leverageSanTransport&#39; is set to true. | [optional] 
**is_multi_stage_restore** | **bool** | Specifies whether this is a multistage restore which is used for migration/hot-standby purpose. | [optional] 
**leverage_san_transport** | **bool** | Specifies whether to enable SAN transport for copy recovery or not | [optional] 
**overwrite_existing_vm** | **bool** | Specifies whether to overwrite the VM at the target location. This is a data destructive operation and if this is selected, the original VM may no longer be accessible. This option is only applicable if renameRecoveredVmParams is null and powerOffAndRenameExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false. | [optional] 
**power_off_and_rename_existing_vm** | **bool** | Specifies whether to power off and mark the VM at the target location as deprecated. As an example, &lt;vm_name&gt; will be renamed to deprecated::&lt;vm_name&gt;, and a new VM with the name &lt;vm_name&gt; in place of the now deprecated VM. Both deprecated::&lt;vm_name&gt; and &lt;vm_name&gt; will exist on the primary, but the corresponding protection job will only backup &lt;vm_name&gt; on its next run. Only applicable if renameRecoveredVmParams is null and overwriteExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false. | [optional] 
**power_on_vms** | **bool** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**recovery_target_config** | [**VmwareVmRecoveryTargetConfig**](VmwareVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.vmware_target_params_for_recover_vm import VmwareTargetParamsForRecoverVM

# TODO update the JSON string below
json = "{}"
# create an instance of VmwareTargetParamsForRecoverVM from a JSON string
vmware_target_params_for_recover_vm_instance = VmwareTargetParamsForRecoverVM.from_json(json)
# print the JSON string representation of the object
print(VmwareTargetParamsForRecoverVM.to_json())

# convert the object into a dict
vmware_target_params_for_recover_vm_dict = vmware_target_params_for_recover_vm_instance.to_dict()
# create an instance of VmwareTargetParamsForRecoverVM from a dict
vmware_target_params_for_recover_vm_from_dict = VmwareTargetParamsForRecoverVM.from_dict(vmware_target_params_for_recover_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


