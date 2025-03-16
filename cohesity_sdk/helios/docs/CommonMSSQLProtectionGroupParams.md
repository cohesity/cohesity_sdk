# CommonMSSQLProtectionGroupParams

Specifies the common params to create a MSSQL Protection Group.

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

## Example

```python
from cohesity_sdk.helios.models.common_mssql_protection_group_params import CommonMSSQLProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonMSSQLProtectionGroupParams from a JSON string
common_mssql_protection_group_params_instance = CommonMSSQLProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(CommonMSSQLProtectionGroupParams.to_json())

# convert the object into a dict
common_mssql_protection_group_params_dict = common_mssql_protection_group_params_instance.to_dict()
# create an instance of CommonMSSQLProtectionGroupParams from a dict
common_mssql_protection_group_params_from_dict = CommonMSSQLProtectionGroupParams.from_dict(common_mssql_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


