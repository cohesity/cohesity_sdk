# RecoverOracleAppOriginalSourceConfig

Specifies the additional Source configuration parameters when databases will be recovered to original location.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_complete_recovery** | **bool, none_type** | Whether or not this is a complete recovery attempt. | [optional] 
**roll_forward_log_path_vec** | **[str], none_type** | List of archive logs to apply on Database after overwrite restore. | [optional] 
**roll_forward_time_msecs** | **int, none_type** | UTC time in msecs till which we have to roll-forward the database. | [optional] 
**db_channels** | [**[OracleDbChannel], none_type**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 
**granular_restore_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies information about list of objects (PDBs) to restore. | [optional] 
**oracle_archive_log_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies Range in Time, Scn or Sequence to restore archive logs of a DB. | [optional] 
**oracle_recovery_validation_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters related to Oracle Recovery Validation. | [optional] 
**recovery_mode** | **bool, none_type** | Specifies if database should be left in recovery mode. | [optional] 
**restore_spfile_or_pfile_info** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Specifies parameters related to spfile/pfile restore. | [optional] 
**restore_time_usecs** | **int, none_type** | Specifies the time in the past to which the Oracle db needs to be restored. This allows for granular recovery of Oracle databases. If this is not set, the Oracle db will be restored from the full/incremental snapshot. | [optional] 
**shell_evironment_vars** | [**[ShellKeyValuePair], none_type**](ShellKeyValuePair.md) | Specifies key value pairs of shell variables which defines the restore shell environment. | [optional] 
**use_scn_for_restore** | **bool, none_type** | Specifies whether database recovery performed should use scn value or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


