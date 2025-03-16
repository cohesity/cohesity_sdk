# FileSizePolicy

Specifies the file's selection rule by file size eg. 1. select files greather than 10 Bytes. 2. select files less than 20 TiB. 3. select files greather than 5 MiB. type: object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | Specifies condition for the file selection. | [optional] 
**n_bytes** | **int** | Specifies the number of bytes. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.file_size_policy import FileSizePolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FileSizePolicy from a JSON string
file_size_policy_instance = FileSizePolicy.from_json(json)
# print the JSON string representation of the object
print(FileSizePolicy.to_json())

# convert the object into a dict
file_size_policy_dict = file_size_policy_instance.to_dict()
# create an instance of FileSizePolicy from a dict
file_size_policy_from_dict = FileSizePolicy.from_dict(file_size_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


