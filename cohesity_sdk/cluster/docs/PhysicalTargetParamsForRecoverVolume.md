# PhysicalTargetParamsForRecoverVolume

Specifies the parameters for a physical recovery target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mount_target** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**volume_mapping** | [**[RecoverVolumeMapping], none_type**](RecoverVolumeMapping.md) | Specifies the mapping from source volumes to destination volumes. | 
**force_unmount_volume** | **bool, none_type** | Specifies whether volume would be dismounted first during LockVolume failure. If not specified, default is false. | [optional] 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


