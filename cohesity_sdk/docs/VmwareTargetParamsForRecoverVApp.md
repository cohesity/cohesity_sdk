# VmwareTargetParamsForRecoverVApp

Specifies the parameters for a VMware recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_differential_restore** | **bool, none_type** | Specifies whether to attempt differential restore. | [optional] 
**continue_on_error** | **bool, none_type** | Specifies whether to continue recovering other vms if one of vms failed to recover. Default value is false. | [optional] 
**disk_provision_type** | **str, none_type** | Specifies the Virtual Disk Provisioning Policies for Vmware VM | [optional] 
**enable_nbdssl_fallback** | **bool, none_type** | If this field is set to true and SAN transport recovery fails, then recovery will fallback to use NBDSSL transport. This field only applies if &#39;leverageSanTransport&#39; is set to true. | [optional] 
**leverage_san_transport** | **bool, none_type** | Specifies whether to enable SAN transport for copy recovery or not | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether to power on vms after recovery. If not specified, or false, recovered vms will be in powered off state. | [optional] 
**recovery_process_type** | **str** | Specifies type of Recovery Process to be used. InstantRecovery/CopyRecovery etc... Default value is InstantRecovery. | [optional] 
**recovery_target_config** | [**VmwareVAppRecoveryTargetConfig**](VmwareVAppRecoveryTargetConfig.md) |  | [optional] 
**rename_recovered_v_apps_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**rename_recovered_vms_params** | [**RecoveredOrClonedVmsRenameConfig**](RecoveredOrClonedVmsRenameConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


