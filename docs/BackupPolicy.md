# BackupPolicy

Specifies the backup schedule and retentions of a Protection Policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bmr** | [**BmrBackupPolicy**](BmrBackupPolicy.md) |  | [optional] 
**cdp** | [**CdpBackupPolicy**](CdpBackupPolicy.md) |  | [optional] 
**log** | [**LogBackupPolicy**](LogBackupPolicy.md) |  | [optional] 
**regular** | [**RegularBackupPolicy**](RegularBackupPolicy.md) |  | 
**run_timeouts** | [**List[CancellationTimeoutParams]**](CancellationTimeoutParams.md) | Specifies the backup timeouts for different type of runs(kFull, kRegular etc.). | [optional] 
**storage_array_snapshot** | [**StorageArraySnapshotBackupPolicy**](StorageArraySnapshotBackupPolicy.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.backup_policy import BackupPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of BackupPolicy from a JSON string
backup_policy_instance = BackupPolicy.from_json(json)
# print the JSON string representation of the object
print(BackupPolicy.to_json())

# convert the object into a dict
backup_policy_dict = backup_policy_instance.to_dict()
# create an instance of BackupPolicy from a dict
backup_policy_from_dict = BackupPolicy.from_dict(backup_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


