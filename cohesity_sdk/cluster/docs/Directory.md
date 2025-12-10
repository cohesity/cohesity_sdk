# Directory

Directory is the struct to represent a file or a folder on a VM.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_stat_info** | [**FileStatInfo**](FileStatInfo.md) |  | [optional] 
**full_path** | **str** | Path of the file/directory. | [optional] 
**item_id** | **str** | ItemId is the id of the file/directory. Currently only used in case of OneDrive files/directories. | [optional] 
**name** | **str** | Name is the name of the file or folder. For /test/file.txt, name will be file.txt. | [optional] 
**type** | **str** | Specifies the file type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.directory import Directory

# TODO update the JSON string below
json = "{}"
# create an instance of Directory from a JSON string
directory_instance = Directory.from_json(json)
# print the JSON string representation of the object
print(Directory.to_json())

# convert the object into a dict
directory_dict = directory_instance.to_dict()
# create an instance of Directory from a dict
directory_from_dict = Directory.from_dict(directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


