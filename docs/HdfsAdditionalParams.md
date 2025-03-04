# HdfsAdditionalParams

Additional params for Hdfs protection source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_type** | **str** | Authentication type. | [optional] [readonly] 
**namenode_address** | **str** | The HDFS Namenode IP or hostname. | [optional] [readonly] 
**webhdfs_port** | **int** | The HDFS WebHDFS port. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.hdfs_additional_params import HdfsAdditionalParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsAdditionalParams from a JSON string
hdfs_additional_params_instance = HdfsAdditionalParams.from_json(json)
# print the JSON string representation of the object
print(HdfsAdditionalParams.to_json())

# convert the object into a dict
hdfs_additional_params_dict = hdfs_additional_params_instance.to_dict()
# create an instance of HdfsAdditionalParams from a dict
hdfs_additional_params_from_dict = HdfsAdditionalParams.from_dict(hdfs_additional_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


