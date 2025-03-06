# RecoverHdfsNoSqlObjectParams

Specifies the fully qualified object name and other attributes of each object to be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_name** | **str** | Specifies the fully qualified name of the object to be restored. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_hdfs_no_sql_object_params import RecoverHdfsNoSqlObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverHdfsNoSqlObjectParams from a JSON string
recover_hdfs_no_sql_object_params_instance = RecoverHdfsNoSqlObjectParams.from_json(json)
# print the JSON string representation of the object
print(RecoverHdfsNoSqlObjectParams.to_json())

# convert the object into a dict
recover_hdfs_no_sql_object_params_dict = recover_hdfs_no_sql_object_params_instance.to_dict()
# create an instance of RecoverHdfsNoSqlObjectParams from a dict
recover_hdfs_no_sql_object_params_from_dict = RecoverHdfsNoSqlObjectParams.from_dict(recover_hdfs_no_sql_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


