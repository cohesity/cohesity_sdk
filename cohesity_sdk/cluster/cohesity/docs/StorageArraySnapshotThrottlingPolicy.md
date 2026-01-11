# StorageArraySnapshotThrottlingPolicy

Specifies the throttling policy for individual volume/lun.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the volume ID of the Storage Snapshot Mgmt throttling Policy. | [optional] 
**max_snapshots_config_enabled** | **bool, none_type** | Specifies whether we will use storage snapshot managmement max snapshots config to all volumes/luns that are part of the registered entity. | [optional] 
**max_snapshots_mgmt_snapshot_config** | [**StorageArraySnapshotMaxSnapshotConfig**](StorageArraySnapshotMaxSnapshotConfig.md) |  | [optional] 
**max_snapshots_mgmt_space_config** | [**StorageArraySnapshotMaxSpaceConfig**](StorageArraySnapshotMaxSpaceConfig.md) |  | [optional] 
**max_space_config_enabled** | **bool, none_type** | Specifies whether we will use storage snapshot managmement max space config to all volumes/luns that are part of the registered entity. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


