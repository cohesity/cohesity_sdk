# FileId

Specifies the file Identifier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int** | Specifies the entity id of the file. | [optional] 
**root_inode_id** | **int** | Specifies the root inode id of the file system that file belongs to. | [optional] 
**view_id** | **int** | Specifies the id of the View the file belongs to. | [optional] 

## Example

```python
from cohesity_sdk.models.file_id import FileId

# TODO update the JSON string below
json = "{}"
# create an instance of FileId from a JSON string
file_id_instance = FileId.from_json(json)
# print the JSON string representation of the object
print(FileId.to_json())

# convert the object into a dict
file_id_dict = file_id_instance.to_dict()
# create an instance of FileId from a dict
file_id_from_dict = FileId.from_dict(file_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


