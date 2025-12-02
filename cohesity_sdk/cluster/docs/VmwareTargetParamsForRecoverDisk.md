# VmwareTargetParamsForRecoverDisk

Specifies the parameters for a VMware recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continue_on_error** | **bool, none_type** | Specifies whether or not to continue performing the recovery in the event that an error is encountered. | [optional] 
**original_source_config** | [**VmwareRecoverDisksOriginalSourceConfig**](VmwareRecoverDisksOriginalSourceConfig.md) |  | [optional] 
**power_off_vms** | **bool, none_type** | Specifies whether or not to power off VMs before performing the recovery. | [optional] 
**power_on_vms** | **bool, none_type** | Specifies whether or not to power on VMs after performing the recovery. | [optional] 
**target_source_config** | [**VmwareRecoverDisksTargetSourceConfig**](VmwareRecoverDisksTargetSourceConfig.md) |  | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


