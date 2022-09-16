# HyperVMountVolumesNewTargetConfig

Specifies the configuration for mounting volumes to a new target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**bring_disks_online** | **bool, none_type** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to false because bring disks online is only supported for Windows VM. If this is set to true, HyperV Integration Services must be installed on the VM. | 
**target_vm_credentials** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies credentials to access the target VM. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


