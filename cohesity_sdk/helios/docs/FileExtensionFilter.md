# FileExtensionFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_extensions_list** | **List[str]** | The list of file extensions to apply | [optional] 
**is_enabled** | **bool** | If set, it enables the file extension filter | [optional] 
**mode** | **str** | The mode applied to the list of file extensions &#39;Whitelist&#39; indicates a whitelist extension filter. &#39;Blacklist&#39; indicates a blacklist extension filter. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.file_extension_filter import FileExtensionFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FileExtensionFilter from a JSON string
file_extension_filter_instance = FileExtensionFilter.from_json(json)
# print the JSON string representation of the object
print(FileExtensionFilter.to_json())

# convert the object into a dict
file_extension_filter_dict = file_extension_filter_instance.to_dict()
# create an instance of FileExtensionFilter from a dict
file_extension_filter_from_dict = FileExtensionFilter.from_dict(file_extension_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


