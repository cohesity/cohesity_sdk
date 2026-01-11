# HostBasedBackupScriptParams

Specifies params of a pre/post scripts to be executed before and after a backup run.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ScriptHost**](ScriptHost.md) |  | 
**post_backup_script** | [**CommonPrePostScriptParams**](CommonPrePostScriptParams.md) |  | [optional] 
**post_script** | [**CommonPrePostScriptParams**](CommonPrePostScriptParams.md) |  | [optional] 
**post_snapshot_script** | [**CommonPrePostScriptParams**](CommonPrePostScriptParams.md) |  | [optional] 
**pre_script** | [**CommonPreBackupScriptParams**](CommonPreBackupScriptParams.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


