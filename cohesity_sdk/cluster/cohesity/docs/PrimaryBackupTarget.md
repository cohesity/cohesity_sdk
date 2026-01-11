# PrimaryBackupTarget

Specifies the primary backup target settings for regular backups. If the backup target field is not specified then backup will be taken locally on the Cohesity cluster.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_settings** | [**PrimaryArchivalTarget**](PrimaryArchivalTarget.md) |  | [optional] 
**target_type** | **str, none_type** | Specifies the primary backup location where backups will be stored. If not specified, then default is assumed as local backup on Cohesity cluster. | [optional]  if omitted the server will use the default value of "Local"
**use_default_backup_target** | **bool, none_type** | Specifies if the default primary backup target must be used for backups. If this is not specified or set to false, then targets specified in &#39;archivalTargetSettings&#39; will be used for backups. If the value is specified as true, then default backup target is used internally. This field should only be set in the environment where tenant policy management is enabled and external targets are assigned to tenant when provisioning tenants. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


