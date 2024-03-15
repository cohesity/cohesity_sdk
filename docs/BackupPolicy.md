# BackupPolicy

Specifies the backup schedule and retentions of a Protection Policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regular** | [**RegularBackupPolicy**](RegularBackupPolicy.md) |  | 
**bmr** | [**BmrBackupPolicy**](BmrBackupPolicy.md) |  | [optional] 
**cdp** | [**CdpBackupPolicy**](CdpBackupPolicy.md) |  | [optional] 
**log** | [**LogBackupPolicy**](LogBackupPolicy.md) |  | [optional] 
**run_timeouts** | [**[CancellationTimeoutParams], none_type**](CancellationTimeoutParams.md) | Specifies the backup timeouts for different type of runs(kFull, kRegular etc.). | [optional] 
**storage_array_snapshot** | [**StorageArraySnapshotBackupPolicy**](StorageArraySnapshotBackupPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


