# HyperVTargetParamsForRecoverVm

Specifies the parameters for a HyperV recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**instant_recovery** | **bool, none_type** | Specifies whether to perform an instant recovery. By instant recovery, the recovered VM is available before files are completely copied to the recovered VM. Default is true. | [optional] 
**overwrite_existing_vms** | **bool, none_type** | Specifies whether to overwrite existing VMs while performing recovery of a VM. Default value is false. | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**preserve_uuids** | **bool, none_type** | Specifies whether to preserve uuids of recovered VMs. Default is false. | [optional] 
**recover_excluded_disk** | **bool, none_type** | Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false. | [optional] 
**recovery_target_config** | [**HyperVVmRecoveryTargetConfig**](HyperVVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**use_smb_service** | **bool, none_type** | Specifies if the HyperV recovery is using the SMB service to perform the restore. It is false for copy-recovery if nothing is specified. For instant-recovery it is true by default. Since DMaaS does not support SMB, only stream copy recovery is supported. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


