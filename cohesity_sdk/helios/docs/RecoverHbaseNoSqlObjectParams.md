# RecoverHbaseNoSqlObjectParams

Specifies the fully qualified object name and other attributes of each object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_name** | **str** | Specifies the fully qualified name of the object to be restored. | 
**rename_to** | **str** | Specifies the new name to which the object should be renamed. at the time of recovery. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.recover_hbase_no_sql_object_params import RecoverHbaseNoSqlObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHbaseNoSqlObjectParams from a JSON string
recover_hbase_no_sql_object_params_instance = RecoverHbaseNoSqlObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHbaseNoSqlObjectParams.to_json())

# convert the object into a dict
recover_hbase_no_sql_object_params_dict = recover_hbase_no_sql_object_params_instance.to_dict()
# create an instance of RecoverHbaseNoSqlObjectParams from a dict
recover_hbase_no_sql_object_params_from_dict = RecoverHbaseNoSqlObjectParams.from_dict(recover_hbase_no_sql_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


