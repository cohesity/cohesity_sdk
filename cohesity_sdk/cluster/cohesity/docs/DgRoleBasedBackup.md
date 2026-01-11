# DgRoleBasedBackup

Control the Oracle Data Guard role based backup.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_backup_archivelog_on_any_role** | **bool, none_type** | Specifies if the archive log backup is allowed on all the roles. | [optional]  if omitted the server will use the default value of False
**backup_on_dg_role** | **str** | Specifies the Data Guard role for which backup is allowed. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


