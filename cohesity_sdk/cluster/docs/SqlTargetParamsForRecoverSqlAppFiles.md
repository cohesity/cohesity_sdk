# SqlTargetParamsForRecoverSqlAppFiles

Specifies the target params for recovering to a SQL database as files.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat_file_directory_location** | **str, none_type** | Specifies the directory where to put the database data files. Missing directory will be automatically created. | 
**host** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**overwrite_existing_files** | **bool, none_type** | Specifies the flag to overwrite existing files at destination. By default files will not be overwritten. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


