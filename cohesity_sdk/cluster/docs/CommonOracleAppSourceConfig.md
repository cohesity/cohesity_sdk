# CommonOracleAppSourceConfig

Specifies a common parameters used when restoring back to original or new source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_channels** | [**[OracleDbChannel], none_type**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 
**granular_restore_info** | [**RecoverOracleGranularRestoreInfo**](RecoverOracleGranularRestoreInfo.md) |  | [optional] 
**oracle_archive_log_info** | [**OracleArchiveLogInfo**](OracleArchiveLogInfo.md) |  | [optional] 
**oracle_recovery_validation_info** | [**OracleRecoveryValidationInfo**](OracleRecoveryValidationInfo.md) |  | [optional] 
**recovery_mode** | **bool, none_type** | Specifies if database should be left in recovery mode. | [optional] 
**restore_spfile_or_pfile_info** | [**RestoreSpfileOrPfileInfo**](RestoreSpfileOrPfileInfo.md) |  | [optional] 
**restore_time_usecs** | **int, none_type** | Specifies the time in the past to which the Oracle db needs to be restored. This allows for granular recovery of Oracle databases. If this is not set, the Oracle db will be restored from the full/incremental snapshot. | [optional] 
**shell_evironment_vars** | [**[ShellKeyValuePair], none_type**](ShellKeyValuePair.md) | Specifies key value pairs of shell variables which defines the restore shell environment. | [optional] 
**use_scn_for_restore** | **bool, none_type** | Specifies whether database recovery performed should use scn value or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


