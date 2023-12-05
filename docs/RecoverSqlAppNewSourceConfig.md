# RecoverSqlAppNewSourceConfig

Specifies the new destination Source configuration where the databases will be recovered.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_file_directory_location** | **str, none_type** | Specifies the directory where to put the database data files. Missing directory will be automatically created. | [optional] 
**database_name** | **str, none_type** | Specifies a new name for the restored database. If this field is not specified, then the original database will be overwritten after recovery. | [optional] 
**host** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Specifies the source id of target host where databases will be recovered. This source id can be a physical host or virtual machine. | [optional] 
**instance_name** | **str, none_type** | Specifies an instance name of the Sql Server that should be used for restoring databases to. | [optional] 
**log_file_directory_location** | **str, none_type** | Specifies the directory where to put the database log files. Missing directory will be automatically created. | [optional] 
**keep_cdc** | **bool, none_type** | Specifies whether to keep CDC (Change Data Capture) on recovered databases or not. If not passed, this is assumed to be true. If withNoRecovery is passed as true, then this field must not be set to true. Passing this field as true in this scenario will be a invalid request. | [optional] 
**multi_stage_restore_options** | [**MultiStageRestoreOptions**](MultiStageRestoreOptions.md) |  | [optional] 
**native_recovery_with_clause** | **str, none_type** | &#39;with_clause&#39; contains &#39;with clause&#39; to be used in native sql restore command. This is only applicable for database restore of native sql backup. Here user can specify multiple restore options. Example: &#39;WITH BUFFERCOUNT &#x3D; 575, MAXTRANSFERSIZE &#x3D; 2097152&#39;. | [optional] 
**overwriting_policy** | **str, none_type** | Specifies a policy to be used while recovering existing databases. | [optional] 
**restore_time_usecs** | **int, none_type** | Specifies the time in the past to which the Sql database needs to be restored. This allows for granular recovery of Sql databases. If this is not set, the Sql database will be restored from the full/incremental snapshot. | [optional] 
**secondary_data_files_dir_list** | [**[FilenamePatternToDirectory], none_type**](FilenamePatternToDirectory.md) | Specifies the secondary data filename pattern and corresponding direcories of the DB. Secondary data files are optional and are user defined. The recommended file extention for secondary files is \&quot;.ndf\&quot;. If this option is specified and the destination folders do not exist they will be automatically created. | [optional] 
**with_no_recovery** | **bool, none_type** | Specifies the flag to bring DBs online or not after successful recovery. If this is passed as true, then it means DBs won&#39;t be brought online. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


