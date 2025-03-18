# HdfsFileFolderParams

Object details for Hdfs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified_time_usecs** | **int** | Specifies the last time file was modified in unix timestamp. | [optional] 
**name** | **str** | Specifies the name. | [optional] 
**path** | **str** | Specifies the path. | [optional] 
**size_bytes** | **int** | Specifies the file size in bytes. | [optional] 
**type** | **str** | Specifies the type of the contents. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hdfs_file_folder_params import HdfsFileFolderParams

# TODO update the JSON string below
json = "{}"
# create an instance of HdfsFileFolderParams from a JSON string
hdfs_file_folder_params_instance = HdfsFileFolderParams.from_json(json)
# print the JSON string representation of the object
print(HdfsFileFolderParams.to_json())

# convert the object into a dict
hdfs_file_folder_params_dict = hdfs_file_folder_params_instance.to_dict()
# create an instance of HdfsFileFolderParams from a dict
hdfs_file_folder_params_from_dict = HdfsFileFolderParams.from_dict(hdfs_file_folder_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


