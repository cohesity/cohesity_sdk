# StorageArraySnapshotMaxSnapshotConfig

Specifies max snapshots threshold configuration that can used by snapshots to take storage snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_snapshots** | **int** | Specifies max number of storage snapshots allowed per volume/lun. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.storage_array_snapshot_max_snapshot_config import StorageArraySnapshotMaxSnapshotConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArraySnapshotMaxSnapshotConfig from a JSON string
storage_array_snapshot_max_snapshot_config_instance = StorageArraySnapshotMaxSnapshotConfig.from_json(json)
# print the JSON string representation of the object
print(StorageArraySnapshotMaxSnapshotConfig.to_json())

# convert the object into a dict
storage_array_snapshot_max_snapshot_config_dict = storage_array_snapshot_max_snapshot_config_instance.to_dict()
# create an instance of StorageArraySnapshotMaxSnapshotConfig from a dict
storage_array_snapshot_max_snapshot_config_from_dict = StorageArraySnapshotMaxSnapshotConfig.from_dict(storage_array_snapshot_max_snapshot_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


