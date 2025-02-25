# HyperVTargetParamsForRecoverVm

Specifies the parameters for a HyperV recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**instant_recovery** | **bool, none_type** | Specifies whether to perform an instant recovery. By instant recovery, the recovered VM is available before files are completely copied to the recovered VM. Default is true. | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**preserve_uuids** | **bool, none_type** | Specifies whether to preserve uuids of recovered VMs. Default is false. | [optional] 
**recover_excluded_disk** | **bool, none_type** | Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false. | [optional] 
**recovery_target_config** | [**HyperVVmRecoveryTargetConfig**](HyperVVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**use_smb_service** | **bool, none_type** | Specifies if the HyperV recovery is using the SMB service to perform the restore. On-prem, this is the case by default. However, as of today, DMaaS does not support SMB, and HyperV VM VM restores will employ an alternative restore method in this case. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


