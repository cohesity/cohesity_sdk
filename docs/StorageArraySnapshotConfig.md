# StorageArraySnapshotConfig

Specifies the storage array snapshot config for individual volume/lun.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_snapshot_config** | [**StorageArraySnapshotMaxSnapshotConfig**](StorageArraySnapshotMaxSnapshotConfig.md) |  | [optional] 
**max_snapshots_config_enabled** | **bool** | Specifies whether we will use storage snapshot managmement max snapshots config to all volumes/luns that are part of the registered entity. | [optional] 
**max_space_config** | [**StorageArraySnapshotMaxSpaceConfig**](StorageArraySnapshotMaxSpaceConfig.md) |  | [optional] 
**max_space_config_enabled** | **bool** | Specifies whether we will use storage snapshot managmement max space config to all volumes/luns that are part of the registered entity. | [optional] 
**storage_array_snapshot_throttling_policies** | [**List[StorageArraySnapshotThrottlingPolicy]**](StorageArraySnapshotThrottlingPolicy.md) | Specifies the list of storage array snapshot management throttling policies for individual volume/lun. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.storage_array_snapshot_config import StorageArraySnapshotConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArraySnapshotConfig from a JSON string
storage_array_snapshot_config_instance = StorageArraySnapshotConfig.from_json(json)
# print the JSON string representation of the object
print(StorageArraySnapshotConfig.to_json())

# convert the object into a dict
storage_array_snapshot_config_dict = storage_array_snapshot_config_instance.to_dict()
# create an instance of StorageArraySnapshotConfig from a dict
storage_array_snapshot_config_from_dict = StorageArraySnapshotConfig.from_dict(storage_array_snapshot_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


