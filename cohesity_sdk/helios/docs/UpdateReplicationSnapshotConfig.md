# UpdateReplicationSnapshotConfig

Specifies the params to perform actions on replication snapshots taken by a Protection Group Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_snapshot_config** | [**List[RunReplicationConfig]**](RunReplicationConfig.md) | Specifies the new configuration about adding Replication Snapshot to existing Protection Group Run. | [optional] 
**update_existing_snapshot_config** | [**List[UpdateExistingReplicationSnapshotConfig]**](UpdateExistingReplicationSnapshotConfig.md) | Specifies the configuration about updating an existing Replication Snapshot Run. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.update_replication_snapshot_config import UpdateReplicationSnapshotConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReplicationSnapshotConfig from a JSON string
update_replication_snapshot_config_instance = UpdateReplicationSnapshotConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateReplicationSnapshotConfig.to_json())

# convert the object into a dict
update_replication_snapshot_config_dict = update_replication_snapshot_config_instance.to_dict()
# create an instance of UpdateReplicationSnapshotConfig from a dict
update_replication_snapshot_config_from_dict = UpdateReplicationSnapshotConfig.from_dict(update_replication_snapshot_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


