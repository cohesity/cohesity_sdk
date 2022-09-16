# OracleCloneTask

Specifies the information about an Oracle clone task.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str, none_type** | Specifies the name of the cloned database. | 
**home_folder** | **str, none_type** | Specifies the home folder for the cloned database. | 
**base_folder** | **str, none_type** | Specifies the base folder of Oracle installation on the target host. | 
**pre_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**post_script** | [**CommonPostBackupScriptParams**](CommonPostBackupScriptParams.md) |  | [optional] 
**sga** | **str, none_type** | Specifies the System Global Area (SGA) for the clone database. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


