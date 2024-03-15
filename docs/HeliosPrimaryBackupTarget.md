# HeliosPrimaryBackupTarget

Specifies the primary backup target settings for regular backups. If the backup target field is not specified then backup will be taken locally on the Cohesity cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_settings** | [**PrimaryArchivalTarget**](PrimaryArchivalTarget.md) |  | [optional] 
**target_type** | **str, none_type** | Specifies the primary backup location where backups will be stored. If not specified, then default is assumed as local backup on Cohesity cluster. | [optional]  if omitted the server will use the default value of "Local"

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


