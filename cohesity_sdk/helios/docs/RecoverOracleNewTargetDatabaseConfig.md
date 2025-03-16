# RecoverOracleNewTargetDatabaseConfig

Specifies recovery parameters when recovering to a database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bct_file_path** | **str** | Specifies BCT file path. | [optional] 
**database_name** | **str** | Specifies a new name for the restored database. If this field is not specified, then the original database will be overwritten after recovery. | [optional] 
**db_config_file_path** | **str** | Specifies the config file path on selected host which configures the restored database. | [optional] 
**db_files_destination** | **str** | Specifies the location to restore database files. | [optional] 
**disaster_recovery_options** | [**DisasterRecoveryOptions**](DisasterRecoveryOptions.md) |  | [optional] 
**enable_archive_log_mode** | **bool** | Specifies archive log mode for oracle restore. | [optional] 
**is_multi_stage_restore** | **bool** | Specifies whether this task is a multistage restore task. If set, we migrate the DB after clone completes. | [optional] 
**new_name_clause** | **str** | Specifies newname clause for db files which allows user to have full control on how their database files can be renamed during the oracle alternate restore workflow. | [optional] 
**no_filename_check** | **bool** | Specifies whether to validate filenames or not in Oracle alternate restore workflow. | [optional] 
**num_tempfiles** | **int** | Specifies no. of tempfiles to be used for the recovered database. | [optional] 
**oracle_base_folder** | **str** | Specifies the oracle base folder at selected host. | [optional] 
**oracle_home_folder** | **str** | Specifies the oracle home folder at selected host. | [optional] 
**oracle_update_restore_options** | [**MigrateCloneParams**](MigrateCloneParams.md) | Specifies the parameters that are needed for updating oracle restore options. | [optional] 
**pfile_parameter_map** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies a key value pair for pfile parameters. | [optional] 
**redo_log_config** | [**RedoLogGroupConfig**](RedoLogGroupConfig.md) | Specifies redo log config. | [optional] 
**restore_to_rac** | **bool** | Whether or not to restore to a RAC database. | [optional] 
**skip_clone_nid** | **bool** | Whether or not to skip the nid step in Oracle Clone workflow. Applicable to both smart and old clone workflow. | [optional] 
**db_channels** | [**List[OracleDbChannel]**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 
**granular_restore_info** | [**RecoverOracleGranularRestoreInfo**](RecoverOracleGranularRestoreInfo.md) | Specifies information about list of objects (PDBs) to restore. | [optional] 
**oracle_archive_log_info** | [**OracleArchiveLogInfo**](OracleArchiveLogInfo.md) | Specifies Range in Time, Scn or Sequence to restore archive logs of a DB. | [optional] 
**oracle_recovery_validation_info** | [**OracleRecoveryValidationInfo**](OracleRecoveryValidationInfo.md) | Specifies parameters related to Oracle Recovery Validation. | [optional] 
**recovery_mode** | **bool** | Specifies if database should be left in recovery mode. | [optional] 
**restore_spfile_or_pfile_info** | [**RestoreSpfileOrPfileInfo**](RestoreSpfileOrPfileInfo.md) | Specifies parameters related to spfile/pfile restore. | [optional] 
**restore_time_usecs** | **int** | Specifies the time in the past to which the Oracle db needs to be restored. This allows for granular recovery of Oracle databases. If this is not set, the Oracle db will be restored from the full/incremental snapshot. | [optional] 
**shell_evironment_vars** | [**List[ShellKeyValuePair]**](ShellKeyValuePair.md) | Specifies key value pairs of shell variables which defines the restore shell environment. | [optional] 
**use_scn_for_restore** | **bool** | Specifies whether database recovery performed should use scn value or not. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_oracle_new_target_database_config import RecoverOracleNewTargetDatabaseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleNewTargetDatabaseConfig from a JSON string
recover_oracle_new_target_database_config_instance = RecoverOracleNewTargetDatabaseConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleNewTargetDatabaseConfig.to_json())

# convert the object into a dict
recover_oracle_new_target_database_config_dict = recover_oracle_new_target_database_config_instance.to_dict()
# create an instance of RecoverOracleNewTargetDatabaseConfig from a dict
recover_oracle_new_target_database_config_from_dict = RecoverOracleNewTargetDatabaseConfig.from_dict(recover_oracle_new_target_database_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


