# FilesAndFoldersObject

Specifies a file or folder to download.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**absolute_path** | **str** | Specifies the absolute path of the file or folder. | 
**is_directory** | **bool** | Specifies whether the file or folder object is a directory. | [optional] 

## Example

```python
from cohesity_sdk.models.files_and_folders_object import FilesAndFoldersObject

# TODO update the JSON string below
json = "{}"
# create an instance of FilesAndFoldersObject from a JSON string
files_and_folders_object_instance = FilesAndFoldersObject.from_json(json)
# print the JSON string representation of the object
print(FilesAndFoldersObject.to_json())

# convert the object into a dict
files_and_folders_object_dict = files_and_folders_object_instance.to_dict()
# create an instance of FilesAndFoldersObject from a dict
files_and_folders_object_from_dict = FilesAndFoldersObject.from_dict(files_and_folders_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


