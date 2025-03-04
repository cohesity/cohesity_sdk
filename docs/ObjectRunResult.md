# ObjectRunResult

Snapshot, replication, archival results for an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_info** | [**ArchivalRun**](ArchivalRun.md) |  | [optional] 
**cloud_spin_info** | [**CloudSpinRun**](CloudSpinRun.md) |  | [optional] 
**local_snapshot_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**object** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**on_legal_hold** | **bool** | Specifies if object&#39;s snapshot is on legal hold. | [optional] 
**original_backup_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**replication_info** | [**ReplicationRun**](ReplicationRun.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.object_run_result import ObjectRunResult

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectRunResult from a JSON string
object_run_result_instance = ObjectRunResult.from_json(json)
# print the JSON string representation of the object
print(ObjectRunResult.to_json())

# convert the object into a dict
object_run_result_dict = object_run_result_instance.to_dict()
# create an instance of ObjectRunResult from a dict
object_run_result_from_dict = ObjectRunResult.from_dict(object_run_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


