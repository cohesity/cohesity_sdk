# ConstructRestoreMetaInfoOracleParams

Params to fetch oracle restore meta info

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_dir** | **str, none_type** | Specifies the base directory of Oracle at destination. | 
**home_dir** | **str, none_type** | Specifies the home directory of Oracle at destination. | 
**is_clone** | **bool, none_type** | Specifies whether operation is clone or not | 
**db_name** | **str, none_type** | Specifies the name of the Oracle database that we restore to. | [optional] 
**db_file_destination** | **str, none_type** | Specifies the location to put the database files(datafiles, logfiles etc.) | [optional] 
**is_granular_restore** | **bool, none_type** | Specifies whether the operation is granular restore or not. | [optional] 
**is_recovery_validation** | **bool, none_type** | Specifies whether the operation is recovery validation or not. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


