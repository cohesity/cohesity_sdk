# UpdateExistingReplicationSnapshotConfig

Specifies the configuration about updating an existing Replication Snapshot Run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_lock** | **str** | Specifies WORM retention type for the snapshots. When a WORM retention type is specified, the snapshots of the Protection Groups using this policy will be kept until the maximum of the snapshot retention time. During that time, the snapshots cannot be deleted. &lt;br&gt;&#39;Compliance&#39; implies WORM retention is set for compliance reason. &lt;br&gt;&#39;Administrative&#39; implies WORM retention is set for administrative purposes. | [optional] 
**days_to_keep** | **int** | Specifies number of days to retain the snapshots. If positive, then this value is added to exisiting expiry time thereby increasing  the retention period of the snapshot. Conversly, if this value is negative, then value is subtracted to existing expiry time thereby decreasing the retention period of the snaphot. Here, by this operation if expiry time goes below current time then snapshot is immediately deleted. | [optional] 
**delete_snapshot** | **bool** | Specifies whether to delete the snapshot. When this is set to true, all other params will be ignored. | [optional] 
**enable_legal_hold** | **bool** | Specifies whether to retain the snapshot for legal purpose. If set to true, the snapshots cannot be deleted until the retention period. Note that using this option may cause the Cluster to run out of space. If set to false explicitly, the hold is removed, and the snapshots will expire as specified in the policy of the Protection Group. If this field is not specified, there is no change to the hold of the run. This field can be set only by a User having Data Security Role. | [optional] 
**id** | **int** | Specifies the cluster id of the replication cluster. | 
**name** | **str** | Specifies the cluster name of the replication cluster. | [optional] 
**resync** | **bool** | Specifies whether to retry the replication operation in case if earlier attempt failed. If not specified or set to false, replication is not retried. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.update_existing_replication_snapshot_config import UpdateExistingReplicationSnapshotConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExistingReplicationSnapshotConfig from a JSON string
update_existing_replication_snapshot_config_instance = UpdateExistingReplicationSnapshotConfig.from_json(json)
# print the JSON string representation of the object
print(UpdateExistingReplicationSnapshotConfig.to_json())

# convert the object into a dict
update_existing_replication_snapshot_config_dict = update_existing_replication_snapshot_config_instance.to_dict()
# create an instance of UpdateExistingReplicationSnapshotConfig from a dict
update_existing_replication_snapshot_config_from_dict = UpdateExistingReplicationSnapshotConfig.from_dict(update_existing_replication_snapshot_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


