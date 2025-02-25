# HyperVMountVolumesOriginalTargetConfig

Specifies the configuration for mounting volumes to the original target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bring_disks_online** | **bool, none_type** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to false because bring disks online is only supported for Windows VM. For Windows, this is optional. If this is set to true, HyperV Integration Services must be installed on the VM. | 
**target_vm_credentials** | [**Credentials**](Credentials.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


