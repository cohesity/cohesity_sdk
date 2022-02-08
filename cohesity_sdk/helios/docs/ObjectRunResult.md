# ObjectRunResult

Snapshot, replication, archival results for an object.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**local_snapshot_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**original_backup_info** | [**BackupRun**](BackupRun.md) |  | [optional] 
**replication_info** | [**ReplicationRun**](ReplicationRun.md) |  | [optional] 
**archival_info** | [**ArchivalRun**](ArchivalRun.md) |  | [optional] 
**cloud_spin_info** | [**CloudSpinRun**](CloudSpinRun.md) |  | [optional] 
**on_legal_hold** | **bool, none_type** | Specifies if object&#39;s snapshot is on legal hold. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


