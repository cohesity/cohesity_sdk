# PhysicalTargetParamsForRecoverVolume

Specifies the parameters for a physical recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_target** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the target entity where the volumes are being mounted. | 
**volume_mapping** | [**[RecoverVolumeMapping], none_type**](RecoverVolumeMapping.md) | Specifies the mapping from source volumes to destination volumes. | 
**force_unmount_volume** | **bool, none_type** | Specifies whether volume would be dismounted first during LockVolume failure. If not specified, default is false. | [optional] 
**vlan_config** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies VLAN Params associated with the recovered. If this is not specified, then the VLAN settings will be automatically selected from one of the below options: a. If VLANs are configured on Cohesity, then the VLAN host/VIP will be automatically based on the client&#39;s (e.g. ESXI host) IP address. b. If VLANs are not configured on Cohesity, then the partition hostname or VIPs will be used for Recovery. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


