# CommonSqlAppSourceConfig

Specifies a common parameters used when restroring back to original or new source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keep_cdc** | **bool** | Specifies whether to keep CDC (Change Data Capture) on recovered databases or not. If not passed, this is assumed to be true. If withNoRecovery is passed as true, then this field must not be set to true. Passing this field as true in this scenario will be a invalid request. | [optional] 
**multi_stage_restore_options** | [**MultiStageRestoreOptions**](MultiStageRestoreOptions.md) |  | [optional] 
**native_recovery_with_clause** | **str** | &#39;with_clause&#39; contains &#39;with clause&#39; to be used in native sql restore command. This is only applicable for database restore of native sql backup. Here user can specify multiple restore options. Example: &#39;WITH BUFFERCOUNT &#x3D; 575, MAXTRANSFERSIZE &#x3D; 2097152&#39;. | [optional] 
**overwriting_policy** | **str** | Specifies a policy to be used while recovering existing databases. | [optional] 
**replay_entire_last_log** | **bool** | Specifies the option to set replay last log bit while creating the sql restore task and doing restore to latest point-in-time. If this is set to true, we will replay the entire last log without STOPAT. | [optional] 
**restore_time_usecs** | **int** | Specifies the time in the past to which the Sql database needs to be restored. This allows for granular recovery of Sql databases. If this is not set, the Sql database will be restored from the full/incremental snapshot. | [optional] 
**secondary_data_files_dir_list** | [**List[FilenamePatternToDirectory]**](FilenamePatternToDirectory.md) | Specifies the secondary data filename pattern and corresponding direcories of the DB. Secondary data files are optional and are user defined. The recommended file extention for secondary files is \&quot;.ndf\&quot;. If this option is specified and the destination folders do not exist they will be automatically created. | [optional] 
**with_no_recovery** | **bool** | Specifies the flag to bring DBs online or not after successful recovery. If this is passed as true, then it means DBs won&#39;t be brought online. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.common_sql_app_source_config import CommonSqlAppSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSqlAppSourceConfig from a JSON string
common_sql_app_source_config_instance = CommonSqlAppSourceConfig.from_json(json)
# print the JSON string representation of the object
print(CommonSqlAppSourceConfig.to_json())

# convert the object into a dict
common_sql_app_source_config_dict = common_sql_app_source_config_instance.to_dict()
# create an instance of CommonSqlAppSourceConfig from a dict
common_sql_app_source_config_from_dict = CommonSqlAppSourceConfig.from_dict(common_sql_app_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


