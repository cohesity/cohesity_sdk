# VmwareTargetParamsForMountVolume

Specifies the parameters for a VMware mount volume target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_to_original_target** | **bool, none_type** | Specifies whether to mount to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**mounted_volume_mapping** | [**[MountedVolumeMapping], none_type**](MountedVolumeMapping.md) | Specifies the mapping of original volumes and mounted volumes | [optional] [readonly] 
**new_target_config** | [**VMwareMountVolumesNewTargetConfig**](VMwareMountVolumesNewTargetConfig.md) |  | [optional] 
**original_target_config** | [**VMwareMountVolumesOriginalTargetConfig**](VMwareMountVolumesOriginalTargetConfig.md) |  | [optional] 
**read_only_mount** | **bool, none_type** | Specifies whether to perform a read-only mount. Default is false. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 
**volume_names** | **[str], none_type** | Specifies the names of volumes that need to be mounted. If this is not specified then all volumes that are part of the source VM will be mounted on the target VM. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


