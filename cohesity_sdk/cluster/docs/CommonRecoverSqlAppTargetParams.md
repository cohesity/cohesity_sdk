# CommonRecoverSqlAppTargetParams

Specifies the snapshot parameters to recover Sql databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**CommonSqlAppSourceConfig**](CommonSqlAppSourceConfig.md) |  | [optional] 
**original_source_config** | [**CommonSqlAppSourceConfig**](CommonSqlAppSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new sources or an original Source Target. | 

## Example

```python
from cohesity_sdk.cluster.models.common_recover_sql_app_target_params import CommonRecoverSqlAppTargetParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonRecoverSqlAppTargetParams from a JSON string
common_recover_sql_app_target_params_instance = CommonRecoverSqlAppTargetParams.from_json(json)
# print the JSON string representation of the object
print(CommonRecoverSqlAppTargetParams.to_json())

# convert the object into a dict
common_recover_sql_app_target_params_dict = common_recover_sql_app_target_params_instance.to_dict()
# create an instance of CommonRecoverSqlAppTargetParams from a dict
common_recover_sql_app_target_params_from_dict = CommonRecoverSqlAppTargetParams.from_dict(common_recover_sql_app_target_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


