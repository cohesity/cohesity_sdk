# VmwareTargetParamsForRecoverVM

Specifies the parameters for a VMware recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_recovered_vms_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies params to rename the VMs that are recovered. If not specified, the original names of the VMs are preserved. | [optional] 
**recovery_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the recovery target configuration if recovery has to be done to a different location which is different from original source or to original Source with different configuration. If not specified, then the recovery of the vms will be performed to original location with all configuration parameters retained. | [optional] 
**vlan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**attempt_differential_restore** | **bool, none_type** | Specifies whether to attempt differential restore. | [optional] 
**overwrite_existing_vm** | **bool, none_type** | Specifies whether to overwrite the VM at the target location. This is a data destructive operation and if this is selected, the original VM may no longer be accessible. This option is only applicable if renameRecoveredVmParams is null and powerOffAndRenameExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false. | [optional] 
**power_off_and_rename_existing_vm** | **bool, none_type** | Specifies whether to power off and mark the VM at the target location as deprecated. As an example, &lt;vm_name&gt; will be renamed to deprecated::&lt;vm_name&gt;, and a new VM with the name &lt;vm_name&gt; in place of the now deprecated VM. Both deprecated::&lt;vm_name&gt; and &lt;vm_name&gt; will exist on the primary, but the corresponding protection job will only backup &lt;vm_name&gt; on its next run. Only applicable if renameRecoveredVmParams is null and overwriteExistingVm is false. This option is not supported for vApp or vApp template recoveries. Default value is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


