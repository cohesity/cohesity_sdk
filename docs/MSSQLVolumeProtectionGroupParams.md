# MSSQLVolumeProtectionGroupParams

Specifies the params to create a Volume based MSSQL Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aag_backup_preference_type** | **str** | Specifies the preference type for backing up databases that are part of an AAG. If not specified, then default preferences of the AAG server are applied. This field wont be applicable if user DB preference is set to skip AAG databases. | [optional] 
**advanced_settings** | [**AdvancedSettings**](AdvancedSettings.md) |  | [optional] 
**backup_system_dbs** | **bool** | Specifies whether to backup system databases. If not specified then parameter is set to true. | [optional] 
**exclude_filters** | [**List[Filter]**](Filter.md) | Specifies the list of exclusion filters applied during the group creation or edit. These exclusion filters can be wildcard supported strings or regular expressions. Objects satisfying the will filters will be excluded during backup and also auto protected objects will be ignored if filtered by any of the filters. | [optional] 
**full_backups_copy_only** | **bool** | Specifies whether full backups should be copy-only. | [optional] 
**log_backup_num_streams** | **int** | Specifies the number of streams to be used for log backups. | [optional] 
**log_backup_with_clause** | **str** | Specifies the WithClause to be used for log backups. | [optional] 
**pre_post_script** | [**PrePostScriptParams**](PrePostScriptParams.md) |  | [optional] 
**use_aag_preferences_from_server** | **bool** | Specifies whether or not the AAG backup preferences specified on the SQL Server host should be used. | [optional] 
**user_db_backup_preference_type** | **str** | Specifies the preference type for backing up user databases on the host. | [optional] 
**additional_host_params** | [**List[MSSQLVolumeProtectionGroupHostParams]**](MSSQLVolumeProtectionGroupHostParams.md) | Specifies settings which are to be applied to specific host containers in this protection group. | [optional] 
**backup_db_volumes_only** | **bool** | Specifies whether to only backup volumes on which the specified databases reside. If not specified (default), all the volumes of the host will be protected. | [optional] 
**incremental_backup_after_restart** | **bool** | Specifies whether or to perform incremental backups the first time after a server restarts. By default, a full backup will be performed. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[MSSQLVolumeProtectionGroupObjectParams]**](MSSQLVolumeProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 

## Example

```python
from cohesity_sdk.models.mssql_volume_protection_group_params import MSSQLVolumeProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of MSSQLVolumeProtectionGroupParams from a JSON string
mssql_volume_protection_group_params_instance = MSSQLVolumeProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(MSSQLVolumeProtectionGroupParams.to_json())

# convert the object into a dict
mssql_volume_protection_group_params_dict = mssql_volume_protection_group_params_instance.to_dict()
# create an instance of MSSQLVolumeProtectionGroupParams from a dict
mssql_volume_protection_group_params_from_dict = MSSQLVolumeProtectionGroupParams.from_dict(mssql_volume_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


