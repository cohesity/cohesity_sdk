# AwsTargetParamsForRecoverVm

Specifies the parameters for an AWS recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**custom_tags** | [**[SimpleTags], none_type**](SimpleTags.md) | Specifies the custom tags that need to be present on on every temporary and permanent entity that this job creates. | [optional] 
**fleet_config** | [**FleetConfig**](FleetConfig.md) |  | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_target_config** | [**AwsVmRecoveryTargetConfig**](AwsVmRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


