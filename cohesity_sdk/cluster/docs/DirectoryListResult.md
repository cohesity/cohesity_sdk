# DirectoryListResult

DirectoryListResult is a struct containing information about each directory entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_list** | [**Directories**](Directories.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.directory_list_result import DirectoryListResult

# TODO update the JSON string below
json = "{}"
# create an instance of DirectoryListResult from a JSON string
directory_list_result_instance = DirectoryListResult.from_json(json)
# print the JSON string representation of the object
print(DirectoryListResult.to_json())

# convert the object into a dict
directory_list_result_dict = directory_list_result_instance.to_dict()
# create an instance of DirectoryListResult from a dict
directory_list_result_from_dict = DirectoryListResult.from_dict(directory_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


