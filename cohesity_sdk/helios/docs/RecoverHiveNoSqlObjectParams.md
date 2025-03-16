# RecoverHiveNoSqlObjectParams

Specifies the fully qualified object name and other attributes of each object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_name** | **str** | Specifies the fully qualified name of the object to be restored. | 

## Example

```python
from cohesity_sdk.helios.models.recover_hive_no_sql_object_params import RecoverHiveNoSqlObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHiveNoSqlObjectParams from a JSON string
recover_hive_no_sql_object_params_instance = RecoverHiveNoSqlObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHiveNoSqlObjectParams.to_json())

# convert the object into a dict
recover_hive_no_sql_object_params_dict = recover_hive_no_sql_object_params_instance.to_dict()
# create an instance of RecoverHiveNoSqlObjectParams from a dict
recover_hive_no_sql_object_params_from_dict = RecoverHiveNoSqlObjectParams.from_dict(recover_hive_no_sql_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


