# RecoverAwsRDSOracleNewSourceConfig

Specifies the new destination Source configuration where the Oracle instances will be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bct_file_path** | **str** | Specifies BCT file path. | [optional] 
**database_name** | **str** | Specifies a new name for the restored database. If this field is not specified, then the original database will be overwritten after recovery. | 
**db_files_destination** | **str** | Specifies the location to restore database files. | 
**enable_archive_log_mode** | **bool** | Specifies archive log mode for oracle restore. | [optional] 
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**no_filename_check** | **bool** | Specifies whether to validate filenames or not in Oracle alternate restore workflow. | [optional] 
**num_tempfiles** | **int** | Specifies no. of tempfiles to be used for the recovered database. | [optional] 
**oracle_base_folder** | **str** | Specifies the oracle base folder at selected host. | 
**oracle_home_folder** | **str** | Specifies the oracle home folder at selected host. | 
**pfile_parameter_map** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies a key value pair for pfile parameters. | 
**recovery_mode** | **bool** | Specifies if database should be left in recovery mode. | [optional] 
**redo_log_config** | [**RedoLogGroupConfig**](RedoLogGroupConfig.md) |  | [optional] 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 

## Example

```python
from cohesity_sdk.cluster.models.recover_aws_rds_oracle_new_source_config import RecoverAwsRDSOracleNewSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverAwsRDSOracleNewSourceConfig from a JSON string
recover_aws_rds_oracle_new_source_config_instance = RecoverAwsRDSOracleNewSourceConfig.from_json(json)
# print the JSON string representation of the object
print(RecoverAwsRDSOracleNewSourceConfig.to_json())

# convert the object into a dict
recover_aws_rds_oracle_new_source_config_dict = recover_aws_rds_oracle_new_source_config_instance.to_dict()
# create an instance of RecoverAwsRDSOracleNewSourceConfig from a dict
recover_aws_rds_oracle_new_source_config_from_dict = RecoverAwsRDSOracleNewSourceConfig.from_dict(recover_aws_rds_oracle_new_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


