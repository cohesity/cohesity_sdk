# HdfsParams

Specifies the recovery options specific to HDFS environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_hdfs_params** | [**RecoverHdfsParams**](RecoverHdfsParams.md) |  | 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.hdfs_params import HdfsParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsParams from a JSON string
hdfs_params_instance = HdfsParams.from_json(json)
# print the JSON string representation of the object
print(HdfsParams.to_json())

# convert the object into a dict
hdfs_params_dict = hdfs_params_instance.to_dict()
# create an instance of HdfsParams from a dict
hdfs_params_from_dict = HdfsParams.from_dict(hdfs_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


