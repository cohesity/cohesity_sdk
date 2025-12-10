# SqlTargetParamsForRecoverSqlAppFiles

Specifies the target params for recovering to a SQL database as files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flat_file_directory_location** | **str** | Specifies the directory where to put the database data files. Missing directory will be automatically created. | 
**host** | [**RecoveryObjectIdentifier**](RecoveryObjectIdentifier.md) |  | 
**overwrite_existing_files** | **bool** | Specifies the flag to overwrite existing files at destination. By default files will not be overwritten. | 

## Example

```python
from cohesity_sdk.cluster.models.sql_target_params_for_recover_sql_app_files import SqlTargetParamsForRecoverSqlAppFiles

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTargetParamsForRecoverSqlAppFiles from a JSON string
sql_target_params_for_recover_sql_app_files_instance = SqlTargetParamsForRecoverSqlAppFiles.from_json(json)
# print the JSON string representation of the object
print(SqlTargetParamsForRecoverSqlAppFiles.to_json())

# convert the object into a dict
sql_target_params_for_recover_sql_app_files_dict = sql_target_params_for_recover_sql_app_files_instance.to_dict()
# create an instance of SqlTargetParamsForRecoverSqlAppFiles from a dict
sql_target_params_for_recover_sql_app_files_from_dict = SqlTargetParamsForRecoverSqlAppFiles.from_dict(sql_target_params_for_recover_sql_app_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


