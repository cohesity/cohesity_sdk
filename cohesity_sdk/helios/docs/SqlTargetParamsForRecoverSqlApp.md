# SqlTargetParamsForRecoverSqlApp

Specifies the params for recovering to a sql host. Specifiy seperate settings for each db object that need to be recovered. Provided sql backup should be recovered to same type of target host. For Example: If you have sql backup taken from a physical host then that should be recovered to physical host only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverSqlAppNewSourceConfig**](RecoverSqlAppNewSourceConfig.md) | Specifies the destination Source configuration parameters where the databases will be recovered. This is mandatory if recoverToNewSource is set to true. | [optional] 
**original_source_config** | [**RecoverSqlAppOriginalSourceConfig**](RecoverSqlAppOriginalSourceConfig.md) | Specifies the Source configuration if databases are being recovered to Original Source. If not specified, all the configuration parameters will be retained. | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new sources or an original Source Target. | 

## Example

```python
from cohesity_sdk.helios.models.sql_target_params_for_recover_sql_app import SqlTargetParamsForRecoverSqlApp

# TODO update the JSON string below
json = "{}"
# create an instance of SqlTargetParamsForRecoverSqlApp from a JSON string
sql_target_params_for_recover_sql_app_instance = SqlTargetParamsForRecoverSqlApp.from_json(json)
# print the JSON string representation of the object
print(SqlTargetParamsForRecoverSqlApp.to_json())

# convert the object into a dict
sql_target_params_for_recover_sql_app_dict = sql_target_params_for_recover_sql_app_instance.to_dict()
# create an instance of SqlTargetParamsForRecoverSqlApp from a dict
sql_target_params_for_recover_sql_app_from_dict = SqlTargetParamsForRecoverSqlApp.from_dict(sql_target_params_for_recover_sql_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


