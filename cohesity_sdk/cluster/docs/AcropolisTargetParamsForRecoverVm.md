# AcropolisTargetParamsForRecoverVm

Specifies the parameters for an Acropolis recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recover_excluded_disk** | **bool, none_type** | Specifies whether to recover excluded disk while performing recovery of a VM by creating empty disks for them. Default value is false. | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**recovery_target_config** | [**RecoverAcropolisVmTargetConfig**](RecoverAcropolisVmTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


