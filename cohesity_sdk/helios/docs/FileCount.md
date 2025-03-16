# FileCount

Specifies the number of files with provided size range.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies the number of files with size in this range. | [optional] 
**lower_size_bytes** | **int** | Specifies the lower bound of file size in bytes. This value is inclusive. | [optional] 
**upper_size_bytes** | **int** | Specifies the upper bound of file size in bytes. This value is exclusive. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.file_count import FileCount

# TODO update the JSON string below
json = "{}"
# create an instance of FileCount from a JSON string
file_count_instance = FileCount.from_json(json)
# print the JSON string representation of the object
print(FileCount.to_json())

# convert the object into a dict
file_count_dict = file_count_instance.to_dict()
# create an instance of FileCount from a dict
file_count_from_dict = FileCount.from_dict(file_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


