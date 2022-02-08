# PhysicalTargetParamsForMountVolume

Specifies the parameters for a physical recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_to_original_target** | **bool, none_type** | Specifies whether to mount to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified. | 
**original_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the configuration for mounting to the original target. | [optional] 
**new_target_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the configuration for mounting to a new target. | [optional] 
**read_only_mount** | **bool, none_type** | Specifies whether to perform a read-only mount. Default is false. | [optional] 
**volume_names** | **[str], none_type** | Specifies the names of volumes that need to be mounted. If this is not specified then all volumes that are part of the source VM will be mounted on the target VM. | [optional] 
**mounted_volume_mapping** | [**[MountedVolumeMapping], none_type**](MountedVolumeMapping.md) | Specifies the mapping of original volumes and mounted volumes | [optional] [readonly] 
**vlan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


