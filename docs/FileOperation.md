# FileOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_path** | **str** |  | 
**operation** | **str** |  | 

## Example

```python
from cohesity_sdk.models.file_operation import FileOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperation from a JSON string
file_operation_instance = FileOperation.from_json(json)
# print the JSON string representation of the object
print(FileOperation.to_json())

# convert the object into a dict
file_operation_dict = file_operation_instance.to_dict()
# create an instance of FileOperation from a dict
file_operation_from_dict = FileOperation.from_dict(file_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


