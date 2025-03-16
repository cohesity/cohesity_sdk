# FileFolderInfo

Specifies information of the contents (files and folders).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str** | Specifies the environment of the object. | [optional] 
**hdfs_params** | [**List[HdfsFileFolderParams]**](HdfsFileFolderParams.md) | Specifies the parameters for Hdfs. | [optional] 
**pagination_info** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.file_folder_info import FileFolderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FileFolderInfo from a JSON string
file_folder_info_instance = FileFolderInfo.from_json(json)
# print the JSON string representation of the object
print(FileFolderInfo.to_json())

# convert the object into a dict
file_folder_info_dict = file_folder_info_instance.to_dict()
# create an instance of FileFolderInfo from a dict
file_folder_info_from_dict = FileFolderInfo.from_dict(file_folder_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


