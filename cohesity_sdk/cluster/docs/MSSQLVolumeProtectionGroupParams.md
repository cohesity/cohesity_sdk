# MSSQLVolumeProtectionGroupParams

Specifies the params to create a Volume based MSSQL Protection Group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[MSSQLVolumeProtectionGroupObjectParams], none_type**](MSSQLVolumeProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 
**incremental_backup_after_restart** | **bool, none_type** | Specifies whether or to perform incremental backups the first time after a server restarts. By default, a full backup will be performed. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**backup_db_volumes_only** | **bool, none_type** | Specifies whether to only backup volumes on which the specified databases reside. If not specified (default), all the volumes of the host will be protected. | [optional] 
**additional_host_params** | [**[MSSQLVolumeProtectionGroupHostParams]**](MSSQLVolumeProtectionGroupHostParams.md) | Specifies settings which are to be applied to specific host containers in this protection group. | [optional] 
**user_db_backup_preference_type** | **str, none_type** | Specifies the preference type for backing up user databases on the host. | [optional] 
**backup_system_dbs** | **bool, none_type** | Specifies whether to backup system databases. If not specified then parameter is set to true. | [optional] 
**use_aag_preferences_from_server** | **bool, none_type** | Specifies whether or not the AAG backup preferences specified on the SQL Server host should be used. | [optional] 
**aag_backup_preference_type** | **str, none_type** | Specifies the preference type for backing up databases that are part of an AAG. If not specified, then default preferences of the AAG server are applied. This field wont be applicable if user DB preference is set to skip AAG databases. | [optional] 
**full_backups_copy_only** | **bool, none_type** | Specifies whether full backups should be copy-only. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**exclude_filters** | [**[Filter], none_type**](Filter.md) | Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying the will filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters. | [optional] 
**log_backup_num_streams** | **int, none_type** | Specifies the number of streams to be used for log backups. | [optional] 
**log_backup_with_clause** | **str, none_type** | Specifies the WithClause to be used for log backups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


