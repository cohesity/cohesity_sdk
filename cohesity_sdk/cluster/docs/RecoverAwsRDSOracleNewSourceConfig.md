# RecoverAwsRDSOracleNewSourceConfig

Specifies the new destination Source configuration where the Oracle instances will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_name** | **str** | Specifies a new name for the restored database. If this field is not specified, then the original database will be overwritten after recovery. | 
**db_files_destination** | **str** | Specifies the location to restore database files. | 
**instance** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**oracle_base_folder** | **str** | Specifies the oracle base folder at selected host. | 
**oracle_home_folder** | **str** | Specifies the oracle home folder at selected host. | 
**pfile_parameter_map** | [**[KeyValuePair], none_type**](KeyValuePair.md) | Specifies a key value pair for pfile parameters. | 
**source** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**bct_file_path** | **str, none_type** | Specifies BCT file path. | [optional] 
**enable_archive_log_mode** | **bool, none_type** | Specifies archive log mode for oracle restore. | [optional] 
**no_filename_check** | **bool, none_type** | Specifies whether to validate filenames or not in Oracle alternate restore workflow. | [optional] 
**num_tempfiles** | **int, none_type** | Specifies no. of tempfiles to be used for the recovered database. | [optional] 
**recovery_mode** | **bool, none_type** | Specifies if database should be left in recovery mode. | [optional] 
**redo_log_config** | [**RedoLogGroupConfig**](RedoLogGroupConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


