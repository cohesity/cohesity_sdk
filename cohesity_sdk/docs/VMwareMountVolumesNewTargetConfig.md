# VMwareMountVolumesNewTargetConfig

Specifies the configuration for mounting volumes to a new target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_target** | [**RecoverTarget**](RecoverTarget.md) |  | 
**bring_disks_online** | **bool, none_type** | Specifies whether the volumes need to be online within the target environment after attaching the disks. For linux VMs, this should always be set to true. For Windows, this is optional. If this is set to true, VMware tools must be installed on the VM. If this is set to false, useExistingAgent and targetCredentials are not needed. | 
**use_existing_agent** | **bool, none_type** | Specifies whether this will use an existing agent on the target vm or will deploy a new agent. This is required if bringDisksOnline is set to true. | [optional] 
**target_vm_credentials** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies credentials to access the target VM. This is required if bringDisksOnline is set to true and useExistingAgent set to false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


