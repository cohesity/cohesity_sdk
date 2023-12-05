# RemoteAdapterHost

Specifies params of the remote host.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_type** | **str, none_type** | Specifies the Operating system type of the host. | [optional] 
**hostname** | **str, none_type** | Specifies the Hostname or IP address of the host where the pre and post script will be run. | [optional] 
**username** | **str, none_type** | Specifies the username for the host. | [optional] 
**full_backup_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**incremental_backup_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**log_backup_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


