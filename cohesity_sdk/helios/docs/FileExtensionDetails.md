# FileExtensionDetails

Details of a file extension in this run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of files with this extension for this run. | [optional] 
**extension_name** | **str** | The name of the file extension | [optional] 
**is_malicious** | **bool** | Is this extension know to be malicious. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.file_extension_details import FileExtensionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of FileExtensionDetails from a JSON string
file_extension_details_instance = FileExtensionDetails.from_json(json)
# print the JSON string representation of the object
print(FileExtensionDetails.to_json())

# convert the object into a dict
file_extension_details_dict = file_extension_details_instance.to_dict()
# create an instance of FileExtensionDetails from a dict
file_extension_details_from_dict = FileExtensionDetails.from_dict(file_extension_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


