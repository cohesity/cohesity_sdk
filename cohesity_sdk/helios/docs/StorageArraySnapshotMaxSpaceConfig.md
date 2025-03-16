# StorageArraySnapshotMaxSpaceConfig

Specifies max space threshold configuration that can used by snapshots to take storage snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_snapshot_space_percentage** | **int** | Specifies max space threshold can used by snapshots in percentage in volume/lun to take storage snapshot. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.storage_array_snapshot_max_space_config import StorageArraySnapshotMaxSpaceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArraySnapshotMaxSpaceConfig from a JSON string
storage_array_snapshot_max_space_config_instance = StorageArraySnapshotMaxSpaceConfig.from_json(json)
# print the JSON string representation of the object
print(StorageArraySnapshotMaxSpaceConfig.to_json())

# convert the object into a dict
storage_array_snapshot_max_space_config_dict = storage_array_snapshot_max_space_config_instance.to_dict()
# create an instance of StorageArraySnapshotMaxSpaceConfig from a dict
storage_array_snapshot_max_space_config_from_dict = StorageArraySnapshotMaxSpaceConfig.from_dict(storage_array_snapshot_max_space_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


