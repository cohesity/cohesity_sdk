# FilenamePatternToDirectory

Specifies a filename pattern and the directory path where to keep files matching that pattern.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory** | **str** | Specifies the directory where to keep the files matching the pattern. | [optional] 
**filename_pattern** | **str** | Specifies a pattern to be matched with filenames. This can be a regex expression. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.filename_pattern_to_directory import FilenamePatternToDirectory

# TODO update the JSON string below
json = "{}"
# create an instance of FilenamePatternToDirectory from a JSON string
filename_pattern_to_directory_instance = FilenamePatternToDirectory.from_json(json)
# print the JSON string representation of the object
print(FilenamePatternToDirectory.to_json())

# convert the object into a dict
filename_pattern_to_directory_dict = filename_pattern_to_directory_instance.to_dict()
# create an instance of FilenamePatternToDirectory from a dict
filename_pattern_to_directory_from_dict = FilenamePatternToDirectory.from_dict(filename_pattern_to_directory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


