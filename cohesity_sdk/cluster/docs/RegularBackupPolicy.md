# RegularBackupPolicy

Specifies the Incremental and Full policy settings and also the common Retention policy settings.\"

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full** | [**FullBackupPolicy**](FullBackupPolicy.md) |  | [optional] 
**full_backups** | [**[FullScheduleAndRetention]**](FullScheduleAndRetention.md) | Specifies multiple schedules and retentions for full backup. Specify either of the &#39;full&#39; or &#39;fullBackups&#39; values. Its recommended to use &#39;fullBaackups&#39; value since &#39;full&#39; will be deprecated after few releases. | [optional] 
**incremental** | [**IncrementalBackupPolicy**](IncrementalBackupPolicy.md) |  | [optional] 
**primary_backup_target** | [**PrimaryBackupTarget**](PrimaryBackupTarget.md) |  | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


