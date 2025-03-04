# FileStats

Specifies the file stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_count** | **int** | Specifies the number of files. | [optional] 
**files_size_bytes** | **int** | Specifies the size of all the files in bytes. | [optional] 
**type** | **str** | Specifies the file type. | [optional] 

## Example

```python
from cohesity_sdk.models.file_stats import FileStats

# TODO update the JSON string below
json = "{}"
# create an instance of FileStats from a JSON string
file_stats_instance = FileStats.from_json(json)
# print the JSON string representation of the object
print(FileStats.to_json())

# convert the object into a dict
file_stats_dict = file_stats_instance.to_dict()
# create an instance of FileStats from a dict
file_stats_from_dict = FileStats.from_dict(file_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


