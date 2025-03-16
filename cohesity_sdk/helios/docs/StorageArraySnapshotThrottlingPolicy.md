# StorageArraySnapshotThrottlingPolicy

Specifies the throttling policy for individual volume/lun.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the volume ID of the Storage Snapshot Mgmt throttling Policy. | [optional] 
**max_snapshots_config_enabled** | **bool** | Specifies whether we will use storage snapshot managmement max snapshots config to all volumes/luns that are part of the registered entity. | [optional] 
**max_snapshots_mgmt_snapshot_config** | [**StorageArraySnapshotMaxSnapshotConfig**](StorageArraySnapshotMaxSnapshotConfig.md) |  | [optional] 
**max_snapshots_mgmt_space_config** | [**StorageArraySnapshotMaxSpaceConfig**](StorageArraySnapshotMaxSpaceConfig.md) |  | [optional] 
**max_space_config_enabled** | **bool** | Specifies whether we will use storage snapshot managmement max space config to all volumes/luns that are part of the registered entity. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.storage_array_snapshot_throttling_policy import StorageArraySnapshotThrottlingPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArraySnapshotThrottlingPolicy from a JSON string
storage_array_snapshot_throttling_policy_instance = StorageArraySnapshotThrottlingPolicy.from_json(json)
# print the JSON string representation of the object
print(StorageArraySnapshotThrottlingPolicy.to_json())

# convert the object into a dict
storage_array_snapshot_throttling_policy_dict = storage_array_snapshot_throttling_policy_instance.to_dict()
# create an instance of StorageArraySnapshotThrottlingPolicy from a dict
storage_array_snapshot_throttling_policy_from_dict = StorageArraySnapshotThrottlingPolicy.from_dict(storage_array_snapshot_throttling_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


