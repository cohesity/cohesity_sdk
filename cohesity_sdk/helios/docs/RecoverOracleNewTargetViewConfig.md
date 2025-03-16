# RecoverOracleNewTargetViewConfig

Specifies recovery parameters when recovering to a view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**view_mount_path** | **str** | Specifies the directory where cohesity view for app recovery will be mounted. | [optional] 
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
from cohesity_sdk.helios.models.recover_oracle_new_target_view_config import RecoverOracleNewTargetViewConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverOracleNewTargetViewConfig from a JSON string
recover_oracle_new_target_view_config_instance = RecoverOracleNewTargetViewConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverOracleNewTargetViewConfig.to_json())

# convert the object into a dict
recover_oracle_new_target_view_config_dict = recover_oracle_new_target_view_config_instance.to_dict()
# create an instance of RecoverOracleNewTargetViewConfig from a dict
recover_oracle_new_target_view_config_from_dict = RecoverOracleNewTargetViewConfig.from_dict(recover_oracle_new_target_view_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


