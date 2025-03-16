# RecoverOracleAppOriginalSourceConfig

Specifies the additional Source configuration parameters when databases will be recovered to original location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attempt_complete_recovery** | **bool** | Whether or not this is a complete recovery attempt. | [optional] 
**roll_forward_log_path_vec** | **List[str]** | List of archive logs to apply on Database after overwrite restore. | [optional] 
**roll_forward_time_msecs** | **int** | UTC time in msecs till which we have to roll-forward the database. | [optional] 
**stop_active_passive** | **bool** | Specifies whether allowed to automatically stop active passive resource. | [optional] 
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
from cohesity_sdk.helios.models.recover_oracle_app_original_source_config import RecoverOracleAppOriginalSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleAppOriginalSourceConfig from a JSON string
recover_oracle_app_original_source_config_instance = RecoverOracleAppOriginalSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleAppOriginalSourceConfig.to_json())

# convert the object into a dict
recover_oracle_app_original_source_config_dict = recover_oracle_app_original_source_config_instance.to_dict()
# create an instance of RecoverOracleAppOriginalSourceConfig from a dict
recover_oracle_app_original_source_config_from_dict = RecoverOracleAppOriginalSourceConfig.from_dict(recover_oracle_app_original_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


