# FileFilteringPolicy

Specifies a set of filters for a file based Protection Group. These values are strings which can represent a prefix or suffix. Example: '/tmp' or '*.mp4'. For file based Protection Groups, all files under prefixes specified by the 'includeFilters' list will be protected unless they are explicitly excluded by the 'excludeFilters' list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_list** | **List[str]** | Specifies the list of excluded files for this protection Protection Group. Exclude filters have a higher priority than include filters. | [optional] 
**include_list** | **List[str]** | Specifies the list of included files for this Protection Group. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.file_filtering_policy import FileFilteringPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of FileFilteringPolicy from a JSON string
file_filtering_policy_instance = FileFilteringPolicy.from_json(json)
# print the JSON string representation of the object
print(FileFilteringPolicy.to_json())

# convert the object into a dict
file_filtering_policy_dict = file_filtering_policy_instance.to_dict()
# create an instance of FileFilteringPolicy from a dict
file_filtering_policy_from_dict = FileFilteringPolicy.from_dict(file_filtering_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


