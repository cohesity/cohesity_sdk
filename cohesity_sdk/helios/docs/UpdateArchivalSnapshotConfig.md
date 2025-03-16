# UpdateArchivalSnapshotConfig

Specifies the params to perform actions on archival snapshots taken by a Protection Group Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_snapshot_config** | [**List[RunArchivalConfig]**](RunArchivalConfig.md) | Specifies the new configuration about adding Archival Snapshot to existing Protection Group Run. | [optional] 
**update_existing_snapshot_config** | [**List[UpdateExistingArchivalSnapshotConfig]**](UpdateExistingArchivalSnapshotConfig.md) | Specifies the configuration about updating an existing Archival Snapshot Run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_archival_snapshot_config import UpdateArchivalSnapshotConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateArchivalSnapshotConfig from a JSON string
update_archival_snapshot_config_instance = UpdateArchivalSnapshotConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateArchivalSnapshotConfig.to_json())

# convert the object into a dict
update_archival_snapshot_config_dict = update_archival_snapshot_config_instance.to_dict()
# create an instance of UpdateArchivalSnapshotConfig from a dict
update_archival_snapshot_config_from_dict = UpdateArchivalSnapshotConfig.from_dict(update_archival_snapshot_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


