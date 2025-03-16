# StorageArraySnapshotBackupPolicy

Specifies storage snapshot managment backup settings for a Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retention** | [**Retention**](Retention.md) |  | 
**schedule** | [**StorageArraySnapshotSchedule**](StorageArraySnapshotSchedule.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.storage_array_snapshot_backup_policy import StorageArraySnapshotBackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of StorageArraySnapshotBackupPolicy from a JSON string
storage_array_snapshot_backup_policy_instance = StorageArraySnapshotBackupPolicy.from_json(json)
# print the JSON string representation of the object
print(StorageArraySnapshotBackupPolicy.to_json())

# convert the object into a dict
storage_array_snapshot_backup_policy_dict = storage_array_snapshot_backup_policy_instance.to_dict()
# create an instance of StorageArraySnapshotBackupPolicy from a dict
storage_array_snapshot_backup_policy_from_dict = StorageArraySnapshotBackupPolicy.from_dict(storage_array_snapshot_backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


