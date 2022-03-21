# StorageArraySnapshotConfig

Specifies the storage array snapshot config for individual volume/lun.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_snapshots_config_enabled** | **bool, none_type** | Specifies whether we will use storage snapshot managmement max snapshots config to all volumes/luns that are part of the registered entity. | [optional] 
**max_space_config_enabled** | **bool, none_type** | Specifies whether we will use storage snapshot managmement max space config to all volumes/luns that are part of the registered entity. | [optional] 
**max_space_config** | [**StorageArraySnapshotMaxSpaceConfig**](StorageArraySnapshotMaxSpaceConfig.md) |  | [optional] 
**max_snapshot_config** | [**StorageArraySnapshotMaxSnapshotConfig**](StorageArraySnapshotMaxSnapshotConfig.md) |  | [optional] 
**storage_array_snapshot_throttling_policies** | [**[StorageArraySnapshotThrottlingPolicy], none_type**](StorageArraySnapshotThrottlingPolicy.md) | Specifies the list of storage array snapshot management throttling policies for individual volume/lun. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


