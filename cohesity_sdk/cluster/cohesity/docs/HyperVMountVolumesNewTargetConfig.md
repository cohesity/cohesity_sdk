# HyperVMountVolumesNewTargetConfig

Specifies the configuration for mounting volumes to a new target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bring_disks_online** | **bool, none_type** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to false because bring disks online is only supported for Windows VM. If this is set to true, HyperV Integration Services must be installed on the VM. | 
**mount_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


