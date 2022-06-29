# CommonOracleAppSourceConfig

Specifies a common parameters used when restoring back to original or new source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**restore_time_usecs** | **int, none_type** | Specifies the time in the past to which the Oracle db needs to be restored. This allows for granular recovery of Oracle databases. If this is not set, the Oracle db will be restored from the full/incremental snapshot. | [optional] 
**db_channels** | [**[OracleDbChannel], none_type**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 
**recovery_mode** | **bool, none_type** | Specifies if database should be left in recovery mode. | [optional] 
**shell_evironment_vars** | [**[ShellKeyValuePair], none_type**](ShellKeyValuePair.md) | Specifies key value pairs of shell variables which defines the restore shell environment. | [optional] 
**granular_restore_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies information about list of objects (PDBs) to restore. | [optional] 
**oracle_archive_log_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies Range in Time, Scn or Sequence to restore archive logs of a DB. | [optional] 
**oracle_recovery_validation_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters related to Oracle Recovery Validation. | [optional] 
**restore_spfile_or_pfile_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters related to spfile/pfile restore. | [optional] 
**use_scn_for_restore** | **bool, none_type** | Specifies whether database recovery performed should use scn value or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

