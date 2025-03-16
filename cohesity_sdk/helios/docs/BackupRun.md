# BackupRun

Specifies information about backup run for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_attempts** | [**List[BackupAttempt]**](BackupAttempt.md) | Failed backup attempts for an object. | [optional] 
**snapshot_info** | [**SnapshotInfo**](SnapshotInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.backup_run import BackupRun

# TODO update the JSON string below
json = "{}"
# create an instance of BackupRun from a JSON string
backup_run_instance = BackupRun.from_json(json)
# print the JSON string representation of the object
print(BackupRun.to_json())

# convert the object into a dict
backup_run_dict = backup_run_instance.to_dict()
# create an instance of BackupRun from a dict
backup_run_from_dict = BackupRun.from_dict(backup_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


