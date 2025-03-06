# CommonOracleAppSourceConfig

Specifies a common parameters used when restoring back to original or new source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_channels** | [**List[OracleDbChannel]**](OracleDbChannel.md) | Specifies the Oracle database node channels info. If not specified, the default values assigned by the server are applied to all the databases. | [optional] 
**granular_restore_info** | [**RecoverOracleGranularRestoreInfo**](RecoverOracleGranularRestoreInfo.md) |  | [optional] 
**oracle_archive_log_info** | [**OracleArchiveLogInfo**](OracleArchiveLogInfo.md) |  | [optional] 
**oracle_recovery_validation_info** | [**OracleRecoveryValidationInfo**](OracleRecoveryValidationInfo.md) |  | [optional] 
**recovery_mode** | **bool** | Specifies if database should be left in recovery mode. | [optional] 
**restore_spfile_or_pfile_info** | [**RestoreSpfileOrPfileInfo**](RestoreSpfileOrPfileInfo.md) |  | [optional] 
**restore_time_usecs** | **int** | Specifies the time in the past to which the Oracle db needs to be restored. This allows for granular recovery of Oracle databases. If this is not set, the Oracle db will be restored from the full/incremental snapshot. | [optional] 
**shell_evironment_vars** | [**List[ShellKeyValuePair]**](ShellKeyValuePair.md) | Specifies key value pairs of shell variables which defines the restore shell environment. | [optional] 
**use_scn_for_restore** | **bool** | Specifies whether database recovery performed should use scn value or not. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_oracle_app_source_config import CommonOracleAppSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CommonOracleAppSourceConfig from a JSON string
common_oracle_app_source_config_instance = CommonOracleAppSourceConfig.from_json(json)
# print the JSON string representation of the object
print(CommonOracleAppSourceConfig.to_json())

# convert the object into a dict
common_oracle_app_source_config_dict = common_oracle_app_source_config_instance.to_dict()
# create an instance of CommonOracleAppSourceConfig from a dict
common_oracle_app_source_config_from_dict = CommonOracleAppSourceConfig.from_dict(common_oracle_app_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


