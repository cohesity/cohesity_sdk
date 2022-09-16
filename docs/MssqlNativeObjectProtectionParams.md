# MssqlNativeObjectProtectionParams

Specifies the params to create a Native based MSSQL Object Protection.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**[MssqlNativeObjectProtection], none_type**](MssqlNativeObjectProtection.md) | Specifies the list of objects to be protected. | 
**num_streams** | **int, none_type** | Specifies the number of streams to be used. | [optional] 
**with_clause** | **str, none_type** | Specifies the WithClause to be used. | [optional] 
**user_db_backup_preference_type** | **str, none_type** | Specifies the preference type for backing up user databases on the host. | [optional] 
**backup_system_dbs** | **bool, none_type** | Specifies whether to backup system databases. If not specified then parameter is set to true. | [optional] 
**use_aag_preferences_from_server** | **bool, none_type** | Specifies whether or not the AAG backup preferences specified on the SQL Server host should be used. | [optional] 
**aag_backup_preference_type** | **str, none_type** | Specifies the preference type for backing up databases that are part of an AAG. If not specified, then default preferences of the AAG server are applied. This field wont be applicable if user DB preference is set to skip AAG databases. | [optional] 
**full_backups_copy_only** | **bool, none_type** | Specifies whether full backups should be copy-only. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**exclude_filters** | [**[Filter], none_type**](Filter.md) | Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying the will filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


